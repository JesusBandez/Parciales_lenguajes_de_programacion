/* Autor: Jesus Bandez 1710046
Implementacion de la funcion producto de matrices en Java
*/

public class ProductoMatriz {    

/* Metodo para conseguir el producto de dos matrices

    Parametros:
        A: Matriz de Double de tamanio NxM
        B: Matriz de Double de tamanio MxP
        N: Int con la cantidad de filas de A
        M: Int con la cantidad de columnas y filas de A y B, respectivamente
        P: Int con la cantidad de filas de B
    
    Retorna:
        resultado: Matriz de Doubles de tamanio NxP con la matriz resultado
            del producto de AxB
 */
public static double[][] productoDeMatrices(
        double[][] A, double[][] B, int N, int M, int P){
    
    // variable con la matriz donde se guardan los resultados
    double[][] resultado = new double[N][P];
    
    // Por cada fila en la matriz resultado
    for (int i=0; i < N; i++){
        // Por cada columna en la matriz resultado
        for (int j=0; j< P; j++){
            // Se inicia un double acumulador
            double acc = 0;
            
            // Se obtiene la suma de A[i][k]*B[k][j] con
            // 0 <= k < M
            for (int k=0; k < M; k++){
                acc = acc + A[i][k]*B[k][j];
            }

            // Se guarda el resultado en la matriz         
            resultado[i][j] = acc;
        }
    }

    return resultado;

}

/* Metodo que recibe una matriz y la imprime por la salida estandar

    Parametros:
        matriz: matriz de doubles a imprimir
*/
public static void imprimirMatriz(double[][] matriz){
    
    for (double[] row : matriz){
        for (double num : row){
            System.out.print(num);
            System.out.print(' ');
        }
        System.out.println();
    }

}

public static void main(String[] args) {

    // Se definen los tamanios de las matrices
    int N, M, P;
    N = 2; M = 3; P = 2;

    // Se definen las matrices
    double[][] A =new double[][] { {-1, -2, -3}, {3,2,1} }; 
    double[][] B =new double[][] { {0.2, 3.2}, {0.1, 2.1}, {-0.3, 3.4} };
    
    // Se obtiene la matriz resultado
    double[][] resultado = productoDeMatrices(A, B, N, M, P);

    // Se imprimen las matrices por la salida estandar:
    System.out.println("A:");
    imprimirMatriz(A);
    System.out.println("B:");
    imprimirMatriz(B);
    System.out.println("resultado de AxB:");
    imprimirMatriz(resultado);

}
}
