from django.test import TestCase
from mipalo.models import *

class TestModels(TestCase):

    def test_model(self):
        self.productosprueba = tablaproducto.objects.create(
            producto="Leche",
            tipoproducto="Lacteo",
            marcaproducto="Salud",
            descripcionproducto="Leche salud de alta calidad",
            stockproducto=2,
            precioproducto=9.50
        )