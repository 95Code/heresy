# --- IMPORTS ---

import numpy as np
import imageio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# --- FUNCTIONS ---

def imread(filename):
    img = imageio.imread(filename) / 255.0
    img = np.asarray(img, dtype=np.float32)
    return img

def imwrite(filename, img):
    img = np.asarray(255 * img, dtype=np.uint8)
    imageio.imwrite(filename, img)

def kernel_show(kernel):
    if len(img.shape) != 2:
        return

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    m, n = img.shape
    x = index(m, n, axis="x")
    y = index(m, n, axis="y")

    cmap = "viridis"    # "plasma"
    ax.plot_surface(x, y, img, cmap=cmap)
    plt.show()


# --- SCRIPT ---

if __name__ == "__main__":
    pass

