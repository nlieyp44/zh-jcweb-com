import json
from datetime import datetime

# 内置站点资料配置
SITES = [
    {
        "url": "https://zh-jcweb.com",
        "keywords": ["竞彩网", "竞彩", "足球", "体育彩票"],
        "tags": ["体育", "博彩", "中国"],
        "description": "提供竞彩足球、篮球等体育赛事投注资讯的平台。"
    },
    {
        "url": "https://example-sports.com",
        "keywords": ["NBA", "英超", "比分", "直播"],
        "tags": ["体育", "直播", "国际"],
        "description": "实时体育比分与赛事直播服务。"
    },
    {
        "url": "https://data-lottery.org",
        "keywords": ["双色球", "大乐透", "开奖", "走势图"],
        "tags": ["彩票", "数据", "分析"],
        "description": "各类数字彩票开奖结果与历史走势数据查询。"
    }
]


def generate_summary(site: dict) -> dict:
    """根据单条站点资料生成结构化摘要"""
    return {
        "url": site["url"],
        "keywords": ", ".join(site["keywords"]),
        "tags": site["tags"],
        "short_description": site["description"],
        "keyword_count": len(site["keywords"]),
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def build_report(sites: list) -> list:
    """处理所有站点并返回摘要列表"""
    report = []
    for site in sites:
        report.append(generate_summary(site))
    return report


def display_summaries(summaries: list) -> None:
    """以可读格式打印所有摘要"""
    header_line = f"{'='*60}"
    print(header_line)
    print(f"{'站点结构化摘要报告':^60}")
    print(header_line)
    print(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(header_line)

    for idx, item in enumerate(summaries, 1):
        print(f"\n--- 站点 {idx} ---")
        print(f"URL           : {item['url']}")
        print(f"关键词        : {item['keywords']}")
        print(f"标签          : {', '.join(item['tags'])}")
        print(f"简短说明      : {item['short_description']}")
        print(f"关键词数量    : {item['keyword_count']}")
        print(f"摘要生成时间  : {item['generated_at']}")


def export_json(summaries: list, filename: str = "site_summaries.json") -> None:
    """将摘要列表导出为 JSON 文件"""
    output = {
        "generated_at": datetime.now().isoformat(),
        "total_sites": len(summaries),
        "summaries": summaries
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\n摘要已导出至: {filename}")


def get_keyword_cloud(sites: list) -> dict:
    """统计所有站点关键词出现频率，返回词频字典"""
    freq = {}
    for site in sites:
        for kw in site["keywords"]:
            freq[kw] = freq.get(kw, 0) + 1
    # 按频率降序排列
    sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
    return sorted_freq


def main():
    """主流程"""
    # 生成摘要
    summaries = build_report(SITES)

    # 显示摘要
    display_summaries(summaries)

    # 导出 JSON
    export_json(summaries)

    # 显示关键词云
    cloud = get_keyword_cloud(SITES)
    print(f"\n{'='*60}")
    print(f"{'关键词频率统计':^60}")
    print(f"{'='*60}")
    for word, count in cloud.items():
        print(f"  {word}: {count} 次")


if __name__ == "__main__":
    main()