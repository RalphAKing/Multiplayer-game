import socket
import threading
import pickle
import time

HOST = '127.0.0.1'  
PORT = 5555

players = {}
player_keys = {}
clients = []  
player_speed = 5 
UPDATE_RATE = 30 
PLAYER_RADIUS = 10 
MAX_HEALTH = 100  
player_health = {}


def handle_client(conn, addr):
    global players, clients, player_health
    username = conn.recv(1024).decode('utf-8')
    print(f"{username} connected from {addr}")
    
    players[username] = (400, 300)  
    player_keys[username] = {"w": False, "s": False, "a": False, "d": False}
    player_health[username] = MAX_HEALTH 
    clients.append(conn)
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            key_data = pickle.loads(data)
            player_keys[username] = key_data

            if player_health[username] <= 0:
                death_message = pickle.dumps({"death": username})
                for client in clients:
                    try:
                        client.sendall(death_message)
                    except:
                        clients.remove(client)

                break

    except:
        pass
    finally:
        del players[username]
        del player_keys[username]
        del player_health[username]
        clients.remove(conn)
        conn.close()
        print(f"{username} disconnected.")





def detect_collisions():
    global players, player_health
    for player1, pos1 in players.items():
        for player2, pos2 in players.items():
            if player1 != player2:
                dist = ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
                if dist < 2 * PLAYER_RADIUS:
                    resolve_collision(player1, player2, pos1, pos2)

def resolve_collision(player1, player2, pos1, pos2):
    global player_health
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    dist = max(((dx ** 2 + dy ** 2) ** 0.5), 1) 
    overlap = 2 * PLAYER_RADIUS - dist
    if overlap > 0:
        push_x = (dx / dist) * (overlap / 2)
        push_y = (dy / dist) * (overlap / 2)

        players[player1] = (pos1[0] + push_x, pos1[1] + push_y)
        players[player2] = (pos2[0] - push_x, pos2[1] - push_y)

        player_health[player1] = max(0, player_health[player1] - 1)
        player_health[player2] = max(0, player_health[player2] - 1)

        if player_health[player1] <= 0:
            death_message = pickle.dumps({"death": player1})
            for client in clients:
                try:
                    client.sendall(death_message)
                except:
                    clients.remove(client)

        if player_health[player2] <= 0:
            death_message = pickle.dumps({"death": player2})
            for client in clients:
                try:
                    client.sendall(death_message)
                except:
                    clients.remove(client)


def update_positions():
    global players
    for username, keys in player_keys.items():
        x, y = players[username]
        if keys.get("w"):
            y -= player_speed
        if keys.get("s"):
            y += player_speed
        if keys.get("a"):
            x -= player_speed
        if keys.get("d"):
            x += player_speed

        x = max(0, min(x, 800))
        y = max(0, min(y, 600))

        players[username] = (x, y)
    detect_collisions()

def broadcast_positions():
    global clients
    while True:
        update_positions()
        data = pickle.dumps({"positions": players, "health": player_health})
        for client in list(clients):  
            try:
                client.sendall(data)
            except:
                clients.remove(client)
        time.sleep(1 / UPDATE_RATE)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server running on {HOST}:{PORT}")

    threading.Thread(target=broadcast_positions, daemon=True).start()

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
