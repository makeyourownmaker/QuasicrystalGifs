# -*- coding: utf-8 -*-
import os
import sys
import time
import argparse
import threading
import numpy as np
from math import pi
from itertools import cycle
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter


def main(args):
    fig = plt.figure(figsize=(4.75, 4.75))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')

    k       = args.waves       # number of plane waves
    stripes = args.stripes     # number of stripes (or periods) per wave
    N       = args.resolution  # image size in pixels
    ite     = args.iterations  # iterations

    image  = np.empty((N, N))
    phases = np.arange(0, 2 * pi, 2 * pi / ite)
    d = np.arange(-N / 2, N / 2, dtype=np.float64)  # origin at the image center
    xv, yv = np.meshgrid(d, d)

    # Apply log-polar transformation
    if args.log_polar:
        theta  = np.arctan2(yv, xv)
        r      = np.log(np.sqrt(xv * xv + yv * yv))
        r[np.isinf(r) is True] = 0
        tcos   = theta * np.cos(np.arange(0, pi, pi / k))[:, np.newaxis, np.newaxis]
        rsin   = r * np.sin(np.arange(0, pi, pi / k))[:, np.newaxis, np.newaxis]
        inner  = (tcos - rsin) * stripes
    else:
        xcos = xv * np.cos(np.arange(0, pi, pi / k))[:, np.newaxis, np.newaxis]
        ysin = yv * np.sin(np.arange(0, pi, pi / k))[:, np.newaxis, np.newaxis]
        inner = (xcos + ysin) * 2 * pi * stripes / N

    # Rotation angles for waves to be summed
    cinner = np.cos(inner)
    sinner = np.sin(inner)

    plt.imshow(image, cmap=args.colormap)

    def animate_func(i):
        image[:] = np.sum(cinner * np.cos(phases[i]) - sinner * np.sin(phases[i]), axis=0) + k
        im = plt.imshow(image, cmap=args.colormap)
        return [im]

    anim = animation.FuncAnimation(fig,
                                   animate_func,
                                   frames=ite,
                                   interval=args.delay
                                   )

    def progress():
        for c in cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rSaving animation: ' + c)
            sys.stdout.flush()
            time.sleep(0.1)

    if args.quiet is False:
        done = False
        t = threading.Thread(target=progress)
        t.daemon = True  # allow keyboard interrupts
        t.start()

    anim.save(args.filename, writer='pillow')

    if args.quiet is False:
        time.sleep(2)
        done = True
        sys.stdout.write('\rSaving animation: Done!     \n')
        sys.stdout.flush()

    sys.exit(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="Generate animated gifs of quasicrystals using sum of plane waves https://github.com/makeyourownmaker/QuasicrystalGifs")

    required = parser.add_argument_group('required arguments')
    required.add_argument('-fn', '--filename',
            help='Filename for animation', type=str, required=True)

    optional = parser._action_groups.pop()
    optional.add_argument('-wa', '--waves',
            help='Number of plane waves - default=5',
            default=5, type=int, metavar="[4, 50]", choices=range(4, 151))
    optional.add_argument('-st', '--stripes',
            help='Number of stripes per wave - default=37',
            default=37, type=int, metavar="[2, 150]", choices=range(2, 151))
    optional.add_argument('-rs', '--resolution',
            help='Image size in pixels - default=512',
            default=512, type=int, metavar="[64, 4096]", choices=range(64, 4096))
    optional.add_argument('-it', '--iterations',
            help='Number of frames in animation - default=30',
            default=30, type=int, metavar="[1, 120]", choices=range(1, 120))
    optional.add_argument('-de', '--delay',
            help='Number of microseconds between animation frames - default=8',
            default=8, type=int, metavar="[1, 100]", choices=range(1, 100))
    optional.add_argument('-lp', '--log_polar',
            help='Turn on log-polar transform - default=off',
            default=False, action='store_true')
    optional.add_argument('-cm', '--colormap',
            help='Matplotlib colormap See https://bit.ly/2WyFI4f - default=PiYG',
            default='PiYG', type=str,
            choices=plt.colormaps())
    optional.add_argument('-q', '--quiet',
            help='Turn off messages - default=on',
            default=False, action='store_true')

    parser._action_groups.append(optional)
    args = parser.parse_args()

    if not args.filename.endswith('.gif'):
        print("\nERROR: filename (%s) does not end with .gif" % args.filename)
        print("Add .gif to end of -fn/--filename option")
        print("https://github.com/makeyourownmaker/QuasicrystalGifs")
        sys.exit(1)

    if os.path.exists(args.filename):
        print("\nERROR: filename (%s) already exists!" % args.filename)
        print("Check file and remove it OR modify -fn/--filename option")
        print("https://github.com/makeyourownmaker/QuasicrystalGifs")
        sys.exit(1)

    folder = os.path.dirname(args.filename) or None
    if folder is not None and not os.path.isdir(folder):
        os.mkdir(folder)

    main(args)
