# Asteroids

## Description
A Pygame-based recreation of the classic arcade game *Asteroids*.  
Control a triangular spaceship, destroy incoming asteroids, and survive as long as possible.

## Features
- Player-controlled triangular ship
- Shooting mechanics
- Asteroid spawning and collision system
- Simple, classic arcade gameplay

## Intense Gameplay
![Asteroid](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnJ0aXY0cGU4OGtldW0ydnIxa2l4ODlmMDVqYWsyYWI2YnEwZTljMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1QwgNgYshbX7WTYZY5/giphy.gif)
## Dependencies
- **Language:** Python 3.13  
- **Libraries:** Pygame 2.6.1  
- **Environment:** WSL (Ubuntu recommended)  
- **Tools:** uv astral (python project manager), jq

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/JaegerNolte/asteroids.git
cd asteroids
```
### 2. Install UV
```bash
pipx install uv
```

### 3. Intialize existing project using UV
```bash
uv init
```

### 4. Sync the enviroment
This creates a .venv directory and installs all dependencies specified in your pyproject.toml into uv.lock.
```bash
uv sync
```

### 5. Congrats, now you can run Asteroids
```bash
uv run main.py
```
