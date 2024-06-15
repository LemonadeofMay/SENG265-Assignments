#!/usr/bin/env python
# coding: utf-8

# In[5]:


"""Assignment 4 Part 3"""
print(__doc__)

from typing import IO
from froma41 import Circle, Rectangle, Ellipse, SvgCanvas, HtmlDocument
from froma42 import PyArtConfig, RandomShape
import random

def nums_to_shapes(config: PyArtConfig) -> list:
    """nums_to_shapes method"""
    storage: list = []
    base = RandomShape()
    base.random_numbers.clear()
    base.generate_shape(config)
    for item in base.random_numbers:
        color: tuple = (item[9], item[10], item[11], item[12])
        if item[1] == 0:
            c: tuple = (item[2], item[3], item[4])
            shape = Circle(c, color)
        elif item[1] == 1:
            r: tuple = (item[2], item[3], item[7], item[8])
            shape = Rectangle(r, color)
        else:
            e: tuple = (item[2], item[3], item[5], item[6])
            shape = Ellipse(e, color)
        storage.append(shape)
    return storage

def create_webpage(fnam: str, title: str, window: tuple, storage: list) -> None:
    """create_webpage method"""
    page = HtmlDocument(title, fnam)
    page.writeHTMLHeader()
    page.writeSVG(storage, window)
    page.closeHTML()

def main() -> None:
    """main method"""
    window1: tuple = (1000, 500)
    window2: tuple = (600, 400)
    window3: tuple = (100, 400)
    items1: int = 500
    items2: int = 10000
    items3: int = 20
    fnam1: str = "a431.html"
    fnam2: str = "a432.html"
    fnam3: str = "a433.html"
    title1: str = "Random Art 1"
    title2: str = "Random Art 2"
    title3: str = "Random Art 3"
        
    config1 = PyArtConfig(items1, window1)
    config2 = PyArtConfig(items2, window2)
    config3 = PyArtConfig(items3, window3)
    
    sto1 = nums_to_shapes(config1)
    sto2 = nums_to_shapes(config2)
    sto3 = nums_to_shapes(config3)
    
    create_webpage(fnam1, title1, window1, sto1)
    create_webpage(fnam2, title2, window2, sto2)
    create_webpage(fnam3, title3, window3, sto3)
    
if __name__ == "__main__":
    main()

