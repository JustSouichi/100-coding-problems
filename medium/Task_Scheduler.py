def least_interval(tasks, n):
    from collections import Counter
    task_counts = Counter(tasks)
    max_count = max(task_counts.values())
    max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)

    return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)
