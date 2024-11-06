import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# Sample surveys data
samplesurveys = [
    {
        "questions": [
            {"question": "What is your favourite gaming genre?", "type": "multiplechoice", "options": ["Action", "Adventure", "RPG", "Simulation", "Sports"]},
            {"question": "How many hours do you game per week?", "type": "entry"},
            {"question": "What platform do you primarily use for gaming?", "type": "multiplechoice", "options": ["PC", "Console", "Mobile"]},
            {"question": "Do you prefer single-player or multiplayer games?", "type": "multiplechoice", "options": ["Single-player", "Multiplayer"]},
            {"question": "What is your favourite game of all time?", "type": "entry"},
            {"question": "How often do you play new releases?", "type": "multiplechoice", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
            {"question": "Do you participate in gaming communities or forums?", "type": "multiplechoice", "options": ["Yes", "No"]},
            {"question": "What is the most important factor in a game for you?", "type": "multiplechoice", "options": ["Graphics", "Storyline", "Gameplay", "Multiplayer features"]},
            {"question": "How do you discover new games?", "type": "multiplechoice", "options": ["Friends", "Online reviews", "Social media", "Advertisements"]},
            {"question": "What would you like to see improved in gaming?", "type": "entry"}
        ]
    },
    {
        "questions": [
            {"question": "How many mobile games do you play regularly?", "type": "entry"},
            {"question": "What is your favourite mobile game?", "type": "entry"},
            {"question": "How do you feel about in-app purchases?", "type": "multiplechoice", "options": ["Very positive", "Somewhat positive", "Neutral", "Somewhat negative", "Very negative"]},
            {"question": "How often do you play mobile games?", "type": "multiplechoice", "options": ["Daily", "Weekly", "Monthly", "Rarely", "Never"]},
            {"question": "What genre do you prefer in mobile games?", "type": "multiplechoice", "options": ["Puzzle", "Action", "Adventure", "Strategy"]},
            {"question": "Do you prefer online or offline mobile games?", "type": "multiplechoice", "options": ["Online", "Offline"]},
            {"question": "How much are you willing to spend on a mobile game?", "type": "entry"},
            {"question": "What features do you value most in a mobile game?", "type": "multiplechoice", "options": ["Graphics", "Gameplay", "Story", "Multiplayer"]},
            {"question": "How do you typically find new mobile games?", "type": "multiplechoice", "options": ["App store", "Social media", "Friends", "Advertisements"]},
            {"question": "What improvements would you like to see in mobile gaming?", "type": "entry"}
        ]
    },
    {
        "questions": [
            {"question": "What is your favourite PC game?", "type": "entry"},
            {"question": "How many hours do you spend on PC gaming each week?", "type": "entry"},
            {"question": "What is your primary reason for playing PC games?", "type": "multiplechoice", "options": ["Entertainment", "Socialising", "Competitive gaming", "Relaxation"]},
            {"question": "Which gaming platform do you prefer?", "type": "multiplechoice", "options": ["Steam", "Epic Games Store", "Origin", "Others"]},
            {"question": "What genre do you enjoy the most?", "type": "multiplechoice", "options": ["FPS", "RPG", "Strategy", "MMO"]},
            {"question": "How do you feel about modding in games?", "type": "multiplechoice", "options": ["Very positive", "Positive", "Neutral", "Negative", "Very negative"]},
            {"question": "What type of peripherals do you use for gaming?", "type": "multiplechoice", "options": ["Mouse", "Keyboard", "Controller", "VR"]},
            {"question": "Do you attend gaming events or conventions?", "type": "multiplechoice", "options": ["Yes", "No"]},
            {"question": "How do you keep up with gaming news?", "type": "multiplechoice", "options": ["YouTube", "Websites", "Social media", "Friends"]},
            {"question": "What would enhance your PC gaming experience?", "type": "entry"}
        ]
    },
    {
        "questions": [
            {"question": "What is your preferred gaming console?", "type": "multiplechoice", "options": ["PlayStation", "Xbox", "Nintendo", "Others"]},
            {"question": "How often do you purchase games for your console?", "type": "multiplechoice", "options": ["Monthly", "Quarterly", "Annually", "Rarely"]},
            {"question": "What genre do you prefer for console gaming?", "type": "multiplechoice", "options": ["Action", "Adventure", "Sports", "RPG"]},
            {"question": "Do you play games online?", "type": "multiplechoice", "options": ["Yes", "No"]},
            {"question": "What is your favourite multiplayer console game?", "type": "entry"},
            {"question": "How important is graphics to you in console games?", "type": "multiplechoice", "options": ["Very important", "Somewhat important", "Not important"]},
            {"question": "Do you use subscription services for gaming?", "type": "multiplechoice", "options": ["Yes", "No"]},
            {"question": "How do you typically find new console games?", "type": "multiplechoice", "options": ["Friends", "Online reviews", "Game trailers"]},
            {"question": "What would you like to see in future console games?", "type": "entry"},
            {"question": "What do you enjoy most about console gaming?", "type": "entry"}
        ]
    },
    {
        "questions": [
            {"question": "How often do you watch e-sports?", "type": "multiplechoice", "options": ["Daily", "Weekly", "Monthly", "Rarely", "Never"]},
            {"question": "What is your favourite e-sport game?", "type": "entry"},
            {"question": "Which team do you support in e-sports?", "type": "entry"},
            {"question": "How do you feel about e-sports becoming mainstream?", "type": "multiplechoice", "options": ["Very positive", "Somewhat positive", "Neutral", "Somewhat negative", "Very negative"]},
            {"question": "Do you participate in e-sports tournaments?", "type": "multiplechoice", "options": ["Yes", "No"]},
            {"question": "What is the most important aspect of e-sports for you?", "type": "multiplechoice", "options": ["Skill level", "Entertainment", "Community", "Prize money"]},
            {"question": "How do you usually watch e-sports events?", "type": "multiplechoice", "options": ["Twitch", "YouTube", "TV", "In-person"]},
            {"question": "What do you enjoy most about e-sports?", "type": "entry"},
            {"question": "Which e-sports league do you follow?", "type": "entry"},
            {"question": "What improvements would you like to see in the e-sports industry?", "type": "entry"}
        ]
    },
    {
        "questions": [
            {"question": "What type of games do you prefer developing?", "type": "multiplechoice", "options": ["2D", "3D", "Mobile", "VR"]},
            {"question": "What programming languages do you use for game development?", "type": "entry"},
            {"question": "What game engine do you prefer?", "type": "multiplechoice", "options": ["Unity", "Unreal Engine", "Godot", "Others"]},
            {"question": "How long have you been developing games?", "type": "entry"},
            {"question": "What is the biggest challenge you face in game development?", "type": "entry"},
            {"question": "Do you collaborate with other developers?", "type": "multiplechoice", "options": ["Yes", "No"]},
            {"question": "How do you market your games?", "type": "entry"},
            {"question": "What resources do you find most helpful in game development?", "type": "entry"},
            {"question": "How do you gather feedback on your games?", "type": "entry"},
            {"question": "What would you like to learn next in game development?", "type": "entry"}
        ]
    },
    {
        "questions": [
            {"question": "What indie game have you enjoyed the most?", "type": "entry"},
            {"question": "How do you discover new indie games?", "type": "multiplechoice", "options": ["Steam", "Social media", "Friends", "Indie game events"]},
            {"question": "What do you think makes a great indie game?", "type": "entry"},
            {"question": "Do you support indie games through crowdfunding?", "type": "multiplechoice", "options": ["Yes", "No"]},
            {"question": "What genre of indie games do you prefer?", "type": "multiplechoice", "options": ["Puzzle", "Platformer", "Adventure", "RPG"]},
            {"question": "How often do you play indie games?", "type": "multiplechoice", "options": ["Daily", "Weekly", "Monthly", "Rarely"]},
            {"question": "What is your preferred price range for indie games?", "type": "entry"},
            {"question": "How important is the story in an indie game for you?", "type": "multiplechoice", "options": ["Very important", "Somewhat important", "Not important"]},
            {"question": "What improvements would you like to see in indie games?", "type": "entry"},
            {"question": "What platforms do you use to play indie games?", "type": "multiplechoice", "options": ["PC", "Console", "Mobile"]}  
        ]
    },
    {
        "questions": [
            {"question": "Do you own a VR headset?", "type": "multiplechoice", "options": ["Yes", "No"]},
            {"question": "What is your favourite VR game?", "type": "entry"},
            {"question": "How often do you play VR games?", "type": "multiplechoice", "options": ["Daily", "Weekly", "Monthly", "Rarely", "Never"]},
            {"question": "What features do you enjoy most in VR gaming?", "type": "multiplechoice", "options": ["Immersion", "Graphics", "Gameplay", "Multiplayer"]},
            {"question": "How do you feel about the current VR market?", "type": "multiplechoice", "options": ["Very positive", "Somewhat positive", "Neutral", "Somewhat negative", "Very negative"]},
            {"question": "What improvements would you like to see in VR gaming?", "type": "entry"},
            {"question": "Do you play VR games alone or with friends?", "type": "multiplechoice", "options": ["Alone", "With friends"]},
            {"question": "What genres do you prefer in VR?", "type": "multiplechoice", "options": ["Action", "Adventure", "Simulation", "Puzzle"]},
            {"question": "How did you first learn about VR gaming?", "type": "multiplechoice", "options": ["Friends", "YouTube", "Social media", "Advertisements"]},
            {"question": "What is your biggest concern about VR gaming?", "type": "entry"}
        ]
    },
    {
        "questions": [
            {"question": "Do you watch game streamers?", "type": "multiplechoice", "options": ["Yes", "No"]},
            {"question": "What platform do you prefer for streaming?", "type": "multiplechoice", "options": ["Twitch", "YouTube", "Facebook Gaming", "Others"]},
            {"question": "What type of content do you enjoy most in game streaming?", "type": "multiplechoice", "options": ["Gameplay", "Tutorials", "Reviews", "Entertainment"]},
            {"question": "How often do you watch game streams?", "type": "multiplechoice", "options": ["Daily", "Weekly", "Monthly", "Rarely", "Never"]},
            {"question": "Who is your favourite game streamer?", "type": "entry"},
            {"question": "How do you interact with streamers?", "type": "multiplechoice", "options": ["Chat", "Donations", "Social media", "Others"]},
            {"question": "What would improve your streaming experience?", "type": "entry"},
            {"question": "Do you prefer live streams or recorded content?", "type": "multiplechoice", "options": ["Live", "Recorded"]},
            {"question": "What games do you prefer to watch being streamed?", "type": "entry"},
            {"question": "How do you usually discover new streamers?", "type": "multiplechoice", "options": ["Recommendations", "Social media", "Browsing platforms"]}  
        ]
    },
    {
        "questions": [
            {"question": "What is your favourite story-driven game?", "type": "entry"},
            {"question": "How important is a narrative in a game for you?", "type": "multiplechoice", "options": ["Very important", "Somewhat important", "Not important"]},
            {"question": "What narrative elements do you enjoy the most?", "type": "multiplechoice", "options": ["Character development", "Plot twists", "World-building", "Dialogue"]},
            {"question": "Do you prefer linear or open-world storytelling?", "type": "multiplechoice", "options": ["Linear", "Open-world"]},
            {"question": "How do you feel about player choices impacting the story?", "type": "multiplechoice", "options": ["Very positive", "Somewhat positive", "Neutral", "Somewhat negative", "Very negative"]},
            {"question": "What game has the best character development in your opinion?", "type": "entry"},
            {"question": "What would you like to see more of in game narratives?", "type": "entry"},
            {"question": "How often do you replay games for their story?", "type": "multiplechoice", "options": ["Always", "Often", "Sometimes", "Rarely", "Never"]},
            {"question": "What influences your interest in a game's story?", "type": "entry"},
            {"question": "Do you read or watch content related to game narratives?", "type": "multiplechoice", "options": ["Yes", "No"]}
        ]
    }
]

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
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=20)

    def create_survey_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.new_survey = {"questions": []}
        tk.Label(self.root, text="Create a New Survey", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Survey Name:").pack()
        self.survey_name_entry = tk.Entry(self.root)
        self.survey_name_entry.pack()

        tk.Label(self.root, text="Number of Questions:").pack()
        self.num_questions_entry = tk.Entry(self.root)
        self.num_questions_entry.pack()

        tk.Button(self.root, text="Next", command=self.create_questions).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def create_questions(self):
        survey_name = self.survey_name_entry.get()
        num_questions = self.num_questions_entry.get()

        if not survey_name or not num_questions.isdigit():
            messagebox.showerror("Error", "Please enter a valid survey name and number of questions.")
            return

        self.new_survey['name'] = survey_name
        self.new_survey['questions'] = []
        self.num_questions = int(num_questions)
        self.question_index = 0
        self.ask_question()

    def ask_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.question_index >= self.num_questions:
            self.save_survey()
            return

        tk.Label(self.root, text=f"Question {self.question_index + 1}:", font=("Arial", 12)).pack(pady=5)
        self.question_text = tk.Entry(self.root, width=50)
        self.question_text.pack()

        tk.Label(self.root, text="Question Type (multiplechoice or entry):").pack()
        self.question_type_var = tk.StringVar(value="multiplechoice")
        self.question_type_entry = ttk.Combobox(self.root, textvariable=self.question_type_var, values=["multiplechoice", "entry"])
        self.question_type_entry.pack()

        self.option_entries = []
        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack()
        self.create_option_entries()

        tk.Button(self.root, text="Next Question", command=self.add_question).pack(pady=10)

    def create_option_entries(self):
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        if self.question_type_var.get() == "multiplechoice":
            tk.Label(self.root, text="Options:").pack(pady=5)
            self.option_entries = [tk.Entry(self.options_frame) for _ in range(5)]
            for entry in self.option_entries:
                entry.pack()
        else:
            self.option_entries = []

    def add_question(self):
        question_text = self.question_text.get()
        question_type = self.question_type_var.get()

        if question_type == "multiplechoice":
            options = [entry.get() for entry in self.option_entries if entry.get()]
            question_data = {"question": question_text, "type": "multiplechoice", "options": options}
        else:
            question_data = {"question": question_text, "type": "entry"}

        self.new_survey['questions'].append(question_data)
        self.question_index += 1

        if self.question_index < self.num_questions:
            self.ask_question()
        else:
            self.save_survey()

    def save_survey(self):
        survey_path = f"surveys/{self.new_survey['name']}.json"
        with open(survey_path, 'w') as file:
            json.dump(self.new_survey, file)
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

        tk.Button(self.root, text="Take Selected Survey", command=self.start_survey).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def ask_survey_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Check if all questions are answered
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

        # Bind Enter key to the same function as the Submit button
        self.root.bind('<Return>', self.record_answer)
        tk.Button(self.root, text="Submit Answer", command=self.record_answer).pack(pady=10)

    def record_answer(self, event=None):
        question = self.survey_data['questions'][self.current_question_index]
        
        # Record the answer based on the question type
        if question["type"] == "multiplechoice":
            selected_answers = [option for i, option in enumerate(question["options"]) if self.answer_vars[i].get()]
            if not selected_answers:
                selected_answers = ["none"]
            self.results[question["question"]] = selected_answers
        else:
            answer = self.answer_entry.get()
            self.results[question["question"]] = answer if answer else "none"

        # Proceed to the next question
        self.current_question_index += 1
        self.ask_survey_question()

    def start_survey(self):
        selected_index = self.survey_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a survey.")
            return

        # Get the selected survey file name
        self.survey_file = self.survey_listbox.get(selected_index[0])

        # Ensure you are using the correct path when loading the file
        survey_file_path = f"surveys/{self.survey_file}"  # This should correctly point to the selected file
        with open(survey_file_path, 'r') as file:
            self.survey_data = json.load(file)

        # Reset the results and start the survey
        self.results = {}
        self.current_question_index = 0
        self.ask_survey_question()

    def save_survey_results(self):
        # Ensure the 'results' directory exists
        if not os.path.exists('results'):
            os.makedirs('results')

        # Define the path where results will be saved using the survey's name
        results_path = f"results/{self.survey_file}"  # Corrected the file naming here

        # Save the results as a JSON file named after the survey
        with open(results_path, 'w') as file:
            json.dump(self.results, file, indent=4)

        self.main_menu()
        messagebox.showinfo("Results Saved", f"Survey results saved as {results_path}")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = SurveyApp(root)
    root.mainloop()
