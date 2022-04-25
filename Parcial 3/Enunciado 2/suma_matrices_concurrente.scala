// Autor: Jesus Bandez 17-10046,
// Modulo escrito en Scala que contiene la suma de matrices de manera concurrente.
// Nota: Si por alguna razon el primer print no muestra un "Future(<not completed>)"
// incremente el tamanio de las matrices a y b. 
// Esto puede pasar si su procesador es los suficientemente potente para calcular
// la suma antes de que se ejecute el primer "println(k)"

import scala.concurrent._
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration._
import scala.util.{Failure, Success}

object Suma_de_matrices{
    def main(args: Array[String]): Unit = {

        // Se crean las matrices a sumar        
        var a = Array(Array(1.0, 2.0, 3.0, 1.0, 2.0, 3.0), 
                      Array(1.0, 2.0, 3.0, 1.0, 2.0, 3.0),
                      Array(1.0, 2.0, 3.0, 1.0, 2.0, 3.0),
                      Array(1.0, 2.0, 3.0, 1.0, 2.0, 3.0))

        var b = Array(Array(3.0, 4.0, 5.0, 3.0, 4.0, 5.0), 
                      Array(3.0, 4.0, 5.0, 3.0, 4.0, 5.0),
                      Array(3.0, 4.0, 5.0, 3.0, 4.0, 5.0),
                      Array(3.0, 4.0, 5.0, 3.0, 4.0, 5.0))

        println("Se quieren sumar las matrices:\nA=")
        imprimir_matriz(a)
        println("Y la matriz:\nB=")
        imprimir_matriz(b)
        
        print("\nSe ejecuta la suma y ")
        println("se intenta ver el valor de k de forma inmediata:")
        print("k = ")
        var k = sumar_matrices(a, b)
        println(k)
        println()

        // Se detiene este thread hasta que se obtenga el valor de la 
        // suma por concurrencia o pasen 99 segundos
        print("El programa se detiene hasta obtener el valor de k")
        println(" resultado de la funcion concurrente\n")
        var resultado = Await.result(k, 99 seconds)

        println("Ahora se vuelve a pedir el valor de k:")
        print("k = ")
        println(k)
        println("Se ha ejecutado correctamente la suma de forma concurrente.")

        println("Ahora se imprime el resultado de la suma de matrices contenido en k")
        print("K=\n")
        imprimir_matriz(resultado)
    }

    // Funcion para sumar dos matrices de manera concurrente. Arroja exception si las matrices
    // no tienen dimensiones iguales
    def sumar_matrices(a: Array[Array[Double]], b: Array[Array[Double]]) = {
        if (a.length != b.length) {
            throw new Exception("Matrices de tamanios distintos no se pueden sumar")
        }
        
        for (i <- 0 until a.length) {
            if (a(i).length != b(i).length){
                throw new Exception("Matrices de tamanios distintos no se pueden sumar")
            }
        }        
        var c: Future[Array[Array[Double]]] = Future {
            var res = Array.ofDim[Double](a.length, a(0).length)
            for (i <- 0 until a.length) {
                for (j <- 0 until a(0).length){
                    res(i)(j) = a(i)(j) + b(i)(j)
                }
            }
            res
        }
        c onComplete {
            case Success(res) => {
                res
                }
            case Failure(t) => {
                println("An error has occurred: " + t.getMessage)
            }
        }
        c
    }

    // Funcion que imprime una matriz
    def imprimir_matriz(a: Array[Array[Double]]) = {
        for (i <- 0 until a.length) {
            for (j <- 0 until a(0).length){
                print(a(i)(j))
                print(" ")
            }
            println()
        }
    }
}