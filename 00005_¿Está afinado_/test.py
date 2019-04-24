  
  def test_NO_esta_afinado_443_(self):
    self.assertTrue(not esta_afinado(443))

  def test_NO_esta_afinado_442_(self):
    self.assertTrue(not esta_afinado(442))

  def test_NO_esta_afinado_437_(self):
    self.assertTrue(not esta_afinado(437))

  def test_esta_afinado(440)(self):
    self.assertTrue(esta_afinado(440))

