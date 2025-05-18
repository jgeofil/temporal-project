// P5.js example sketch

let angle = 0;

function setup() {
  createCanvas(windowWidth, windowHeight);
  colorMode(HSB, 360, 100, 100);
  rectMode(CENTER);
  noStroke();
}

function draw() {
  background(234, 34, 24);
  
  translate(width / 2, height / 2);
  
  for (let i = 0; i < 12; i++) {
    push();
    rotate(TWO_PI * i / 12 + angle);
    translate(200, 0);
    
    // Draw shape
    fill((i * 30 + frameCount) % 360, 80, 90);
    rect(0, 0, 100, 100);
    
    pop();
  }
  
  // Update angle
  angle += 0.01;
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}