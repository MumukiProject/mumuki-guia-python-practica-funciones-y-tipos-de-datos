it("me_conviene(25, 8) es falso", () => {
  assert(!me_conviene(25, 8))
})

it("me_conviene(40, 8) es verdadero", () => {
  assert(me_conviene(40, 8))
})

it("me_conviene(40, 10) es verdadero", () => {
  assert(me_conviene(40, 10))
})

it("me_conviene(40, 4) es falso", () => {
  assert(!me_conviene(40, 4))
})


it("me_conviene(50, 16) es falso", () => {
  assert(!me_conviene(50, 16))
})
