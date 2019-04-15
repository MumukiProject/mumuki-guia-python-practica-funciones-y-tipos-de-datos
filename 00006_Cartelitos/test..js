it("escribir_cartelito(\"Dra.\", \"Ana\", \"Pérez\"), es \"Dra. Ana Pérez\"", () => {
  assert.equal(escribir_cartelito("Dra.", "Ana", "Pérez"), "Dra. Ana Pérez")
})
it("escribir_cartelito(\"Dr.\", \"Julio\", \"Gelman\"), es \"Dr. Julio Gelman\"", () => {
  assert.equal(escribir_cartelito("Dr.", "Julio", "Gelman"), "Dr. Julio Gelman")
})
