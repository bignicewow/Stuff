import sys
import os
from PIL import Image, ImageOps

def main():
    arg_validator()
    input_path = sys.argv[1].lower()
    output_path = sys.argv[2].lower()

    if not os.path.exists(input_path):
        sys.exit("Input does not exist")

    if not input_path.endswith((".png", ".jpg", ".jpeg")):
        sys.exit("Not an image file")
    
    if not output_path.endswith((".png", ".jpg", ".jpeg")):
        sys.exit("Invalid output")

    if not os.path.splitext(input_path)[1] == os.path.splitext(output_path)[1]:
        sys.exit("Input and output have different extensions")


    edit_image()


def edit_image():
    input_pic = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    size = shirt.size
    input_pic = ImageOps.fit(input_pic, size)
    input_pic.paste(shirt, shirt)
    input_pic.save(sys.argv[2])

def arg_validator():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        return True


if __name__ == "__main__":
    main()