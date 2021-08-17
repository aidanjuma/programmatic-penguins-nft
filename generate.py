""" ± Imports: ±
• os (Used to interact with the OS)
• numpy (Used to handle arrays)
• PIL (Python Imaging Library - Used to handle generation of images, i.e. Programmatic Penguins)
• secrets (randbelow - Used for random number generation)"""
import os
import numpy as np
from PIL import Image
from secrets import randbelow


DIMENSIONS = 480, 480
DIRNAME = os.path.dirname(__file__)

# ± determineSecondColor() method ± #


def determineSecondColor():
    # ± Get randint (b). If b is greater than 250, orange; if <= 250 or > 28, grey; else, white. ± #
    b = randbelow(750)

    if b > 250:
        sk = (223, 113, 38)
        return sk
    elif b <= 250 and b > 28:
        sk = (89, 86, 82)
        return sk
    else:
        sk = (255, 255, 255)
        return sk

# ± determineEyeColor() method ± #


def determineEyeColor():
    # ± If flipper color = beak color, eyes black; if determiner is between 1359 and 1530, eyes 'crazy red'; else, black. ± #
    x = randbelow(1000)
    if x < 134:
        ey = (172, 50, 50)
        return ey
    else:
        ey = (0, 0, 0)
        return ey


# ± rollColors() method ± #
def rollColors():
    colors = []

    # ± Generate a random RGB color for the penguin's b(o)d(y) - sk determined using functions. ± #
    bd = (randbelow(256), randbelow(256), randbelow(256))
    colors.append(bd)

    sk = determineSecondColor()
    colors.append(sk)

    ey = determineEyeColor()
    colors.append(ey)

    # ± Hair, Background & Outline ± #
    hr = (255, 242, 0)
    colors.append(hr)
    bg = (238, 238, 238)
    colors.append(bg)
    ol = (0, 0, 0)
    colors.append(ol)

    return colors


def rollPenguins():
    e = randbelow(1000)
    if e > 250:
        pixels = tall_penguin
    elif 250 >= e > 150:
        pixels = emperor_penguin
    else:
        pixels = plump_penguin
    return pixels


init = []
flag = 0
# ± Generate Programmatic Penguins ± #
for i in range(0, 1500):

    """ Colors List - 0: bd, 1: sk, 2: ey, 3: hr, 4: bg, 5: ol """
    c = rollColors()
    init.append(c)

    bd = c[0]
    sk = c[1]
    ey = c[2]
    hr = c[3]
    bg = c[4]
    ol = c[5]

    """ Pixel Sets """
    tall_penguin = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol,
         ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bd, bd,
         bd, bd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bd, bd, ey, bd,
         ey, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bd, bd, ey, bd,
         ey, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bd, bd, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol,
         ol, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk,
         sk, ol, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol,
         ol, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, bg, bg, bd, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, bg, bg, bd, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bd, bd,
         bd, bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, bg, ol, ol, ol, ol,
         ol, ol, ol, ol, bd, bd, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol,  sk,  sk, ol,  sk,
         sk,  sk,  sk,  sk, ol, bd, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol,  sk,  sk, ol,  sk,
         sk,  sk,  sk,  sk, ol, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol,
         ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    plump_penguin = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol,
         ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bd, bd, bd,
         bd, bd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bd, bd, ey, bd, bd,
         ey, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bd, bd, bd, bd, bd,
         bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol,
         ol, ol, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk, sk,
         sk, ol, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol,
         ol, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, bg, bg, bd, bd, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bd, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bd, bd, bd,
         bd, bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol,
         ol, ol, ol, ol, ol, bd, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol,  sk,  sk,  sk, ol,  sk,
         sk,  sk,  sk,  sk, ol, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol,
         ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    emperor_penguin = [
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, hr, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, hr, hr, bg, bg,
         hr, hr, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hr, hr,
         ol, bg, bg, bg, hr, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, hr, hr, ol, ol, bg, bg,
         ol, ol, bg, ol, hr, hr, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg,
         bg, ol, ol, bg, bg, hr, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol,
         ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bd, bd,
         bd, bd, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bd, bd, ey, bd,
         ey, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bd, bd, ey, bd,
         ey, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, bd, bd, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol,
         ol, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, sk, sk, sk, sk, sk, sk,
         sk, ol, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol,
         ol, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, bg, bg, bd, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, bg, bg, bd, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bd, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bd,
         bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bd, bd,
         bd, bd, bd, bd, bd, bd, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, bg, ol, ol, ol, ol,
         ol, ol, ol, ol, bd, bd, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, ol, ol,  sk,  sk, ol,  sk,
         sk,  sk,  sk,  sk, ol, bd, ol, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol,  sk,  sk, ol,  sk,
         sk,  sk,  sk,  sk, ol, ol, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol,
         ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg,
         bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
    ]

    if flag == 0:
        last = 0
        flag += 1
    else:
        last = init[i-1]
        current = init[i]
        if current == last:
            same = True
            while same:
                c = rollColors()
                init.append(c)
                if current != last:
                    same = False
                else:
                    pass
        else:
            pass

    pixels = rollPenguins()
    arr = np.array(pixels, dtype=np.uint8)

    # ± Use PIL to create an image using the array of pixels supplied. ± #
    img = Image.fromarray(arr)
    img = img.resize(DIMENSIONS, resample=0)
    filename = DIRNAME + '/output/' + (str(i+1)) + '.png'
    img.save(filename)

    print(f'Created & Saved Image: {i+1}.')
print(f'Created {i+1} Images.')
