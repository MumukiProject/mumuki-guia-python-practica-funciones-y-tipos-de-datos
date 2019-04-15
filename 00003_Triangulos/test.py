def test_perimetro_triangulo_10_10_10_es_30(self):
  self.assertEqual(perimetro_triangulo(10, 10, 10), 30)

def test_perimetro_triangulo_12_10_10_es_32(self):
  self.assertEqual(perimetro_triangulo(12, 10, 10), 32)

def test_perimetro_triangulo_10_14_10_es_34(self):
  self.assertEqual(perimetro_triangulo(10, 14, 10), 34)

def test_perimetro_triangulo_10_10_15_es_35(self):
  self.assertEqual(perimetro_triangulo(10, 10, 15), 35)

def test_area_triangulo_10_10_es_50(self):
  self.assertEqual(area_triangulo(10, 10), 50)

def test_area_triangulo_10_2_es_10(self):
  self.assertEqual(area_triangulo(10, 2), 10)

