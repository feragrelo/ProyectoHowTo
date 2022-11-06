from django.test import TestCase
from AppHowTo.models import Articulo
from django.contrib.auth.models import User

class ViewTestCase(TestCase):
    
    def test_crear_user(self):
        user1=User.objects.create(username="Pepe", password="admin123",email="pepito@gmail.com")
        user2=User.objects.create(username="Juan", password="admin123",email="juancho@gmail.com")
        
        todos_los_user = User.objects.all()
        assert len(todos_los_user) == 2
        assert user1.username == "Pepe"
        assert user2.email == "juancho@gmail.com"

    def test_crear_articulo(self):
        user=User.objects.create(username="Pepe", password="admin123",email="pepito@gmail.com")
        Articulo.objects.create(nombre="Belgrano campeón", contenido="Belgrano es locura belgrano es pasión",user=user)
        todos_los_articulos = Articulo.objects.all()
        todos_los_user = User.objects.all()
        assert len(todos_los_articulos) == 1
        assert todos_los_articulos[0].contenido == "Belgrano es locura belgrano es pasión"
        
    
    