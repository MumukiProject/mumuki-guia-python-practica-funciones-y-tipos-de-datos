describe("esta_afinado", () => {
  it("NO esta_afinado(443)", () => { assert(!esta_afinado(443)) })
  it("NO esta_afinado(442)", () => { assert(!esta_afinado(442)) })
  it("NO esta_afinado(437)", () => { assert(!esta_afinado(437)) })

  it("esta_afinado(440)", () => { assert(esta_afinado(440)) })
})
