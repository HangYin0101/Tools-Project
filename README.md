# Tools Project

Group Name: Beef Noodle Soup

Section 001

## Game description

Greedy snake is a game which was first invented in mid 70s, and it became trending because it adapts the small screen (4.0 sqr inch)phones in early 90s.

Nowadays, the Greedy snakes becomes a common name of video games that players control a line which grows in length. The Greedy snake could be installed in most phones, with variations in versions.


## Greedy Snake Game

While playing the game, players manipulate a long, thin string, we call it snake. The snake keeps moving, with changing in directions to pick up the "apples". Direction changing is controlled by players with "up", "down", "left", and "right" key on the keyboard. Every time the snake successfully picked up an "apple", the snake will grow longer by one unit. When pressing the space key, it can accelerate to make the game more exciting. At the same time, players need to be careful with touching the walls and its body.


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

### Explanation on game
### Main snake object
