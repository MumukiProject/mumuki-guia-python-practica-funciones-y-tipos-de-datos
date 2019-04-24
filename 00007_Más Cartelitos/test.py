  
  def test_escribir_cartelito_Dra_Ana_Pérez_false_es_Dra_Ana_Pérez(self):
    self.assertEqual(escribir_cartelito("Dra.", "Ana", "Pérez", False), "Dra. Ana Pérez")
  
  def test_escribir_cartelito_Dr_Julio_Gelman_false_es_Dr_Julio_Gelman(self):
    self.assertEqual(escribir_cartelito("Dr.", "Julio", "Gelman", False), "Dr. Julio Gelman")
  
  def test_escribir_cartelito_Dra_Ana_Pérez_true_es_Dra_Pérez_(self):
    self.assertEqual(escribir_cartelito("Dra.", "Ana", "Pérez", True), "Dra. Pérez")
  
  def test_escribir_cartelito_Dr_Julio_Gelman_true_es_Dr_Gelman_(self):
    self.assertEqual(escribir_cartelito("Dr.", "Julio", "Gelman", True), "Dr. Gelman")
  
