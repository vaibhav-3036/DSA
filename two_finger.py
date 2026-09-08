# It's like two pointer but in same direction
# Remove the duplicate name without creating another list or array.
# If same name ---> move the right pointer and nothing will change in array
# If different name ---> move the left pointer forward and update new name to new left pointer poisition



names = ["Alice", "Bob", "Bob", "Charlie", "Charlie", "David", "Eve"]

def two_finger(names):
    left = 0

    for right in range(1, len(names) - 1):
        if names[left] != names[right]:
            left += 1
            names[left] = names[right]
        
    return left + 1

count = two_finger(names)
print(names[:count])

