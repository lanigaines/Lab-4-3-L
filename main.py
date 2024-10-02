# Initialize the list with 5 empty slots
numbers = [0] * 5

# Input 5 values from the user 
for i in range(len(numbers)):
    numbers[i] = int(input(f'Enter value {i+1}: '))
    
# Calculte the total sum
    total = 0
for num in numbers:
    total += num
    
# Print the result
print(f"The total sum is: {total}")


