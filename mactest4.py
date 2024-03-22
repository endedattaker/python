# Ask the user for the key to delete
delete_key = input("Enter the key to delete: ")

# Open file in read mode
f = open('data.txt', 'r')
# Read all lines from the file
lines = f.readlines()
# Close the file
f.close()

# Open file in write mode
f = open('data.txt', 'w')
# Loop through the lines
for line in lines:
    # Parse the string back to a dictionary
    data = eval(line)
    # Check if the key exists in the dictionary
    if delete_key in data:
        continue  # Skip writing this line if the key is found
    # Write the dictionary back to the file if the key is not found
    f.write(str(data) + '\n')

# Close the file
f.close()

print("Dictionary with key '{}' deleted successfully.".format(delete_key))
