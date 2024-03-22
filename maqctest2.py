num_entries = int(input("How many entries do you want to input? "))

# Open file in append mode
f = open('data.txt', 'a')

# Loop to input and write multiple entries
for _ in range(num_entries):
    data = {}
    data['name'] = input("Enter name: ")
    data['age'] = int(input("Enter age: "))
    data['city'] = input("Enter city: ")

    # Writing dictionary input to a text file
    f.write(str(data) + '\n')



# Close the file
f.close()

print("Data written to data.txt successfully.")
# Open file in read mode
f = open('data.txt', 'r')

# Read each line from the file
for line in f:
    # Parse the string back to a dictionary
    data = eval(line)
    # Print the dictionary
    print(data)

# Close the file
f.close()


# Open file in read mode
f = open('data.txt', 'r')

# Ask the user for the key and value to search for
search_key = input("Enter the key to search for: ")
search_value = input("Enter the value to search for: ")

# Read each line from the file
for line in f:
    # Parse the string back to a dictionary
    data = eval(line)
    # Check if the key exists in the dictionary and its value matches the search value
    if search_key in data and data[search_key] == search_value:
        print("Found:", data)
        break  # Stop searching after the first occurrence
else:
    print("Key-value pair not found.")

# Close the file
f.close()