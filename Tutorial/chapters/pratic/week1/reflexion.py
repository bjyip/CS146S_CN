"""精简反思修正练习：根据程序给出的失败反馈修正待办列表。"""

import json
import os

from dotenv import load_dotenv
from openai import OpenAI

NOTES = "A. 发布已完成。\nB. 明天检查日志。\nC. 考虑更换监控工具，尚未决定。"
RULE = "只保留明确待执行的事项，排除已完成和未决定的事项，按原顺序返回编号。"
FIRST_ANSWER = ["A", "B"]  # 故意给错，保证能练到修正步骤。
EXPECTED = ["B"]

# 练习：改写下面的提示，让提醒能用于其他待办提取题。
REFLEXION_PROMPT = (
    "根据规则和失败反馈，先总结一条可复用的提醒，再修正上一版答案。只返回 JSON 对象，格式为 "
    '{"lesson": "一条可复用的提醒", "items": ["事项编号"]}。不要加代码围栏。'
)


def main() -> bool:
    feedback = f"上一版答案：{FIRST_ANSWER}。A 已完成，不应列入待办。"
    print(f"初始检查失败：{feedback}")

    load_dotenv()
    api_key = os.getenv("ZAI_API_KEY")
    model = os.getenv("ZAI_MODEL")
    if not api_key or not model:
        raise RuntimeError("请先配置 ZAI_API_KEY 和 ZAI_MODEL 环境变量")

    with OpenAI(
        api_key=api_key,
        base_url="https://open.bigmodel.cn/api/paas/v4/",
        timeout=60.0,
        max_retries=0,
    ) as client:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": REFLEXION_PROMPT},
                {"role": "user", "content": f"笔记：\n{NOTES}\n规则：{RULE}\n反馈：{feedback}"},
            ],
            max_tokens=4096,
        )

    if not response.choices or response.choices[0].finish_reason == "length":
        print("模型没有返回完整回答。")
        return False

    text = response.choices[0].message.content or ""
    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        print(f"模型没有返回合法 JSON：{text}")
        return False

    lesson = result.get("lesson") if isinstance(result, dict) else None
    if not isinstance(lesson, str) or not lesson.strip():
        print("模型回答缺少文本形式的反思提醒。")
        return False

    print(f"反思提醒：{lesson}")
    print(f"修正后的答案：{result.get('items')}")
    passed = result.get("items") == EXPECTED
    print("SUCCESS" if passed else "修正后仍未通过。")
    return passed


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
