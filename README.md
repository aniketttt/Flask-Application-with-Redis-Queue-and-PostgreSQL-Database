# Form Submission with Redis Queue and PostgreSQL

This project is a simple web application for submitting data through a form, storing it in a Redis queue, and then inserting it into a PostgreSQL database. It includes a feature to view the submitted data in a table format.

## Features

- Submit data via a web form
- Store data in a Redis queue
- Insert data into PostgreSQL database
- View submitted data in a table

## Technologies Used

- Python
- Flask
- Redis
- PostgreSQL
- Docker

## Project Structure
<pre>
.
├── Dockerfile
├── Dockerfile.worker
├── app.py
├── worker.py
├── requirements.txt
├── requirements-worker.txt
├── templates
│   ├── index.html
│   ├── view_data.html
│   └── success.html
└── static
    └── style.css
        </pre>

## Setup Instructions

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/aniketttt/testing.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```
3. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```
4. Access the application in your web browser at http://localhost:5000

## Application Endpoints

- `/` - Form submission page
- `/submit` - Form submission handler (POST)
- `/success` - Success message page
- `/view_data` - View submitted data

## Code Overview

### app.py

Main Flask application file. Contains routes for form submission, success message, and viewing data.

### worker.py

Worker script that processes the Redis queue and inserts data into the PostgreSQL database.

### templates/

Directory containing HTML templates for the Flask application.

### static/

Directory containing static files such as CSS for the Flask application.

## Contact

If you have any questions or need further assistance, feel free to contact me at [your-email@example.com](mailto:your-email@example.com).



