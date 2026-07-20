import pygame
import random
import time

pygame.init()
#Screen Dummy
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turtle to the Sea")

# Colors
BEIGE = (245, 245, 220)   
BLUE = (0, 191, 255)       
DARK_GREEN = (0, 100, 0)  
GREEN = (34, 139, 34)      
RED = (220, 20, 60)       
YELLOW = (255, 215, 0)    

PLASTIC_COLORS = [
    (169, 169, 169),   
    (255, 0, 0),       
    (0, 255, 0),       
    (0, 0, 255),      
    (255, 255, 0),    
    (255, 165, 0),    
    (128, 0, 128)     
]

# Turtle setup
turtle_size = 40
turtle_spawn = (WIDTH//2, HEIGHT-60)
turtle = pygame.Rect(*turtle_spawn, turtle_size, turtle_size)

# Ocean setup
ocean = pygame.Rect(0, 0, WIDTH, 60)

# Obstacles
plastic_size = 40
plastics = []  
poisons = []
people = []

# Game variables
clock = pygame.time.Clock()
running = True
round_num = 1
speed = 5
lives = 3
game_over = False

# High score record
high_score_round = 0
high_score_time = float("inf")

# Timer
start_time = None   
final_time = 0

safe_zone = pygame.Rect(WIDTH//2 - 60, HEIGHT-120, 120, 120)

def generate_obstacles(round_num):
    cols = 12
    gap_col = random.randint(0, cols-1)
    
    # Plastics
    if round_num < 3:
        num_new_plastics = 1
    elif round_num < 6:
        num_new_plastics = random.randint(2, 3)
    else:
        num_new_plastics = random.randint(2, 4)
    
    for _ in range(num_new_plastics):
        while True:
            c = random.randint(0, cols-1)
            r = random.randint(0, round_num)
            if c == gap_col:
                continue
            x = c * (WIDTH//cols) + 5
            y = 100 + r * (plastic_size + 15)
            new_rect = pygame.Rect(x, y, plastic_size, plastic_size)
            if safe_zone.colliderect(new_rect):
                continue
            if not any(new_rect.colliderect(p["rect"]) for p in plastics) \
               and not any(new_rect.colliderect(q) for q in poisons) \
               and not any(new_rect.colliderect(person["rect"]) for person in people):
                plastics.append({"rect": new_rect, "color": random.choice(PLASTIC_COLORS)})
                break
    
    # Poisons
    if round_num >= 6:
        num_new_poisons = random.randint(1, 2)
        for _ in range(num_new_poisons):
            while True:
                c = random.randint(0, cols-1)
                r = random.randint(0, round_num)
                if c == gap_col:
                    continue
                x = c * (WIDTH//cols) + 5
                y = 100 + r * (plastic_size + 15)
                new_poison = pygame.Rect(x, y, plastic_size, plastic_size)
                if safe_zone.colliderect(new_poison):
                    continue
                if not any(new_poison.colliderect(p["rect"]) for p in plastics) \
                   and not any(new_poison.colliderect(q) for q in poisons) \
                   and not any(new_poison.colliderect(person["rect"]) for person in people):
                    poisons.append(new_poison)
                    break
    
    # People
    if round_num >= 4:
        num_new_people = random.randint(1, 2)
        for _ in range(num_new_people):
            y = random.randint(150, HEIGHT-200)
            person = pygame.Rect(random.randint(0, WIDTH-40), y, 40, 40)
            people.append({"rect": person, "dir": random.choice([-3, 3])})

def draw_game():
    screen.fill(BEIGE)  
    pygame.draw.rect(screen, BLUE, ocean)
    # Turtle
    pygame.draw.rect(screen, DARK_GREEN, turtle)
    shell = pygame.Rect(turtle.x+5, turtle.y+5, turtle_size-10, turtle_size-10)
    pygame.draw.rect(screen, GREEN, shell)
    # Plastics with random colors
    for p in plastics:
        pygame.draw.rect(screen, p["color"], p["rect"])
    # Poisons
    for q in poisons:
        pygame.draw.rect(screen, RED, q)
    # People
    for person in people:
        pygame.draw.rect(screen, YELLOW, person["rect"])
    # HUD
    font = pygame.font.SysFont(None, 36)
    elapsed = int(time.time() - start_time) if (start_time and not game_over) else final_time
    text = font.render(f"Round {round_num} | Lives: {lives} | Time: {elapsed}s", True, DARK_GREEN)
    screen.blit(text, (10, HEIGHT-40))
    pygame.display.flip()

def draw_game_over():
    screen.fill(BEIGE)
    font_big = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)
    text1 = font_big.render("GAME OVER", True, RED)
    text2 = font_small.render("Press R to Restart or Q to Quit", True, DARK_GREEN)
    text3 = font_small.render(f"Your Score: Round {round_num}, Time {final_time}s", True, DARK_GREEN)
    hs_time = high_score_time if high_score_time != float("inf") else 0
    text4 = font_small.render(f"High Score: Round {high_score_round}, Time {hs_time}s", True, DARK_GREEN)
    screen.blit(text1, (WIDTH//2 - 150, HEIGHT//2 - 120))
    screen.blit(text2, (WIDTH//2 - 200, HEIGHT//2 - 40))
    screen.blit(text3, (WIDTH//2 - 200, HEIGHT//2 + 20))
    screen.blit(text4, (WIDTH//2 - 200, HEIGHT//2 + 60))
    pygame.display.flip()

def end_game():
    global game_over, final_time, high_score_round, high_score_time
    final_time = int(time.time() - start_time) if start_time else 0
    if (round_num > high_score_round) or (round_num == high_score_round and final_time < high_score_time):
        high_score_round = round_num
        high_score_time = final_time
    game_over = True


generate_obstacles(round_num)

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not game_over:
        keys = pygame.key.get_pressed()
        moved = False
        if keys[pygame.K_LEFT] and turtle.left > 0:
            turtle.x -= speed; moved = True
        if keys[pygame.K_RIGHT] and turtle.right < WIDTH:
            turtle.x += speed; moved = True
        if keys[pygame.K_UP] and turtle.top > 0:
            turtle.y -= speed; moved = True
        if keys[pygame.K_DOWN] and turtle.bottom < HEIGHT:
            turtle.y += speed; moved = True

        
        if moved and start_time is None:
            start_time = time.time()

        # People movement
        for person in people:
            person["rect"].x += person["dir"]
            if person["rect"].left <= 0 or person["rect"].right >= WIDTH:
                person["dir"] *= -1

       

        # Plastic collision
        if any(turtle.colliderect(p["rect"]) for p in plastics):
            turtle.x, turtle.y = turtle_spawn
            lives -= 1
            if lives <= 0:
                end_game()

        # Poison collision
        if any(turtle.colliderect(q) for q in poisons):
            turtle.x, turtle.y = turtle_spawn
            lives -= 1
            if lives <= 0:
                end_game()

        # Person collision
        if any(turtle.colliderect(person["rect"]) for person in people):
            turtle.x, turtle.y = turtle_spawn
            lives -= 1
            if lives <= 0:
                end_game()

        
        if turtle.colliderect(ocean):
            round_num += 1
            turtle.x, turtle.y = turtle_spawn
            generate_obstacles(round_num)

        draw_game()

    else:
        draw_game_over()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            # Restart Dummy
            turtle.x, turtle.y = turtle_spawn
            plastics.clear()
            poisons.clear()
            people.clear()

            round_num = 1
            lives = 3
            speed = 5
            start_time = None
            final_time = 0
            game_over = False

            generate_obstacles(round_num)

        elif keys[pygame.K_q]:
            running = False

pygame.quit()