from login import verifyLogin
from signup import signUp



from signup import signUp

def main():
    print("Welcome to Group A!")

    choice = input("Press 1 to create an account or 2 to login: ")

    if choice == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        filepath = "data.txt"
        signUp(username, password, filepath)
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        filepath = "data.txt"
        if verifyLogin(username, password, filepath):
            print("You are successfully logged in")
        else:
            print("Incorrect login credentials")
    else:
        print("You have entered a wrong choice.")

if __name__ == "__main__":
    main()
