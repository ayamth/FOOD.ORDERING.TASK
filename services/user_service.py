from utilities.base_service import BaseService
from models.user import User
from utilities.general_utils import generate_id, hash_password
from utilities.data_utils import save_data

class UserService(BaseService):
    def list_all(self):
        return [User(**user) for user in self.data]

    def add(self, user):
        if not isinstance(user, User):
            raise TypeError("Expected an instance of User.")
        
        new_user = {
            "id": user.id,
            "username": user.username,
            "password": user.password,
            "age": user.age,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_loggedin": user.is_loggedin,
            "role": user.role
        }
        self.data.append(new_user)

    def remove(self, user_id):
        original_count = len(self.data)
        print(f"Original user count: {original_count}")
        print(f"Attempting to remove user with ID: {user_id}")
        
        self.data = [user for user in self.data if user['id'] != user_id]
        new_count = len(self.data)
        print(f"New user count after removal: {new_count}")
        
        if original_count == new_count:
            print("No user was removed. Please check the ID.")
        else:
            print(f"User with ID {user_id} removed successfully.")

    def update(self, user_id, updated_info):
      
        user_found = False
        
        for user in self.data:
            if user['id'] == user_id:
                print(f"Original user data: {user}")  # Debug: Print original data
                user.update(updated_info)
                user_found = True
                print(f"Updated user data: {user}")  # Debug: Print updated data
                break
        
        if not user_found:
            print(f"No user found with ID: {user_id}")  # Debug: No user found


