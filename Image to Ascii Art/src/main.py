from PIL import Image
from pathlib import Path

# Maybe a good way of opening a relative directory from here
ASSET_DIR_LOCATION = Path(Path(__file__).parents[1], 'assets')
FILENAME = "sample.jpg"

def data_to_2d(datalist, width):
    final_arr = []

    for i in range(0, len(datalist), width):
        final_arr.append(list(datalist[i:i+width]))
    
    return final_arr


# Actually, run here
if __name__ == "__main__":
    with Image.open(Path(ASSET_DIR_LOCATION, FILENAME)) as im:

        img_matrix = data_to_2d(list(im.getdata()), im.width)

