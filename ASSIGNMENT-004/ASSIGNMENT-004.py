###          ASSIGNMENT-->4
###  MODULE 5: FILES,EXCEPTIONS,AND ERRORS IN PYTHON


###    TASK-1:READ A FILE AND HANDLE ERRORS

file1 = open('sample.txt.py', 'r' )
reading_file = file1.read()
print(reading_file)
file1.close()


###
###


### TASK-2:WRITE AND APPEND DATA TO A FILE

def write_and_append_file():
    # Step 1: Write user input to output.txt
    user_input = input("Enter some data to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(user_input + '\n')

    # Step 2: Append additional data
    more_data = input("Enter more data to append: ")
    with open('output.txt', 'a') as file:
        file.write(more_data + '\n')

    # Step 3: Read and display the final content
    print("\nFinal contents of 'output.txt':")
    with open('output.txt', 'r') as file:
        print(file.read())

# Call the function
write_and_append_file()

3