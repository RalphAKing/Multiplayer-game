import pygame
import socket
import pickle

WIDTH, HEIGHT = 800, 600
BG_COLOR = (30, 30, 30)
DOT_COLOR = (0, 255, 0)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 20

HOST = '127.0.0.1'
PORT = 5555

def main():
    username = input("Enter your username: ")
 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(username.encode('utf-8'))

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Multiplayer Game")
    font = pygame.font.Font(None, FONT_SIZE)
    
    clock = pygame.time.Clock()
    running = True
    x, y = WIDTH // 2, HEIGHT // 2
    speed = 5

    while running:
        screen.fill(BG_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y -= speed
        if keys[pygame.K_s]:
            y += speed
        if keys[pygame.K_a]:
            x -= speed
        if keys[pygame.K_d]:
            x += speed

        position = (x, y)
        client.send(pickle.dumps(position))

        try:
            data = client.recv(1024)
            players = pickle.loads(data)
        except:
            break
    
        for name, pos in players.items():
            if name == username:
                color = DOT_COLOR
            else:
                color = (255, 0, 0)
            pygame.draw.circle(screen, color, pos, 10)
            text = font.render(name, True, TEXT_COLOR)
            screen.blit(text, (pos[0] - text.get_width() // 2, pos[1] - 20))
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    client.close()

if __name__ == "__main__":
    main()
