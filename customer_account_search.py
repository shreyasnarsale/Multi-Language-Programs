# ---------------- Customer Account Search System ---------------- #

# Customer Account IDs (sample data - already sorted for binary search)
customer_ids = [1005, 1010, 1020, 1035, 1050, 1060, 1075, 1090, 1100, 1120]


# -------- Linear Search --------
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i   # return index if found
    return -1          # not found


# -------- Binary Search --------
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# -------- Main Execution --------
print("Customer Account IDs:", customer_ids)

# Take multiple IDs as input (comma separated)
search_ids = list(map(int, input("\nEnter Customer Account IDs to search (comma separated): ").split(",")))

# Search each ID
for search_id in search_ids:
    print(f"\nSearching for ID {search_id}...")

    # Linear Search
    pos_linear = linear_search(customer_ids, search_id)
    if pos_linear != -1:
        print(f"   Linear Search: ID {search_id} found at position {pos_linear}")
    else:
        print(f"   Linear Search: ID {search_id} not found")

    # Binary Search
    pos_binary = binary_search(customer_ids, search_id)
    if pos_binary != -1:
        print(f"   Binary Search: ID {search_id} found at position {pos_binary}")
    else:
        print(f"   Binary Search: ID {search_id} not found")
