from django.test import TestCase
from A0_blog.models import Arbitro


class A0_blog_Tests(TestCase):
    def test_creacion_arbitro(self):
        arbitro = Arbitro(
            nombre="Nombre Prueba", edad=18, experiencia=Arbitro.EXPERIENCIA.MENOR5
        )
        arbitro.save()

        self.assertEqual(Arbitro.objects.count(), 1)
        self.assertEqual(arbitro.nombre, "Nombre Prueba")
        self.assertEqual(arbitro.edad, 18)
        self.assertEqual(arbitro.experiencia, Arbitro.EXPERIENCIA.MENOR5)

    def test_arbitro_str(self):
        arbitro = Arbitro(
            nombre="Nombre prueba", edad=18, experiencia=Arbitro.EXPERIENCIA.MENOR5
        )
        arbitro.save()

        self.assertEqual(arbitro.__str__(), "Nombre prueba, 18, Menor a 5 años")
