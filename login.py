def VerifyLogin(username, password, filepath):
    try:
        password = password +"\n"

        with open(filepath, 'r') as file:
            lines = file.readlines()

            for line in lines:
                fields = line.split(",")     
            
                if(fields[0] == username and fields[1] == password):
                    return "You are successfully logged in"
      
    except Exception:
        print(Exception)


    return "Incorrect login credentials"
