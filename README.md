# Project Portfolio

---

## About the project

A portfolio and personal blog. In the future, this project may include creative
additions such as blog posts, creative showcases, and interactive elements.

--- 

## Technology Stack

### Backend

- Python 3.10+
- Django 5.0+
- Django Rest Framework 3.15+
- Redis 5.2+
- Celery 5.4+
- Postgresql 15+

### Frontend

- React
- CSS/SASS
- HTML
- JavaScript

### Other technologies

- Docker
- Docker Compose
- Nginx
- GitHub Actions CI/CD

---

## Getting Started

These instructions will help you run the project locally or in a Dockerized environment.

- Make sure Docker and Docker Compose are installed on your machine.
- Create the necessary `.env` files for configuration.

### Setup Instructions

1. **Clone the repository:**

    ```shell
   git clone https://github.com/yuldashov10/portfolio_project.git && cd portfolio_project
    ```

2. **Configure environment variables:**

    - Copy `.env.sample` to `.env` and fill in the necessary environment variables for the backend.
    - Similarly, copy `env.db.sample` to `.env.db` for the database configuration.

3. **Build and run the containers:**

    ```shell
   sudo docker-compose up --build -d
    ```

4. **Run migrations:**

   ```shell
   sudo docker-compose exec backend python manage.py migrate
   ```

5. **Create superuser:**

   ```shell
   sudo docker-compose exec backend python manage.py createsuperuser
   ```

6. **Collect static files:**

   ```shell
   sudo docker-compose exec backend python manage.py collectstatic --no-input
   ```

The backend application should now be available at http://localhost:8000

---

## Author:

- [Telegram](htpps://t.me/shyuldashov)

---

## Licence

This project is distributed under the `MIT License`. For more information, please see the [LICENSE](LICENSE) file.

---
