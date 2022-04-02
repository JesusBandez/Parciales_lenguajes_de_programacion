/**
 Numeros de Church implementados como una clase en Typescript
 La implementacion consiste en que el cero es la clase de Church que contiene
 como atributo 'number' al null.
 El sucesor de una instancia de la clase Church 'a' es aquella instancia de la
 clase Church 'b' que contiene en su atributo 'number' a la clase Church 'a'
 */
var Church = /** @class */ (function () {
    function Church(n) {
        this.number = n;
    }
    // Retorna una nueva clase con el sucesor de la instancia
    Church.prototype.sucesor = function () {
        return new Church(this);
    };
    // Convierte la instancia de Church en su representacion en numeros naturales
    Church.prototype.deChurchANatural = function () {
        var rep = 0;
        var actual = this.number;
        while (actual != null) {
            rep++;
            actual = actual.number;
        }
        return rep;
    };
    // Metodo estatico que convierte un numero natural en un numero de Church
    Church.deNaturalAChurch = function (n) {
        var church = new Church(null);
        while (n > 0) {
            church = church.sucesor();
            n--;
        }
        return church;
    };
    // Suma de dos numeros de Church
    Church.prototype.add = function (m) {
        if (m.number === null) {
            return this;
        }
        else {
            return this.add(m.number).sucesor();
        }
    };
    // Multiplicar dos numeros de Church
    Church.prototype.mult = function (m) {
        if (m.number === null) {
            return m;
        }
        else {
            return this.add(this.mult(m.number));
        }
    };
    return Church;
}());
// El numero 5 en numeros de church
var x = Church.deNaturalAChurch(4);
var y = Church.deNaturalAChurch(3);
// Se suman x e y, y se obtiene el numero 14 en numeros de church
// Luego se convierte a natural y me muestra en pantalla 
console.log(x.add(y).deChurchANatural());
// Se multiplican x e y, y se obtiene el numero 45 en numeros de church
// Luego se convierte a natural y me muestra en pantalla 
console.log(x.mult(y).deChurchANatural());
