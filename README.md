# booking-machine

#### get started

  pip3 install -r requirements.txt
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
  
#### get started (with example db)

  pip3 install -r requirements.txt
  mysql -u root -p < dump.sql
  python3 manage.py runserver
