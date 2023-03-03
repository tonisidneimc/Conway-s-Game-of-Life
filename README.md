# Conway-s-Game-of-Life

An interactive *cellular automaton* simulator for Conway's Game of Life.

<img title="Glider Gun and some other constructs" alt="Glider Gun and some other constructs" src="/gif/cgol.gif">

Game of Life is a zero-player game. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is **Turing complete** and can simulate a universal constructor or any other Turing machine. 

To interact with the grid, you can pause the game with the spacebar key and click on the cells you want to change the state (filled = alive, empty = dead). Upon resuming the game, it will evolve from this state, with every cell interating with its eight neighbours according to the following rules:

1.  Any live cell with fewer than two live neighbours dies, as if by **underpopulation**.
2.  Any live cell with two or three live neighbours lives on to the next generation.
3.  Any live cell with more than three live neighbours dies, as if by **overpopulation**.
4.  Any dead cell with exactly three live neighbours becomes a live cell, as if by **reproduction**.

## Dependencies

To install the project's dependencies, make sure you have the Python package manager (pip) installed on your system and run the following command in the terminal:

```bash
   $ pip install pygame
```

## Building

```bash
  $ git clone https://github.com/tonisidneimc/Conway-s-Game-of-Life/
  $ cd Conway-s-Game-of-Life/
  $ python3 main.py
```

## 

If you want to know more about what this game is capable of, check out [LifeWiki](https://conwaylife.com/wiki/Conway%27s_Game_of_Life).
