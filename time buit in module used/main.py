#######calculate how much time goal will take to comeplete 

import datetime 

user_input = input("enter the goal with a deadline separated by colon\n")
input_list = user_input.split(":")


goal = input_list[0]
deadline = input_list[1]
print(input_list)


deadline_date = (datetime.datetime.strptime(deadline,"%d.%m.%Y")) #Tjis will convert string date which we will input and then this command will convert that string into correct date 

today_date = datetime.datetime.today()# This will provide todays date 

remaining_time_for_goal = (deadline_date - today_date)
remaining_remaining_time_for_goal_in_days = remaining_time_for_goal.days  #this will keep only days
remaining_time_for_goal_in_hors = int(remaining_time_for_goal.total_seconds() /60 /60)

print(f"Dear user! Time remaining for your goal: {goal} is {remaining_time_for_goal}")
print(f"Dear user! Time remaining for your goal: {goal} is {remaining_time_for_goal.days}") #this will keep only days
print(f"Dear user! Time remaining for your goal: {goal} is {remaining_time_for_goal_in_hors} hours") #this will provide hours 