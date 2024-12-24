import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class SurveyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Survey Application")
        self.survey_file = None
        self.survey_data = []
        self.results = {}
        self.load_surveys()
        self.main_menu()

    def load_surveys(self):
        if not os.path.exists('results'):
            os.makedirs('results')
        if not os.path.exists('surveys'):
            os.makedirs('surveys')

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Survey Application", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Create a Survey", command=self.create_survey_menu).pack(pady=5)
        tk.Button(self.root, text="Open a Survey", command=self.open_survey_menu).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=20)

    def create_survey_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.new_survey = {"questions": []}
        tk.Label(self.root, text="Create a New Survey", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Survey Name:").pack()
        self.survey_name_entry = tk.Entry(self.root)
        self.survey_name_entry.pack()

        tk.Button(self.root, text="Add Question", command=self.add_question_menu).pack(pady=10)
        tk.Button(self.root, text="Save Survey", command=self.save_survey).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def add_question_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="New Question:", font=("Arial", 12)).pack(pady=5)
        self.question_text = tk.Entry(self.root, width=50)
        self.question_text.pack()

        tk.Label(self.root, text="Question Type (multiplechoice or entry):").pack()
        self.question_type_var = tk.StringVar(value="multiplechoice")
        self.question_type_entry = ttk.Combobox(self.root, textvariable=self.question_type_var, values=["multiplechoice", "entry"])
        self.question_type_entry.pack()

        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=5)

        self.option_entries = []
        self.delete_buttons = []

        tk.Button(self.root, text="Add Option", command=self.add_option).pack(pady=5)
        
        tk.Button(self.root, text="Save Question", command=self.save_question).pack(pady=10)
        self.root.bind('<Return>', lambda event: self.save_question())
        tk.Button(self.root, text="Back", command=self.create_survey_menu).pack()

    def add_option(self):
        # Add new option entry widget
        option_entry = tk.Entry(self.options_frame)
        option_entry.pack()
        self.option_entries.append(option_entry)
        
        # Create a delete button for this option if there is more than one option
        if len(self.option_entries) > 1:
            delete_button = tk.Button(self.options_frame, text="Delete", command=lambda idx=len(self.option_entries)-1: self.delete_option(idx))
            delete_button.pack()
            self.delete_buttons.append(delete_button)
        else:
            self.delete_buttons = []  # No delete button for the first option

    def delete_option(self, idx):
        # Remove the option at the given index
        self.option_entries[idx].destroy()
        self.option_entries.pop(idx)

        # Remove the corresponding delete button
        self.delete_buttons[idx].destroy()
        self.delete_buttons.pop(idx)

        # Adjust the visibility of delete buttons
        if len(self.option_entries) == 1:
            self.delete_buttons = []  # Remove delete button when only one option remains
        elif len(self.option_entries) > 1:
            self.add_delete_buttons()

    def add_delete_buttons(self):
        # Add delete buttons for all options if there are more than one option
        for i in range(len(self.option_entries)):
            if i < len(self.delete_buttons):
                continue  # Skip if delete button already exists for this option
            delete_button = tk.Button(self.options_frame, text="Delete", command=lambda idx=i: self.delete_option(idx))
            delete_button.pack()
            self.delete_buttons.append(delete_button)

    def save_question(self):
        question_text = self.question_text.get()
        question_type = self.question_type_var.get()

        if question_type == "multiplechoice":
            options = [entry.get() for entry in self.option_entries if entry.get()]
            question_data = {"question": question_text, "type": "multiplechoice", "options": options}
        else:
            question_data = {"question": question_text, "type": "entry"}

        self.new_survey['questions'].append(question_data)
        messagebox.showinfo("Info", "Question added!")
        self.create_survey_menu()

    def save_survey(self):
        survey_name = self.survey_name_entry.get()
        if not survey_name:
            messagebox.showerror("Error", "Please enter a survey name.")
            return

        self.new_survey['name'] = survey_name
        survey_path = f"surveys/{survey_name}.json"
        with open(survey_path, 'w') as file:
            json.dump(self.new_survey, file, indent=4)
        messagebox.showinfo("Saved", f"Survey saved as {survey_path}")
        self.main_menu()

    def open_survey_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        surveys = [f for f in os.listdir('surveys') if f.endswith('.json')]
        if not surveys:
            messagebox.showinfo("Info", "No surveys found.")
            self.main_menu()
            return

        tk.Label(self.root, text="Available Surveys", font=("Arial", 16)).pack(pady=10)
        self.survey_listbox = tk.Listbox(self.root, height=10, width=50)
        for survey in surveys:
            self.survey_listbox.insert(tk.END, survey)
        self.survey_listbox.pack()

        self.root.bind('<Return>', self.start_survey)
        tk.Button(self.root, text="Take Selected Survey", command=self.start_survey).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def start_survey(self, event=None):
        selected_index = self.survey_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a survey.")
            return

        self.survey_file = self.survey_listbox.get(selected_index[0])
        survey_file_path = f"surveys/{self.survey_file}"
        with open(survey_file_path, 'r') as file:
            self.survey_data = json.load(file)

        self.results = {}
        self.current_question_index = 0
        self.ask_survey_question()

    def ask_survey_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.current_question_index >= len(self.survey_data['questions']):
            self.save_survey_results()
            return

        question = self.survey_data['questions'][self.current_question_index]
        tk.Label(self.root, text=question["question"], font=("Arial", 12)).pack(pady=10)

        if question["type"] == "multiplechoice":
            self.answer_vars = []
            for option in question["options"]:
                var = tk.BooleanVar()
                cb = tk.Checkbutton(self.root, text=option, variable=var)
                cb.pack()
                self.answer_vars.append(var)
        else:
            self.answer_entry = tk.Entry(self.root, width=50)
            self.answer_entry.pack()

        self.root.bind('<Return>', self.record_answer)
        tk.Button(self.root, text="Submit Answer", command=self.record_answer).pack(pady=10)

    def record_answer(self, event=None):
        question = self.survey_data['questions'][self.current_question_index]
        
        if question["type"] == "multiplechoice":
            selected_answers = [option for i, option in enumerate(question["options"]) if self.answer_vars[i].get()]
            if not selected_answers:
                selected_answers = ["none"]
            self.results[question["question"]] = selected_answers
        else:
            answer = self.answer_entry.get()
            self.results[question["question"]] = answer if answer else "none"

        self.current_question_index += 1
        self.ask_survey_question()

    def save_survey_results(self):
        if not os.path.exists('results'):
            os.makedirs('results')

        results_path = f"results/{self.survey_file}"

        with open(results_path, 'w') as file:
            json.dump(self.results, file, indent=4)

        self.main_menu()
        messagebox.showinfo("Results Saved", f"Survey results saved as {results_path}")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = SurveyApp(root)
    root.mainloop()
