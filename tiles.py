from abc import ABC, abstractmethod
from lxml import etree, builder
from typing import List

# Initialize some SVG objects
elements = builder.ElementMaker()
svg = elements.svg
path = elements.path
circle = elements.circle
rect = elements.rect


class Tile(ABC):

    def __init__(
            self,
            colors: List[str],
            colors_random: bool = True,
            width: int = 100,
            height: int = 100,
    ):

        # Store parameter data
        self.width = width
        self.height = height

        # Randomize and store the colors
        colors = np.array(colors)
        if colors_random:
            colors = np.random.shuffle(colors)
        self.colors = colors

        # Initialize SVG
        self.doc = svg(
            xmlns='http://www.w3.org/2000/svg',
            height=str(self.height),
            width=str(self.width),
        )

    @abstractmethod
    def build(self):
        pass


class CircleTile(Tile):
    def build(self):
        return a



if __name__ == '__main__':

    print(a.width)