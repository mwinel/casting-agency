# todo-app

Just a simple todo app.

## Technologies

- [Python3](https://www.python.org/download/releases/3.0/)
- [Flask](https://palletsprojects.com/p/flask/)
- [Postgres](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [psycopg2](http://initd.org/psycopg/)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/#)
- [alembic](https://alembic.sqlalchemy.org/en/latest/)

## Installation

```
git clone https://github.com/mwinel/casting-agency.git
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Usage

Run the command below to start the app.

```
export FLASK_APP=app
export FLASK_DEBUG=True
flask run
```

## Unit tests

```
python -m unittest
```

## Running migrations

Use the following commands to run database migrations to add tables or columns.

```
flask db init
flask db migrate
flask db upgrade
```

In order to drop a table or column.

```
...
flask db downgrade
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
