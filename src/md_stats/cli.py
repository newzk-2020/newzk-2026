"""命令行入口：python -m md_stats 或 md-stats。"""

from __future__ import annotations

import argparse
from pathlib import Path

from md_stats.core import MdStats, analyze_md


def collect_markdown_files(root: Path) -> list[Path]:
    """递归收集目录下所有 .md 文件（按路径排序保证稳定）。"""
    return sorted(root.rglob("*.md"))


def run(root: Path) -> list[MdStats]:
    """扫描目录，返回每篇文件的统计。"""
    results: list[MdStats] = []
    for file in collect_markdown_files(root):
        results.append(analyze_md(file.read_text(encoding="utf-8"), str(file)))
    return results


def print_report(stats_list: list[MdStats]) -> None:
    """打印统计表格。"""
    if not stats_list:
        print("未找到任何 .md 文件")
        return
    total = MdStats(
        "合计",
        sum(s.chars for s in stats_list),
        sum(s.words for s in stats_list),
        sum(s.headings for s in stats_list),
        sum(s.links for s in stats_list),
    )
    for s in [total, *stats_list]:
        print(
            f"{s.path:40s} 字符{s.chars:8d} 词数{s.words:8d} 标题{s.headings:4d} 双链{s.links:4d}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Markdown 笔记统计器")
    parser.add_argument("path", nargs="?", default=".", help="要扫描的目录")
    args = parser.parse_args()
    print_report(run(Path(args.path)))


if __name__ == "__main__":
    main()
