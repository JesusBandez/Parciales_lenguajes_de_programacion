// Autor: Jesus Bandez 17-10046,
// Programa en Scala que calcula la cantidad de archivos en el directorio en donde
// se ejecuta el programa
// Nota: Si por alguna razon el primer print no muestra un "Future(<not completed>)"
// mueva el programa a un sitio que contenga mas subdirectorios y archivos, o cree
// nuevos subdirectorios y archivos.
// Esto puede pasar si su procesador es los suficientemente potente para calcular
// la cantidad de archivos antes de que se ejecute la instruccion "println(futura_cantidad_de_archivos)"
import java.io.File
import scala.collection.mutable.ListBuffer
import scala.concurrent._
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration._

object Archivos_en_subdirectorio {
     def main(args: Array[String]): Unit = {
         
        println("\nSe inicia el programa en el directorio actual.")
        println("De inmediato se intenta imprimir la cantidad de archivos conseguidos:")
        var futura_cantidad_de_archivos = contar_archivos_en_arbol_subdirectorio(".")
        println(s"$futura_cantidad_de_archivos\n")
        
        // Se espera a que el hilo termine de calcular o que pasen 120 sg
        println("Ahora se espera a que todos los hilos terminen de calcular en los subdirectorios")
        var cantidad_de_archivos = Await.result(futura_cantidad_de_archivos, 120 seconds)

        println(s"Se vuelve a imprimir el valor:\n$futura_cantidad_de_archivos\n")

        println("Y ahora se imprime la cantidad de archivos conseguidos:")
        println(s"$cantidad_de_archivos archivos conseguidos." )
     }

    // Funcion que obtiene todos los archivos en el directorio pasado como path
    def lista_de_archivos_en_path(path: String):List[File] = {        
        val d = new File(path)
        if (d.exists && d.isDirectory) {
            d.listFiles.toList
        } else {
            List[File]()
        }
    }

    // Funcion que crea un nuevo Thread al ser invocada. Esta funcion genera nuevos
    // threads por cada subdirectorio conseguido en el directorio path. Luego espera
    // a que terminen los threads de esos subdirectorios para obtener el total
    // de archivos en el directorio path.
    def contar_archivos_en_arbol_subdirectorio(path: String):Future[Int] = Future {
        // Obtener los archivos en el directorio actual
        var archivos = lista_de_archivos_en_path(path)
        
        // Separar los archivos de las carpetas
        var directorios_y_archivos = separar_archivos_y_directorios(archivos)
        
        // Obtener la cantidad de archivos en el directorio actual
        var cantidad_de_archivos = directorios_y_archivos(1).length

        // LLamar recursivamente esta funcion en todos los subdirectorios
        var futures = ListBuffer[Future[Int]]()
        for (directorio <- directorios_y_archivos(0)){
            futures += contar_archivos_en_arbol_subdirectorio(directorio.toPath.toString)
        }

        // Esperar los resultados de cada subarbol e irlo sumando en la cantidad de archivos
        for (futuro <- futures){
            // Esto espera a que termine el thread o pasen 99 segundos
            cantidad_de_archivos += Await.result(futuro, 99 seconds)
        }

        cantidad_de_archivos
    }

    // Funcion que recibe una lista de archivos y los separa en archivos y directorios
    def separar_archivos_y_directorios(elementos: List[File]): List[ListBuffer[File]] = {
        var directorios = new ListBuffer[File]()
        var archivos = new ListBuffer[File]()

        for (elemento <- elementos){
            if (elemento.isDirectory){
                directorios += elemento
            } else {
                archivos += elemento
            }
        }
        List(directorios, archivos)
    }
}
