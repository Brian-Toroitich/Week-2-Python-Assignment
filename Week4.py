def file_read_write():
    # Ask user for input filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Create new output file name
        new_filename = "modified_" + filename

        # Write modified content to new file
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File processed successfully! Modified version saved as '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
file_read_write()
