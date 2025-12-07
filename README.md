# Small-Fun-Projects-Python
This is a collection of small to medium-sized Python projects, which I do in my free time, to improve my object-oriented programming, algorithmic-thinking skills, and overall, my knowledge in techspace. Each project includes a short description and simple instructios to run it locally.
The main idea is to either completely not use, or use minimal AI help. If you have any suggestions, please create an issue.

---

-[Game of Life](https://github.com/Jigitovka/Small-Fun-Projects-Python/tree/main/Game%20Of%20Life)

---

## Game Of Life

### 📌 Description
A Python implementation of Conway’s **Game of Life**, a zero-player cellular automaton. Each cell on a 2D grid lives, dies, or reproduces based on the number of neighboring cells. The simulation evolves step-by-step and creates interesting emergent behavior. The rules are:
- Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
- Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
- Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
- Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

P.S A weird thing: My program gets H(height) X W(width), but the correct way, and the standard is W x H x D. So I messed up on that part. Next project is not that way.


### ❔ What this project taught me?
- Working with 2D matrices
- Basic Algorithms
- Creating classes, structuring object methods and attributes
- Basic terminal visualization

### ▶️ How to Run
You can just change to the directory and run it with python, as there are no external dependencies required:
```
cd 'Game of Life'
python main.py
```
