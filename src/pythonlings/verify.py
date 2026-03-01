from pathlib import Path
from .runner import run_exercise, ExerciseResult, SENTINEL
from .progress import get_completed_count

def verify_exercise(path: Path) -> ExerciseResult:
    """Run all verification checks on an exercise."""
    return run_exercise(path)

def verify_all(exercise_paths: list[Path]) -> tuple[bool, str | None, ExerciseResult | None]:
    """Run all exercises in order. Returns (all_passed, first_failed_name, first_failed_result)."""
    for path in exercise_paths:
        result = run_exercise(path)
        if result.skipped or not result.passed:
            return False, path.stem, result
    return True, None, None
