# Necro(ネクロ)
# sidmishra94540@gmail.com

import PIL.Image
try:
    path = input('Enter the path of image: ')
    icon = PIL.Image.open(path)
    width, height = icon.size
    crop = width if width <= height else height
    icon = icon.crop(((width - crop) // 2, (height - crop) // 2, (width + crop) // 2, (height + crop) // 2)).resize((256,256))
    icon.save('icon.ico', format = 'ICO', sizes=[(256,256)], quality=95)
    print('Done!')
except:
    print('Error!')