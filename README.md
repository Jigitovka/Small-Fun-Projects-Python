# Small-Fun-Projects-Python
This is a collection of small to medium-sized Python projects, which I do in my free time, to improve my object-oriented programming, algorithmic-thinking skills, and overall, my knowledge in techspace. Each project includes a short description and simple instructios to run it locally.
The main idea is to either completely not use, or use minimal AI help. If you have any suggestions, please create an issue.

---

-[Game of Life](https://github.com/Jigitovka/Small-Fun-Projects-Python/tree/main/Game%20Of%20Life)
-[Image to ASCII](https://github.com/Jigitovka/Small-Fun-Projects-Python/tree/main/Image%20to%20Ascii%20Art)

---

## Game Of Life

### 📌 Description
A Python implementation of Conway’s **Game of Life**, a zero-player cellular automaton. Each cell on a 2D grid lives, dies, or reproduces based on the number of neighboring cells. The simulation evolves step-by-step and creates interesting emergent behavior. The rules are:
- Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
- Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
- Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
- Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

P.S A weird thing: My program gets H(height) X W(width), but the correct way, and the standard is W x H x D. So I messed up on that part. Next project is not that way.

### 📷 Example output
![Game of life](https://github.com/Jigitovka/Small-Fun-Projects-Python/blob/main/game_of_life.gif)

### ▶️ How to Run
You can just change to the directory and run it with python, as there are no external dependencies required:
```
cd 'Game of Life'
python main.py
```

## Image to ASCII

### 📌 Description
**Image to ASCII** converts any image into a text-based ASCII representation. And this time around, I did not mess up the standards for width and height, though the structure of the program leaves much to be desired. I decided to take things a little further with the algorithm for determining the brightness of given RGB colors. There were many methods of doing it. Basically, I convert the gamma encoded R´G´B´ image values to linear luminance(Y), then convert Y to non-linear perceived lightness.
1. Convert all sRGB 8-bit values(0-255) to decimal 0.0-1.0
2. Convert gamma-encoded RGB to a linear(V´) value.
3. Take each of the calculated V´ values for a single pixel(Rlin, Glin, Blin) and apply the standard coefficients for sRGB. This is the calculation for luminance:
```Y = (0.2126 * sRGBtoLin(vR) + 0.7152 * sRGBtoLin(vG) + 0.0722 * sRGBtoLin(vB))```
4. Take Luminance, and transform to L*, which is a value from 0(black) to 100(white) where 50 is supposedly middle gray.

You can read more about the maths and physics behind it here: https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color

The tool works well for most inputs, but it’s still evolving — there are a few areas that can be refined and improved over time as the project grows.

### 📷 Example output
![Image to ASCII](https://github.com/Jigitovka/Small-Fun-Projects-Python/blob/main/image_to_ascii.gif)

### ▶️ How to Run
This project makes use of Pillow imaging Library. You will need to install pipenv. For most users, you can do:
```pip install --user pipenv```
If you have cloned this repo locally, then:
```
cd 'Game of Life'
pipenv shell
pipenv install
python main.py
```
