import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }

        int[][] dp = new int[n + 1][k + 1];

        for (int j = 0; j <= k; j++) {
            dp[0][j] = 0;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                int max = Integer.MIN_VALUE;
                if (i >= 1) {
                    int prev = dp[i - 1][j];
                    if (prev != Integer.MIN_VALUE) {
                        max = Math.max(max, prev + a[i - 1]);
                    }
                }
                if (i >= 2) {
                    int prev = dp[i - 2][j];
                    if (prev != Integer.MIN_VALUE) {
                        max = Math.max(max, prev + a[i - 1]);
                    }
                }
                if (j > 0) {
                    for (int m = 0; m < i; m++) {
                        int prev = dp[m][j - 1];
                        if (prev != Integer.MIN_VALUE) {
                            max = Math.max(max, prev);
                        }
                    }
                }
                dp[i][j] = max == Integer.MIN_VALUE ? 0 : max;
            }
        }

        int result = Integer.MIN_VALUE;
        for (int j = 0; j <= k; j++) {
            if (dp[n][j] > result) {
                result = dp[n][j];
            }
        }
        System.out.println(result);
    }
}