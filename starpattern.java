import java.util.Scanner;

public class StarPatterns {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of rows: ");
        int n = sc.nextInt();

        // 1. Square Pattern
        System.out.println("\n1. Square Pattern");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        // 2. Left Half Pyramid
        System.out.println("\n2. Left Half Pyramid");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        // 3. Inverted Left Half Pyramid
        System.out.println("\n3. Inverted Left Half Pyramid");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n - i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        // 4. Right Half Pyramid
        System.out.println("\n4. Right Half Pyramid");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n - i - 1; j++) {
                System.out.print("  ");
            }
            for(int j = 0; j <= i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        // 5. Inverted Right Half Pyramid
        System.out.println("\n5. Inverted Right Half Pyramid");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < i; j++) {
                System.out.print("  ");
            }
            for(int j = 0; j < n - i; j++) {
                System.out.print("* ");
            }
            System.out.println();
        }

        // 6. Full Pyramid
        System.out.println("\n6. Full Pyramid");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            for(int j = 0; j < 2 * i + 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // 7. Inverted Full Pyramid
        System.out.println("\n7. Inverted Full Pyramid");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            for(int j = 0; j < 2 * (n - i) - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // 8. Diamond Pattern
        System.out.println("\n8. Diamond Pattern");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            for(int j = 0; j < 2 * i + 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        for(int i = n - 2; i >= 0; i--) {
            for(int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            for(int j = 0; j < 2 * i + 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // 9. Hollow Square
        System.out.println("\n9. Hollow Square");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(i == 0 || i == n - 1 || j == 0 || j == n - 1)
                    System.out.print("* ");
                else
                    System.out.print("  ");
            }
            System.out.println();
        }

        // 10. Hollow Pyramid
        System.out.println("\n10. Hollow Pyramid");
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            for(int j = 0; j < 2 * i + 1; j++) {
                if(j == 0 || j == 2 * i || i == n - 1)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.println();
        }

        sc.close();
    }
}
