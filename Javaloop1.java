import java.io.*;



public class Javaloop1{
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());

        bufferedReader.close();
        for(int i = 1; i <= 10; i++ ){
            int resultado = N * i;
            System.out.println(N + " x " + i + " = " + resultado);
        }
    }
}