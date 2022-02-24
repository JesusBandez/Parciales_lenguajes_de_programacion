public class ProductoMatriz {
    

public static double[][] productoDeMatrices(
        double[][] A, double[][] B, int N, int M, int P){
    
    double[][] resultado = new double[N][P];

    for (int i=0; i < N; i++){
        for (int j=0; j< P; j++){
            double acc = 0;

            for (int k=0; k < M; k++){
                acc = acc + A[i][k]*B[k][j];
            }
            resultado[i][j] = acc;
        }
    }

    return resultado;

}

public static void main(String[] args) {

    int N, M, P;
    N = 1;
    M = 3;
    P = 1;

    double[][] A =new double[][] { {-1, -2, -3} }; 
    double[][] B =new double[][] { {0.2}, {0.1}, {-0.3} };
    
    double[][] resultado = productoDeMatrices(A, B, N, M, P);

    System.out.println("La matriz resultante es:");
    for (double[] row : resultado){
        for (double num : row){
            System.out.print(num);
            System.out.print(' ');
        }
        System.out.println();
    }

}
}
