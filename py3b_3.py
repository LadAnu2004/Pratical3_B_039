even_numbers = []

for num in range(1, 101):
    if num % 2 == 0:
        even_numbers.append(num)

print("List of Even Numbers:")
print(even_numbers)

print("Minimum Even Number:", min(even_numbers))

print("Maximum Even Number:", max(even_numbers))

print("Total Sum of Even Numbers:", sum(even_numbers))

