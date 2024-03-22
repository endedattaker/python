# Open file in read mode
f = open('data.txt', 'r')

# Read all lines from the file
lines = (f.readlines())

# Close the file
f.close()

# Ask the user for the key and value to update
update_key = input("Enter the key to update: ")
update_value = input("Enter the new value: ")

# Open file in write mode
f = open('data.txt', 'w')

# Loop through the lines
for line in lines:
    # Parse the string back to a dictionary
    data = eval(line)
    # Check if the key exists in the dictionary
    if update_key in data:
        # Update the value of the key
        data[update_key] = update_value
    # Write the modified dictionary back to the file
    f.write(str(data) + '\n')

# Close the file
f.close()

print("Value updated successfully.")
