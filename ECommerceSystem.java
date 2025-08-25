import java.util.Scanner;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;

class Product {
    private String name;
    private double price;
    private int quantity;

    public Product() {
        this.name = "Unknown";
        this.price = 0.0;
        this.quantity = 0;
    }

    public Product(String name, double price) {
        this.name = name;
        this.price = price;
        this.quantity = 1;
    }

    public Product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    public double getTotalPrice() {
        return price * quantity;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    public double getPrice() {
        return price;
    }
}

class Customer {
    private String name;
    private String phone;
    private String address;

    public Customer(String name, String phone, String address) {
        this.name = name;
        this.phone = phone;
        this.address = address;
    }

    public String getName() { return name; }
    public String getPhone() { return phone; }
    public String getAddress() { return address; }
}

class Order {
    private Product[] products;
    private int productCount;
    private static final int MAX_PRODUCTS = 10;
    private static final double GST_RATE = 0.18;
    private Customer customer;
    private String paymentMode;
    private String transactionId;

    public Order(Customer customer, String paymentMode) {
        products = new Product[MAX_PRODUCTS];
        productCount = 0;
        this.customer = customer;
        this.paymentMode = paymentMode;
        this.transactionId = generateTransactionId(paymentMode);
    }

    private String generateTransactionId(String mode) {
        Random rand = new Random();
        int num = 100000 + rand.nextInt(900000);
        return mode + "-" + num;
    }

    public void addProduct(Product p) {
        if (productCount < MAX_PRODUCTS) {
            products[productCount++] = p;
        } else {
            System.out.println("Cannot add more products. Limit reached.");
        }
    }

    public double calculateSubtotal() {
        double total = 0;
        for (int i = 0; i < productCount; i++) {
            total += products[i].getTotalPrice();
        }
        return total;
    }

    public double applyDiscount(double total) {
        double discount = 0;
        if (total > 5000) {
            discount = 0.20;
        } else if (total > 2000) {
            discount = 0.10;
        } else if (total > 1000) {
            discount = 0.05;
        }
        return total - (total * discount);
    }

    public void printInvoice() {
        Random rand = new Random();
        int invoiceId = 100000 + rand.nextInt(900000);
        String date = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss").format(new Date());

        System.out.println("\n=========== E-COMMERCE INVOICE ===========");
        System.out.println("Invoice No : " + invoiceId);
        System.out.println("Date       : " + date);
        System.out.println("------------------------------------------");
        System.out.println("Customer   : " + customer.getName());
        System.out.println("Phone      : " + customer.getPhone());
        System.out.println("Address    : " + customer.getAddress());
        System.out.println("Payment    : " + paymentMode);
        System.out.println("Txn ID     : " + transactionId);
        System.out.println("------------------------------------------");
        System.out.printf("%-15s %-10s %-10s %-10s%n", "Product", "Price", "Qty", "Total");
        System.out.println("------------------------------------------");

        for (int i = 0; i < productCount; i++) {
            Product p = products[i];
            System.out.printf("%-15s %-10.2f %-10d %-10.2f%n",
                    p.getName(), p.getPrice(), p.getQuantity(), p.getTotalPrice());
        }

        System.out.println("------------------------------------------");
        double subtotal = calculateSubtotal();
        System.out.printf("Subtotal (Before Discount): %.2f%n", subtotal);

        double afterDiscount = applyDiscount(subtotal);
        System.out.printf("After Discount            : %.2f%n", afterDiscount);

        double gstAmount = afterDiscount * GST_RATE;
        System.out.printf("GST (18%%)                 : %.2f%n", gstAmount);

        double finalAmount = afterDiscount + gstAmount;
        System.out.println("------------------------------------------");
        System.out.printf("TOTAL PAYABLE             : %.2f%n", finalAmount);
        System.out.println("==========================================\n");
    }
}

public class ECommerceSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Customer Details
        System.out.println("Enter Customer Details:");

        System.out.print("Name: ");
        String custName = sc.nextLine().trim();
        while (custName.isEmpty()) {
            System.out.print("Name cannot be empty. Enter again: ");
            custName = sc.nextLine().trim();
        }

        System.out.print("Phone (10 digits): ");
        String phone;
        while (true) {
            phone = sc.nextLine().trim();
            if (phone.matches("\\d{10}")) break;
            System.out.print("Invalid phone. Enter 10 digits: ");
        }

        System.out.print("Address: ");
        String address = sc.nextLine().trim();
        while (address.isEmpty()) {
            System.out.print("Address cannot be empty. Enter again: ");
            address = sc.nextLine().trim();
        }

        // Payment Mode
        System.out.print("Payment Mode (Cash/Card/UPI): ");
        String paymentMode;
        while (true) {
            paymentMode = sc.nextLine().trim().toUpperCase();
            if (paymentMode.equals("CASH") || paymentMode.equals("CARD") || paymentMode.equals("UPI")) {
                break;
            } else {
                System.out.print("Invalid. Enter Cash, Card, or UPI: ");
            }
        }

        Customer customer = new Customer(custName, phone, address);
        Order order = new Order(customer, paymentMode);

        // Product details
        System.out.print("\nEnter number of products you want to buy: ");
        int n;
        while (true) {
            if (sc.hasNextInt()) {
                n = sc.nextInt();
                if (n > 0 && n <= 10) break;
                else System.out.print("Enter a valid number (1–10): ");
            } else {
                System.out.print("Enter a valid integer: ");
                sc.next();
            }
        }
        sc.nextLine(); // consume newline

        for (int i = 0; i < n; i++) {
            System.out.println("\nEnter details for product " + (i + 1));

            System.out.print("Product name: ");
            String name = sc.nextLine().trim();
            while (name.isEmpty()) {
                System.out.print("Name cannot be empty. Enter again: ");
                name = sc.nextLine().trim();
            }

            System.out.print("Price: ");
            double price;
            while (true) {
                if (sc.hasNextDouble()) {
                    price = sc.nextDouble();
                    if (price > 0) break;
                    else System.out.print("Price must be > 0. Enter again: ");
                } else {
                    System.out.print("Enter a valid number: ");
                    sc.next();
                }
            }

            System.out.print("Quantity: ");
            int qty;
            while (true) {
                if (sc.hasNextInt()) {
                    qty = sc.nextInt();
                    if (qty > 0) break;
                    else System.out.print("Quantity must be > 0. Enter again: ");
                } else {
                    System.out.print("Enter a valid integer: ");
                    sc.next();
                }
            }
            sc.nextLine(); // consume newline

            if (qty == 1) {
                order.addProduct(new Product(name, price));
            } else {
                order.addProduct(new Product(name, price, qty));
            }
        }

        // Print final invoice
        order.printInvoice();
        sc.close();
    }
}
