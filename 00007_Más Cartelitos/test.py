def test_escribir_cartelito_Dra_Ana_Pérez_false_es_Dra_Ana_Pérez(self):
  self.assertEqual(escribir_cartelito("Dra.", "Ana", "Pérez", false), "Dra. Ana Pérez")

def test_escribir_cartelito_Dr_Julio_Gelman_false_es_Dr_Julio_Gelman(self):
  self.assertEqual(escribir_cartelito("Dr.", "Julio", "Gelman", false), "Dr. Julio Gelman")

def test_escribir_cartelito_Dra_Ana_Pérez_true_es_Dra_Pérez_(self):
  self.assertEqual(escribir_cartelito("Dra.", "Ana", "Pérez", true), "Dra. Pérez")

def test_escribir_cartelito_Dr_Julio_Gelman_true_es_Dr_Gelman_(self):
  self.assertEqual(escribir_cartelito("Dr.", "Julio", "Gelman", true), "Dr. Gelman")

