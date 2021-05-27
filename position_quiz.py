import os
import colored
from colored import stylize

class Person:

    data = {}

    def __init__(self):
        self.record = None
        self.read_file()

    def write_user_data(self, fname, height, weight, exp):    
        try:
            current_folder = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_folder, 'user_info.csv')
            file = open(file_path, "a")

            self.fname = fname
            self.height = height
            self.weight = weight
            self.exp = exp

            file.write(f"\n{fname};{height};{weight};{exp}")

            file.close()

        except IOError as e:
            print("Error: ", e)

    def read_file(self):
        try:
            current_folder = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_folder, 'user_info.csv')
            file = open(file_path, "r")

        except FileNotFoundError as e:
            print("Error: ", e)

        for line in file: 
            row = line.split(';')
            row = [i.strip() for i in row]
                
        file.close()

class Admin:

    data = {}

    def __init__(self):
        self.record = None
        self.read_file()

    def write_admin_file(self, key, name, pw):
        try:
            current_folder = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_folder, 'admins.csv')
            file = open(file_path, "a")

            self.key = key
            self.name = name
            self.pw = pw

            file.write(f"\n{key};{name};{pw}")

            file.close()

        except IOError as e:
            print("Error: ", e)   

    def read_file(self):
        try:
            current_folder = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_folder, 'admins.csv')
            file = open(file_path, "r")

            for line in file: 
                row = line.split(',')
                row = [i.strip() for i in row]
                Admin.data[int(row[0])] = [str(row[1]), str(row[2])]

            file.close() 

        except FileNotFoundError as e:
            print("Error: ", e)              

    def admin_login(self):

        print(stylize(("\n---Admin Login---\n"), colored.fg("magenta_3b")))
        account_id = int(input(stylize(("UID: "), colored.fg("gold_3b"))))
        password = str(input(stylize(("Password: "), colored.fg("gold_3b"))))

        if Admin.data.get(account_id):
            self.record = Admin.data.get(account_id)
            if self.record[1] == password:
                print(stylize(("\n---Login Successful---\n"), colored.fg("magenta_3b")))
                self.admin_menu()
            else: 
                self.record = None
                print(stylize(("*Incorrect UID or Password*"), colored.fg("dark_red_1")))
                self.admin_login()
        else:
            print(stylize(("*Incorrect UID or Password*"), colored.fg("dark_red_1")))
            self.admin_login()

    def admin_menu(self):

        print(stylize(("---Welcome Admin---\n"), colored.fg("hot_pink_3a")))
        print(stylize(("Here's the list of actions: \n"), colored.fg("hot_pink_3a")))

        admin_actions = {
            1 : "View Info",
            2 : "Logout",
            3 : "Close Program"
        }
        for key, value in admin_actions.items():
            print(stylize((f"{key} : {value}"), colored.fg("hot_pink_3a")))

        answer = input(stylize("\nPlease input the number of the action you want to perform: ", colored.fg("dark_sea_green_2")))

        if answer == '1':
            print(stylize(("---View Info---\n"), colored.fg("dark_sea_green_2")))
            self.view_info()
        elif answer == '2':
            print(stylize(("---Logging Out---"), colored.fg("magenta_3b")))
            self.admin_login()
        elif answer == '3':
            print(stylize("\n---Exiting program---\n", colored.fg("magenta_3b")))
            print(stylize("Program is closed. See you again!\n", colored.fg("magenta_3b")))

        else:
            answer = input(stylize("---Invalid input, please try again. Press 'Enter'---\n", colored.fg("deep_pink_2")))
            self.admin_menu()

    def view_info(self):
        print(stylize(("Viewing info:\n"), colored.fg("dark_sea_green_2")))
        print(stylize(("Inputted information not saved, functionality coming soon!\n"), colored.fg("red_1")))

    # ran out of time with this one. Tried to create a flow for this, but I struggled and ran out of time. 

class User(Person, Admin): 

    def __init__(self):
        Person.__init__(self)

    def start(self):
        print(stylize("---WHAT BASKETBALL POSITION SUITS YOU?---\n", colored.fg("light_sky_blue_1")))
        print(stylize("Welcome! Here's the list of actions: \n", colored.fg("hot_pink_3a")))

        user_menu = {
            1 : "Begin the quiz!",
            2 : "Exit quiz",
            3 : "Login for Admins"
        }

        for key, value in user_menu.items():
            print(stylize((f"{key} : {value}"), colored.fg("hot_pink_3a")))

        answer = input(stylize("\nPlease input the number of the action you want to perform: ", colored.fg("dark_sea_green_2")))

        if answer == '1':
            print(stylize("---Beginning Quiz---\n", colored.fg("magenta_3b")))
            self.run_quiz()
        elif answer == '2':
            print(stylize("\n---Exiting program---\n", colored.fg("magenta_3b")))
            print(stylize("Program is closed. See you again!\n", colored.fg("magenta_3b")))
        elif answer == '3':
            self.admin_login()
            self.start()
        else:
            answer = input(stylize("---Invalid input, please try again. Press 'Enter'---\n", colored.fg("deep_pink_2")))
            self.start()

    def run_quiz(self):

        print(stylize("---User Information---\nPlease enter your information: \n", colored.fg("gold_3b")))
        fname = str(input(stylize("First name: ", colored.fg("gold_3b"))))
        height = int(input(stylize("Height in inches: ", colored.fg("gold_3b"))))
        weight = int(input(stylize("Weight in lbs: ", colored.fg("gold_3b"))))
        exp = int(input(stylize("Years of experience: ", colored.fg("gold_3b"))))

        self.write_user_data(fname, height, weight, exp)

        # quiz results are Guard, Forward, Center
        # Forwards/Centers are generally tall, Guard is generally small
        # Forwards/Centers can range from 77inches - 84inches and weigh > 170 
        # Guards can range from 65inches - 75inches and weigh < 170

        #self.write_user_data(fname,height, weight, exp)

        #Person.__new_user_data[input] = [fname,height, weight, exp]

        print(stylize(f"\nThanks for participating, {fname}! Please answer the following questions:", colored.fg("magenta_3b")))

        guard_score = 0
        forward_score = 0
        center_score = 0

        q1 = input(stylize("\nDo you know what basketball is? yes or no? \n", colored.fg("light_sky_blue_1")))
        if q1 == 'yes' or 'y':
            guard_score +=1
            forward_score +=1
            center_score +=1
        elif q1 == 'no' or 'n': 
            print(stylize(("You might want to learn what basketball is.."), colored.fg("yellow")))
        else:
            print(stylize(("Invalid input, start over"), colored.fg("deep_pink_2")))
            self.run_quiz()
        q2 = input(stylize("\nAre you a team player? yes or no? \n", colored.fg("light_sky_blue_1")))
        if q2 == 'yes' or 'y':
            guard_score +=1
            forward_score +=1
            center_score +=1
        elif q2 == 'no' or 'n':
            print(stylize(("But basketball is a team sport.."), colored.fg("yellow")))
        else:
            print(stylize(("Invalid input, start over"), colored.fg("deep_pink_2")))
            self.run_quiz()
        q3 = input(stylize("\nDo you consider yourself a leader? \na. Yes, I like to lead \nb. No, I like to have someone else lead \nc. Sometimes, whenever I need to be \nd. No leading for me \n", colored.fg("light_sky_blue_1")))
        if q3 == 'a':
            guard_score +=1
        elif q3 == 'b':
            center_score +=1
        elif q3 == 'c':
            forward_score +=1
        elif q3 == 'd':
            print(stylize(("We all need a leader.."), colored.fg("yellow")))
        else:
            print(stylize(("Invalid input, start over"), colored.fg("deep_pink_2")))
            self.run_quiz()
        q4 = input(stylize("\nDo you like shooting and getting as many points as possible? \na. Yes, I want all the points \nb. No, someone else can score \nc. I'm indifferent \nd. I don't score at all \n", colored.fg("light_sky_blue_1")))
        if q4 == 'a':
            guard_score +=1
            forward_score +=1
        elif q4 == 'b':
            forward_score +=1
            center_score +=1
        elif q4 == 'c':
            center_score +=1
        elif q4 == 'd':
            print(stylize(("You need to score to win.."), colored.fg("yellow")))
        else:
            print(stylize(("Invalid input, start over"), colored.fg("deep_pink_2")))
            self.run_quiz()
        q5 = input(stylize("\nAre you a defensive person? \na. Yeah, I like defense \nb. Defense? What's defense? \nc. I'm indifferent \nd. No, the other team can score \n", colored.fg("light_sky_blue_1")))
        if q5 == 'a':
            center_score +=1
        elif q5 == 'b':
            guard_score +=1
        elif q5 == 'c':
            forward_score +=1
        elif q5 == 'd':
            print(stylize(("But defense wins championships.."), colored.fg("yellow")))
        else:
            print(stylize(("Invalid input, start over"), colored.fg("deep_pink_2")))
            self.run_quiz()
        q6 = input(stylize("\nWhat's your lifestyle? \na. Go, go, go \nb. Laid back \nc. Antsy \nd. What's a lifestyle? \n", colored.fg("light_sky_blue_1")))
        if q6 == 'a':
            guard_score +=1
        elif q6 == 'b':
            center_score +=1
        elif q6 == 'c':
            forward_score +=1
        elif q6 == 'd':
            print(stylize(("You might need to do some self reflection.."), colored.fg("yellow")))
        else:
            print(stylize(("Invalid input, start over"), colored.fg("deep_pink_2")))
        q7 = input(stylize("\nWhen playing a group game, are you.. \na. Super competitive \nb. Just want to have fun \nc. The know-it-all \nd. What's a group game? \n", colored.fg("light_sky_blue_1")))
        if q7 == 'a':
            guard_score +=1
            forward_score +=1
            center_score +=1
        elif q7 == 'b':
            guard_score +=1
            forward_score +=1
            center_score +=1
        elif q7 == 'c':
            guard_score +=1
            forward_score +=1
            center_score +=1
        elif q7 == 'd':
            print(stylize(("Might want to find some friends.."), colored.fg("yellow")))
        else:
            print(stylize(("Invalid input, start over"), colored.fg("deep_pink_2")))
        q8 = input(stylize("\nWhat trait would you like to have? \na. Agility \nb. Vision \nc. Accuracy \nd. Hustle \ne. Tenacity \n", colored.fg("light_sky_blue_1")))
        if q8 == 'a':
            guard_score +=1
            forward_score +=1
        elif q8 == 'b':
            guard_score +=1
        elif q8 == 'c':
            forward_score +=1
        elif q8 == 'd':
            forward_score +=1
            center_score +=1
        elif q8 == 'e':
            center_score +=1
        else:
            print(stylize(("Invalid input, start over"), colored.fg("deep_pink_2")))

        if guard_score > forward_score and guard_score > center_score:
            print(stylize((f"\nCongrats, {fname}, You're a Guard!\n"), colored.fg("aquamarine_1b")))
        elif forward_score > guard_score and forward_score > center_score:
            print(stylize((f"\nCongrats, {fname}, You're a Forward!\n"), colored.fg("aquamarine_1b")))
        elif center_score > guard_score and center_score > forward_score:
            print(stylize((f"\nCongrats, {fname} You're a Center!\n"), colored.fg("aquamarine_1b")))
        elif guard_score == forward_score:
            print(stylize((f"\n{fname}, You have a choice between Guard and Forward!"), colored.fg("dark_sea_green_3a")))
        elif forward_score == center_score:
            print(stylize((f"\n{fname}, You have a choice between Forward and Center!"), colored.fg("dark_sea_green_3a")))
        elif center_score == guard_score:
            print(stylize((f"\n{fname}, You have a choice between Center and Guard!"), colored.fg("dark_sea_green_3a")))
        elif guard_score and center_score and forward_score == 0:
            print(stylize(("\nYou might want to look at a different sport.."), colored.fg("dark_sea_green_1")))

        print(stylize((f"Here's your scores: \nYour Guard score is: {guard_score}\nYour Forward score is: {forward_score}\nYour Center score is: {center_score}\n"), colored.fg("medium_purple")))
        print(stylize(input("Want to try again? Press 'Enter' to head back.."), colored.fg("medium_purple")))
        self.run_quiz()

# I want to code in an easter egg where if users input answers in a specific way, they are brought to the creation of an admin account. Of course, this will be super tough to do as admins can see already inputted information and results.

def main():
    """
    Call Functions
    """
    user = User()
    admin = Admin()
    user.start()
    admin.admin_login()

if __name__ == '__main__':
    main()

