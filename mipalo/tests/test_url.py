from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mipalo.views import*

class Testurls(SimpleTestCase):

    def test_url(self):
      url= reverse('productos')
      print(resolve(url))
      self.assertEquals(resolve(url).func,productos)