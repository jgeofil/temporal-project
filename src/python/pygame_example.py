import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Animation Example")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Animation variables
angle = 0
radius = 150

def main():
    global angle
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill(BLACK)
        
        # Calculate position for orbiting circles
        for i in range(8):
            orbit_angle = angle + (i * math.pi / 4)
            x = WIDTH // 2 + int(radius * math.cos(orbit_angle))
            y = HEIGHT // 2 + int(radius * math.sin(orbit_angle))
            
            # Draw orbiting circle
            color = ((i * 32) % 256, 255 - ((i * 32) % 256), ((i * 64) % 256))
            pygame.draw.circle(screen, color, (x, y), 30)
        
        # Update angle for animation
        angle += 0.02
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()