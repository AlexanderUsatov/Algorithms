import java.util.Scanner;

public class SimpleStrings {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        StringBuilder sb = new StringBuilder();
        sb.append(s.charAt(0));
        char next = '0';
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) != sb.charAt(i - 1))
                sb.append(s.charAt(i));
            else {
                while (!((next = (char) (int) (Math.random() * ('z' - 'a' + 1) + 'a')) != s.charAt(i - 1) && next != s.charAt(i + 1 == s.length() ? i - 1 : i + 1)))
                    ;
                sb.append(next);
            }
        }
        System.out.println(sb.toString());
    }
}
