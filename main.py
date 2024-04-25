from login import verifyLogin
from signup import signUp




def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # file where user data is stored
    filepath = "data.txt"

    if verifyLogin(username, password, filepath):
        print("You are successfully logged in")
    else:
        print("Incorrect login credentials")




if __name__ == "__main__":
    main()
