# Hash Table Implementation using Chaining 

# Initialize Hash Table 
def initialize_table(size): 
    return [[] for _ in range(size)] 

# Hash Function (Division Method) 
def hash_function(key): 
    return key % 10 

# Insert Key-Value Pair 
def insert(table, key, value): 
    index = hash_function(key) 
    for i, (k, v) in enumerate(table[index]): 
        if k == key: 
            table[index][i] = (key, value)   # Update if key exists 
            print("Key updated successfully.")
            return 
    table[index].append((key, value))       # Insert new key 
    print("Key inserted successfully.")

# Search Key 
def search(table, key): 
    index = hash_function(key) 
    for k, v in table[index]: 
        if k == key: 
            return v 
    return "Key not found" 

# Delete Key 
def delete(table, key): 
    index = hash_function(key) 
    for i, (k, v) in enumerate(table[index]): 
        if k == key: 
            table[index].pop(i) 
            print("Key deleted successfully.")
            return 
    print("Key not found") 

# Display Hash Table 
def display(table): 
    print("\n--- Hash Table ---") 
    for i in range(len(table)): 
        print(i, " --> ", table[i]) 

# Main Program 
table = initialize_table(10) 

while True: 
    print("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit") 
    choice = int(input("Enter your choice: ")) 

    if choice == 1: 
        key = int(input("Enter Key (Integer): ")) 
        value = input("Enter Value: ") 
        insert(table, key, value) 

    elif choice == 2: 
        key = int(input("Enter Key to Search: ")) 
        print("Search Result:", search(table, key)) 

    elif choice == 3: 
        key = int(input("Enter Key to Delete: ")) 
        delete(table, key) 

    elif choice == 4: 
        display(table) 

    elif choice == 5: 
        print("Program Ended.") 
        break 

    else: 
        print("Invalid Choice! Try Again.")
