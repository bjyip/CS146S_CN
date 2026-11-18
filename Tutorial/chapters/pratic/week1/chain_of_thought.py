import os
import re

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("ZAI_API_KEY")
model = os.getenv("ZAI_MODEL")

if not api_key:
    raise RuntimeError("请先配置 ZAI_API_KEY 环境变量")

if not model:
    raise RuntimeError("请先配置 ZAI_MODEL 环境变量")

client = OpenAI(
    api_key=api_key,
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    timeout=60.0,
    max_retries=0,
)

NUM_RUNS_TIMES = 5

# 给出可复核的模运算步骤，避免直接计算巨大整数。
YOUR_SYSTEM_PROMPT = """
你是一名数学助手，请分步解决用户给出的幂取余问题。

要求：
1. 寻找并验证幂取余的循环规律，避免直接计算巨大的整数。
2. 根据循环规律化简指数，列出关键计算等式。
3. 计算最终余数，并检查结果是否在合法范围内。
4. 简要展示可核对的计算步骤。
5. 最后一行只写 Answer: <数字>，将 <数字> 替换为计算结果。
"""


USER_PROMPT = """
请解决以下问题，然后在最后一行以“Answer: <数字>”的格式给出最终答案。

3^{12345} (mod 100) 等于多少？
"""


# 对于这个简单示例，我们只要求最终的数值答案
EXPECTED_OUTPUT = "Answer: 43"


def extract_final_answer(text: str) -> str:
    """从详细的推理过程中提取最后一行“Answer: ...”。

    - 查找最后一个以“Answer:”开头的行（不区分大小写）
    - 如果其中包含数字，则规范化为“Answer: <数字>”
    - 如果未检测到数字，则回退为返回匹配到的内容
    """
    matches = re.findall(r"(?mi)^\s*answer\s*:\s*(.+)\s*$", text)
    if matches:
        value = matches[-1].strip()
        # 如果可行，优先将结果规范化为数字格式（支持整数和小数）
        num_match = re.search(r"-?\d+(?:\.\d+)?", value.replace(",", ""))
        if num_match:
            return f"Answer: {num_match.group(0)}"
        return f"Answer: {value}"
    return text.strip()


def test_your_prompt(system_prompt: str) -> bool:
    """最多运行 NUM_RUNS_TIMES 次；若任意一次输出与 EXPECTED_OUTPUT 匹配，则返回 True。

    找到匹配项时打印“SUCCESS”。
    """
    for idx in range(NUM_RUNS_TIMES):
        print(f"正在运行第 {idx + 1}/{NUM_RUNS_TIMES} 次测试")
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            temperature=0.3,
        )
        if not response.choices:
            raise RuntimeError("模型未返回任何回答")

        output_text = response.choices[0].message.content
        if output_text is None:
            raise RuntimeError("模型未返回文本回答")

        final_answer = extract_final_answer(output_text)
        if final_answer.strip() == EXPECTED_OUTPUT.strip():
            print("SUCCESS")
            return True
        else:
            print(f"预期输出：{EXPECTED_OUTPUT}")
            print(f"实际输出：{final_answer}")
    return False


if __name__ == "__main__":
    success = test_your_prompt(YOUR_SYSTEM_PROMPT)
    raise SystemExit(0 if success else 1)
