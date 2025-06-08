import math

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        else:
            print("❌ Please enter 'yes' or 'no'.")

print("📊 Welcome to the Ultimate Budgeting Tool!\n")

# Get weekly budget info
weekly_expense = get_float("How much are your weekly expenses? $")
weekly_pay = get_float("How much is your weekly pay? $")

weekly_savings = weekly_pay - weekly_expense

# Handle zero or negative savings
if weekly_savings <= 0:
    print("\n⚠️ You are not saving anything right now. Try reducing expenses or increasing income.")
else:
    print(f"\n✅ You can save ${weekly_savings:.2f} per week.\n")

    goals = []

    # Collect multiple goals
    while True:
        goal_name = input("What are you saving up for? (e.g., 'laptop'): ").strip()
        goal_cost = get_float(f"How much does '{goal_name}' cost? $")
        goals.append((goal_name, goal_cost))

        if not get_yes_no("Do you want to add another goal? (yes/no): "):
            break

    # Display summary
    print("\n💡 Savings Plan Summary:")
    for name, cost in goals:
        weeks = math.ceil(cost / weekly_savings)
        print(f" - {name.capitalize()}: ${cost:.2f} will take ~{weeks} week(s) to save.")

    print("\n🎯 Keep saving and good luck reaching your goals!")
