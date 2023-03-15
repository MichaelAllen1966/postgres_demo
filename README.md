# postgres_demo

Testing use of postgres with Titanic data set.

## Installing postgres on Linux

`sudo apt install postgresql postgresql-contrib`

## Start service:

To have postgressql start automatically (e.g. on computer reset) use the following command:

`sudo systemctl start postgresql.service`

## Setting up virtual environment

This demo used Python 3.10

To set up virtual environment:

`python -m venv ven`

To activate virtual environment:

`source venv/bin/activate`

To install requirements:

`pip install -U -r requirements.txt`
