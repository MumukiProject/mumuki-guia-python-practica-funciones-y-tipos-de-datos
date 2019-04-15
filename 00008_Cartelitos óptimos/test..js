it("escribe un cartelito largo cuando el nombre completo es corto", () => {
  assert.equal(escribir_cartelito_optimo("Ing.", "Carla", "Toledo"), "Ing. Carla Toledo")
})
it("escribe un cartelito corto cuando el nombre completo es largo", () => {
  assert.equal(escribir_cartelito_optimo("Dr.", "Estanislao", "Schwarzschild"), "Dr. Schwarzschild")
})
