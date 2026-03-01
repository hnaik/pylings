import json
from datetime import datetime, timezone
from pathlib import Path

PROGRESS_FILE = Path(".pythonlings_progress.json")

def load_progress() -> dict:
    """Load progress from JSON file. Returns empty dict if file doesn't exist."""
    if not PROGRESS_FILE.exists():
        return {}
    with PROGRESS_FILE.open() as f:
        return json.load(f)

def save_progress(progress: dict) -> None:
    """Save progress to JSON file."""
    with PROGRESS_FILE.open("w") as f:
        json.dump(progress, f, indent=2)

def mark_complete(exercise_name: str) -> None:
    """Mark an exercise as complete. No duplicates."""
    progress = load_progress()
    if exercise_name not in progress:
        progress[exercise_name] = {
            "completed": True,
            "completed_at": datetime.now(timezone.utc).isoformat(),
        }
        save_progress(progress)

def is_complete(exercise_name: str) -> bool:
    """Check if an exercise is complete."""
    progress = load_progress()
    return progress.get(exercise_name, {}).get("completed", False)

def get_completed_count(all_exercises: list[str]) -> int:
    """Get count of completed exercises."""
    progress = load_progress()
    return sum(1 for name in all_exercises if progress.get(name, {}).get("completed", False))
