import surveycreator
import surveybrowser
import escapedetector
import json
import os
import sys

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

def main_menu():
        print("1. Create a Survey")
        print("2. Open a Survey")
        print("3. TKinter Edition (Beta)")
        print("Any other key: Quit")
        choice = input("Select an option: ")
        if choice == "1":
                surveycreator.create_survey_menu()
        elif choice == "2":
                surveybrowser.open_survey_menu()
        else:
                escapedetector.end()
                surveybrowser.end()
                surveycreator.end()
                sys.exit()

if __name__ == "__main__":
        # Ensure the 'results' directory exists
        if not os.path.exists('results'):
            os.makedirs('results')
        
        # Ensure the 'surveys' directory exists and check if it's empty
        if not os.path.exists('surveys'):
            os.makedirs('surveys')
    
        # Check if any sample survey exists; if not, save the samplesurveys
        if not any(os.path.isfile(os.path.join('surveys', f)) for f in os.listdir('surveys')):
                for i, survey in enumerate(samplesurveys):
                        with open(f"surveys/Sample Survey {i+1}.json", "w") as file:
                                json.dump(survey, file)
                
        escapedetector.start_esc_listener(main_menu)
