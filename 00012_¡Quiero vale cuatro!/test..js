it("valor_canto_truco(\"retruco\") es 3", ()  => {
  assert.equal(valor_canto_truco("retruco"), 3)
})

it("valor_canto_truco(\"truco\") es 2", ()  => {
  assert.equal(valor_canto_truco("truco"), 2)
})

it("valor_canto_truco(\"vale cuatro\") es 4", ()  => {
  assert.equal(valor_canto_truco("vale cuatro"), 4)
})
