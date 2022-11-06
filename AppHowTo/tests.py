from django.test import TestCase
from AppHowTo.models import Articulo


class ViewTestCase(TestCase):

    def test_crear_articulo(self):
        Articulo.objects.create(nombre="Belgrano campeón", contenido="Belgrano es locura belgrano es pasión",autor="Vegetti")
        todos_los_articulos = Articulo.objects.all()
        assert len(todos_los_articulos) == 1
        assert todos_los_articulos[0].contenido == "Belgrano es locura belgrano es pasión"