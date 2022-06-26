# blango

Starting point for the Advanced Django course. This is the equivalent of the following command:

```bash
$ django-admin.py startproject blango
```
Navigate to the project and run the following commands
```bash
$ python3 manage.py runserver 
```
If you are using linux but if you are using windows you can just run ```python manage.py runserver``` it is also going to for you.

After runnig the previous commands you would need to create a migration and then migrate the changes to the database using the following commands

```bash
$ python3 manage.py makemigrations 
```
Then run

```bash
$ python3 manage.py migrate 
```
