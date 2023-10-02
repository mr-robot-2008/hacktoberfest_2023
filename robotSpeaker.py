'''
This Python program provides a user-friendly interface for controlling a robotic speaker. Upon execution, the program allows the user to input text through the terminal, and the entered text is then converted into speech using an automated voice. This makes it easy for users to communicate or command the robot speaker by simply typing messages in the terminal and having them spoken aloud by the robot.
'''


import os

if __name__ == '__main__':
    print("Welcome to the Robot Speaker")
    while True:
        user_input = input("Write your message (type 'q' to exit): ")
        if user_input == "q":
            break
        command = f"say {user_input}"
        os.system(command)
