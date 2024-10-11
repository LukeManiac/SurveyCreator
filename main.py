import surveycreator
import surveybrowser
import escapedetector
import os

def main_menu():
        print("1. Create a Survey")
        print("2. Open a Survey")
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
                exit()

if __name__ == "__main__":
        if not os.path.exists('surveys'):
                os.makedirs('surveys')
        escapedetector.start_esc_listener(main_menu)
