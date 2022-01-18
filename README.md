# invoice_bill

#How to run the application locally


Steps -->
1) Clone this repo and navigate to under parent directory(invoice_bill).
2) Create the virtualenv under the parent directory and activate it.
3) Execute the command "pip install -r requirements.txt"
4) Set DEBUG=False in api_store/settings.py file
5) Execute the command 'python manage.py makemigrations'
6) Then execute the sane command with app name ''python manage.py makemigrations apistore_app'
7) Then execute the migrate command 'python manage.py migrate'
8) Then run the server 'python manage.py runserver' access the default url(https://127.0.0.1:8000).
9) Create the super user 'python manage.py createsuperuser'.(Note: You can also register new account in the application only).
10) Then login to the app and add some items for purchase and click on 'go to cart" which has total amount.
