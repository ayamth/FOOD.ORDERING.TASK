from models.user import User
from utilities.general_utils import verify_password, hash_password, generate_id

class AuthenticationService:
    def __init__(self, users):
        self.current_user= None
        self.users= users

    def signin(self, username, password):
        for user in self.users:
            if user['username']== username and verify_password(password, user['password']):
                self.current_user= user
                user['is_loggedin']=True
                print(f"welcome {user['first_name']}")
                return True
        print("invalid username or password")
        return False
    
    def signup(self, username, password, age, first_name, last_name):
        #check if the username already exist
        for user in self.users:
            if user['username']== username:
                return "username already exist"
        hashed_password= hash_password(password)
        user_id= generate_id()
        new_user= {
            "id": user_id,
            "username": username,
            "password": hashed_password,
            "age": age,
            "first_name": first_name,
            "last_name": last_name,
            "is_loggedin": False,
            "role": "user" 
        }
        self.users.append(new_user)
        return f"user {username} created successfully"
    
    def signout(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                user['is_loggedin'] = False
                self.current_user = None
                print("signed out successfully.")
                return True
        print("User not found.")
        return False
