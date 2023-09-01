
# Django Calculator Web App

![Calculator](https://raw.githubusercontent.com/Ashok-Prajapati2/django_project/main/screenshot.png)

This is a simple web application built with Django that provides a calculator interface. Users can perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Perform basic arithmetic operations.
- Clear the input field.
- Handle form submissions.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (3.x recommended)
- Django (3.x recommended)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Ashok-Prajapati2/django_project.git

    Navigate to the project directory:

    bash

cd django_project

Install the required Python packages using pip:

bash

    pip install -r requirements.txt

Usage

    Start the Django development server:

    bash

    python manage.py runserver

    Open your web browser and visit http://localhost:8000/calculator/ to access the calculator.

    Enter numbers and operators (e.g., 1+2*3) in the input field.

    Click the "=" button to calculate the result.


How It Works

    The application uses Django views to handle different pages:
        homepage - Renders the homepage with a calculator.
        about - Renders the about page with optional data.
        form - Handles form submissions and redirects to the about page.
        submitform - Handles form submissions and returns the username.
        calculator - Performs calculations based on user input.

Contributing

If you'd like to contribute to this project, please follow these guidelines:

    Fork the repository.
    Create a new branch (git checkout -b feature/your-feature-name).
    Make your changes and commit them (git commit -m 'Add some feature').
    Push to the branch (git push origin feature/your-feature-name).
    Create a new Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    Django - The web framework used.
    Bootstrap - CSS framework for styling.

Contact

If you have any questions or feedback, please contact Ashok Prajapat