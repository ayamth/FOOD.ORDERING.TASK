from utilities.general_utils import generate_id

class User:
    def __init__(self, user_id=None, first_name=None, last_name=None, username=None, age=None, password=None, is_loggedin=False, role="user") -> None:
        if not user_id:
            user_id = generate_id()  # Generate a new ID only if one is not provided
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.password = password
        self.is_loggedin = is_loggedin
        self.role = role
