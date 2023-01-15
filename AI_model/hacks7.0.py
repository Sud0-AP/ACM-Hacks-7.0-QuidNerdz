# List of tasks and their respective difficulty levels
tasks = [
    {'task': 'Task 1', 'difficulty': 5},
    {'task': 'Task 2', 'difficulty': 2},
    {'task': 'Task 3', 'difficulty': 3},
    {'task': 'Task 4', 'difficulty': 4},
    {'task': 'Task 5', 'difficulty': 1},
]

# Calculate the average difficulty of the tasks
total_difficulty = 0
for task in tasks:
    total_difficulty += task['difficulty']
average_difficulty = total_difficulty / len(tasks)

print(f'The average difficulty of the tasks is: {average_difficulty:.2f}')