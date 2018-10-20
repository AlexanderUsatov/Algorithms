import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {

    static int[] cats;
    static int m;
    static ArrayList<Integer>[] g;

    public static void main(String[] args) throws IOException {

        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String s = sc.readLine();
        int n = Integer.parseInt(s.split(" ")[0]);
        m = Integer.parseInt(s.split(" ")[1]);
        String[] ss = sc.readLine().split(" ");
        cats = new int[ss.length];
        for (int i = 0; i < cats.length; i++)
            cats[i] = Integer.parseInt(ss[i]);
        g = new ArrayList[cats.length];
        for (int i = 0; i < g.length; i++)
            g[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            ss = sc.readLine().split(" ");
            g[Integer.parseInt(ss[0]) - 1].add(Integer.valueOf(ss[1]) - 1);
            g[Integer.parseInt(ss[1]) - 1].add(Integer.valueOf(ss[0]) - 1);
        }

        System.out.println(rec(0, -1, 0));
    }

    static int rec(int i, int par, int cats_prev) {
        cats_prev = cats_prev * cats[i] + cats[i];
        if (cats_prev > m)
            return 0;
        if (g[i].size() == 1 && i != 0)
            return 1;
        int sum = 0;
        for (int j : g[i]) {
            if (j == par)
                continue;
            sum += rec(j, i, cats_prev);
        }
        return sum;

    }
}
