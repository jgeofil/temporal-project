from processing_py import PGraphics, PApplet
from math import sin, cos, radians, pi

class ProcessingSketch(PApplet):
    def __init__(self, width=800, height=600):
        PApplet.__init__(self, width, height)
        self.particles = []
        self.time = 0
        
    def setup(self):
        self.size(800, 600)
        self.colorMode(mode=self.HSB, max1=360, max2=100, max3=100)
        self.background(0)
        
        # Create particles
        for i in range(30):
            self.particles.append({
                'x': self.width / 2,
                'y': self.height / 2,
                'size': self.random(10, 30),
                'angle': self.random(0, 360),
                'speed': self.random(1, 5),
                'hue': self.random(0, 360),
                'offset': self.random(0, pi)
            })
    
    def draw(self):
        self.background(0, 0, 20)
        self.time += 0.01
        
        # Draw each particle
        for p in self.particles:
            # Update position
            p['x'] += cos(radians(p['angle'])) * p['speed']
            p['y'] += sin(radians(p['angle'])) * p['speed']
            
            # Bounce off edges
            if p['x'] < 0 or p['x'] > self.width:
                p['angle'] = 180 - p['angle']
            if p['y'] < 0 or p['y'] > self.height:
                p['angle'] = 360 - p['angle']
            
            # Draw particle
            self.noStroke()
            size = p['size'] + sin(self.time + p['offset']) * 5
            hue = (p['hue'] + self.frameCount / 10) % 360
            self.fill(hue, 80, 90)
            self.ellipse(p['x'], p['y'], size, size)
            
            # Draw trail
            self.strokeWeight(2)
            self.stroke(hue, 80, 90, 30)
            trail_x = p['x'] - cos(radians(p['angle'])) * 20
            trail_y = p['y'] - sin(radians(p['angle'])) * 20
            self.line(p['x'], p['y'], trail_x, trail_y)

if __name__ == '__main__':
    sketch = ProcessingSketch()
    sketch.run()