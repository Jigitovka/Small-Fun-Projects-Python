from PIL import Image
from pathlib import Path

# Maybe a good way of opening a relative directory from here
ASSET_DIR_LOCATION = Path(Path(__file__).parents[1], 'assets')
FILENAME = "sample.jpg"

# Actually, run here
if __name__ == "__main__":
    im = Image.open(Path(ASSET_DIR_LOCATION, FILENAME))
    print("Successfully loaded image!")
    print(f"{im.width} x {im.height}")

