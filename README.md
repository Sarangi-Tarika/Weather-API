# Code Challenge Template

# Frameworks

- Django
- Django Rest Framework

# Database

- SQLite
  <br>

# Structure

- wx_data --> Weather data
- src --> Source Code
- answers --> output.log

# Steps to run the program

- Create and run the virtual environment using commands: <br>

  ```bash
  pip install virtualenv
  virtualenv env
  ```

  To activate virtual environment :

  ```bash
  env/Scripts/activate (in Windows)
  source env/bin/activate (in Linux and Mac)
  ```


- Install all the requirements using command <br>

```bash
  pip install -r requirements.txt
```

- Navigate to “src” directory using command cd in terminal

- Migrate the models: <br>

```bash
  python src/manage.py makemigrations
  python src/manage.py migrate
```

- Ingesting the data:<br>

```bash
    python src/manage.py ingest
```

- Run the python server using command: <br>

```bash
  python src/manage.py runserver
```

- And other functionalities can be accessed through these API links: <br>
  http://127.0.0.1:8000/api/swagger/<br>
  http://127.0.0.1:8000/api/weather<br>
  http://127.0.0.1:8000/api/weather/stats/
- With query params it can also be accessed such as : <br>
  http://127.0.0.1:8000/api/weather/?date=20100101
  <br><br>

# Tests

```bash
  cd src
  python manage.py test
```

# AWS Deployment

### Deploy Django API:

- Use AWS Elastic Beanstalk to easily deploy and run a web application in multiple languages, including Python, which is used by Django.
- Configure a load balancer to handle incoming traffic and distribute it to multiple instances of the Django application.

### Deploy database:

- Use Amazon Relational Database Service (RDS) to host a PostgreSQL database. It is fully managed and provides a scalable and secure database solution.
- Configure database access in Django to securely connect to the RDS instance.

### Data Storage:

- Use AWS S3 to store text files.

### Scheduling data ingestion:

- Use AWS ECS FARGATE to run the data ingestion code on a schedule and ECR for storing the Image.
- Use Amazon CloudWatch Events to set up a rule to trigger the Fargate tasks at specific intervals.
- Store the ingested data in the RDS database.

### Conclusion

- With this approach, you get a scalable, secure, and easily managed deployment of your Django API, database, and data ingestion code.
- The load balancer and auto-scaling features of AWS Elastic Beanstalk and Amazon RDS will ensure that the API and database can handle changing levels of traffic, while AWS ECS FARGATE and Amazon CloudWatch Events allow you to run the data ingestion code as needed without having to manage any infrastructure.

# Screen Shot

![Alt text](/ss.png?raw=true "Optional Title")
