# Python script to resize and crop images
from PIL import Image
def resize_image(input_path, output_path, width, height):
    image = Image.open(input_path)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(output_path)
    def crop_image(input_path, output_path, left, top, right, bottom):
        image = Image.open(input_path)
        cropped_image = image.crop((left, top, right, bottom))
        cropped_image.save(output_path)





