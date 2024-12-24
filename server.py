import socket
import threading
import pickle

HOST = '127.0.0.1'  
PORT = 5555

players = {}

def handle_client(conn, addr):
    global players
    username = conn.recv(1024).decode('utf-8')
    print(f"{username} connected from {addr}")
    
    players[username] = (0, 0)  
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            players[username] = pickle.loads(data)  
            
            conn.sendall(pickle.dumps(players))
    except:
        pass
    finally:
        del players[username]
        conn.close()
        print(f"{username} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server running on {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
