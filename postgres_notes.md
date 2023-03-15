# Setting up a postgres database

Some useful links:

https://youtu.be/-LwI4HMR_Eg
https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart

## The postgres 'user' account on Linux

When you install the PostgreSQL database on a Linux system, it creates a system user account named postgres by default. This user account is used to run the PostgreSQL server process and manage the PostgreSQL system files.

The postgres user account is created with restricted privileges and cannot log in to the system shell. It is also typically configured with its own home directory and environment variables.

In addition to the postgres user account, PostgreSQL also creates a default PostgreSQL database cluster with a set of default users and databases. These users and databases are managed by the PostgreSQL server process and are not the same as system user accounts.

So, to summarize, the postgres account is a system user account that is created by the PostgreSQL database installer on Linux systems to run the PostgreSQL server process and manage the PostgreSQL system files.

## Install postgres

`sudo apt install postgresql postgresql-contrib`

Postgresql is installed in `/etc/postgresql/`

See postgres commands with `service postgresql`

This gives us: {start|stop|restart|reload|force-reload|status}

## See postgresql manual

From linux terminal `man psogresql`

## Switch to postgres user

Installing postgres creates a special postgres user.

Run commands as the postgres user:

`sudo -i -u postgres`

`sudo -i -u postgres` maintains the permissions of the user who calls the postgres user. Users can also be switched with `sudo su postgres`. The `su` command switches users, which is similar, but the permissions of the user switched to are now used (which may be lower permission).

Or open postgres directly as the postgres user:

`sudo -u postgres psql`

## Start service:

To have postgressql start automatically (e.g. on computer reset) use the following command:

`sudo systemctl start postgresql.service`

## Open postgres command prompt

psql

## Exit postgress 

\q

## Switch back to main user

exit

## List databases, tables, etc

From the postgres command prompt:

`\l` lists databases
`du` lists users

## Users and roles

In PostgreSQL, CREATE USER and CREATE ROLE are two different commands that can be used to create a new user or role in the database system.

The main difference between them is in the default privileges that are granted to the newly created user/role.

CREATE USER is used to create a new database user account that can connect to the database and own objects such as tables, views, and functions. By default, when you create a user with CREATE USER, the user has no special privileges or roles granted to them.

CREATE ROLE, on the other hand, is used to create a new role, which is a named group of privileges that can be granted to users or other roles. By default, when you create a role with CREATE ROLE, the role has no login ability, meaning it cannot be used to connect to the database.

In other words, a role is a set of permissions that can be granted to multiple users, while a user is an account that can connect to the database and own objects. A user can also be assigned one or more roles to inherit their permissions.

## Creating a new user account in postgres

`CREATE ROLE username WITH LOGIN PASSWORD 'password';`

CREATE USER metoffice WITH LOGIN PASSWORD 'weather123';

CREATE ROLE metoffice WITH LOGIN PASSWORD 'weather123';


Give a user super privileges:

ALTER USER metoffice WITH SUPERUSER;

## Allow access to databases

main/pg_hba.conf

## Granting selected privileges to users

GRANT INSERT, UPDATE ON TABLE my_table TO john;
GRANT ALL ON TABLE my_table TO john;


GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA schema_name TO username;


GRANT ALL PRIVILEGES ON DATABASE weather TO metoffice;

GRANT ALL OM TABLE IN SCHEMA public TO michael

## To give permission to create database 

ALTER USER username CREADTDB ;

## Change passwords

`ALTER USER usernam WITH PASSWORD 'new_password';`

## Delete user or role

(If needed you may need to reassign permissions to main postgres user:

`REASSIGN OWNED BY username TO postgres;`

DROP USER username;
DROP ROLE rolename;


