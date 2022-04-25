/*Clase conjunto que implementa la interfaz Coleccion. Un conjunto no puede 
contener repetidos
*/
public class Conjunto<T>() : Coleccion<T>{

    // El conjunto se implementa con una lista mutable
    val conjunto = mutableListOf<T>()

    // Agrega un elemento si no existe en el conjunto
    override fun agregar(elemento:T){
        if (!(elemento in conjunto)){
            conjunto.add(elemento)
        }
    }

    // Remueve un elemento del conjunto. Si no existe el elemento, arroja una
    // runtime Exception
    override fun remover(elemento:T){
        if (elemento in conjunto){
            conjunto.remove(elemento)
        } else {
            throw RuntimeException("El elemento no existe ${elemento} en el conjunto")
        }
    }

    // Muestra si el conjunto esta vacio
    override fun vacio(): Boolean{
        return conjunto.size == 0

    }

    // Muestra los contenidos del conjunto
    override fun toString(): String {
        return conjunto.toString()

    }
}