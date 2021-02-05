# Necro(ネクロ)
# sidmishra94540@gmail.com

try:
    import PIL.Image
    path = input('Enter the path of image: ')
    icon = PIL.Image.open(path)
    choice = input('Enter 1 for cropped icon and 0 for original: ')
    if choice:
        width, height = icon.size
        crop = width if width <= height else height
        icon = icon.crop(((width - crop) // 2, (height - crop) // 2, (width + crop) // 2, (height + crop) // 2)).resize((256,256))
    icon.save('icon.ico', format = 'ICO', sizes=[(256,256)], quality=95)
    print('Done!')
except:
    print('Error!')