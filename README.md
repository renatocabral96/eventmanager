# Event Manager
Django Restful API for event management in cities

## Connection to the database

For this project, it was used a PostgreSQL docker image with the PostGIS extension:

docker pull mdillon/postgis


-----To run it: <br />
docker run --name some-postgis -e POSTGRES_PASSWORD=mysecretpassword -d mdillon/postgis


-----To connect to the database: <br />
docker run -it --link some-postgis:postgres --rm postgres \
    sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'
    
    
## Starting the Django API

-----Clone the project: <br />
https://github.com/renatocabral96/eventmanager.git


------Start a a virtual environment: <br />
source venv/bin/activate


------Install the project dependencies: <br />
pip install -r requirements.txt


------Make migrations to database: <br />
python manage.py migrate

------Create a superuser: <br />
python manage.py createsuperuser

-----Make migrations to the application: <br />
python manage.py makemigrations 

-----Run the server: <br />
python manage.py runserver

## Endpoints
http://127.0.0.1:8000/events/ ---- Allows POST and GET event occurrences <br />
http://127.0.0.1:8000/events/"eventid"/ ---- Allows PUT, PATCH and DELETE event occurrences <br />
http://127.0.0.1:8000/events/filter/ ---- Allows filtering event occurrences by Author, Location and Category (Event Type) <br />
http://127.0.0.1:8000/admin/ ---- Administrator interface 
