# -*- coding: utf-8 -*-
import os
import argparse
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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
    d = np.arange(-N / 2, N / 2, dtype=np.float64)
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

    anim.save(args.filename, writer='imagemagick')
    # If writer='imagemagick' option is removed then ffmpeg is used which creates bigger gif

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="Generate animated gifs of quasicrystals using sum of plane waves")

    optional = parser._action_groups.pop()
    optional.add_argument('-wa', '--waves',
            help='Number of plane waves - default=5',
            default=5, type=int, metavar="[2, 50]", choices=range(2, 51))
    optional.add_argument('-st', '--stripes',
            help='Number of stripes per wave - default=37',
            default=37, type=int, metavar="[2, 50]", choices=range(2, 51))
    optional.add_argument('-it', '--iterations',
            help='Number of frames in animation - default=30',
            default=30, type=int, metavar="[1, 120]", choices=range(1, 120))
    optional.add_argument('-de', '--delay',
            help='Number of microseconds between animation frames - default=8',
            default=8, type=int, metavar="[1, 100]", choices=range(1, 100))
    optional.add_argument('-rs', '--resolution',
            help='Image size in pixels - default=512',
            default=512, type=int, metavar="[64, 4096]", choices=range(64, 4096))
    optional.add_argument('-cm', '--colormap',
            help='Matplotlib colormap See https://bit.ly/2WyFI4f - default=PiYG',
            default='PiYG', type=str,
            choices=plt.colormaps())
    optional.add_argument('-lp', '--log_polar',
            help='Turn on log-polar transform - default=off',
            default=False, action='store_true')
    optional.add_argument('-fn', '--filename',
            help='Filename for animation - default=qc.gif',
            default='qc.gif', type=str)

    parser._action_groups.append(optional)
    args = parser.parse_args()

    if not args.filename.endswith('.gif'):
        print("ERROR: filename (%s) does not end with .gif" % args.filename)
        print("Add .gif to end of -fn/--filename option")
        exit()

    if os.path.exists(args.filename):
        print("ERROR: filename (%s) already exists!" % args.filename)
        print("Check file and remove it OR modify -fn/--filename option")
        exit()

    folder = os.path.dirname(args.filename) or None
    if folder is not None and not os.path.isdir(folder):
        os.mkdir(folder)

    main(args)
