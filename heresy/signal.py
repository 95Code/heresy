# --- IMPORTS ---

import numpy as np
import imageio
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# --- FUNCTIONS ---

def imread(filename):
    """Read the image at the given filename.

    :param filename: Path to the image.
    :returns: Numpy array of float image scaled between 0 and 1.

    """
    img = imageio.imread(filename) / 255.0
    img = np.asarray(img, dtype=np.float32)
    return img

def imwrite(filename, img):
    """Write an image to the desired filename.

    :param filename: Desired path to the image. 
    :param img: Numpy image scaled between 0 and 1.

    """
    img = np.asarray(255 * img, dtype=np.uint8)
    imageio.imwrite(filename, img)

def imfilter(img, kernel):
    """Filter an RGB image with a kernel. 

    :param img: Numpy RGB image.
    :param kernel: Numpy kernel.

    """
    red = signal.convolve2d(img[:,:,0], kernel, boundary="fill", mode="same") 
    green = signal.convolve2d(img[:,:,1], kernel, boundary="fill", mode="same") 
    blue = signal.convolve2d(img[:,:,2], kernel, boundary="fill", mode="same") 
    new_img = np.dstack([red, green, blue])
    return new_img 

def average_kernel(r):
    """

    :param r: 

    """
    n = 2 * r + 1
    A = np.ones((n,n), dtype=np.float32)
    A /= A.sum()
    return A 

def gaussian_kernel(r, sigma=1, seperable=False):
    """

    :param n: param sigma:  (Default value = 1)
    :param seperable: Default value = False)
    :param sigma:  (Default value = 1)

    """
    n = 2 * r + 1

    if seperable:
        # y == 0
        x = index(1, n, axis="x")
        G = np.ones((1, n), dtype=np.float32) / (2 * np.pi * sigma*sigma)
        G *= np.exp(-x**2 / (2 * sigma))
        G /= G.sum()

    else:
        x = index(n, n, axis="x")
        y = index(n, n, axis="y")
        G = np.ones((n, n), dtype=np.float32) / (2 * np.pi * sigma*sigma)
        G *= np.exp(-(x**2 + y**2) / (2 * sigma))
        G /= G.sum()

    return G

def disc_kernel(r, seperable=False):
    """

    :param n: param seperable:  (Default value = False)
    :param seperable:  (Default value = False)

    """
    n = 2 * r + 1
    x = index(n, n, axis="x")
    y = index(n, n, axis="y")
    D = np.zeros((n,n), dtype=np.float32)
    D[x**2 + y**2 <= (n//2)**2] = 1
    D /= D.sum()
    return D 

def blur(file_in="xmas.jpg", file_out="out.jpg", n=7, mode="avg"):
    """

    :param file_in: Default value = "xmas.jpg")
    :param file_out: Default value = "out.jpg")
    :param n: Default value = 7)
    :param mode: Default value = "avg")

    """
    img = imread(file_in)

    if mode == "avg":
        A = average(n)
        img_blur = imfilter(img, A)
    elif mode == "gaussian":
        G = gaussian(n)
        img_blur = imfilter(img, G)
    elif mode == "gaussian_seperable":


def show_kernel(kernel):
    """

    :param kernel: 

    """
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

def fix(n):
    """

    :param n: 

    """
    if n % 2 == 0:
        print(f"Bug: {n} is even.")
        print(f"Fix: {n} -> {n + 1}")
        n += 1
    return n

def index(m, n, axis="x"):
    """

    :param m: param n:
    :param axis: Default value = "x")
    :param n: 

    """
    def vector(n):
        """

        :param n: 

        """
        n = fix(n)
        x = np.arange(-(n-1)//2, (n+1)//2)
        return x
    
    if m % 2 == 0 or n % 2 == 0:
        print(f"Error! {m} or {n} is not odd!")
        return
    
    M = np.empty((m,n), dtype=np.int32)

    if axis == "x":
        v = vector(n) 
        for k in range(m):
            M[k,:] = v 
    else:
        v = vector(m)
        for k in range(n):
            M[:,k] = v
    
    return M


# --- SCRIPT ---

if __name__ == "__main__":
    pass

