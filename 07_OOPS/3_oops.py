"""
3. how to create class , objects and inheritance methods and it's real-time purpose?

real-world analogy 1:

I want to reuse the same function for team members and managers, but they have small differences.
how do I do that?

both team members and managers should be able to log in, but
- team members -> should log in, view task, and submit tasks.
- managers -> should log in, view task, and assign task
"""
# data collection
user_data = {
    "name": "jhon",
    "role": "manager"
}

# defining the function
def login(user_data):
    print(f"{user_data['name']} has logged in.")

def view_task(user_data):
    print(f"{user_data['name']} has viewed the task.")

def submit_task(user_data):
    if user_data['role'] == 'team_member':
        print(f"{user_data['name']} has submitted a task.")
    else:
        print(f"manager no need to submitted tha task.")


def assign_task(user_data):
    if user_data['role'] == 'manager':
        print(f"{user_data['name']} has assigned the task.")
    else:
        print(f"team member can't assigned tha task.")

# function to be called login(), view_task(), submit_task(), assign_task()

login(user_data)
view_task(user_data)
submit_task(user_data)
assign_task(user_data)










