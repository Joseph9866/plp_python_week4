def read_and_modify_file():
    try:
        filename = input("Enter the name of the file to read: ")
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Could not read or write to the file.")

# Run the function
read_and_modify_file()
