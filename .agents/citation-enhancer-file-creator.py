#!/usr/bin/env python3
# Citation-Enhancer 文件创建器
import os
from pathlib import Path

class CitationFileCreator:
    def __init__(self, obsidian_path):
        self.obsidian_path = Path(obsidian_path) / "Outputs/"

    def create_citation_file(self, paper_info, citation_number, ref_position):
        """创建单个引用文件"""
        file_name = f"{paper_info['file']}.md"
        file_path = self.obsidian_path / paper_info['relative_path'] / "hybrid_auto/" / file_name

        content = f"""---
title: "{paper_info['title']}"
authors:
{', '.join([f'"    - "{author}"' for author in paper_info['authors']])}
date: "{paper_info['date']}"
year: "{paper_info['year']}"
journal: "{paper_info['journal']}"
keywords:
{', '.join([f'"    - "[{keyword}"]' for keyword in paper_info['keywords']])}
abstract: "{paper_info['abstract']}"
abstract_cn: "{paper_info.get('abstract_cn', '')}"
cite: "{paper_info['cite']}"
aiSum: "{paper_info.get('aiSum', '')}"
---
# 引用内容
{ref_position} {paper_info['content']}

## 参考文献
[1] {paper_info['cite']}

---
## 文件路径
{file_path}

**注意事项**:
- 确保相对路径正确
- 文件名包含完整标题
- 引用编号与文件中的插入位置一致

"""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                print(f"✅ 成功创建: {file_path}")
                return True
        except Exception as e:
                print(f"❌ 创建失败: {file_path} - {e}")
                return False

    def create_main_report(self, report_content):
        """创建主报告文件"""
        report_path = self.obsidian_path / "citation-enhancer-report-2024-04-10-FeFET-Edge-Intelligence.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
            print(f"✅ 主报告创建完成: {report_path}")
            return True

if __name__ == '__main__':
    obsidian_path = "/Users/liuyang/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers/Outputs/"
    creator = CitationFileCreator(obsidian_path)

    # 示例使用
    # creator.create_citation_file(
    #     paper_info={
    #         'file': '../../Outputs/Edge Computing Vision and Challenges.md',
    #         'title': 'Edge Computing Vision and Challenges',
    #         'citation': '[[Edge Computing Vision and Challenges]]',
    #         'ref_position': '存内计算优势',
    #         'content': '存内计算架构有效解决...'
    #     }
    # )

    print("Citation File Creator已初始化")
    print("可以创建文件，请运行 python3 citation-enhancer-file-creator.py")