/*Interfaz coleccion que representa una coleccion de objetos */
interface Coleccion<T> {
    // Se puede agregar elementos a una coleccion
    fun agregar(elemento:T)

    // Se pueden eliminar elementos de una coleccion
    fun remover(elemento:T)

    //Una coleccion puede estar vacia
    fun vacio(): Boolean
}