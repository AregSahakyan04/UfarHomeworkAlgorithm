def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        merged = []
        i = j = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged
    else:
        return arr


array = []
print("Enter numbers one by one. Type 'finish' to end input.")

while True:
    user_input = input("Enter a number (or 'finish' to sort): ")
    if user_input.lower() == "finish":
        break
    try:
        number = int(user_input)  # Convert input to integer
        array.append(number)
    except ValueError:
        print("Please enter a valid integer or 'finish' to end.")

# Sort and display the array
sorted_array = merge_sort(array)
print("Sorted array:", sorted_array)
