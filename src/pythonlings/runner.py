import subprocess
import sys
from pathlib import Path

SENTINEL = "# I AM NOT DONE"

class ExerciseResult:
    def __init__(self, passed: bool, output: str, stderr: str, skipped: bool = False):
        self.passed = passed
        self.output = output
        self.stderr = stderr
        self.skipped = skipped  # True if I AM NOT DONE is present

def run_exercise(path: Path) -> ExerciseResult:
    """Run a single exercise file and return the result."""
    content = path.read_text()
    
    if SENTINEL in content:
        return ExerciseResult(passed=False, output="", stderr="", skipped=True)
    
    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True,
        timeout=10,
    )
    
    passed = result.returncode == 0
    return ExerciseResult(
        passed=passed,
        output=result.stdout,
        stderr=result.stderr,
        skipped=False,
    )
