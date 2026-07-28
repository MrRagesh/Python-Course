# 2. Creating Modules VS Purpose of OOPS

"""
real-world analogy 1:

I want to reuse the same function for team members and managers, but they have small differences.
how do I do that?

both team members and managers should be able to log in, but
- team members -> should log in, view task, and submit tasks.
- managers -> should log in, view task, and assign task
"""

# without OOPS:

def login(user):
    return f"{user['name']} has logged in."

def view_task(user):
    return f"{user['name']} can view assigned tasks."

def submit_task(user):
    if user['role'] == 'team_member':
        return f"{user['name']} has submited the task."
    else:
        return f"Only team members can submit tasks."

def assign_task(user):
    if user['role'] == 'manager':
        return f"{user['name']} has assigned a new task."
    else:
        return "Only managers can assign tasks."

    #