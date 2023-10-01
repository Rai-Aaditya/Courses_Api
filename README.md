# Django Courses App 🎓

Welcome to the Django Courses App repository! This app allows you to manage courses and their deliveries.

## Directory Structure

1. **Server:** Contains configuration files for the Django app.
2. **Courses:** Contains Django app components (views, models, serializers, etc.).
3. **Docker:** Dockerization files for the backend.

## Course Entity

A course has the following attributes:
- **Title:** Introduction to Computer Architecture
- **Course Code:** CS 102
- **Description:** Provides a basic introduction to the architecture and algorithms of computer systems.

## Course Delivery Instance

An instance of course delivery contains the following attributes:
- **Year:** 2022, 2023
- **Semester:** 1, 2
- **Course ID:** 23

## API Endpoints

- **List/Create Courses:** `/api/courses/`
- **Retrieve Course Details:** `/api/courses/<int:pk>/`
- **Delete Course:** `/api/courses/<int:pk>/delete/`
- **Create New Course Instance:** `/api/instances/add/`
- **List Course Instances:** `/api/instances/`
- **List Instances by Year and Semester:** `/api/instances/<int:year>/<int:semester>/`
- **Retrieve Instance Details:** `/api/instances/<int:year>/<int:semester>/<int:pk>/`
- **Delete Course Instance:** `/api/instances/<int:year>/<int:semester>/<int:pk>`

## Usage

To set up the app and run it locally, follow these steps:
1. Clone this repository.
2. Navigate to the `Server` directory and configure `settings.py`.
3. Set up the database and apply migrations.
4. Run the Django development server.

Feel free to contribute and improve this project! 🚀

## Contributing

If you'd like to contribute, please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and submit a pull request.

