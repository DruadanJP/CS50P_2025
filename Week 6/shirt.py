import sys
import os
from PIL import Image, ImageOps


def main():
    # Ensure the program is executed with exactly two command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_file output_file")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Validate file extensions (must be .jpg, .jpeg, or .png)
    valid_extensions = (".jpg", ".jpeg", ".png")
    if not (
        input_file.lower().endswith(valid_extensions)
        and output_file.lower().endswith(valid_extensions)
    ):
        sys.exit("Invalid input or output format")

    # Ensure the input and output have the same extension
    if (
        os.path.splitext(input_file)[1].lower()
        != os.path.splitext(output_file)[1].lower()
    ):
        sys.exit("Input and output have different extensions")

    # Ensure the input file exists
    if not os.path.isfile(input_file):
        sys.exit("Input does not exist")

    try:
        # Open the input image
        with Image.open(input_file) as in_image:

            # Open the shirt template
            with Image.open("shirt.png") as shirt_image:
                # Resize and crop input to match shirt size
                cropped_image = ImageOps.fit(in_image, shirt_image.size)

                # Overlay the shirt
                cropped_image.paste(shirt_image, mask=shirt_image)

                # Save the result to the output file
                cropped_image.save(output_file)

    except Exception as e:
        sys.exit(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
