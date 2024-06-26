
# **AppointMeNext1**

AppointMeNext1 is a Django project for managing appointments between owners and customers.

## Description
The project provides the following features:
Creating appointments and managing a schedule.
Customer registration and profile management.
Reminders and alerts for appointments-will be added later.
Administrative reports on appointments and activity-will be added later.

## Installation
  1.Clone the repository:
  `git clone https://github.com/kettyvaisbrot/AppointMeNext1.git
  Navigate to the project directory:
  cd AppointMeNext1`

  2.Install dependencies:
  `pip install -r requirements.txt`

  3.Apply database migrations:
  `python manage.py migrate`

  4.Create a superuser (for admin access):
  `python manage.py createsuperuser`

  5.Run the development server:
  `python manage.py runserver`


## Usage
Access the admin interface at http://127.0.0.1:8000/ to manage appointments, users, and other data.
Users can register, log in, and schedule/cancel appointments through the web interface.

## Built With
[Python](https://www.python.org/downloads/) Ensure you have python installed.

[Django framework](https://docs.djangoproject.com/en/5.0/topics/install/) Ensure you have Django installed.

## License
This project is licensed under the MIT License.
