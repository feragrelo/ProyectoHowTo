from django.test import TestCase
from AppConsulta.models import Consulta
from django.contrib.auth.models import User

class ViewTestCase(TestCase):
    
    def test_crear_consulta(self):
        user=User.objects.create(username="Carlos", password="admin123",email="carlos@gmail.com")
        consulta= Consulta.objects.create(user=user,contenido="por qué al ingresar.....",telefono="1651616",email="carlos@gmail.com")
        
        todos_los_user= User.objects.all()
        todas_las_consultas = Consulta.objects.all()
        assert len(todas_las_consultas) == 1
        assert todas_las_consultas[0].contenido == "por qué al ingresar....."