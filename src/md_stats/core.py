# /src/md_stats/core.py

"""Markdown 文本统计核心逻辑。"""

from __future__ import annotations

import re
from dataclasses import dataclass

LINK_PATTERN = re.compile(r"\[\[[^\]]+\]\]")


@dataclass
class MdStats:
    """单篇 Markdown 的统计结果。"""

    path: str
    chars: int
    words: int
    headings: int
    links: int


def count_words(text: str) -> int:
    """统计中英文混合文本的近似词数。"""
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    english_words = len(re.findall(r"[A-Za-z0-9_]+", text))
    return chinese_chars + english_words


def analyze_md(text: str, path: str = "") -> MdStats:
    """分析一篇 Markdown 文本，返回统计结果。"""
    lines = text.splitlines()
    headings = sum(1 for line in lines if line.lstrip().startswith("#"))
    links = len(LINK_PATTERN.findall(text))
    return MdStats(
        path=path,
        chars=len(text),
        words=count_words(text),
        headings=headings,
        links=links,
    )
