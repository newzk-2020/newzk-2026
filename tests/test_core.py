import pytest

from md_stats.core import analyze_md, count_words


def test_标题统计():
    stats = analyze_md("# 标题一\n## 标题二\n正文")
    assert stats.headings == 2


def test_双链统计():
    stats = analyze_md("见 [[笔记A]] 和 [[笔记B]]")
    assert stats.links == 2


def test_空文件():
    stats = analyze_md("")
    assert (stats.chars, stats.headings, stats.links) == (0, 0, 0)


@pytest.mark.parametrize(
    "文本,期望词数",
    [
        ("你好世界", 4),  # 4 个汉字
        ("hello world", 2),  # 2 个英文词
        ("你好 hello", 3),  # 混合
    ],
)
def test_词数(文本, 期望词数):
    assert count_words(文本) == 期望词数
