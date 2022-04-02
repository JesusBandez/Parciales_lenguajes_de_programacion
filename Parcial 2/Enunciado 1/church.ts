/**
 Numeros de Church implementados como una clase en Typescript
 La implementacion consiste en que el cero es la clase de Church que contiene
 como atributo 'number' al null.
 El sucesor de una instancia de la clase Church 'a' es aquella instancia de la 
 clase Church 'b' que contiene en su atributo 'number' a la clase Church 'a'   
 */

class Church {
  number: Church;

  constructor(n: Church){
    this.number = n;
  }

  // Retorna una nueva clase con el sucesor de la instancia
  sucesor(){
    return new Church(this)
  }

  // Convierte la instancia de Church en su representacion en numeros naturales
  deChurchANatural(): number {
    let rep = 0;
    let actual = this.number
    while (actual != null){
      rep++
      actual = actual.number
    }
    return rep  
  }

  // Metodo estatico que convierte un numero natural en un numero de Church
  static deNaturalAChurch(n: number): Church {
    let church = new Church(null)

    while (n > 0){
      church = church.sucesor()
      n--
    }

    return church
  }

  // Suma de dos numeros de Church
  add(m:Church){
    if (m.number === null){
      return this
    } else {
      return this.add(m.number).sucesor()
    }
  }

  // Multiplicar dos numeros de Church
  mult(m:Church){
    if (m.number === null){
      return m
    } else {
      return this.add(this.mult(m.number))
    }

  }
}

// El numero 5 en numeros de church
let x: Church = Church.deNaturalAChurch(9)
let y: Church = Church.deNaturalAChurch(5)

// Se suman x e y, y se obtiene el numero 14 en numeros de church
// Luego se convierte a natural y me muestra en pantalla 
console.log(x.add(y).deChurchANatural())

// Se multiplican x e y, y se obtiene el numero 45 en numeros de church
// Luego se convierte a natural y me muestra en pantalla 
console.log(x.mult(y).deChurchANatural())
