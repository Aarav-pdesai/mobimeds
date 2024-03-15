# Mobimeds Application

The **Mobimeds** application is a simple desktop-based pharmacy management system implemented using Python's Tkinter for the graphical user interface and PIL (Pillow) for image processing. The application is designed to provide functionalities for both customers and store owners.

## Features

### Customer Module

- **Purchase**: Allows customers to make purchases.
- **Registration**: Customers can register, with special discounts for members.

### Owner Module

- **Employee Management**: Enables owners to manage employees.
- **Product Management**: Facilitates the management of products in the pharmacy.

### General Features

- **Authorization**: Secure access with an authorization code.
- **Responsive Design**: Utilizes Tkinter for a user-friendly interface.

## Installation

1. Ensure you have Python installed.
2. Install required libraries:
   ```bash
   pip install pillow
   ```
3. Run the application:
   ```bash
   python your_script_name.py
   ```

## Usage

- Upon running the application, a main window with two options (Customer and Owner) is displayed.
- Customers can make purchases or register, while owners need to enter an authorization code to access their module.
- Owners can manage employees and products within the dedicated Owner module.

## Dependencies
### libraries required
- Tkinter
- Pillow (PIL)

### Database Setup

To set up the database for this project, follow these steps:

1. **Database Dump File**: The SQL dump file (`mobitrans.sql`) containing the necessary database structure and data is provided in the `database` directory of this repository.

2. **MySQL Installation**: Ensure that MySQL is installed on your system. If not, you can download it from [MySQL Downloads](https://dev.mysql.com/downloads/).

3. **Importing Database Structure**:

   - Navigate to the `database` directory of this repository.
   - Open a terminal or command prompt.
   - Run the following command to import the SQL dump file into MySQL:
     ```bash
     mysql -u username -p database_name < mobitrans.sql
     ```
     Replace `username` with your MySQL username and `database_name` with the desired name of the new database (if different).

4. **Database Schema**: The database schema includes the following tables:
   
   - **allopathic_medicines**: This table stores information about allopathic medicines.
   - **ayurvedic_medicines**: This table stores information about ayurvedic medicines.
   - **employees**: This table stores information about employees.
   - **nutrition_fitness_supplements**: This table stores information about nutrition and fitness supplements.
   - **personal_care**: This table stores information about personal care products.
   - **shortterm_ailments**: This table stores information about short-term ailments.
## Authors

Aarav Desai
<br>
Ayush Bhatnagar
