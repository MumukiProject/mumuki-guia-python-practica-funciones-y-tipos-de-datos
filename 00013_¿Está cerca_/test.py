def test_esta_cerca_443(self):
  self.assertTrue(esta_cerca(443))

def test_esta_cerca_442(self):
  self.assertTrue(esta_cerca(442))

def test_esta_cerca_441(self):
  self.assertTrue(esta_cerca(441))

def test_esta_cerca_439(self):
  self.assertTrue(esta_cerca(439))

def test_esta_cerca_438(self):
  self.assertTrue(esta_cerca(438))

def test_esta_cerca_437(self):
  self.assertTrue(esta_cerca(437))

def test_NO_esta_cerca_440(self):
  self.assertTrue(not esta_cerca(440))

def test_NO_esta_cerca_420(self):
  self.assertTrue(not esta_cerca(420))

def test_NO_esta_cerca_460(self):
  self.assertTrue(not esta_cerca(460))
