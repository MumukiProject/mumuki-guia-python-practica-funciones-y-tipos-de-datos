it("escribir_cartelito(\"Dra.\", \"Ana\", \"Pérez\", false), es \"Dra. Ana Pérez\"", () => {
  assert.equal(escribir_cartelito("Dra.", "Ana", "Pérez", false), "Dra. Ana Pérez")
})
it("escribir_cartelito(\"Dr.\", \"Julio\", \"Gelman\", false), es \"Dr. Julio Gelman\"", () => {
  assert.equal(escribir_cartelito("Dr.", "Julio", "Gelman", false), "Dr. Julio Gelman")
})
it("escribir_cartelito(\"Dra.\", \"Ana\", \"Pérez\", true), es \"Dra. Pérez\"", () => {
  assert.equal(escribir_cartelito("Dra.", "Ana", "Pérez", true), "Dra. Pérez")
})
it("escribir_cartelito(\"Dr.\", \"Julio\", \"Gelman\", true), es \"Dr. Gelman\"", () => {
  assert.equal(escribir_cartelito("Dr.", "Julio", "Gelman", true), "Dr. Gelman")
})
