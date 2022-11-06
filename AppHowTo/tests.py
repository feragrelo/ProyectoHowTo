from django.test import TestCase
from AppHowTo.models import Articulo,Autor


class ViewTestCase(TestCase):
    
    def test_crear_autor(self):
        autor1= Autor.objects.create(nombre="Pablo",apellido="Vegetti",email="pv@gmail.com")
        autor2= Autor.objects.create(nombre="Miguel",apellido="Suarez",email="mg@gmail.com")
        todos_los_autores = Autor.objects.all()
        assert len(todos_los_autores) == 2
        assert autor1.nombre == "Pablo"
        assert autor2.email == "mg@gmail.com"

    def test_crear_articulo(self):
        autor= Autor.objects.create(nombre="Pablo",apellido="Vegetti",email="pv@gmail.com")
        Articulo.objects.create(nombre="Belgrano campeón", contenido="Belgrano es locura belgrano es pasión",autor=autor)
        todos_los_articulos = Articulo.objects.all()
        todos_los_autores = Autor.objects.all()
        assert len(todos_los_articulos) == 1
        assert todos_los_articulos[0].contenido == "Belgrano es locura belgrano es pasión"
        
    
    