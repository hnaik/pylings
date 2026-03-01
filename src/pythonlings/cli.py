import argparse
import sys
from pathlib import Path

from .hints import get_exercise_list, get_hint, get_current_exercise
from .progress import load_progress, mark_complete, get_completed_count
from .runner import run_exercise
from .ui import (
    print_success, print_failure, print_hint, print_info,
    print_progress, print_exercise_list, print_not_done_reminder
)

EXERCISES_DIR = Path("exercises")

def cmd_watch(args):
    from .watcher import start_watching
    start_watching(EXERCISES_DIR, Path("exercise_info.toml"))

def cmd_verify(args):
    exercises = get_exercise_list()
    all_passed = True
    for ex in exercises:
        path = Path(ex["path"])
        result = run_exercise(path)
        if result.skipped:
            print_info(f"⏭️  Skipped: {ex['name']} (remove # I AM NOT DONE)")
            all_passed = False
            break
        if not result.passed:
            print_failure(ex["name"], result.stderr or result.output)
            all_passed = False
            break
        else:
            print_info(f"✅  Passed: {ex['name']}")
    if all_passed:
        print_info("🎉 All exercises passed!")

def cmd_run(args):
    exercises = get_exercise_list()
    name = args.name
    ex = next((e for e in exercises if e["name"] == name), None)
    if ex is None:
        print_info(f"❌ Exercise '{name}' not found.")
        sys.exit(1)
    path = Path(ex["path"])
    result = run_exercise(path)
    if result.skipped:
        print_not_done_reminder(name)
    elif result.passed:
        print_success(name, 0, len(exercises))
        if result.output:
            print_info(result.output)
    else:
        print_failure(name, result.stderr or result.output)

def cmd_hint(args):
    exercises = get_exercise_list()
    progress = load_progress()
    current = get_current_exercise(progress, exercises)
    if current is None:
        print_info("🎉 You've completed all exercises!")
        return
    hint = get_hint(current["name"])
    print_hint(hint or "No hint available.")

def cmd_list(args):
    exercises = get_exercise_list()
    progress = load_progress()
    completed_set = {name for name, data in progress.items() if data.get("completed")}
    print_exercise_list(exercises, completed_set)

def cmd_reset(args):
    import subprocess
    name = args.name
    exercises = get_exercise_list()
    ex = next((e for e in exercises if e["name"] == name), None)
    if ex is None:
        print_info(f"❌ Exercise '{name}' not found.")
        sys.exit(1)
    result = subprocess.run(["git", "checkout", ex["path"]], capture_output=True, text=True)
    if result.returncode == 0:
        print_info(f"🔄 Reset {name} to its original state.")
    else:
        print_info(f"❌ Could not reset {name}. Make sure you have Git installed and the file is tracked in version control.")

def cmd_progress(args):
    exercises = get_exercise_list()
    names = [ex["name"] for ex in exercises]
    progress = load_progress()
    completed = get_completed_count(names)
    total = len(names)
    print_progress(completed, total)

def main():
    parser = argparse.ArgumentParser(
        prog="pythonlings",
        description="Learn Python by fixing small, broken programs! 🐍",
    )
    subparsers = parser.add_subparsers(dest="command")
    
    subparsers.add_parser("watch", help="Watch for changes and run the current exercise")
    subparsers.add_parser("verify", help="Run all exercises and report first failure")
    
    run_parser = subparsers.add_parser("run", help="Run a single exercise by name")
    run_parser.add_argument("name", help="Exercise name (e.g., variables1)")
    
    subparsers.add_parser("hint", help="Show hint for the current exercise")
    subparsers.add_parser("list", help="List all exercises with completion status")
    
    reset_parser = subparsers.add_parser("reset", help="Reset an exercise to its original state")
    reset_parser.add_argument("name", help="Exercise name to reset")
    
    subparsers.add_parser("progress", help="Show overall progress")
    
    args = parser.parse_args()
    
    commands = {
        "watch": cmd_watch,
        "verify": cmd_verify,
        "run": cmd_run,
        "hint": cmd_hint,
        "list": cmd_list,
        "reset": cmd_reset,
        "progress": cmd_progress,
    }
    
    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
