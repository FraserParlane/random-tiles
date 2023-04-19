from abc import ABC, abstractmethod
from lxml import etree, builder
from typing import List
from tqdm import tqdm
import numpy as np
import shutil
import os


# Initialize some SVG objects
elements = builder.ElementMaker()
svg = elements.svg
path = elements.path
circle = elements.circle
rect = elements.rect

# Colors to use
color_list = [
    '#003f5c',
    # '#2f4b7c',
    '#665191',
    # '#a05195',
    '#d45087',
    # '#f95d6a',
    '#ff7c43',
    # '#ffa600',
]

# color_list = [
#     '#f8981d',
#     '#191717',
#     '#d9d9d9',
#     '#282525',
# ]


class Tile(ABC):
    """
    Base tile class.
    """

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
        self._color_idx = -1
        self.colors = np.array(colors)
        if colors_random:
            np.random.shuffle(self.colors)

        # Initialize the svg
        self.doc = None
        self._init_svg()
        self.build()

    def get_color(self) -> str:
        """
        Get the current color.
        :return: color.
        """
        self._color_idx += 1
        return self.colors[self._color_idx % len(self.colors)]

    def _init_svg(self):
        """
        Initialize the SVG document.
        :return: None
        """

        # Make doc
        self.doc = svg(
            xmlns='http://www.w3.org/2000/svg',
            height=str(self.height),
            width=str(self.width),
        )

        # Make background
        self.doc.append(
            rect(
                x='0',
                y='0',
                width=str(self.width),
                height=str(self.height),
                fill=self.get_color(),
            )
        )

    def save(self, filepath: str):
        """
        Save to disk
        :param filepath: Where to save
        :return: None
        """
        with open(filepath, 'wb') as f:
            f.write(etree.tostring(self.doc, pretty_print=True))

    @abstractmethod
    def build(self):
        pass


class HalfCircleTile(Tile):
    def build(self):
        reflect = np.random.choice([True, False])
        color = self.get_color()
        for y in [0, self.height]:
            kwargs = {
                'cx': str(self.width / 2),
                'cy': str(y),
            }
            if reflect:
                kwargs['cx'], kwargs['cy'] = kwargs['cy'], kwargs['cx']

            self.doc.append(
                circle(
                    r=str(self.height / 2),
                    fill=color,
                    **kwargs,
                )
            )


class QuarterCircleTile(Tile):
    def build(self):
        color = self.get_color()
        for x in [0, self.width]:
            for y in [0, self.height]:
                self.doc.append(
                    circle(
                        cx=str(x),
                        cy=str(y),
                        r=str(self.width / 2),
                        fill=color,
                    )
                )


class InsetCircleTile(Tile):
    def build(self):
        n = np.random.choice([1, 2, 2, 2])
        for r in np.linspace(0, self.width / 2, n+1)[1:][::-1]:
            self.doc.append(
                circle(
                    cx=str(self.width / 2),
                    cy=str(self.height / 2),
                    r=str(r),
                    fill=self.get_color(),
                )
            )


def generate_tiles(
        tiles: List,
        n: int = 400,
        folder: str = 'tiles',
) -> None:
    """
    Generate tiles.
    :param n: Number of tiles to generate
    :param tiles: Tile classes to use
    :param folder: Path to store tiles.
    :return: None
    """

    # Make empty folder
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    # For each tile
    for i in tqdm(range(n)):

        # Get a random tile class
        tile_class = np.random.choice(tiles)
        t: Tile = tile_class(colors=color_list)
        t.save(f'{folder}/{str(i).zfill(3)}.svg')


if __name__ == '__main__':

    generate_tiles(
        tiles=[
            HalfCircleTile,
            QuarterCircleTile,
            InsetCircleTile,
        ]
    )
