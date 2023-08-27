import matplotlib.cm
from PIL import Image

from mandelbrot import MandelbrotSet
from viewport import Viewport


def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stability = mandelbrot_set.stability(complex(pixel), smooth)
        index = int(min(stability * len(palette), len(palette) - 1))
        pixel.color = palette[index % len(palette)]


def denormalize(palette):
    return [
        tuple(int(channel * 255) for channel in color) for color in palette
    ]


if __name__ == "__main__":
    print("This might take a while...")

    colormap = matplotlib.cm.get_cmap("twilight").colors
    palette = denormalize(colormap)

    mandelbrot_set = MandelbrotSet(max_iterations=1000, escape_radius=1500)
    image = Image.new(mode="RGB", size=(1500, 1500))
    viewport = Viewport(image, center=-0.7442 + 0.131415926j, width=0.00069)
    paint(mandelbrot_set, viewport, palette, smooth=True)
    image.show()
