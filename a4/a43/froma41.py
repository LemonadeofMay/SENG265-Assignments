#!/usr/bin/env python
"""Assignment 4 Part 1 Version 3 template"""
print(__doc__)

from typing import IO

class Circle:
    """Circle class"""
    def __init__(self, cir: tuple, col: tuple) -> None:
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
    
    def draw_circle(self, f: IO[str]) -> None:
        """draw_circle method"""
        ts: str = "   " * 2
        line1: str = f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.rad}" '
        line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></circle>'
        f.write(f"{ts}{line1+line2}\n")
        
class Rectangle:
    """Rectangle class"""
    def __init__(self, rect: tuple, col: tuple) -> None:
        self.x: int = rect[0]
        self.y: int = rect[1]
        self.w: int = rect[2]
        self.h: int = rect[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def draw_rectangle(self, f: IO[str]) -> None:
        """draw_rectangle method"""
        ts: str = "   " * 2
        line1: str = f'<rect x="{self.x}" y="{self.y}" width="{self.w}" height="{self.h}" '
        line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></rect>'
        f.write(f"{ts}{line1+line2}\n")
        
class Ellipse:
    """Ellipse class"""
    def __init__(self, ell: tuple, col: tuple) -> None:
        self.cx: int = ell[0]
        self.cy: int = ell[1]
        self.rx: int = ell[2]
        self.ry: int = ell[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def draw_ellipse(self, f: IO[str]) -> None:
        """draw_ellipse method"""
        ts: str = "   " * 2
        line1: str = f'<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" '
        line2: str = f'fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></ellipse>'
        f.write(f"{ts}{line1+line2}\n")

class SvgCanvas:
    """SvgCanvas class"""
    def __init__(self, shapes: list, window: tuple) -> None:
        self.shapes: tuple = shapes
        self.width: int = window[0]
        self.height: int = window[1]
    
    def gen_art(self, f: IO[str]) -> None:
        """gen_art method"""
        ts: str = "   "
        openline: str = f'<svg width="{self.width}" height="{self.height}">'
        f.write(f"{ts}{openline}\n")
        for item in self.shapes:
            if isinstance(item, Circle):
                item.draw_circle(f)
            elif isinstance(item, Rectangle):
                item.draw_rectangle(f)
            else:
                item.draw_ellipse(f)
        endline: str = f'</svg>'
        f.write(f"{ts}{endline}\n")
            
class HtmlDocument:
    """HtmlDocument class"""
    def __init__(self, header: str, fnam: str) -> None:
        self.header: str = header
        self.f: IO[str] = open(fnam, "w")

    def writeHTMLcomment(self, com: str) -> None:
        """writeHTMLcomment method"""
        ts: str = "   "
        self.f.write(f"{ts}<!--{com}-->\n")

    def writeHTMLline(self, line: str) -> None:
        """writeLineHTML method"""
        self.f.write(f"{line}\n")
    
    def writeHTMLHeader(self) -> None:
        """writeHTMLHeader method"""
        self.writeHTMLline("<html>")
        self.writeHTMLline("<head>")
        self.writeHTMLline(f"   <title>{self.header}</title>")
        self.writeHTMLline("</head>")
        self.writeHTMLline("<body>")

    def closeHTML(self) -> None:
        """closeSVGcanvas method"""
        self.f.write(f"</body>\n")
        self.f.write(f"</html>\n")
        self.f.close()
    
    def writeSVG(self, shapes: tuple, window: tuple) -> None:
        """writeSVG method"""
        self.writeHTMLcomment("Define SVG drawing box")
        drawing: SvgCanvas = SvgCanvas(shapes, window)
        drawing.gen_art(self.f)
    

def main() -> None:
    """main method"""
    shapes: list = [Circle((50,50,50), (255,0,0,1.0)), Circle((150,50,50), (255,0,0,1.0)), Circle((250,50,50), (255,0,0,1.0)), Circle((350,50,50), (255,0,0,1.0)),Circle((450,50,50), (255,0,0,1.0)),Circle((50,250,50), (0,0,255,1.0)),Circle((150,250,50), (0,0,255,1.0)),Circle((250,250,50), (0,0,255,1.0)),Circle((350,250,50), (0,0,255,1.0)),Circle((450,250,50), (0,0,255,1.0))]
    windows: tuple = (500,300)
    fnam: str = "a41.html"
    winTitle = "My Art"
    page = HtmlDocument(winTitle, fnam)
    page.writeHTMLHeader()
    page.writeSVG(shapes, windows)
    page.closeHTML()

if __name__ == "__main__":
    main()
