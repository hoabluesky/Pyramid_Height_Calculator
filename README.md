# Pyramid Height Calculator

git 

## Problem Description
Given a number of blocks, the program determines how many complete levels of a pyramid can be built, where:
- Level 1 requires 1 block
- Level 2 requires 2 blocks
- Level 3 requires 3 blocks
- Each subsequent level requires one additional block than the previous level

## Example
```bash
Please enter the number of blocks: 8
The height of the pyramid is: 3
```

## Features
- Validates input
- Calculates pyramid height
- Includes unit tests

## Installation
1. Create and activate a virtual environment 
```bash
python -m venv venv
venv\Scripts\activate #Windows
```
2. Install the project in editable mode
```bash
pip install -e .
```
3. (Optional) Install development dependencies 
```bash
pip install -r requirements.txt
```

## Requirements
- Python 3.9+

## Run
```bash
python -m pyramid_calculator.cli
```

## Run Tests
```bash
pytest
```
