def main():
    # Input File name
    filename = input("File name: ").strip().lower()

    # Check if the file ends with ".gif"
    if filename.endswith(".gif"):
        mediatype = "gif"
        print(f"image/{mediatype}")
        
     # Check if the file ends with ".jpg"
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        mediatype = "jpeg"
        print(f"image/{mediatype}")

        # Check if the file ends with ".png"
    elif filename.endswith(".png"):
        mediatype = "png"
        print(f"image/{mediatype}")

        # Check if the file ends with ".pdf"
    elif filename.endswith(".pdf"):
        mediatype = "pdf"
        print(f"application/{mediatype}")

        # Check if the file ends with ".txt"
    elif filename.endswith(".txt"):
        mediatype = "plain"
        print(f"text/{mediatype}")

        # Check if the file ends with ".zip"
    elif filename.endswith(".zip"):
        print("ZIP archive")

        # Check else
    else:
        print("application/octet-stream")

main()
