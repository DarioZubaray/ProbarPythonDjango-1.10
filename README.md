# Try Django

### Obtener las versiones de python y pip
```
python --version
pip --version
```

### Interprete de python
```
python
```

##### Para salir del interprete
```
exit()
```

### conocer los paquetes instaldo por pip
```
pip freeze
```

### instalar virtualenv
```
pip install virtualenv 
```

### ejecutar virtualenv sobre la carpeta deseada
```
virtualenv .
```

### activar virtualenv 
```
.\Scripts\activate
```

### instalar django espeficando una version
```
pip install django==1.10
```

### crear proyecto
```
python .\Scripts\django-admin.py startproject miApp
```

### renombrar el directorio del proyecto y entrar en él
```
ren miApp src && cd src
```

### correr servidor
```
python manage.py runserver
```

### realizar las migraciones
```
python manage.py migrate
```

### crear un usuario administrador
```
python manage.py createsuperuser
```

### crear app dentro del proyecto
```
python manage.py startapp boletin
```

### realizar las migraciones y aplicarlas
```
python manage.py makemigrations && python manage.py migrate
```

### utilizar el python shell
```
python manage.py shell
    from boletin.models import Registrado
    
    gente = Registrado.objects.all()
    gente
    <QuerySet []>
    
    persona1 = Registrado.objects.create(nombre='Dario', email='dario@email.com')
    persona1
    <Registrado: dario@email.com>
    
    gente
    <QuerySet [<Registrado: dario@email.com>]>
    
    quit()
```
### enviar archivos estaticos al servidor
```
python manage.py collectstatic
```