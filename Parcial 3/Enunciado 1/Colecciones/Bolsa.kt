/*Clase Bolsa que implementa la interfaz Coleccion.
Una bolsa puede contener todas las repeticiones de elementos
que quiera.
*/
public class Bolsa<T>() : Coleccion<T>{

    // La bolsa se implementa con una lista mutable
    val bolsa = mutableListOf<T>()

    // Agrega un elemento a la bolsa
    override fun agregar(elemento:T){
        bolsa.add(elemento)
    }

    // Remueve un elemento. Si no existe el elemento, arroja una
    // Runtime Exception
    override fun remover(elemento:T){
        if (elemento in bolsa){
            bolsa.remove(elemento)
        } else {
            throw RuntimeException("El elemento no existe ${elemento} en la bolsa")
        }

    }

    // Muestra si la bolsa no tiene elementos
    override fun vacio(): Boolean{
        return bolsa.size == 0

    }

    // Muestra los contenidos de la bolsa
    override fun toString(): String {
        return bolsa.toString()

    }

}