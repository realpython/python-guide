correct_username= "Nilu"
correct_password= "1923"
username =input("enter username:")
password =input("enter password:")
if username == correct_username and password == correct_password:
    print("login successful!wellcome",username)
else:
    print("login failed! invalid username or password.")
