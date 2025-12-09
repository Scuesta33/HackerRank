import java.util.HashMap;

public class ContarLetras {
    public static HashMap<Character, Integer> contar(String palabra) {
        HashMap<Character, Integer> conteo = new HashMap<>();

        for (char c : palabra.toCharArray()) {
            conteo.put(c, conteo.getOrDefault(c, 0) + 1);
        }

        return conteo;
    }

    public static void main(String[] args) {
        System.out.println(contar("hola"));
    }
}
