/* Jesus Bandez 17-10046
Modulo que muestra las pruebas de las clases Grafos y los algoritmos de
busqueda
*/

fun main(){

    // Crear el grafo para las pruebas
    print("Se crea un grafo con 5 vertices y los arcos:")
    println(" (0, 1), (1, 2), (2, 0), (3, 1) (4, 3)")
    val grafo = Grafo(5)
    grafo.agregarArco(0, 1)
    grafo.agregarArco(1, 2)
    grafo.agregarArco(2, 0)
    grafo.agregarArco(3, 1)
    grafo.agregarArco(4, 3)

    // Ejecutar e imprimir los resultados de varias pruebas
    mostrarBusqueda(grafo, 0, 1)
    mostrarBusqueda(grafo, 1, 0)
    mostrarBusqueda(grafo, 1, 3)
    mostrarBusqueda(grafo, 4, 1)
    mostrarBusqueda(grafo, 4, 0)
}

fun mostrarBusqueda(grafo:Grafo, D:Int, H:Int){
    println("Busqueda con BFS sobre el grafo desde $D hasta $H")
    println("El camino contiene: ${grafo.BFS().buscar(D, H)} vertices")

    println("Busqueda con DFS sobre el grafo desde $D hasta $H")
    println("El camino contiene: ${grafo.DFS().buscar(D, H)} vertices")
    println()    
}