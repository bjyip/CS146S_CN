"""智谱原生工具调用：模型提取参数，程序计算，模型根据结果回答。

在 pratic 目录运行：poetry run python week1/tool_calling.py
使用同目录 .env 中的 ZAI_API_KEY 和 ZAI_MODEL，不需要 Ollama。
"""

import json
import math
import os

from dotenv import load_dotenv
from openai import OpenAI

SYSTEM_PROMPT = """
你是购物计算助手。
- 用户需要计算商品总价时，使用 calculate_total 工具，不自行计算替代工具。
- 从用户描述中提取单价和数量，不编造缺失的参数；信息不足时先询问用户。
- 普通知识问题直接回答，不必调用工具。
- 工具返回结果后，用简短中文回答，说明单价、数量和总价。
- 工具返回错误时，说明无法完成计算，不编造结果。
"""

# 可修改为缺少单价的问题，观察模型是否询问；或改为知识问题，观察是否不调用工具。
USER_PROMPT = "我想买 7 本笔记本，每本 18.5 元。一共需要多少钱？"

# 这里只描述工具接口，不包含当前题目的参数或答案。
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculate_total",
            "description": "根据商品单价（元）和数量计算总价。不包含折扣或运费。",
            "parameters": {
                "type": "object",
                "properties": {
                    "unit_price": {"type": "number", "description": "商品单价，单位为元"},
                    "quantity": {"type": "integer", "description": "商品数量"},
                },
                "required": ["unit_price", "quantity"],
                "additionalProperties": False,
            },
        },
    }
]


def calculate_total(unit_price: float, quantity: int) -> dict:
    """教学用计算器：仅计算，不购买商品，也不调用其他服务。"""
    if (
        type(unit_price) not in (int, float)
        or not math.isfinite(unit_price)
        or not 0 <= unit_price <= 1_000_000
    ):
        raise ValueError("单价必须是 0 到 1000000 之间的有限数字")
    if type(quantity) is not int or not 1 <= quantity <= 10_000:
        raise ValueError("数量必须是 1 到 10000 之间的整数")
    return {
        "unit_price": unit_price,
        "quantity": quantity,
        "total": round(unit_price * quantity, 2),
        "currency": "CNY",
    }


def main() -> None:
    load_dotenv()
    api_key = os.getenv("ZAI_API_KEY")
    model = os.getenv("ZAI_MODEL")
    if not api_key or not model:
        raise RuntimeError("请先配置 ZAI_API_KEY 和 ZAI_MODEL 环境变量")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT},
    ]
    print(f"用户：{USER_PROMPT}")

    with OpenAI(
        api_key=api_key,
        base_url="https://open.bigmodel.cn/api/paas/v4/",
        timeout=60.0,
        max_retries=0,
    ) as client:
        # 第一次请求：模型自行判断是否需要工具，并生成工具参数。
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0.3,
            max_tokens=4096,
        )
        if not response.choices or response.choices[0].finish_reason == "length":
            raise RuntimeError("模型未返回完整响应")
        message = response.choices[0].message
        if not message.tool_calls:
            if not message.content:
                raise RuntimeError("模型既未返回工具调用，也未返回回答")
            print(f"模型未调用工具，直接回答：\n{message.content}")
            return

        # 保留模型的工具调用消息，包括调用 ID 和接口可能返回的推理字段。
        messages.append(message.model_dump(exclude_none=True))
        for call in message.tool_calls:
            print(f"模型请求工具：{call.function.name}")
            print(f"模型生成参数：{call.function.arguments}")
            try:
                if call.function.name != "calculate_total":
                    raise ValueError("未知工具")
                args = json.loads(call.function.arguments)
                if not isinstance(args, dict) or set(args) != {"unit_price", "quantity"}:
                    raise ValueError("参数必须且只能包含 unit_price 和 quantity")
                result = calculate_total(**args)
            except (ValueError, TypeError) as err:
                result = {"error": str(err)}
            print(f"程序执行结果：{result}")
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": json.dumps(result, ensure_ascii=False),
                }
            )

        # 第二次请求：模型读取工具结果组织回答，禁止追加工具调用。
        final = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=TOOLS,
            tool_choice="none",
            temperature=0.3,
            max_tokens=4096,
        )
        if not final.choices or final.choices[0].finish_reason == "length":
            raise RuntimeError("模型未返回完整的最终回答")
        answer = final.choices[0].message
        if answer.tool_calls or not answer.content:
            raise RuntimeError("模型未按要求返回最终文本回答")
        print(f"模型最终回答：\n{answer.content}")


if __name__ == "__main__":
    main()
