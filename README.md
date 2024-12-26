This is a simple multiplayer game built using Python's `pygame` library for the client-side interface and `socket` programming for the server. The game allows players to connect to a server, move their character (represented by a dot) around the screen, and see the positions of other players in real time.

## Files

### 1. `server.py`
This script runs the game server that manages client connections and player data.

- **Functionality:**
  - Accepts player connections.
  - Receives player positions and updates the list of active players.
  - Sends updated player positions to all connected clients.
  - Handles client disconnections.

- **Dependencies:**
  - `socket`: For network communication.
  - `threading`: For handling multiple client connections simultaneously.
  - `pickle`: For serializing and deserializing player data.

### 2. `player.py`
This script runs the client-side of the game, handling player movement, rendering, and communication with the server.

- **Functionality:**
  - Prompts the player to enter a username.
  - Connects to the server and sends the username.
  - Listens for updates on player positions from the server.
  - Allows the player to move using the `WASD` keys.
  - Draws the player's position as a circle and displays usernames on the screen.
  
- **Dependencies:**
  - `pygame`: For rendering the game window, player movement, and drawing.
  - `socket`: For network communication with the server.
  - `pickle`: For serializing and deserializing player data.

## Setup Instructions

### Prerequisites
Before running the game, make sure you have Python 3.x installed and the required libraries:

```bash
pip install pygame
```

### Running the Game

#### Step 1: Start the Server
To start the server, run the `server.py` script:

```bash
python server.py
```

The server will listen for incoming connections on `127.0.0.1` (localhost) at port `5555`.

#### Step 2: Run the Client
To start a client instance, run the `player.py` script:

```bash
python player.py
```

The client will prompt you for a username and then connect to the server. The player's dot will be displayed on the screen, and the player can move it using the `WASD` keys.

### How the Game Works

- The server manages the connections and keeps track of all connected players' positions.
- Each client sends its current position to the server regularly, and the server broadcasts all players' positions to all connected clients.
- Players see each other’s positions on the screen as colored circles. Their own dot is green, while other players' dots are red.
- The server maintains a list of all connected players and sends updates to all clients every time a player's position changes.

### Controls

- **W**: Move up
- **S**: Move down
- **A**: Move left
- **D**: Move right

### Notes
- The game currently supports multiple clients (players) but runs only locally (localhost).
- The server can handle multiple clients simultaneously using threading, so each player can interact with others in real time.
- The game is a simple 2D environment where players can move around and see each other's positions.

## Troubleshooting

- **Server not starting**: Make sure that no other application is using port `5555`.
- **Connection issues**: Ensure both the client and server are running on the same machine, and verify that `127.0.0.1` is accessible.


You do not have to pay for using or modifying this code if you choose to use the MIT license. The MIT license is a permissive open-source license, meaning you can freely use, modify, and distribute the code with minimal restrictions.

However, if you want to include the MIT license in your project, it typically requires including a short disclaimer and the full text of the license. This is usually added to a `LICENSE` file in the root of your project or at the bottom of your README.

Here’s an example of how you can include the license at the bottom of your README:

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
