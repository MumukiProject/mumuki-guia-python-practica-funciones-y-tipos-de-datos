def test_escribir_cartelito_Dra_Ana_Pérez_es_Dra_Ana_Pérez(self):
  self.assertEqual(escribir_cartelito("Dra.", "Ana", "Pérez"), "Dra. Ana Pérez")

def test_escribir_cartelito_Dr_Julio_Gelman_es_Dr_Julio_Gelman(self):
  self.assertEqual(escribir_cartelito("Dr.", "Julio", "Gelman"), "Dr. Julio Gelman")

