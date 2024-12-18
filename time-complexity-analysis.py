# 1. Constant Time Complexity: O(1)
# Explanation: Accessing an element in an array takes the same time regardless of array size.
# Equation: T(n) = c (constant time)
def get_element(arr, index):
    return arr[index]


# 2. Linear Time Complexity: O(n)
# Explanation: Traversing an array requires visiting each element once, so the time grows linearly.
# Equation: T(n) = c1 + c2 * n (time depends linearly on the size of the input array)
def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total


# 3. Quadratic Time Complexity: O(n^2)
# Explanation: Nested loops iterate over all pairs of elements in an array, leading to n^2 operations.
# Equation: T(n) = c1 + c2 * n + c3 * n^2 (time grows quadratically with input size)
def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])


# 4. Cubic Time Complexity: O(n^3)
# Explanation: Triple nested loops generate all possible triplets, leading to n^3 operations.
# Equation: T(n) = c1 + c2 * n + c3 * n^2 + c4 * n^3

def print_triplets(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                print(arr[i], arr[j], arr[k])


# 5. Logarithmic Time Complexity: O(log n)
# Explanation: Binary search repeatedly divides the search space by half, leading to logarithmic growth.
# Equation: T(n) = c1 + c2 * log2(n)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 6. Linearithmic Time Complexity: O(n log n)
# Explanation: Merge Sort divides the array into halves (log n levels) and merges them (n operations per level).
# Equation: T(n) = c1 * n + c2 * n log n
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# 7. Exponential Time Complexity: O(2^n)
# Explanation: Generating all subsets requires two choices (include/exclude) for each element, leading to 2^n subsets.
# Equation: T(n) = c * 2^n
def subsets(arr):
    if not arr:
        return [[]]
    first = arr[0]
    rest = subsets(arr[1:])
    return rest + [[first] + r for r in rest]


# 8. Factorial Time Complexity: O(n!)
# Explanation: Generating all permutations involves arranging n elements in all possible orders, leading to n! operations.
# Equation: T(n) = c * n!
def permutations(s, prefix=""):
    if not s:
        print(prefix)
    else:
        for i in range(len(s)):
            permutations(s[:i] + s[i+1:], prefix + s[i])
