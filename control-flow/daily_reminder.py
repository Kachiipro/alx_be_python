# The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

task = input("Enter your task:")
task_priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match task_priority:
    case "high":
        if time_bound == "yes":
            time = " that requires immediate attention today!"
        elif time_bound == "no":
            time = ", Consider completing it when you have free time."
        else:
            time_bound = input("Is it time-bound? (yes/no): ")
        print(f"\'{task}\' is a high priority task{time} ")
    case "medium":
        if time_bound == "yes":
            time = " that requires immediate attention today!"
        elif time_bound == "no":
            time = ", Consider completing it when you have free time."
        else:
            time_bound = input("Is it time-bound? (yes/no): ")
        print(f"\'{task}\' is a medium priority task{time} ")

    case "low":
        if time_bound == "yes":
            time = " that requires immediate attention today!"
        elif time_bound == "no":
            time = ", Consider completing it when you have free time."
        else:
            time_bound = input("Is it time-bound? (yes/no): ")
        print(f"\'{task}\' is a low priority task{time} ")
