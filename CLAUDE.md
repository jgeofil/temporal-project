# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains tools and examples for creating animations using various JavaScript and Python libraries. It supports:

- JavaScript: Three.js, P5.js
- Python: Pygame, Arcade, Processing.py

## Development Commands

### JavaScript Development

```bash
# Install dependencies
npm install

# Run the development server (serves the examples)
npm run serve

# Lint JavaScript files
npm run lint:js
```

### Python Development

```bash
# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Python examples
python src/python/pygame_example.py
python src/python/arcade_example.py
python src/python/processing_example.py
```

## Architecture

The repository is organized as follows:

- `src/js/` - JavaScript animation source code
  - Uses Three.js for 3D animations
  - Uses P5.js for creative coding and 2D animations
  
- `src/python/` - Python animation source code
  - Pygame examples for 2D game development
  - Arcade examples for modern Python game development
  - Processing.py for Processing-style animations

- `examples/` - Complete example projects demonstrating the libraries
  - JavaScript examples have HTML files that can be viewed in a browser
  - Python examples are standalone scripts that can be run directly

- `assets/` - Shared resources like images, models, textures, and audio files

## Conventions

### JavaScript
- Use ES6 modules for JavaScript code
- Follow the ESLint configuration for code style

### Python
- PEP 8 style guide for Python code
- Use virtual environments for dependency management