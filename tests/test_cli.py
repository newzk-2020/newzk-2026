from pathlib import Path

import pytest

from md_stats.cli import run


@pytest.fixture
def fake_notes(tmp_path: Path) -> Path:
    (tmp_path / "a.md").write_text("# 标题\n正文", encoding="utf-8")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "b.md").write_text("[[链接]]", encoding="utf-8")
    return tmp_path


def test_递归收集_md文件(fake_notes: Path):
    result = run(fake_notes)
    assert len(result) == 2


def test_无md文件时为空(tmp_path: Path):
    assert run(tmp_path) == []
