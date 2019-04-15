def test_escribe_un_cartelito_largo_cuando_el_nombre_completo_es_corto(self):
  self.assertEqual(escribir_cartelito_optimo("Ing.", "Carla", "Toledo"), "Ing. Carla Toledo")

def test_escribe_un_cartelito_corto_cuando_el_nombre_completo_es_largo(self):
  self.assertEqual(escribir_cartelito_optimo("Dr.", "Estanislao", "Schwarzschild"), "Dr. Schwarzschild")

