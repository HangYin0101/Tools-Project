# Tools Project - Greedy Snake Game

Group Name: Beef Noodle Soup

Group Members: Yuanyuan Gao, Bingsu Mo, Wenjie Wang, Hang Yin

Section 001

## Game description

Greedy snake is a game which was first invented in mid 70s, and it became trending because it adapts the small screen (4.0 sqr inch) phones in early 90s.

Nowadays, the Greedy snakes becomes a common name of video games that players control a line which grows in length. The Greedy snake could be installed in most phones, with variations in versions.


## How to play?

To start playing the game, press any key to begin. The goal is to eat as many apples as you can without being "killed". The final score of each game is equivalent to how many apples, which are the red objects on the screen, your snake had eaten before it dies.

While playing the game, player controls a long, thin string, we call it snake. The snake keeps moving, with changing in directions to pick up the "apples".

Moving direction is controlled by the "up", "down", "left", and "right" keys on the keyboard.

When pressing the "space" key, it accelerates the snake to make the game more exciting.

Each time the snake successfully picked up an "apple", it will grow longer by one unit.  

At the same time, player needs to be careful not to touch the walls or its own body.

Again, press any key to restart the game, the scores do not accumulate each time each time your snake dies.


## Instructions

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Development env for running: Python

First, clone the repository by doing the following on the terminal after arriving on a directory where you wish to locate the repository:
```
git clone https://github.com/HangYin0101/Tools-Project/
```

Once cloned, move to the repo directory and install dependencies - the only dependency is pygame.
```
cd Tools-Project
python3 -m pip install -r requirements.txt
```

Once pygame has been installed, all other dependencies should already be installed, since the libraries required by the game is random, sys, and pygame only.

To check that pygame has been installed properly and works, open any terminal and run python. Then import pygame and check that you see the following message.

```
>>>import pygame
pygame 1.9.4

'Hello from the pygame community. https://www.pygame.org/contribute.html'
```

Once checked, you can proceed to play the game by cloning this repo and running game.py, as is shown below:

```
cd Tools-Project

python game.py

```

## Explanation on game
### Main snake object

A Snake class was created to initiate properties and location of the moving object, which can be called in the main function and rungame function in game.py.

The speed and length of the snake were defined as 5 and 3 units. The "change_length" and "change_speed" methods allows player to increase the length or speed of the snake, depending on whether an apple is eaten, or "space" key is pressed by the player.

The snake can change directions based on the arrow control keys.

The life status of the snake changes when its head hits the edges of the window, or it hits the snake body.

### Main game

The main game adds displays of all subjects, and assures the game run and exit smoothly.

For more information: The number of apples showing on screen was default to be 10, and can be changed with player preference.
