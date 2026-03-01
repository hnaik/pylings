"""Tests for the exercise runner."""
import sys
from pathlib import Path

import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from pythonlings.runner import SENTINEL, ExerciseResult, run_exercise


@pytest.fixture
def tmp_exercise(tmp_path):
    """Helper to create a temporary exercise file."""
    def _create(content: str) -> Path:
        f = tmp_path / "test_exercise.py"
        f.write_text(content)
        return f
    return _create


def test_passing_exercise(tmp_exercise):
    path = tmp_exercise(
        'def main():\n    print("hello")\n\nif __name__ == "__main__":\n    main()\n'
    )
    result = run_exercise(path)
    assert result.passed is True
    assert result.skipped is False


def test_failing_exercise(tmp_exercise):
    path = tmp_exercise(
        'def main():\n    raise ValueError("bad")\n\nif __name__ == "__main__":\n    main()\n'
    )
    result = run_exercise(path)
    assert result.passed is False
    assert result.skipped is False


def test_not_done_exercise(tmp_exercise):
    path = tmp_exercise(
        f"# {SENTINEL.lstrip('# ')}\ndef main():\n    pass\n\nif __name__ == '__main__':\n    main()\n"
    )
    # Write the sentinel properly
    path.write_text(f"{SENTINEL}\ndef main():\n    pass\n\nif __name__ == '__main__':\n    main()\n")
    result = run_exercise(path)
    assert result.skipped is True
    assert result.passed is False


def test_assertion_failure(tmp_exercise):
    path = tmp_exercise(
        'def main():\n    assert 1 == 2\n\nif __name__ == "__main__":\n    main()\n'
    )
    result = run_exercise(path)
    assert result.passed is False
    assert result.skipped is False
