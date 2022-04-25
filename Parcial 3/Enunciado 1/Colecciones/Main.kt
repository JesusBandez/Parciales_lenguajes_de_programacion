/* Jesus Bandez 17-10046
Modulo con la prueba de las clases Bolsa y Conjunto
*/

fun main(){
    println("Se crea una bolsa")
    var bolsita: Bolsa<Int> = Bolsa<Int>()

    println("Se muestra que la bolsa esta vacia")
    println(bolsita.vacio())

    println("Se agregan tres elementos a ella")
    bolsita.agregar(2)
    bolsita.agregar(3)
    bolsita.agregar(4)
    println(bolsita.toString())

    println("Se agrega el elemento 4 dos veces mas")
    bolsita.agregar(4)
    bolsita.agregar(4)
    println(bolsita.toString())
    
    println("Se intenta eliminar el 3 de la bolsa")
    bolsita.remover(3)

    println("Se muestra que se ha eliminado el 3")
    println(bolsita.toString())

    println("Se insiste en eliminar el 3 otra vez")
    try {
        bolsita.remover(3)
    } catch(e:RuntimeException) {
        println("Se atajo el error de remover 3 de la bolsita")
    }

    ///////////////////////////////
    print("\n\n\n\n")
    //////////////////////////////

    println("Se crea un Conjunto")
    var conjunto: Conjunto<Int> = Conjunto<Int>()

    println("Se muestra que el conjunto esta vacio")
    println(conjunto.vacio())

    println("Se agregan tres elementos al conjunto")
    conjunto.agregar(2)
    conjunto.agregar(3)
    conjunto.agregar(4)
    println(conjunto.toString())

    println("Se agrega el elemento 4 dos veces mas")
    conjunto.agregar(4)
    conjunto.agregar(4)
    println(conjunto.toString())
    
    println("Se intenta eliminar el 3 del conjunto")
    conjunto.remover(3)

    println("Se muestra que se ha eliminado el 3")
    println(conjunto.toString())

    println("Se insiste en eliminar el 3 otra vez")
    try {
        conjunto.remover(3)
    } catch(e:RuntimeException) {
        println("Se atajo el error de remover 3 del conjunto")
    }    
}