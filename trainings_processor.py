import json, os
from datetime import datetime, timedelta

# Helper function to get fiscal year for a given date
def get_fiscal_year(date):
    return date.year if date.month < 7 else date.year + 1

# Task 1: List each completed training with a count of how many people have completed that training
def completed_training_count():
    training_counts = {}
    for person in data:
        for completion in person['completions']:
            training_name = completion['name']
            training_counts[training_name] = training_counts.get(training_name, 0) + 1
    return training_counts

# Task 2: Given a list of trainings and a fiscal year, list all people who completed those trainings in the specified fiscal year
def completed_trainings_in_fiscal_year(trainings, year):
    completed_trainings = {}
    for person in data:
        for completion in person['completions']:
            if completion['name'] in trainings:
                completion_date = datetime.strptime(completion['timestamp'], '%m/%d/%Y')
                if get_fiscal_year(completion_date) == year:
                    if person['name'] not in completed_trainings:
                        completed_trainings[person['name']] = []
                    completed_trainings[person['name']].append(completion['name'])
    return completed_trainings

# Task 3: Find all people with completed trainings that have expired or will expire within one month of a specified date
def expired_or_expiring_trainings(date):
    expired_trainings = {}
    specified_date = datetime.strptime(date, '%m/%d/%Y')
    expires_in_a_month = specified_date + timedelta(days = 30)
    for person in data:
        for completion in person['completions']:
            if completion['expires'] is not None:
                completion_date = datetime.strptime(completion['timestamp'], '%m/%d/%Y')
                expiration_date = datetime.strptime(completion['expires'], '%m/%d/%Y')
                if completion_date < specified_date and (expiration_date < specified_date or expiration_date < expires_in_a_month):
                    if person['name'] not in expired_trainings:
                        expired_trainings[person['name']] = []
                    expired_trainings[person['name']].append({
                        'name': completion['name'],
                        'expired': expiration_date < specified_date,
                        'expires_soon': expiration_date > specified_date
                    })
    return expired_trainings

# Read data from trainings.txt file
filename = 'trainings.txt'
with open(filename, 'r') as file:
    data = json.load(file)

# Execute tasks with inputs
while True:
    print(f"Choose a function to test using as '{filename}' data:")
    print("1. List each completed training with a count of how many people have completed that training")
    print("2. Given a list of trainings and a fiscal year, list all people who completed those trainings in the specified fiscal year")
    print("3. Find all people with completed trainings that have expired or will expire within one month of a specified date")
    print(f"4. Read in new input data (current input file: '{filename}')")
    print("5. Exit")
    choice = input("Enter a number between 1 and 5 inclusive: ")

    # Cases 1-5
    if choice == "1":
        output1 = completed_training_count()

        # Write outputs to JSON files
        with open('output1.json', 'w') as file:
            json.dump(output1, file, indent = 2)
        print("Output has been generated with the file name output1.json.")
        print("")

    elif choice == "2":
        num_training = int(input("How many trainings do you want to enter? "))
        trainings_list = []
        print("Make sure all trainings title are valid")
        for i in range(num_training):
            index = input(f"Enter training {i + 1}: ")
            trainings_list.append(index)
        year = int(input("Enter a fiscal year: "))
        output2 = completed_trainings_in_fiscal_year(trainings_list, year)

        # Write outputs to JSON files
        with open('output2.json', 'w') as file:
            json.dump(output2, file, indent = 2)
        print("Output has been generated with the file name output2.json.")
        print("")

    elif choice == "3":
        date = '01/01/1000'
        while True:
            date_input = input("Enter a date (MM/DD/YYYY): ")
            try:
                date = datetime.strptime(date_input, '%m/%d/%Y').strftime('%m/%d/%Y')
                break;
            except ValueError:
                print("Invalid date format. Please enter a date in (MM/DD/YYYY) format.")
        output3 = expired_or_expiring_trainings(date)
        
        # Write outputs to JSON files
        with open('output3.json', 'w') as file:
            json.dump(output3, file, indent = 2)
        print("Output has been generated with the file name output3.json.")
        print("")

    elif choice == "4":
        filename = input("Enter a valid file name: ")
        while not os.path.exists(filename):
            print(f"The file '{filename}' does not exist in the current directory.")
            filename = input("Enter a valid file name: ")

        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"'{filename}' has been entered as data")
        print("")

    elif choice == "5":
        print("See you next time!")
        break;

    else:
        print(f"{choice} is not a valid input!")
        choice = input("Enter a number between 1 and 5 inclusive: ")
