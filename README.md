# Car Rental Management System 🚗
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![SQLite](https://img.shields.io/badge/database-SQLite-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A comprehensive Object-Oriented Programming (OOP) project built in Python for managing car rentals with separate admin and customer functionalities.

## 📋 Table of Contents
- [Features](#-features)
- [Technologies Used](#️-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Classes Overview](#️-classes-overview)
- [Database Schema](#️-database-schema)
- [Key OOP Concepts](#-key-oop-concepts-demonstrated)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### Admin Features
- **Secure Admin Login** - Default credentials (username: `ekansh`, password: `admin123`)
- **Car Management**
  - Add new cars to the fleet
  - Remove cars from the system
  - View all cars (available and booked)
- **Booking Overview** - View all customer bookings
- **Persistent Data Storage** - SQLite database integration

### Customer Features
- **User Registration** - Create new customer accounts
- **Secure Login System** - Password-protected customer accounts
- **Car Browsing** - View available cars with details
- **Car Booking** - Book available cars
- **Car Return** - Return previously booked cars
- **Personal Booking History** - Track your booked cars

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **SQLite3** - Database for persistent storage
- **Colorama** - Terminal color formatting
- **PyFiglet** - ASCII art text generation
- **Object-Oriented Programming** - Clean code architecture

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/exorev07/Car-Rental-Management-System-OOP.git
   cd Car-Rental-Management-System-OOP
   ```

2. **Install required dependencies**
   ```bash
   pip install colorama pyfiglet
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 🚀 Usage

### Getting Started
1. Run the application using `python main.py`
2. Choose from the main menu options:
   - **Admin Login** - Access administrative features
   - **Customer Login** - Access customer features
   - **Customer Registration** - Create a new customer account
   - **Exit** - Close the application

### Admin Access
- **Username**: `ekansh`
- **Password**: `admin123`

### Sample Workflow
1. **Admin Setup**: Login as admin and add some cars to the system
2. **Customer Registration**: Create a customer account
3. **Browse & Book**: Login as customer, view available cars, and make bookings
4. **Return**: Return cars when done

## 📁 Project Structure

```
Car-Rental-Management-System-OOP/
│
├── main.py                 # Main application file
├── rental_system.db        # SQLite database (created automatically)
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies (optional)
```

## 🏗️ Classes Overview

### Core Classes

#### `User` (Base Class)
- Base class for all users
- Attributes: `username`, `password`

#### `Admin` (Inherits from User)
- Administrator with system management privileges
- Inherits all User attributes

#### `Customer` (Inherits from User)
- Regular customers who can book cars
- Additional attribute: `booked_cars` list

#### `Car`
- Represents a rental car
- Attributes: `car_id`, `brand`, `model`, `year`, `rental_rate`, `is_available`

#### `Booking`
- Represents a car booking
- Links customers with their booked cars

#### `CarRentalSystem`
- Main system class managing all operations
- Handles database operations, user authentication, and business logic

## 🗄️ Database Schema

### Customers Table
```sql
CREATE TABLE customers (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
);
```

### Cars Table
```sql
CREATE TABLE cars (
    car_id TEXT PRIMARY KEY,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    year TEXT NOT NULL,
    rental_rate REAL NOT NULL,
    is_available INTEGER NOT NULL
);
```

## 🎯 Key OOP Concepts Demonstrated

- **Inheritance** - Admin and Customer classes inherit from User
- **Encapsulation** - Data and methods bundled within classes
- **Polymorphism** - Different user types with specific behaviors
- **Abstraction** - Complex database operations abstracted into simple methods

## 🔧 Future Enhancements

- [ ] Add rental duration and pricing calculation
- [ ] Implement booking history with dates
- [ ] Add car categories (SUV, Sedan, Hatchback)
- [ ] Email notifications for bookings
- [ ] GUI interface using Tkinter or PyQt
- [ ] Advanced search and filtering options
- [ ] Payment integration
- [ ] Rental agreement generation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Ekansh Arohi (@exorev07)**  
Data Science & AI undergrad at IIIT Naya Raipur     
Passionate about electronics, smart hardware prototyping, and real-world problem solving through tech.   
🔗 [LinkedIn Profile](https://www.linkedin.com/in/ekansharohi)

> “Find what you love and let it kill you.”


## 📞 Support

If you have any questions or issues, please open an issue on GitHub or contact the author.

---

⭐ **Star this repository if you found it helpful!**
