# Jazz Band Django Project

## Description
This is a Django project for a jazz band website, including features for blogging, polls, and contact forms. Users can register, sign in, vote in polls, view blog posts about upcoming events, and submit booking inquiries.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Credits](#credits)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/demayne/django-jazz-website.git
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

## Usage
1. Run the development server:
    ```bash
    python manage.py runserver
    ```

2. Open a web browser and navigate to `http://127.0.0.1:8000/`.

3. To use Docker:
    ```bash
    docker build -t jazzband .
    docker run -p 8000:8000 jazzband
    ```

## Credits
- [Demayne Govender](https://github.com/demayne)
