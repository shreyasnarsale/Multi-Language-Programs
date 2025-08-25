import java.util.Scanner;

public class calculator {
    private double num1, num2;
    private char operator;

    public void getInput() {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.print("Enter first number: ");
            num1 = Double.parseDouble(scanner.nextLine());

            System.out.print("Enter operator (+, -, *, /): ");
            operator = scanner.nextLine().charAt(0);

            System.out.print("Enter second number: ");
            num2 = Double.parseDouble(scanner.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter numeric values.");
            getInput(); // recursive call for re-entry
        }
    }

    public void calculate() {
        double result;
        switch (operator) {
            case '+':
                result = add(num1, num2);
                break;
            case '-':
                result = subtract(num1, num2);
                break;
            case '*':
                result = multiply(num1, num2);
                break;
            case '/':
                if (num2 == 0) {
                    System.out.println("Error: Division by zero is not allowed.");
                    return;
                }
                result = divide(num1, num2);
                break;
            default:
                System.out.println("Invalid operator. Please use +, -, *, or /.");
                return;
        }
        System.out.println("Result: " + result);
    }

    // Operation methods
    private double add(double a, double b) {
        return a + b;
    }

    private double subtract(double a, double b) {
        return a - b;
    }

    private double multiply(double a, double b) {
        return a * b;
    }

    private double divide(double a, double b) {
        return a / b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean continueCalc = true;

        System.out.println("==== OOP-Based Java Calculator ====");

        while (continueCalc) {
            calculator calc = new calculator();
            calc.getInput();
            calc.calculate();

            System.out.print("Do you want to perform another calculation? (yes/no): ");
            String response = scanner.nextLine().trim().toLowerCase();
            if (!response.equals("yes")) {
                continueCalc = false;
                System.out.println("Goodbye!");
            }
        }

        scanner.close();
    }
}
