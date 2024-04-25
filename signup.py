def signUp(username, password, filepath):
    try:
        with open(filepath, 'a') as file:
            file.write(f"{username},{password}\n")
        print("User successfully added.")
    except Exception as e:
        print(f"An error occurred: {e}")