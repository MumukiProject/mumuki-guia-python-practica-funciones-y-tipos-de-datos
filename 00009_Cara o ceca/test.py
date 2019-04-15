describe("decision_con_moneda", () => {
  it("decision_con_moneda(\"cara\", \"pizzas\", \"empanadas\") es \"pizzas\"", () => {
    assert.equal(decision_con_moneda("cara", "pizzas", "empanadas"), "pizzas")
  })
  it("decision_con_moneda(\"cara\", \"asado\", \"empanadas\") es \"asado\"", () => {
    assert.equal(decision_con_moneda("cara", "asado", "empanadas"), "asado")
  })
  it("decision_con_moneda(\"ceca\", \"pizzas\", \"empanadas\") es \"empanadas\"", () => {
    assert.equal(decision_con_moneda("ceca", "pizzas", "empanadas"), "empanadas")
  })
  it("decision_con_moneda(\"ceca\", \"pizzas\", \"pastas\") es \"pastas\"", () => {
    assert.equal(decision_con_moneda("ceca", "pizzas", "pastas"), "pastas")
  })
})
