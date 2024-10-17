import os
import json
import escapedetector
import main
from random import randint as randomnumber

def open_survey_menu():
        surveys = [f for f in os.listdir('surveys') if f.endswith('.json')]
        if not surveys:
                print("No surveys found. Returning to main menu.")
                main.main_menu()
                return
        
        # Sort the surveys by name
        surveys.sort()

        print("Available surveys:")
        for i, survey in enumerate(surveys):
                print(f"{i + 1}. {survey}")
        
        survey_id = int(input("Enter the ID of the survey to open (write any other number for a random survey): "))
        if survey_id > len(surveys) or survey_id < 1:
                survey_id = randomnumber(1,len(surveys))
                print(f"Choosing survey number {survey_id - 1}, named {surveys[survey_id - 1]}...")
        selected_survey = surveys[survey_id - 1]

        action = int(input(f"Take survey?\n\n1. Yes\n2. Nah\n"))

        if action == 1:
                take_survey(selected_survey)
        elif action == 2:
                main.main_menu()
                return

        if escapedetector.esc_confirm("Exit to main menu?"):
                main.main_menu()
                return

def take_survey(survey_file):
        with open(f"surveys/{survey_file}", 'r') as file:
                survey = json.load(file)

        results = {}
        for question in survey['questions']:
                print(question['question'])
                if question['type'] == "multiplechoice":
                        for i, option in enumerate(question['options']):
                                print(f"{i + 1}. {option}")
                        answer = input("Select your answer: ")
                        options = question['options']
                        results[question['question']] = options[int(answer) - 1]
                else:
                        answer = input("Write your response: ")
                        results[question['question']] = answer

                if escapedetector.esc_confirm("Exit survey without saving?"):
                        main.main_menu()
                        return
        saveresults = int(input("Save results?\n\n1. Yes\nAny other key. No\n"))
        if saveresults == 1:
                with open(f"results/{survey_file}", 'w') as file:
                        json.dump(results, file)
                print(f"Results saved in results/{survey_file}.")
        main.main_menu()
        return

def end():
        exit()
