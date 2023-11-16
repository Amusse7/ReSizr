from PIL import Image

image = Image.open('ReSizr.png')
print(f"Current Size: {image.size}")

resized_image = image.resize((250, 250))
resized_image.save('ReSizr_resized.png')
