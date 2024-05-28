# Django Jazz Website

This is a Django project for a jazz band website. The site includes features for user authentication, blogging, polls, and contact forms. Users can register, sign in, vote in polls, view blog posts about upcoming events, and submit booking inquiries.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Docker](#docker)
4. [Development](#development)


## Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Demayne/django-jazz-website.git
    cd django-jazz-website
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin interface:

    ```bash
    python manage.py createsuperuser
    ```

## Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Open a web browser and navigate to `http://127.0.0.1:8000/`.

3. Access the admin interface at `http://127.0.0.1:8000/admin/`.

## Docker

To run the application using Docker:

1. Build the Docker image:

    ```bash
    docker build -t django-jazz-website .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8000:8000 django-jazz-website
    ```

3. Open a web browser and navigate to `http://127.0.0.1:8000/`.

## Development

### Adding a .gitignore file

A `.gitignore` file is included to exclude unnecessary files such as binaries and virtual environments. Make sure to review and modify it as needed for your project.

### Requirements.txt

Ensure your project has a `requirements.txt` file to simplify dependency installation:

```bash
pip freeze > requirements.txt
