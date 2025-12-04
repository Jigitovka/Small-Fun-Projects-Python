# I KNOW. MY PROGRAM STRUCTURE SUCKS. IF YOU READ THIS, AND YOU ARE AN EXPERIENCED PROGRAMMER,
# PLEASE, LET ME KNOW


from PIL import Image
from pathlib import Path


ASSET_DIR_LOCATION = Path(Path(__file__).parents[1], 'assets')
ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
FILENAME = "sample.jpg"


def data_to_2d(datalist, width):
    final_arr = []

    for i in range(0, len(datalist), width):
        final_arr.append(list(datalist[i:i+width]))
    return final_arr


def sRGBtoLinear(colorChannel) -> float:
    vGamma = round(colorChannel / 255, 5)
    if vGamma <= 0.04045:
        return colorChannel / 12.92
    
    return pow(((vGamma + 0.055) / 1.055), 2.4)


def luminance(rl, gl, bl) -> float:
    return rl * 0.2126 + gl * 0.7152 + bl * 0.0722

# Need to look at CIE standard
def perceived_lightness(y) -> float:
    if y <= 216/24389:
        return y * 24389/27

    return pow(y, 1/3) * 116 - 16


# Actually, run here
if __name__ == "__main__":
    with Image.open(Path(ASSET_DIR_LOCATION, FILENAME)) as im:
        img_matrix = data_to_2d(list(im.getdata()), im.width)
        
        pl_matrix = []

        for pixel_row in img_matrix:
            for r, g, b in pixel_row:
                lum_p = luminance(sRGBtoLinear(r), sRGBtoLinear(g), sRGBtoLinear(b))
                pl_p = int(perceived_lightness(lum_p))
                pl_matrix.append(pl_p)
        
        pl_matrix = data_to_2d(pl_matrix, im.width)

