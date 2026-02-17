import pytest

from pyramid_calculator.calculator import calculate_height_of_pyramid

# Check the height of pyramind when blocks=0
def test_blocks_0_height_0():
    assert calculate_height_of_pyramid(0)==0

# Check the height of pyramid when blocks=6
def test_blocks_6_height_3():
    assert calculate_height_of_pyramid(6)==3

# Check the height of pyramid when blocks=200
def test_blocks_200_height_19():
    assert calculate_height_of_pyramid(200)==19


