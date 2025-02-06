# Custody App

## Overview
Custody App is a PyQt5-based application for managing assets, loans, and employee records. It supports multiple languages and includes features for adding, editing, and searching records.

## Features
- **Employee Management**: Add, edit, and remove employee records.
- **Asset Allocation and Inventory Management**: Manage asset allocation and inventory.
- **Loan Management**: Manage loans and payments.
- **Multi-language Support**: Supports English and Arabic.
- **Dark Mode**: Toggle dark mode for better visibility.

## Screenshots

### Login Page
![Login Page](https://github.com/Custody-App/Custody-App/blob/main/Project-C2-Team-5/UI%20Photos/Login_page.png)
  
### Asset Management
![Asset Management](https://github.com/Custody-App/Custody-App/blob/main/Project-C2-Team-5/UI%20Photos/Assets_record.png)
### Loan Management
![Loan Management](https://github.com/Custody-App/Custody-App/blob/main/Project-C2-Team-5/UI%20Photos/Loan_record.png)

## Getting Started

### Prerequisites
- Python 3.7+
- PyQt5
- SQLModel

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/CustodyApp.git
    cd CustodyApp
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application
1. Run the application:
    ```sh
    python main.py
    ```

## Usage
1. Launch the application.
2. Log in using your credentials. If you don't have an account, contact the administrator to create one for you.
3. Use the various tabs to manage employees, assets, loans, and payments.

## Project Structure
- **main.py**: Entry point of the application.
- **LoginPage.py**: Handles the login page UI and functionality.
- **ProgramMainWindow.py**: Main window of the application.
- **RuternPage.py**: Handles the return page UI and functionality.
- **Localization.py**: Contains translation data and functions.
- **encpass.py**: Contains password hashing functions.
- **data_opersion.py**: Contains data operation classes and methods.
- **Data_modeling.py**: Contains database models and schema definitions.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
