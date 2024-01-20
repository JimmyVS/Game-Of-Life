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
`git clone https://github.com/your-username/game-of-life-pygame.git`

Navigate to the project directory:
`cd game-of-life-pygame`

Run the game_of_life.py script:
`python game_of_life.py`

## Controls

- Left-click: Place cells
- Right-click: Place a "glider" pattern
- Space: Play/Pause the simulation
- Escape or close window: Quit the simulation

## Rules

The rules of Conway's Game of Life are applied to update the grid:

1. A living cell with fewer than 2 or more than 3 living neighbors dies.
2. A dead cell with exactly 3 living neighbors becomes alive.
3. Otherwise, cells maintain their current state.

## Windows Security Notice

Some users on Windows 11 may receive a security notification when attempting to run the executable. This warning is likely due to the fact that the script is an interpreted Python script bundled into an executable using a tool like PyInstaller or cx_Freeze. The executable is safe and contains only the code provided in this repository.

### Why You Shouldn't Worry

1. Source Code Review: The source code is available in this repository, and you can review it to ensure that it does not contain any malicious code.
2. Open Source Community: This project is open source, and contributions from the community help ensure transparency and security.
3. No Malicious Intent: The executable is a straightforward implementation of Conway's Game of Life and does not include any harmful code.

If you encounter the warning, you can choose to run the executable by allowing it through Windows Defender or your antivirus software. Rest assured, the provided script is safe and only intended for educational and recreational purposes.

## Contributing

If you'd like to contribute to the project, feel free to open an issue, suggest enhancements, or submit pull requests.

## License

**This project is licensed under the MIT License.**
Made by **Jim Grysmpolakis.** Please do not claim as yours.


Have fun exploring the fascinating patterns and behaviors that emerge in Conway's Game of Life!
