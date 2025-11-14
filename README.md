# Snake Python 🐍

A faithful Snake clone built entirely with Python’s built-in `turtle` graphics library. Steer the snake, eat food, grow longer, and avoid collisions to chase a high score.

## Features
- **Pure Python** – no external dependencies, just the standard library.
- **Modular architecture** – dedicated modules for snake movement, food logic, and scoring.
- **Responsive controls** – arrow keys change direction instantly while preventing 180° turns.
- **Scoreboard** – session high score tracking with game-over messaging.
- **Randomized food** – food spawns at random coordinates each time it’s eaten.

## File Overview
- `main.py` – initializes the screen, binds input, and runs the main game loop.
- `snake.py` – defines the `Snake` class (segments, movement, growth, collision helpers).
- `food.py` – handles spawning food objects and repositioning them after each bite.
- `scoreboard.py` – renders the current score and displays “GAME OVER” when you lose.

## Requirements
- Python 3.x (the `turtle` module is included with the interpreter).

## Getting Started
```bash
git clone https://github.com/<your-user>/Snake_Python.git
cd Snake_Python
python main.py
```

## Controls
- `↑` move up
- `↓` move down
- `←` move left
- `→` move right

## Gameplay Tips
- Grow by eating food pellets; each one adds a segment and increases your score.
- Avoid crashing into the walls or your own body.
- Restart the session by re-running `python main.py`.

## Possible Enhancements
- Persist high scores to a file.
- Add difficulty modes (speed, obstacles, wrap-around walls).
- Introduce power-ups (slow time, shrink snake, etc.).

## Contributing
Issues and pull requests are welcome! Share your ideas for new mechanics, graphical polish, or refactors.
