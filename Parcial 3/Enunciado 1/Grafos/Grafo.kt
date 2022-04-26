/* Autor: Jesus Bandez 17-10046
Clase grafo que representa a un grafo como una lista de 
adyacencias. 
 */
public class Grafo(val size: Int){
    // Lista de adyacencias para representar el grafo
    private var adyacencias = MutableList(size) {mutableListOf<Int>()}

    // Metodo para agregar un arco al grafo. Arroja RuntimeException si uno de los vertices
    // no pertenece al grafo o se intenta crear arcos repetidos
    fun agregarArco(verticeInicial: Int, verticeFinal: Int){
        if (verticeInicial >= adyacencias.size || verticeInicial < 0 
            || verticeFinal >= adyacencias.size || verticeFinal < 0){
            throw RuntimeException("${verticeInicial} o ${verticeFinal} no pertenecen al grafo")
        } else if (verticeFinal in adyacencias[verticeInicial]) {        
            var msg = "El arco (${verticeInicial}, ${verticeFinal}) ya pertenece al grafo."
            msg += " No se permiten arcos repetidos"
            throw RuntimeException(msg)                                   
        }

        adyacencias[verticeInicial].add(verticeFinal)
    }

    // Convierte la lista de adyacencias a strings
    override fun toString(): String{
        return adyacencias.toString()
    }

    // Clase anidada abstracta busqueda
    inner abstract class Busqueda{       
        // Buscar cantidad de vertices desde D hasta H
        abstract fun buscar(D: Int, H:Int): Int             
    }

    // Clase concreta subtipo de la clase abstracta busqueda.
    // Implementa el algoritmo BFS para busqueda en grafos
    inner class BFS() : Grafo.Busqueda(){
        override fun buscar(D: Int, H:Int) : Int {
            if (D >= adyacencias.size || H >= adyacencias.size
                || D < 0 || H < 0){
                throw RuntimeException("${D} o ${H} no pertenecen al grafo")
            }
            // Inicializar las listas que contienen la propiedades
            var distanciaHasta = MutableList<Int>(size){-1}
            var verticeYaExplorado = MutableList<Boolean>(size){false}

            // Inicializar el vertice raiz
            distanciaHasta[D] = 0
            verticeYaExplorado[D] = true

            // Inicilizar la cola. Se usa una lista mutable como cola
            var cola: MutableList<Int> = mutableListOf()
            cola.add(D)

            // BFS
            while (cola.size != 0){
                var actual = cola.removeAt(0)

                for (vertice in adyacencias[actual]){
                    if (!verticeYaExplorado[vertice]){                        
                        distanciaHasta[vertice] = distanciaHasta[actual] + 1
                        cola.add(vertice)
                    }
                }
                verticeYaExplorado[actual] = true
            }

            return distanciaHasta[H]
        }
    }

    // Clase concreta subtipo de la clase abstracta busqueda.
    // Implementa el algoritmo DFS para busqueda en grafos
    inner class DFS() : Grafo.Busqueda(){
        // Variables necesarias para DFS
        var tiempo = 0
        var predecesorDe = MutableList<Int>(size){-1} 
        var verticeYaExplorado = MutableList<Boolean>(size){false}
        var tiempoInicialDe = MutableList<Int>(size){-1}
        var tiempoFinalDe = MutableList<Int>(size){-1}

        
        override fun buscar(D: Int, H:Int) : Int {   
            if (D >= adyacencias.size || H >= adyacencias.size
                || D < 0 || H < 0){
                throw RuntimeException("${D} o ${H} no pertenecen al grafo")
            }

            // Se ejecuta DFS con D siendo la raiz.
            dfsVisit(D)

            var verticesExplorados = -1
            if (tiempoInicialDe[D] < tiempoInicialDe[H] && tiempoFinalDe[D] > tiempoFinalDe[H]){
                verticesExplorados = calcularCantidadDeVerticesDesdeHasta(D, H)
            } 

            // Es necesario reiniciar las variables de la clase a su estado inicial
            reiniciarVariables()
            return verticesExplorados
        }

        // DFS
        fun dfsVisit(verticeInicial : Int) {
            tiempo += 1
            verticeYaExplorado[verticeInicial] = true
            tiempoInicialDe[verticeInicial] = tiempo

            for (verticeFinal in adyacencias[verticeInicial]){
                if (!verticeYaExplorado[verticeFinal]){
                    predecesorDe[verticeFinal] = verticeInicial
                    dfsVisit(verticeFinal)
                }
            }
            tiempo += 1
            tiempoFinalDe[verticeInicial] = tiempo            
        }

        // Funcion que navega por los predecesores de H hasta llegar D y 
        // retorna la cantidad de vertices que se encuentra en el camino
        fun calcularCantidadDeVerticesDesdeHasta(D: Int, H:Int): Int {
            var actual = H
            var contador = 0
            while (actual != D){
                actual = predecesorDe[actual]
                contador += 1
            }
            return contador
        }

        // Reestablecer las variables a su estado inicial
        fun reiniciarVariables(){
            tiempo = 0
            predecesorDe = MutableList<Int>(size){-1} 
            verticeYaExplorado = MutableList<Boolean>(size){false}
            tiempoInicialDe = MutableList<Int>(size){-1}
            tiempoFinalDe = MutableList<Int>(size){-1}
        }
    }
}
