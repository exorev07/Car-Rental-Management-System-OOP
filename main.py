import sqlite3
import colorama
from colorama import Fore, Back, Style
import pyfiglet

colorama.init(autoreset=True)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.booked_cars = []

class Car:
    def __init__(self, car_id, brand, model, year, rental_rate, is_available=True):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
        self.is_available = is_available

class Booking:
    def __init__(self, customer_username, car: Car):
        self.customer_username = customer_username
        self.car = car

class CarRentalSystem:
    def __init__(self):
        # Default admin
        self.admins = {"ekansh": "admin123"}
        self.customers = {}
        self.cars = {}
        self.bookings = []

        self.setup_database()
        self.load_customers()
        self.load_cars()

    def setup_database(self):
        self.conn = sqlite3.connect('rental_system.db')
        self.cursor = self.conn.cursor()

        # Customers Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                                username TEXT PRIMARY KEY,
                                password TEXT NOT NULL)''')

        # Cars Table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                                car_id TEXT PRIMARY KEY,
                                brand TEXT NOT NULL,
                                model TEXT NOT NULL,
                                year TEXT NOT NULL,
                                rental_rate REAL NOT NULL,
                                is_available INTEGER NOT NULL)''')

        self.conn.commit()

    def load_customers(self):
        self.cursor.execute("SELECT username, password FROM customers")
        for username, password in self.cursor.fetchall():
            self.customers[username] = Customer(username, password)

    def load_cars(self):
        self.cursor.execute("SELECT car_id, brand, model, year, rental_rate, is_available FROM cars")
        for car_id, brand, model, year, rental_rate, is_available in self.cursor.fetchall():
            self.cars[car_id] = Car(car_id, brand, model, year, rental_rate, bool(is_available))

    def register_customer(self):
        username = input(Fore.YELLOW + "Enter new username: ")
        if username in self.customers:
            print(Fore.RED + "Username already exists. Try logging in.")
            return
        password = input(Fore.YELLOW + "Enter password: ")
        try:
            self.cursor.execute("INSERT INTO customers (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            self.customers[username] = Customer(username, password)
            print(Fore.GREEN + f"Customer '{username}' registered successfully!")
        except sqlite3.IntegrityError:
            print(Fore.RED + "Username already exists. Try again.")

    def customer_login(self):
        username = input(Fore.YELLOW + "Enter username: ")
        password = input(Fore.YELLOW + "Enter password: ")
        customer = self.customers.get(username)
        if customer and customer.password == password:
            print(Fore.GREEN + f"Welcome back {username}!")
            self.customer_menu(customer)
        else:
            print(Fore.RED + "Invalid credentials.")

    def admin_login(self):
            """
            Authenticate an admin user by prompting for username and password.
    
            This method:
            1. Prompts the user to enter admin username
            2. Prompts the user to enter admin password
            3. Checks credentials against the self.admins dictionary
            4. If credentials are valid:
               - Prints a welcome message
               - Calls the admin_menu() method
            5. If credentials are invalid:
               - Prints an error message
    
            Note: To update Python in terminal, use:
            - For Ubuntu/Debian: sudo apt update && sudo apt upgrade python3
            - For macOS with Homebrew: brew update && brew upgrade python
            - For Windows: Download latest version from python.org or use winget
            """
            username = input(Fore.YELLOW + "Enter admin username: ")
            password = input(Fore.YELLOW + "Enter admin password: ")
            if self.admins.get(username) == password:
                print(Fore.GREEN + f"Welcome Admin: {username}!")
                self.admin_menu()
            else:
                print(Fore.RED + "Invalid admin credentials.")
    def admin_login(self):
        username = input(Fore.YELLOW + "Enter admin username: ")
        password = input(Fore.YELLOW + "Enter admin password: ")
        if self.admins.get(username) == password:
            print(Fore.GREEN + f"Welcome Admin: {username}!")
            self.admin_menu()
        else:
            print(Fore.RED + "Invalid admin credentials.")

    def add_car(self):
        car_id = input(Fore.YELLOW + "Enter Car ID: ")
        if car_id in self.cars:
            print(Fore.RED + "Car ID already exists.")
            return
        brand = input(Fore.YELLOW + "Enter Brand: ")
        model = input(Fore.YELLOW + "Enter Model: ")
        year = input(Fore.YELLOW + "Enter Year: ")
        rental_rate = float(input(Fore.YELLOW + "Enter Rental Rate per day: "))
        car = Car(car_id, brand, model, year, rental_rate)
        self.cars[car_id] = car

        self.cursor.execute('''INSERT INTO cars (car_id, brand, model, year, rental_rate, is_available)
                               VALUES (?, ?, ?, ?, ?, ?)''', (car_id, brand, model, year, rental_rate, 1))
        self.conn.commit()

        print(Fore.GREEN + f"Car {brand} {model} added successfully!")

    def remove_car(self):
        if not self.cars:
            print(Fore.RED + "No cars available to remove.")
            return

        car_id = input(Fore.YELLOW + "Enter Car ID to remove: ")
        if car_id in self.cars:
            del self.cars[car_id]
            self.cursor.execute("DELETE FROM cars WHERE car_id = ?", (car_id,))
            self.conn.commit()
            print(Fore.GREEN + f"Car {car_id} removed successfully!")
        else:
            print(Fore.RED + "Car ID not found.")

    def view_cars(self, available_only=False):
        cars_found = False
        for car in self.cars.values():
            if available_only and not car.is_available:
                continue
            status = "Available" if car.is_available else "Booked"
            print(Fore.CYAN + f"ID: {car.car_id} | {car.brand} {car.model} ({car.year}) - ₹{car.rental_rate}/day [{status}]")
            cars_found = True
        if not cars_found:
            print(Fore.RED + "No cars available at the moment.")

    def book_car(self, customer: Customer):
        available_cars = [car for car in self.cars.values() if car.is_available]
        if not available_cars:
            print(Fore.RED + "Sorry, no cars available for booking at the moment.")
            return

        self.view_cars(available_only=True)
        car_id = input(Fore.YELLOW + "Enter Car ID to book: ")
        car = self.cars.get(car_id)
        if car and car.is_available:
            booking = Booking(customer.username, car)
            self.bookings.append(booking)
            car.is_available = False
            customer.booked_cars.append(car)

            
            self.cursor.execute("UPDATE cars SET is_available = 0 WHERE car_id = ?", (car_id,))
            self.conn.commit()

            print(Fore.GREEN + f"Car {car.brand} {car.model} booked successfully!")
        else:
            print(Fore.RED + "Invalid Car ID or Car not available.")

    def return_car(self, customer: Customer):
        if not customer.booked_cars:
            print(Fore.RED + "You have no cars to return.")
            return

        print(Fore.CYAN + "Your booked cars:")
        for idx, car in enumerate(customer.booked_cars, 1):
            print(Fore.YELLOW + f"{idx}. {car.brand} {car.model} ({car.year})")
        choice = int(input(Fore.YELLOW + "Select car to return (number): "))
        if 1 <= choice <= len(customer.booked_cars):
            car = customer.booked_cars.pop(choice - 1)
            car.is_available = True

            
            self.cursor.execute("UPDATE cars SET is_available = 1 WHERE car_id = ?", (car.car_id,))
            self.conn.commit()

            print(Fore.GREEN + f"Returned {car.brand} {car.model} successfully!")
        else:
            print(Fore.RED + "Invalid choice.")

    def admin_menu(self):
        while True:
            print(Fore.MAGENTA + "\n--- Admin Menu ---")
            print(Fore.CYAN + "1. Add Car")
            print(Fore.CYAN + "2. Remove Car")
            print(Fore.CYAN + "3. View All Cars")
            print(Fore.CYAN + "4. View Bookings")
            print(Fore.CYAN + "5. Logout")
            choice = input(Fore.YELLOW + "Enter choice: ")
            if choice == '1':
                self.add_car()
            elif choice == '2':
                self.remove_car()
            elif choice == '3':
                self.view_cars()
            elif choice == '4':
                self.view_bookings()
            elif choice == '5':
                break
            else:
                print(Fore.RED + "Invalid choice.")

    def customer_menu(self, customer: Customer):
        while True:
            print(Fore.MAGENTA + "\n--- Customer Menu ---")
            print(Fore.CYAN + "1. View Available Cars")
            print(Fore.CYAN + "2. Book a Car")
            print(Fore.CYAN + "3. Return a Car")
            print(Fore.CYAN + "4. Logout")
            choice = input(Fore.YELLOW + "Enter choice: ")
            if choice == '1':
                self.view_cars(available_only=True)
            elif choice == '2':
                self.book_car(customer)
            elif choice == '3':
                self.return_car(customer)
            elif choice == '4':
                break
            else:
                print(Fore.RED + "Invalid choice.")

    def view_bookings(self):
        if not self.bookings:
            print(Fore.RED + "No bookings yet.")
            return
        for booking in self.bookings:
            print(Fore.CYAN + f"{booking.customer_username} booked {booking.car.brand} {booking.car.model} ({booking.car.year})")

    def main_menu(self):
        while True:
            print(Fore.MAGENTA + "\n--- Welcome to Car Rental System ---")
            print(Fore.CYAN + "1. Admin Login")
            print(Fore.CYAN + "2. Customer Login")
            print(Fore.CYAN + "3. Customer Registration")
            print(Fore.CYAN + "4. Exit")
            choice = input(Fore.YELLOW + "Enter choice: ")
            if choice == '1':
                self.admin_login()
            elif choice == '2':
                self.customer_login()
            elif choice == '3':
                self.register_customer()
            elif choice == '4':
                print(Fore.GREEN + "Thank you for visiting! Exiting system.")
                self.conn.close()
                break
            else:
                print(Fore.RED + "Invalid choice.")

if __name__ == "__main__":
    system = CarRentalSystem()
    system.main_menu()