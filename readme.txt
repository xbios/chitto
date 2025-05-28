
git pull origin main


myenv\Scripts\activate

.venv\Scripts\activate.ps1


python -m pip list

pip install -r requirements.txt


python manage.py showmigrations

python manage.py makemigrations

python manage.py migrate



python.exe .\manage.py runserver


python.exe .\manage.py shell

from shop.models import Product
Product.objects.get(pk=2)
Product.objects.get(pk=2).save()

c1 = Category.objects.get(pk=1)
p1 = Product.objects.get(pk=2)
p1.category = c1
p1.category
p1.save()

c3 = Category(name="veri analizi")
c3.save()
p1.caregory = c3
p1.save()
p1.caregory.name

urun = Product.objects.filter(isActive=True)




