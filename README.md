# Multiplayer Game with Python and Pygame

This project is a simple multiplayer game implemented using Python, Pygame, and sockets for networking. The game allows players to connect to a central server, move around the game space, and interact with other players in real time.

## Features

- **Real-time Multiplayer**: Players can join the server, see others on the screen, and interact with them.
- **Health System**: Players have a health bar that decreases upon collisions with other players.
- **Collision Detection**: Resolves overlapping players and adjusts their positions while reducing their health.
- **Server-Client Architecture**: The server handles player data, collisions, and broadcasts updates to clients.
- **Customizable Controls**: Players can move using `W`, `A`, `S`, `D` keys.

---

## Setup and Installation

### Prerequisites
- Python 3.x
- Required Python libraries: `pygame`, `socket`, `pickle`

Install the dependencies using:
```bash
pip install pygame
```

### Running the Server
1. Navigate to the project directory.
2. Start the server:
   ```bash
   python server.py
   ```

### Running the Client
1. Start the client application:
   ```bash
   python player.py
   ```
2. Enter your username when prompted.
3. The game window will launch, allowing you to control your character.

---

## Gameplay

1. **Movement**: Use the `W`, `A`, `S`, `D` keys to move your character around.
2. **Health**: Each player starts with a full health bar. Colliding with another player reduces health.
3. **Death**: When health reaches zero, the player dies and is removed from the game.

---

## Code Overview

### `player.py` (Client)
- Handles the game interface and user inputs.
- Sends keypress data to the server.
- Receives and displays updates from the server, including player positions and health.

### `server.py` (Server)
- Manages player connections and stores game state (positions, health, etc.).
- Detects and resolves collisions between players.
- Broadcasts updated game state to all connected clients.

---

## Key Functions

### Client (`player.py`)
- **`draw_health_bar(screen, x, y, health, max_health)`**: Draws the health bar for a player.
- **`main()`**: Main game loop for the client.

### Server (`server.py`)
- **`handle_client(conn, addr)`**: Manages communication with a single client.
- **`detect_collisions()`**: Checks and resolves collisions between players.
- **`update_positions()`**: Updates player positions based on inputs.
- **`broadcast_positions()`**: Sends the game state to all clients.
- **`start_server()`**: Initializes the server and listens for incoming connections.

---

## Future Improvements
- Add more game mechanics, such as power-ups or obstacles.
- Enhance graphics with animations and custom assets.
- Implement a scoring system or leaderboard.
- Expand the game space with larger maps.

---

Enjoy the game and feel free to contribute or suggest new features!

---

## License

This project is open-source and available for modification and use under the MIT license.

### MIT License

```
MIT License

Copyright (c) 2024 Ralph King

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
