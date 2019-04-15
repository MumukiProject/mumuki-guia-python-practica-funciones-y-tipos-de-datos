def test_me_conviene_25_8_es_falso(self):
  self.assertEqual(not me_conviene(25, 8))

def test_me_conviene_40_8_es_verdadero(self):
  self.assertEqual(me_conviene(40, 8))

def test_me_conviene_40_10_es_verdadero(self):
  self.assertEqual(me_conviene(40, 10))

def test_me_conviene_40_4_es_falso(self):
  self.assertEqual(not me_conviene(40, 4))

def test_me_conviene_50_16_es_falso(self):
  self.assertEqual(not me_conviene(50, 16))

