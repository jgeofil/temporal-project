# Animation JS/Python

A toolkit for creating animations using various JavaScript and Python libraries.

## Supported Libraries

### JavaScript
- Three.js - 3D animations
- P5.js - Creative coding and 2D animations

### Python
- Pygame - 2D game development
- Arcade - Modern Python framework for 2D video games
- Processing.py - Python implementation of Processing

## Setup

### JavaScript

```bash
# Install dependencies
npm install

# Serve examples
npm run serve
```

Then open your browser to http://localhost:8080/examples/js/

### Python

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run examples
python src/python/pygame_example.py
python src/python/arcade_example.py
python src/python/processing_example.py
```

## Project Structure

```
animation-js/
├── assets/            # Shared assets
│   ├── images/        # Image files
│   ├── models/        # 3D model files
│   ├── textures/      # Texture files
│   └── audio/         # Audio files
├── src/               # Source code
│   ├── js/            # JavaScript animations
│   └── python/        # Python animations
├── examples/          # Example projects
│   ├── js/            # JavaScript examples
│   └── python/        # Python examples
└── docs/              # Documentation
```

## License

MIT