def add_newline_before_hyphens(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    # Adding a newline before each hyphen
    modified_content = content.replace(' - ', '\n - ')

    with open(output_file, 'w') as file:
        file.write(modified_content)

# Replace 'input.txt' and 'output.txt' with your file names
add_newline_before_hyphens('input3.txt', 'output3.md')
