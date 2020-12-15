#!/usr/bin/python3

from PIL import Image

PICTURE_1 = 'picture_1.jpg'
PICTURE_2 = 'picture_2.jpg'
PICTURE_3 = 'picture_3.jpg'
PICTURE_4 = 'picture_4.jpg'

pictures = [PICTURE_1, PICTURE_2, PICTURE_3, PICTURE_4]

print("Konwersja klików z rozszerzeniem .jpg na png")

for pics in pictures:
    picture = Image.open(pics)
    converted_picture = f'{pics[:-4]}.png'
    picture.save(converted_picture)

print("Koniec koncersji rozszerzeń")