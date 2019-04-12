Coingate api project

Simple way to run the project:

0. Clone the repository

1. Create enviroment, by following command: 
    vertualenv --python=python3.6 venv
    
2. Activate with:
    source venv/bin/activate
    
3. Install all requirements
    pip install -r requirements.txt
   
4. Make migrations and run the server
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    
5. Go to your brawser ang following the link: 127.0.0.1:8000

There are 2 languages, switched by buttons.

The pay button to make the payment data and send it to the Coingate.
After the pay passed press Back to merchant and it will redirect you to home page.

