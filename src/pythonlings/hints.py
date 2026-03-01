import tomllib
from pathlib import Path

EXERCISE_INFO_FILE = Path("exercise_info.toml")

def load_exercise_info() -> list[dict]:
    """Load exercise metadata from exercise_info.toml."""
    with EXERCISE_INFO_FILE.open("rb") as f:
        data = tomllib.load(f)
    return data.get("exercises", [])

def get_hint(exercise_name: str) -> str | None:
    """Get the hint for an exercise by name."""
    exercises = load_exercise_info()
    for ex in exercises:
        if ex["name"] == exercise_name:
            return ex.get("hint", "No hint available for this exercise.")
    return None

def get_exercise_list() -> list[dict]:
    """Get all exercises in curriculum order."""
    return load_exercise_info()

def get_current_exercise(progress: dict, exercises: list[dict]) -> dict | None:
    """Get the first incomplete exercise."""
    for ex in exercises:
        if not progress.get(ex["name"], {}).get("completed", False):
            return ex
    return None
