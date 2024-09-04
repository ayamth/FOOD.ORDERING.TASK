from utilities.data_utils import load_data, save_data
from utilities.general_utils import generate_id, hash_password
from models.user import User
from models.meal import Meal
from models.bill import Bill
from services.auth_service import AuthenticationService
from services.user_service import UserService
from services.meal_service import MealService
from services.bill_service import BillService

def display_menu(options):
    print("\nMenu:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("Choose an option: "))
    return choice

def handle_admin_menu(auth_service, user_service, meal_service, bill_service):
    options = ["List Users", "Add User", "Remove User", "Update User",
               "List Meals", "Add Meal", "Remove Meal", "Update Meal",
               "List Bills", "Logout"]
    choice = display_menu(options)

    if choice == 1:
        print(user_service.list_all())
    elif choice == 2:
        username = input("Username: ")
        password = input("Password: ")
        age = int(input("Age: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")

        user_id = generate_id()
        hashed_password = hash_password(password)
    # Create a new user with the required fields
        user = User(
            id=user_id,
            username=username,
            password=hashed_password,
            age=age,
            first_name=first_name,
            last_name=last_name,
            is_loggedin=False,
            role="user"  # You can change this to "admin" if needed
        )
    
        user_service.add(user)
        print("User added successfully!")
    elif choice == 3:
        user_id = input("User ID to remove: ")
        user_service.remove(user_id)
    elif choice == 4:
        user_id = input("User ID to update: ")
        updated_info = {
            "username": input("New Username: "),
            "age": int(input("New Age: ")),
            "first_name": input("New First Name: "),
            "last_name": input("New Last Name: "),
            "role": input("New Role (admin/cashier/user): ")
        }
        user_service.update(user_id, updated_info)
    elif choice == 5:
        print(meal_service.list_all())
    elif choice == 6:
        name = input("Meal Name: ")
        price = float(input("Price: "))
        meal = Meal(name, price)
        meal_service.add(meal)
    elif choice == 7:
        meal_id = input("Meal ID to remove: ")
        meal_service.remove(meal_id)
    elif choice == 8:
        meal_id = input("Meal ID to update: ")
        updated_info = {
            "name": input("New Meal Name: "),
            "price": float(input("New Price: "))
        }
        meal_service.update(meal_id, updated_info)
    elif choice == 9:
        print(bill_service.list_all())
    elif choice == 10:
        return auth_service.signout(auth_service.current_user['id'])

def handle_cashier_menu(bill_service):
    options = ["List Bills", "Mark Bill as Paid", "Logout"]
    choice = display_menu(options)

    if choice == 1:
        print(bill_service.list_all())
    elif choice == 2:
        bill_id = input("Bill ID to mark as paid: ")
        updated_info = {"is_paid": True}
        bill_service.update(bill_id, updated_info)
        print(f"Bill {bill_id} has been marked as paid.")
    elif choice == 3:
        return auth_service.signout(auth_service.current_user['id'])

def handle_user_menu(meal_service, bill_service):
    options = ["List Meals", "Order Meal", "Logout"]
    choice = display_menu(options)

    if choice == 1:
        print(meal_service.list_all())
    elif choice == 2:
        meal_id = input("Meal ID: ")
        quantity = int(input("Quantity: "))
        bill = Bill(auth_service.current_user['id'], meal_id, quantity)
        bill_service.add(bill)
    elif choice == 3:
        return auth_service.signout(auth_service.current_user['id'])

def main():
    users = load_data('database/users.txt')
    meals = load_data('database/meals.txt')
    bills = load_data('database/bills.txt')

    global auth_service
    auth_service = AuthenticationService(users)
    user_service = UserService(users)
    meal_service = MealService(meals)
    bill_service = BillService(bills)

    while True:
        if auth_service.current_user:
            role = auth_service.current_user['role']
            if role == "admin":
                handle_admin_menu(auth_service, user_service, meal_service, bill_service)
            elif role == "cashier":
                handle_cashier_menu(bill_service)
            elif role == "user":
                handle_user_menu(meal_service, bill_service)
        else:
            options = ["Sign In", "Sign Up", "Exit"]
            choice = display_menu(options)

            if choice == 1:
                username = input("Username: ")
                password = input("Password: ")
                auth_service.signin(username, password)
            elif choice == 2:
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                username = input("Username: ")
                password = input("Password: ")
                age = int(input("Age: "))
                print(auth_service.signup(username, password, age, first_name, last_name))
            elif choice == 3:
                print("Exiting...")
                break

        save_data('database/users.txt', users)
        save_data('database/meals.txt', meals)
        save_data('database/bills.txt', bills)

if __name__ == "__main__":
    main()