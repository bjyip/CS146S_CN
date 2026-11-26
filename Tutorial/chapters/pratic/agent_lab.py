"""An offline decision loop with an in-memory sorting fixture, not a real LLM."""

TASKS = [(3, "10:00"), (8, "11:00"), (9, "11:00"), (10, "11:00")]


def fake_model(history):
    if not history or history[-1][1] == "version_conflict":
        return "read"
    return {"read": "edit", "edit": "test", "test": "finish"}[history[-1][0]]


def run_lab(budget=3, conflict=False):
    if budget < 0:
        raise ValueError("budget must be non-negative")
    history = []
    version = 1
    seen_version = None
    numeric_sort = False

    # At most one extra decision, so a final answer can follow the last tool result.
    for _ in range(budget + 1):
        action = fake_model(history)
        if action == "finish":
            status = "verified" if history[-1][1] == [10, 9, 8, 3] else "test_failed"
            return status, history
        if len(history) == budget:
            return "budget_exhausted", history
        if action == "read":
            seen_version = version
            result = version
        elif action == "edit":
            if conflict and version == 1:
                version = 2  # Simulate an independent edit after the first read.
            if seen_version != version:
                result = "version_conflict"
            else:
                numeric_sort = True
                version += 1
                result = "applied"
        else:  # test: compute the actual order, not a hard-coded success flag.
            ordered = sorted(
                TASKS,
                key=lambda task: (task[1], task[0] if numeric_sort else 0),
                reverse=True,
            )
            result = [task[0] for task in ordered]
        history.append((action, result))


if __name__ == "__main__":
    for label, budget, conflict in [("normal", 3, False), ("recovery", 5, True), ("stop", 3, True)]:
        status, trace = run_lab(budget, conflict)
        print(f"{label}: {status}")
        for action, result in trace:
            print(f"  {action}: {result}")
