from PIL import Image

def resize_image(size1, size2):
    image = Image.open('ReSizr.png')
    print(f"Current Size: {image.size}")

    resized_image = image.resize((size1, size2))
    resized_image.save('ReSizr_resized_'+ str(size1) +'.png')

size1 = int(input('enter width:'))
size2 = int(input('enter height:'))
resize_image(size1, size2)