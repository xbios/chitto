myenv\Scripts\activate

.venv\Scripts\activate.ps1


python -m pip list

pip install -r requirements.txt


python manage.py showmigrations

python manage.py makemigrations

python manage.py migrate



python.exe .\manage.py runserver


from shop.models import Product
Product.objects.get(pk=2)
Product.objects.get(pk=2).save()

