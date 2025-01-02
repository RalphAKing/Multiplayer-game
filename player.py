import pygame
import socket
import pickle

WIDTH, HEIGHT = 800, 600
BG_COLOR = (30, 30, 30)
DOT_COLOR = (0, 255, 0)
TEXT_COLOR = (255, 255, 255)
HEALTH_BAR_COLOR = (255, 0, 0)
HEALTH_BAR_BG_COLOR = (100, 100, 100)
FONT_SIZE = 20
BAR_WIDTH = 50
BAR_HEIGHT = 5

HOST = '127.0.0.1'
PORT = 5555

def draw_health_bar(screen, x, y, health, max_health):
    health_ratio = health / max_health
    pygame.draw.rect(screen, HEALTH_BAR_BG_COLOR, (x - BAR_WIDTH // 2, y + 15, BAR_WIDTH, BAR_HEIGHT))
    pygame.draw.rect(screen, HEALTH_BAR_COLOR, (x - BAR_WIDTH // 2, y + 15, BAR_WIDTH * health_ratio, BAR_HEIGHT))
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
    died = False  # Track if the player is dead

    while running:
        screen.fill(BG_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        key_data = {
            "w": keys[pygame.K_w],
            "s": keys[pygame.K_s],
            "a": keys[pygame.K_a],
            "d": keys[pygame.K_d]
        }
        client.send(pickle.dumps(key_data))

        try:
            data = client.recv(4096)
            game_data = pickle.loads(data)
            players = game_data["positions"]
            health = game_data["health"]

            if "death" in game_data:
                if game_data["death"] == username:
                    died = True
                    break
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

            draw_health_bar(screen, pos[0], pos[1], health[name], 100)
        
        if died:
            died_text = font.render("You Died", True, (255, 0, 0))
            screen.blit(died_text, (WIDTH // 2 - died_text.get_width() // 2, HEIGHT // 2 - 20))

        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()
    client.close()


if __name__ == "__main__":
    main()
