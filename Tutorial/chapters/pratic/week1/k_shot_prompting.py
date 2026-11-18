import os
from dotenv import load_dotenv
# from ollama import chat
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

# 用多个示例明确演示“逐词反转”，并固定输出格式。
YOUR_SYSTEM_PROMPT = """
任务：将用户提供的单词按字符倒序输出。

规则：
- 最后一个字符放在最前面，依次倒序排列。
- 不增加、删除或替换字符，保留每个字符原来的大小写。
- 只输出倒序后的单词，不加解释、引号或“输出：”前缀。

示例：
输入：dog
输出：god

输入：python
输出：nohtyp

输入：JavaScript
输出：tpircSavaJ
"""

USER_PROMPT = """
将下列单词中的字母顺序反转。只输出反转后的单词，不要输出任何其他文本：

httpstatus
"""


EXPECTED_OUTPUT = "sutatsptth"

def test_your_prompt(system_prompt: str) -> bool:
    """最多运行 NUM_RUNS_TIMES 次提示；若任意一次输出与 EXPECTED_OUTPUT 匹配，则返回 True。

    找到匹配项时打印“SUCCESS”。
    """
    for idx in range(NUM_RUNS_TIMES):
        print(f"正在运行第 {idx + 1}/{NUM_RUNS_TIMES} 次测试")
        # response = chat(
        #     model="mistral-nemo:12b",
        #     messages=[
        #         {"role": "system", "content": system_prompt},
        #         {"role": "user", "content": USER_PROMPT},
        #     ],
        #     options={"temperature": 0.5},
        # )
        # output_text = response.message.content.strip()
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            temperature=0.5,
        )
        if not response.choices:
            raise RuntimeError("模型未返回任何回答")

        content = response.choices[0].message.content

        if content is None:
            raise RuntimeError("模型未返回文本回答")

        output_text = content.strip()
        if output_text.strip() == EXPECTED_OUTPUT.strip():
            print("SUCCESS")
            return True
        else:
            print(f"预期输出：{EXPECTED_OUTPUT}")
            print(f"实际输出：{output_text}")
    return False

if __name__ == "__main__":
    success = test_your_prompt(YOUR_SYSTEM_PROMPT)
    raise SystemExit(0 if success else 1)
