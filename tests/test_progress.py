"""Tests for progress tracking."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from pythonlings.progress import (
    get_completed_count,
    is_complete,
    load_progress,
    mark_complete,
    save_progress,
)


@pytest.fixture(autouse=True)
def tmp_progress_file(tmp_path, monkeypatch):
    """Redirect progress file to a temp location."""
    import pythonlings.progress as prog_module
    monkeypatch.setattr(prog_module, "PROGRESS_FILE", tmp_path / ".pythonlings_progress.json")


def test_load_empty_progress():
    progress = load_progress()
    assert progress == {}


def test_mark_complete():
    mark_complete("exercise1")
    progress = load_progress()
    assert "exercise1" in progress
    assert progress["exercise1"]["completed"] is True


def test_mark_complete_no_duplicates():
    mark_complete("exercise1")
    mark_complete("exercise1")
    progress = load_progress()
    # Should only have one entry
    assert len([k for k in progress if k == "exercise1"]) == 1


def test_is_complete():
    assert is_complete("exercise1") is False
    mark_complete("exercise1")
    assert is_complete("exercise1") is True


def test_get_completed_count():
    all_exercises = ["e1", "e2", "e3", "e4"]
    assert get_completed_count(all_exercises) == 0

    mark_complete("e1")
    mark_complete("e3")
    assert get_completed_count(all_exercises) == 2


def test_save_and_load_progress():
    data = {"myexercise": {"completed": True, "completed_at": "2024-01-01T00:00:00+00:00"}}
    save_progress(data)
    loaded = load_progress()
    assert loaded == data
