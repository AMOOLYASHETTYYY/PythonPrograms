from collections import deque

def find(tasks, time_slice):
    queue = deque([[i + 1, task] for i, task in enumerate(tasks)])
    completed = 0

    while queue:
        task_num, time_left = queue.popleft()

        if time_left > time_slice:
            print(f"task {task_num} runs for {time_slice} units")
            queue.append([task_num, time_left - time_slice])
        else:
            print(f"task {task_num} runs for {time_left} units")
            completed += 1

    print("total tasks completed:", completed)


tasks = [10, 5, 8]
time_slice = 4

print("output:\ntest Case 1")
find(tasks, time_slice)
