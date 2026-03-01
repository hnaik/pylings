"""Tests for the verification logic."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from pythonlings.runner import SENTINEL
from pythonlings.verify import verify_all, verify_exercise


@pytest.fixture
def tmp_exercise(tmp_path):
    def _create(name: str, content: str) -> Path:
        f = tmp_path / f"{name}.py"
        f.write_text(content)
        return f
    return _create


def test_verify_passing_exercise(tmp_exercise):
    path = tmp_exercise("ex1", 'def main():\n    assert 1 == 1\n\nif __name__ == "__main__":\n    main()\n')
    result = verify_exercise(path)
    assert result.passed is True


def test_verify_failing_exercise(tmp_exercise):
    path = tmp_exercise("ex2", 'def main():\n    assert 1 == 2\n\nif __name__ == "__main__":\n    main()\n')
    result = verify_exercise(path)
    assert result.passed is False


def test_verify_sentinel_exercise(tmp_exercise):
    path = tmp_exercise("ex3", f"{SENTINEL}\ndef main():\n    pass\n\nif __name__ == '__main__':\n    main()\n")
    result = verify_exercise(path)
    assert result.skipped is True


def test_verify_all_passes(tmp_exercise):
    p1 = tmp_exercise("e1", 'def main():\n    pass\n\nif __name__ == "__main__":\n    main()\n')
    p2 = tmp_exercise("e2", 'def main():\n    pass\n\nif __name__ == "__main__":\n    main()\n')
    all_passed, failed_name, failed_result = verify_all([p1, p2])
    assert all_passed is True
    assert failed_name is None


def test_verify_all_first_failure(tmp_exercise):
    p1 = tmp_exercise("e1", 'def main():\n    pass\n\nif __name__ == "__main__":\n    main()\n')
    p2 = tmp_exercise("e2", 'def main():\n    raise Exception("fail")\n\nif __name__ == "__main__":\n    main()\n')
    p3 = tmp_exercise("e3", 'def main():\n    pass\n\nif __name__ == "__main__":\n    main()\n')
    all_passed, failed_name, failed_result = verify_all([p1, p2, p3])
    assert all_passed is False
    assert failed_name == "e2"
