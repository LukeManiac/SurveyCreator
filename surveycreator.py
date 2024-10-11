import json
import os
import escapedetector
import main

def create_survey_menu():
        survey = {}
        survey_name = input("Enter a name for the survey: ")
        if survey_name == "":
                print("Survey name cannot be empty. Returning to main menu.")
                main.main_menu()
                return
        
        if escapedetector.esc_confirm("Exit survey creation?"):
                return

        num_questions = int(input("How many questions in the survey? "))
        survey['questions'] = []
        
        for i in range(num_questions):
                question = input(f"Enter question {i + 1}: ")
                
                # Ask for number of options, or skip if fill-in-the-blank
                num_options = input(f"How many options for question {i + 1} (leave blank for entry)? ")
                
                if num_options == "":
                        # It's a fill-in-the-blank question
                        survey['questions'].append({"question": question, "type": "entry"})
                else:
                        # It's a multiple choice question
                        num_options = int(num_options)
                        options = [input(f"Label for option {j + 1}: ") for j in range(num_options)]
                        survey['questions'].append({"question": question, "type": "multiplechoice", "options": options})

                if escapedetector.esc_confirm("Exit survey creation?"):
                        return

        survey_path = f"surveys/{survey_name}.json"
        with open(survey_path, 'w') as file:
                json.dump(survey, file)
        print(f"Survey saved as {survey_path}")

        main.main_menu()
        return

def end():
        exit()
