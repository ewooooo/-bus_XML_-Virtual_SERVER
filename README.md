# bus_XML_ Virtual_SERVER

공공데이터 포털 버스도착정보 가상 서버(시각장애인 버스이용편의 개선 시스템 시연용

```buildoutcfg
pip install django
pip install djangorestframework
pip install markdown       
pip install django-filter 
pip install djangorestframework-xml
```

라즈베리파이에서는 pip3 이용

```buildoutcfg
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```