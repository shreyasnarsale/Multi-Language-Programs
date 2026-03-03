# All Star Patterns in Python

n = int(input("Enter number of rows: "))

print("\n1. Square Pattern")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print("\n2. Left Half Pyramid")
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("\n3. Inverted Left Half Pyramid")
for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()

print("\n4. Right Half Pyramid")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("\n5. Inverted Right Half Pyramid")
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n - i):
        print("*", end=" ")
    print()

print("\n6. Full Pyramid")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()

print("\n7. Inverted Full Pyramid")
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()

print("\n8. Diamond Pattern")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()

for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()

print("\n9. Hollow Square")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n10. Hollow Pyramid")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

