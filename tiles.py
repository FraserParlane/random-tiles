from abc import ABC, abstractmethod
from typing import List, Optional
from lxml import etree, builder
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
animate_transform = elements.animateTransform

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


def semi_path(
        width: float,
        height: float,
        pos: int = 0,
        reflect: bool = False,
) -> str:

    # Define a lookup dict for the path based on the position and reflection.
    d = {
        0: {
            False: (1.0, 0.5, 0.0, 0.5),
            True:  (0.0, 0.0, 1.0, 0.0),
        },
        1: {
            False: (0.5, 0.0, 0.5, 1.0),
            True:  (0.0, 1.0, 0.0, 0.0),
        },
        2: {
            False: (0.0, 0.5, 1.0, 0.5),
            True:  (1.0, 1.0, 0.0, 1.0),
        },
        3: {
            False: (0.5, 1.0, 0.5, 0.0),
            True:  (1.0, 0.0, 1.0, 1.0),
        }
    }

    # Select the appropriate scalars for the path, and scale.
    ix, iy, jx, jy = np.multiply(d[pos][reflect], [width, height, width, height])

    # Build path string
    d = f'M {ix} {iy} A {0.5 * width} {0.5 * height} 0 0 0 {jx} {jy}'
    return d


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
            animate: bool = True,
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


def arc_test():

    doc = svg(
        xmlns='http://www.w3.org/2000/svg',
        height='100',
        width='100',
    )

    # Make background
    doc.append(
        rect(
            x='0',
            y='0',
            width='100',
            height='100',
            fill='#FFFFFF',
        )
    )

    # Path
    doc.append(
        path(
            # pos 0, False
            # d="M 100 50 A 50 50 0 0 0 0 50",

            # pos 0, True
            # d="M 0 0 A 50 50 0 0 0 100 0",

            # Pos 1, False
            # d="M 50 0 A 50 50 0 0 0 50 100",

            # Pos 1, True
            # d="M 0 100 A 50 50 0 0 0 0 0",

            # pos 2, False
            # d="M 0 50 A 50 50 0 0 0 100 50",

            # pos 2, True
            # d="M 100 100 A 50 50 0 0 0 0 100",

            # Pos 3, False
            # d="M 50 100 A 50 50 0 0 0 50 0",

            # Pos 3, True
            # d="M 100 0 A 50 50 0 0 0 100 100",

            fill="blue",
        )
    )

    with open('test.svg', 'wb') as f:
        f.write(etree.tostring(doc, pretty_print=True))


if __name__ == '__main__':

    make_semicircle(width=100, height=100)

    # arc_test()

    # generate_tiles(
    #     tiles=[
    #         HalfCircleTile,
    #         QuarterCircleTile,
    #         InsetCircleTile,
    #     ]
    # )
