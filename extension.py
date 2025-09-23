# user = str(input("Type the file name: "))

# my_array = [,,"image/png","application/pdf","text/plain","application/zip"]

# if user.endswith("gif"):
#     print("image/gif")

# elif user.endswith("jpg"):
#     print("image/jpeg")

# elif user.endswith("png"):
#     print(my_array[3])

# elif user.endswith("pdf"):
#     print(my_array[4])

# elif user.endswith("plain"):
#     print(my_array[5])

# elif user.endswith("zip"):
#     print(my_array[6])

# try using the newly learned dictionaries

# Step 1: Make a dictionary of extensions and their media types
media_types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

# Step 2: Ask the user for a file name
filename = input("Type the file name: ").lower().strip()

# Step 3: Get the extension (the part after the last ".")
# Example: "happy.jpg" -> "jpg"
if "." in filename:
    extension = filename.split(".")[-1]
else:
    extension = ""  # no extension

# Step 4: Look up the extension in the dictionary
if extension in media_types:
    print(media_types[extension])
else:
    print("application/octet-stream")
