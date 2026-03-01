from pathlib import Path
from watchfiles import watch
from .runner import run_exercise, SENTINEL
from .progress import mark_complete, load_progress
from .hints import get_exercise_list, get_current_exercise
from .ui import (
    print_success, print_failure, print_not_done_reminder, print_info
)

def start_watching(exercises_dir: Path, exercise_info_file: Path) -> None:
    """Start the file system watcher."""
    exercises = get_exercise_list()
    progress = load_progress()
    
    current = get_current_exercise(progress, exercises)
    if current is None:
        print_info("🎉 You've completed all exercises! Amazing work!")
        return
    
    current_path = Path(current["path"])
    print_info(f"👀 Watching: {current['name']}")
    print_info(f"   Open: {current['path']}")
    
    # Run the current exercise once before watching
    _run_and_report(current, current_path, exercises, progress)
    
    for changes in watch(str(exercises_dir)):
        progress = load_progress()
        current = get_current_exercise(progress, exercises)
        if current is None:
            print_info("🎉 You've completed all exercises! Amazing work!")
            return
        current_path = Path(current["path"])
        _run_and_report(current, current_path, exercises, progress)

def _run_and_report(current, current_path, exercises, progress):
    total = len(exercises)
    completed = sum(1 for ex in exercises if progress.get(ex["name"], {}).get("completed", False))
    
    result = run_exercise(current_path)
    if result.skipped:
        print_not_done_reminder(current["name"])
        return
    if result.passed:
        mark_complete(current["name"])
        print_success(current["name"], completed + 1, total)
    else:
        print_failure(current["name"], result.stderr or result.output)
