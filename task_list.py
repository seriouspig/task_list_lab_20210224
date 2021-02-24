tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1.Print a list of uncompleted tasks

def print_uncompleted_tasks(tasks_list):
    uncompleted_tasks = []
    for task in tasks_list:
        if task["completed"] == False:
            uncompleted_tasks.append(task["description"])
     
    return uncompleted_tasks
   
tasks_not_completed = print_uncompleted_tasks(tasks)

print(tasks_not_completed)

# 2.Print a list of completed tasks

def print_completed_tasks(tasks_list):
    completed_tasks = []
    for task in tasks_list:
        if task["completed"] == True:
            completed_tasks.append(task["description"])
     
    return completed_tasks
   
tasks_completed = print_completed_tasks(tasks)

print(tasks_completed)

# 3.Print a list of all task descriptions

def print_all_descriptions(tasks_list):
    all_descriptions = []
    for task in tasks_list:
        all_descriptions.append(task["description"])
    
    return all_descriptions

all_of_descriptions = print_all_descriptions(tasks)

print(all_of_descriptions)

# 4.Print a list of tasks where time_taken is at least a given time

def print_time_given_tasks(tasks_list):
    time_given_tasks = []
    for task in tasks_list:
        if task["time_taken"] != 0:
            time_given_tasks.append(task["description"])
     
    return time_given_tasks
   
tasks_with_given_time = print_time_given_tasks(tasks)

print(tasks_with_given_time)

# 5.Print any task with a given description

def print_task_with_given_description(tasks_list, description_name):
    result_task = None
    for task in tasks_list:
        if task["description"] == description_name:
            result_task = task
    
    return result_task

found_task = print_task_with_given_description(tasks, "Clean Windows")
print(found_task)

# Extension

# 6.Given a description update that task to mark it as complete

def update_task_to_completed(tasks_list, description_name):
    
    for task in tasks_list:
        if task["description"] == description_name:
            task["completed"] = True
    
    
update_task_to_completed(tasks,"Feed Cat")

print(tasks)

# 7.Add a task to the list

def add_task_to_list(tasks_list, task_to_be_added):
    tasks.append({"description": task_to_be_added, "completed":False, "time_taken":None})

add_task_to_list(tasks,"Do Homework")

print(tasks)

# Further Extensions

# 8.Use a while loop to display the following menu and allow the use to enter an option

# print("Menu:")
# print("1: Display All Tasks")
# print("2: Display Uncompleted Tasks")
# print("3: Display Completed Tasks")
# print("4: Mark Task as Complete")
# print("5: Get Tasks Wchi Take Longer Than a Given Time")
# print("6: Find Task by Description")
# print("7: Add a new Task to list")
# print("M or m: Display this menu")
# print("Q or q: Quit")

# 9 Call the appropriate function depending on the users choice