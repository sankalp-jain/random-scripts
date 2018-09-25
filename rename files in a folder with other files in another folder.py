"""import os
path = 'C:\\Users\\sankalpjain\\Desktop\\images'

a = os.listdir(path)
#os.makedirs(path + "\\" + "na")

for i in range(1, 23):
    if i!= 10 and i != 19:
        os.makedirs(path + "\\" + str(i))

"""

import os
import shutil

d = {'1': ['mi-redmi-note-4-na-original-imaeqdxgtcgbgvfh.jpeg', 'mi-redmi-note-4-na-original-imaeqdxhgnerzpeg.jpeg', 'mi-redmi-note-4-na-original-imaeqdxqcrfshtqu.jpeg', 'micromax main image.jpg', 'micromax1.jpeg', 'micromax2.jpeg', 'micromax3.jpeg'], '11': ['acer-aspire-notebook-original-1.jpeg', 'acer-aspire-notebook-original-2.jpeg', 'acer-aspire-notebook-original-3.jpeg'], '12': ['micromax-lt777w-2-in-1-laptop-original-1.jpeg', 'micromax-lt777w-2-in-1-laptop-original-2.jpeg', 'micromax-lt777w-2-in-1-laptop-original-3.jpeg'], '13': ['hp-notebook-original-1.jpeg', 'hp-notebook-original-2.jpeg', 'hp-notebook-original-3.jpeg'], '14': ['lenovo-ideapad-notebook-3.jpeg', 'lenovo-ideapad-notebook-original-1.jpeg', 'lenovo-ideapad-notebook-original-2.jpeg'], '15': ['admin.ico', 'diary-of-a-wimpy-kid-do-it-yourself-book-original-1.jpeg'], '16': ['22-thea-stilton-and-the-tropical-treasure-original-1.jpeg'], '17': ['inaf245-queen-rosewood-sheesham-induscraft-na-honey-brown-original-1.jpeg', 'inaf245-queen-rosewood-sheesham-induscraft-na-honey-brown-original-2.jpeg', 'inaf245-queen-rosewood-sheesham-induscraft-na-honey-brown-original-3.jpeg'], '18': ['flbdorsabrqbblk-queen-carbon-steel-home-by-nilkamal-na-na-original-1.jpeg', 'flbdorsabrqbblk-queen-carbon-steel-home-by-nilkamal-na-na-original-2.jpeg', 'flbdorsabrqbblk-queen-carbon-steel-home-by-nilkamal-na-na-original-3.jpeg'], '19': ['1.jpeg', '2.jpeg', '3.jpeg'], '2': ['apple-iphone-6-1.jpeg', 'apple-iphone-6-2.jpeg', 'apple-iphone-6-3.jpeg'], '20': ['1.jpeg', '2.jpeg', '3.jpeg'], '22': ['mi-redmi-5a-c3b-original-imafy2gf3yraxdha.jpeg', 'mi-redmi-5a-c3b-original-imafy2gfd8byvqyf.jpeg', 'mi-redmi-5a-c3b-original-imafy2gfe6vebg9b.jpeg'], '3': ['mi-redmi-note-4-1.jpeg', 'mi-redmi-note-4-2.jpeg', 'mi-redmi-note-4-3.jpeg'], '4': ['lenovo-k6-power-k33a42-1.jpeg', 'lenovo-k6-power-k33a42-2.jpeg', 'lenovo-k6-power-k33a42-3.jpeg'], '5': ['lenovo-k5-note-pa330010in-1.jpeg', 'lenovo-k5-note-pa330116in-2.jpeg', 'lenovo-k5-note-pa330116in-3.jpeg'], '6': ['micromax-canvas-mega-4g-1.jpeg', 'micromax-canvas-mega-4g-2.jpeg', 'micromax-canvas-mega-4g-3.jpeg'], '7': ['samsung-galaxy-on5-sm-2.jpeg', 'samsung-galaxy-on5-sm-3.jpeg', 'samsung-galaxy-on7-sm-1.jpeg'], '8': ['oppo-a57-na-original-1.jpeg', 'oppo-a57-na-original-2.jpeg', 'oppo-a57-na-original-3.jpeg'], '9': ['amzer-amz98947-original-1.jpeg', 'amzer-amz98947-original-2.jpeg', 'amzer-amz98947-original-3.jpeg'], 'na': ['spigen-rugged-armor-k03cs20615-original-1.jpeg', 'spigen-rugged-armor-k03cs20615-original-2.jpeg', 'spigen-rugged-armor-k03cs20615-original-3.jpeg']}

path = 'C:\\Users\\sankalpjain\\Desktop\\images'

a = os.listdir(path)
print(a)

for i in a:
    path = 'C:\\Users\\sankalpjain\\Desktop\\images\\' + i
    path1 = 'C:\\xampp\\htdocs\\ShoppingPortalProVersion\\shopping\\admin\\productimages\\' + i
    a1 = os.listdir(path)
    a2 = os.listdir(path1)
    print(a1)
    print(a2)
    l = d[i]
    for j in range(len(a1)):
        print(path + "\\" + a1[j])
        print(path1 + "\\" + a2[j])
        shutil.move(path + "\\" + a1[j], path1 + "\\" + a2[j])

