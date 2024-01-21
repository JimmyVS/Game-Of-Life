# Conway's Game of Life with Pygame

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/release)
[![Pygame: 2.0.0+](https://img.shields.io/badge/Pygame-2.0.0%2B-orange.svg)](https://www.pygame.org)

<img width="599" alt="Window" src="https://github.com/JimmyVS/Game-Of-Life/assets/96888699/b209b32f-15a3-41dc-ae63-537f2b050546">

## Introduction

This repository contains a Python implementation of Conway's Game of Life using the Pygame library for visualization and user interaction. Conway's Game of Life is a cellular automaton devised by mathematician John Conway, where the state of each cell evolves over time based on simple rules.

# Getting Started

To run the simulation, follow these steps:

- Make sure you have Python installed on your system.
- Install the Pygame library using the following command:
`pip install pygame`

Clone this repository to your local machine:
`git clone https://github.com/JimmyVS/Game-Of-Life.git`

Navigate to the project directory:
`cd Game-Of-Life`

Run the game_of_life.py script:
`python Game_Of_Life.py`

## Controls
| Controls | Actions |
| ------------- | ------------- |
| Left Click | Place cells |
| Right Click | Place a "glider" pattern |
| Space | Play/Pause the simulation |
| Escape or close window | Quit the simulation |

## Rules

The rules of Conway's Game of Life are applied to update the grid:

1. A living cell with fewer than 2 or more than 3 living neighbors dies.
2. A dead cell with exactly 3 living neighbors becomes alive.
3. Otherwise, cells maintain their current state.

## Contributing

If you'd like to contribute to the project, feel free to open an issue, suggest enhancements, or submit pull requests.

## License

**This project is licensed under the MIT License.**
Made by **Jim Grysmpolakis.** Please do not claim as yours.


Have fun exploring the fascinating patterns and behaviors that emerge in Conway's Game of Life!
