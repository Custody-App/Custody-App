Collecting workspace information

Sure, here is a basic 

README.md

 file for your project:

```markdown
# Custody App

Custody App is a PyQt5-based application designed to manage assets, loans, and employee records. The application supports multiple languages and provides a user-friendly interface for managing various administrative tasks.

## Features

- **Asset Management**: Add, edit, and manage asset inventories.
- **Loan Management**: Add, edit, and manage loans and payments.
- **Employee Management**: Add, edit, and manage employee records.
- **Localization**: Supports multiple languages for the user interface.
- **Dark Mode**: Apply dark mode to the application interface.

## Project Structure

```
__pycache__/


Data_modeling.py




data_opersion.py




encpass.py




Localization.py




LoginPage.py




main.py




main.spec




ProgramMainWindow.py




README.md




resources.py




resources.qrc




RuternPage.py


```

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    python main.py
    ```

## Usage

- **Login**: Start the application and log in using your credentials.
- **Navigate**: Use the main window to navigate between different sections such as assets, loans, and employee records.
- **Localization**: Change the language of the user interface using the language selection option.

## Localization

The application supports multiple languages. The translations are managed in the 

Localization.py

 file. To add a new language, update the 

Localization.py

 file with the necessary translations.

## Development

### Adding New Features

1. Create a new branch for your feature:
    ```sh
    git checkout -b feature-name
    ```

2. Implement your feature and commit your changes:
    ```sh
    git add .
    git commit -m "Add feature description"
    ```

3. Push your branch and create a pull request:
    ```sh
    git push origin feature-name
    ```

### Running Tests

To run the tests, use the following command:
```sh
pytest
```

## Contributing

Contributions are welcome! Please read the CONTRIBUTING.md file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- PyQt5 for the GUI framework.
- SQLAlchemy for database management.
- All contributors and users for their support.

```
