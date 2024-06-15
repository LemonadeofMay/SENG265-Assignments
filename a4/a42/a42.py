#!/usr/bin/env python
# coding: utf-8
"""Assignment 4 Part 2"""
print(__doc__)

import random
#from collections import namedtuple

#Shape = namedtuple("Shape", "num shape x y rad rx ry w h r g b op")

class PyArtConfig:
    """pyArtConfig class"""
    sha: tuple = (0, 2)
    rad: tuple = (0, 100)
    rx: tuple = (10, 30)
    ry: tuple = (10, 30)
    w: tuple = (10, 100)
    h: tuple = (10, 100)
    r: tuple = (0, 255)
    g: tuple = (0, 255)
    b: tuple = (0, 255)
    
    def __init__(self, count: int, viewport: tuple) -> None:
        self.cnt: int = count
        self.x: int = viewport[0]
        self.y: int = viewport[1]
    
class RandomShape:
    """RandomShape class"""
    random_numbers: list = [["CNT","SHA","X","Y","RAD","RX","RY","W","H","R","G","B","OP"]]
        
    def __init__(self):
        pass
    
    def generate_shape(self, ran: PyArtConfig) -> None:
        """generate_shape method"""
        for n in range(ran.cnt):
            new: list = []
            new.append(n)
            new.append(random.randint(ran.sha[0],ran.sha[1]))
            new.append(random.randint(0,ran.x))
            new.append(random.randint(0,ran.y))
            new.append(random.randint(ran.rad[0], ran.rad[1]))
            new.append(random.randint(ran.rx[0],ran.rx[1]))
            new.append(random.randint(ran.ry[0],ran.ry[1]))
            new.append(random.randint(ran.w[0],ran.w[1]))
            new.append(random.randint(ran.h[0],ran.h[1]))
            new.append(random.randint(ran.r[0],ran.r[1]))
            new.append(random.randint(ran.g[0],ran.g[1]))
            new.append(random.randint(ran.b[0],ran.b[1]))
            new.append(random.random())
            # new = list(num=n, shape=shape, x=x, y=y, rad=rad, rx=rx, ry=ry, w=w, h=h, r=r, g=g, b=b, op=op)
            self.random_numbers.append(new)
    
    def __str__(self) -> str:
        """str method"""
        to_return = ""
        for n in self.random_numbers:
            to_return += f'{n}\n'
        return to_return
        
    def as_Part2_line(self) -> str:
        """as_Part2_line method"""
        max_width = max(len(str(element)) for row in self.random_numbers for element in row)
        to_return: str = ""

        for row in self.random_numbers:
            to_add: str = ""
            for element in row:
                if isinstance(element, float):
                    formatted = f'{element:.1g}'
                    to_add += f'{formatted:>{max_width}} '
                else:
                    to_add += f'{element:>{max_width}} '
            to_return += f'{to_add}\n'
        
        return to_return
    
    def as_svg(self) -> str:
        """as_svg method"""
        to_return = ""
        for n in self.random_numbers:
            if n[1] == 0:
                line1: str = f'<circle cx="{n[2]}" cy="{n[3]}" r="{n[4]}" '
                line2: str = f'fill="rgb({n[9]}, {n[10]}, {n[11]})" fill-opacity="{n[12]}"></circle>'
            elif n[1] == 1:
                line1: str = f'<rect x="{n[2]}" y="{n[3]}" width="{n[7]}" height="{n[8]}" '
                line2: str = f'fill="rgb({n[9]}, {n[10]}, {n[11]})" fill-opacity="{n[12]}"></rect>'
            else:
                line1: str = f'<ellipse cx="{n[2]}" cy="{n[3]}" rx="{n[5]}" ry="{n[6]}" '
                line2: str = f'fill="rgb({n[9]}, {n[10]}, {n[11]})" fill-opacity="{n[12]}"></ellipse>'
            to_return += f'{line1}{line2}\n'
        return to_return

def main() -> None:
    """main method"""
    num: int = 10
    grid: tuple = (500, 300)
    new_config = PyArtConfig(num, grid)
    new_art = RandomShape()
    new_art.generate_shape(new_config)
    print(new_art)
    print()
    grid_line = new_art.as_Part2_line()
    print(grid_line)
    svg_line = new_art.as_svg()
    print(svg_line)

if __name__ == "__main__":
    main()

