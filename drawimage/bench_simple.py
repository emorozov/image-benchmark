import subprocess
from io import BytesIO

import pyvips
from PIL import Image, ImageDraw, ImageFont


def draw_imagemagick():
    """Draw text on image using ImageMagick."""
    subprocess.run(['convert', '-font', 'iosevka',  '-fill', 'white', '-pointsize', '60', 
                    '-gravity', 'center', '-draw', "text 0,300 'TEXT TO BE DISPLAYED'", 
                    'drawimage/test.jpg', 'output.jpg'])

def draw_gm():
    """Draw text on image using GraphicsMagick."""
    subprocess.run(['gm', 'convert', '-font', 'iosevka',  '-fill', 'white', '-pointsize', '60', 
                    '-gravity', 'center', '-draw', "text 0,300 'TEXT TO BE DISPLAYED'", 
                    'drawimage/test.jpg', 'output.jpg'])

def draw_pillow():
    """Draw text on image using Pillow."""
    image = Image.open('drawimage/test.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/TTF/iosevka-medium.ttf', 100)
    *_, w, h = draw.textbbox(xy=(0, 0), text='TEXT TO BE DISPLAYED', font=font)
    draw.text(
            xy=(0, 0),
            text='TEXT TO BE DISPLAYED',
            font=font,
            fill=(255, 255, 255, 255)
        )
    image.save(open('output.jpg', 'wb'), format='jpeg')

def draw_vips():
    """Draw text on image using pyvips."""
    image = pyvips.Image.new_from_file('drawimage/test.jpg')
    txt = pyvips.Image.text('TEXT TO BE DISPLAYED', font='Iosevka', dpi=400)
    image = image.insert(txt, 0, 0)
    image.write_to_file('output.jpg')


__benchmarks__ = [
    (draw_pillow, draw_imagemagick, "Drawing text using ImageMagick"),
    (draw_pillow, draw_gm, "Drawing text using GraphicsMagick"),
    (draw_pillow, draw_vips, "Drawing text using pyvips"),
]
