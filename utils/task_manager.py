import sys
import os

# Add the src directory to the Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from ..src.unicore import unicore  # Now you can import unicore as usual

# Define a list of tasks
tasks = [
    {"title": "Buy groceries", "priority": "high", "completed": False},
    {"title": "Write report", "priority": "medium", "completed": False},
    {"title": "Pay bills", "priority": "low", "completed": True},
    {"title": "Schedule meeting", "priority": "medium", "completed": True},
    {"title": "Read book", "priority": "low", "completed": False}
]

# Assign unique IDs to each task using `uniqueId`
for task in tasks:
    task["id"] = unicore.uniqueId("task_")

# Display all tasks
print("\nAll Tasks with Unique IDs:")
for task in tasks:
    print(task)

# 1. Filter out completed tasks
incomplete_tasks = unicore.filter(tasks, lambda t: not t["completed"])
print("\nIncomplete Tasks:")
for task in incomplete_tasks:
    print(task)

# 2. Sort tasks by priority
sorted_tasks = unicore.sortBy(tasks, lambda t: t["priority"])
print("\nTasks Sorted by Priority:")
for task in sorted_tasks:
    print(task)

# 3. Group tasks by priority
grouped_tasks = unicore.groupBy(tasks, lambda t: t["priority"])
print("\nTasks Grouped by Priority:")
for priority, tasks in grouped_tasks.items():
    print(f"Priority {priority}:")
    for task in tasks:
        print(f"  {task['title']} (ID: {task['id']})")

# 4. Map task titles to a list
task_titles = unicore.map(tasks, lambda t: t["title"])
print("\nTask Titles:")
print(task_titles)

# 5. Reduce to count the number of high-priority tasks
high_priority_count = unicore.reduce(tasks, lambda count, t: count + 1 if t["priority"] == "high" else count, 0)
print("\nNumber of High-Priority Tasks:")
print(high_priority_count)

# 6. Generate a unique identifier for a new task
new_task_id = unicore.uniqueId("task_")
print("\nUnique ID for New Task:")
print(new_task_id)

# 7. Use debounce to simulate an auto-save function (here, we'll just demonstrate by calling it twice quickly)
import time

def auto_save():
    print("Auto-save triggered.")

debounced_save = unicore.debounce(auto_save, 1000)  # 1000ms delay
print("\nAuto-Save Simulation:")
debounced_save()
time.sleep(0.5)  # Calling within debounce time to test delay
debounced_save()  # This call should be ignored due to debounce

time.sleep(1.5)  # Wait to let debounce reset
debounced_save()  # This call should go through