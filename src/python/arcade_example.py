import arcade
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Animation Example"
NUM_PARTICLES = 100

class Particle:
    def __init__(self, x, y, size, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.time = 0

    def update(self, delta_time):
        self.time += delta_time
        
        # Update position
        self.x += self.speed_x * delta_time
        self.y += self.speed_y * delta_time
        
        # Bounce off walls
        if self.x < self.size or self.x > SCREEN_WIDTH - self.size:
            self.speed_x *= -1
        
        if self.y < self.size or self.y > SCREEN_HEIGHT - self.size:
            self.speed_y *= -1

class AnimationExample(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.particles = []
        self.time = 0
        
    def setup(self):
        # Create particles
        for i in range(NUM_PARTICLES):
            x = arcade.random.randrange(SCREEN_WIDTH)
            y = arcade.random.randrange(SCREEN_HEIGHT)
            size = arcade.random.randrange(5, 15)
            
            # Random color
            r = arcade.random.randrange(256)
            g = arcade.random.randrange(256)
            b = arcade.random.randrange(256)
            color = (r, g, b)
            
            # Random speed
            speed_x = arcade.random.randrange(-100, 100) / 50
            speed_y = arcade.random.randrange(-100, 100) / 50
            
            particle = Particle(x, y, size, color, speed_x, speed_y)
            self.particles.append(particle)
    
    def on_update(self, delta_time):
        self.time += delta_time
        
        for particle in self.particles:
            particle.update(delta_time)
    
    def on_draw(self):
        self.clear()
        
        for particle in self.particles:
            # Make size pulse
            pulse = (math.sin(self.time * 2 + particle.time) + 1) * 0.5
            size = particle.size * (0.8 + 0.4 * pulse)
            
            arcade.draw_circle_filled(particle.x, particle.y, size, particle.color)

def main():
    window = AnimationExample()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()