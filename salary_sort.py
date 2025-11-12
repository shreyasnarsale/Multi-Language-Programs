# ---------------- Salary Sorting System ---------------- #

# -------- Selection Sort --------
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# -------- Bubble Sort --------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# -------- Main Execution --------
# Example salaries (floating-point)
salaries = [45000.50, 32000.75, 58000.25, 47000.10, 39000.00, 60000.90, 52000.30, 31000.20]

print("Original Salaries:", salaries)

# Using Selection Sort
sel_sorted = selection_sort(salaries.copy())
print("\nSalaries after Selection Sort:", sel_sorted)

# Using Bubble Sort
bub_sorted = bubble_sort(salaries.copy())
print("Salaries after Bubble Sort:", bub_sorted)

# Top 5 highest salaries
top_5 = sorted(salaries, reverse=True)[:5]
print("\nTop 5 Highest Salaries in the Company:", top_5)
