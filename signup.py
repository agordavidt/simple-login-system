def signUp(username, password, filepath):
    try:
        with open(filepath, 'a') as file:
            file.write(f"{username},{password}\n")
        print("Signup successful!")
    except Exception as e:
        print(f"Error occurred: {e}")
