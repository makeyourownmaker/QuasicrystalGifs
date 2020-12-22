# QuasicrystalGifs

![Lifecycle
](https://img.shields.io/badge/lifecycle-experimental-orange.svg?style=flat)
![python
](https://img.shields.io/badge/python-blue.svg?style=flat)

Generate animated gifs of quasicrystals using sum of plane waves with python

If you like the quasicrystal scripts/notebooks, fork the repository and contribute or, give it a star!


## Usage

Assuming you have python in your path and all dependencies installed:
```sh
python quasicrystals.py
```

Here is the generated gif:

<img src="figures/qc.gif" align="center" />

The above command will generate an animated gif called qc.gif with the following default
settings:

| Name       | Short | Long         | Description                                     | Default   |
|------------|-------|--------------|-------------------------------------------------|-----------|
| Waves      | -wa   | --waves      | Number of plane waves                           | 5         |
| Stripes    | -st   | --stripes    | Number of stripes (or periods) per wave         | 37        |
| Iterations | -it   | --iterations | Number of frames in animation                   | 30        |
| Delay      | -de   | --delay      | Number of microseconds between animation frames | 8         |
| Resolution | -rs   | --resolution | Image size in pixels                            | 512       |
| Colormap   | -cm   | --colormap   | Colormap from matplotlib                        | PiYG      |
| Log-polar  | -lp   | --log_polar  | Use log-polar coordinates instead of Cartesian  | Cartesian |
| Filename   | -fn   | --filename   | Filename for animation                          | qc.gif    |

The filename must use the gif file extension and should not use any sub-directories.

A colormap is a matrix of values that define the colors for graphics objects.
Here is a list of 
[matplotlib colormaps](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html).

Check the -h or --help options for further details like acceptable values for 
each command line option.


## Installation

Requires:
 * Recent version of [python 3](https://www.python.org/)
 * [numpy](https://numpy.org/)
 * [matplotlib](https://matplotlib.org/)
 * [ImageMagick](https://imagemagick.org/)

[//]: # " * [Jupyter](https://jupyter.org/) "
[//]: # " One option is to clone the repository and open the notebook(s) in a local "
[//]: # " installation of Jupyter. "
[//]: # " ```sh "
[//]: # " git clone https://github.com/makeyourownmaker/QuasicrystalGifs "
[//]: # " cd QuasicrystalGifs "
[//]: # " jupyter notebook ... "
[//]: # " ``` "
[//]: # " Another option is to run the notebook(s) on NBViewer, MyBinder or Colab. "


After the above dependencies have been installed simply download and run the script:
```sh
wget https://raw.githubusercontent.com/makeyourownmaker/QuasicrystalGifs/master/quasicrystals.py
python quasicrystals.py
```

Alternatively, clone the repository and run the script:
```sh
git clone https://github.com/makeyourownmaker/QuasicrystalGifs
cd QuasicrystalGifs
python quasicrystals.py
```


[//]: # " ## Gallery "
[//]: # " Include command line args ... "


## Details

### What are quasicrystals?

A quasicrystal, or quasiperiodic crystal, is a solid material that is 
intermediate between an orderly crystal and an amorphous glass.  They
resemble crystals because they are composed of repeating structural units 
but they incorporate two or more unit cells into a quasiperiodic structure.
A unit cell is the smallest group of atoms which has the overall symmetry of 
a crystal.  A quasiperiodic structure is periodic on a small scale but 
unpredictable at some larger scale.

Quasicrystals can be thought of as the 3 dimensional generalisation of a
[Penrose tiling](https://en.wikipedia.org/wiki/Penrose_tiling).


### How does this quasicrystal animation work?

Each frame of the animation is a summation of waves at evenly-spaced 
rotations.  That is, every point in each animation frame is colored according 
to the sum of sines and cosines depending on the x and y coordinates.  The
animation is determined by an evenly-spaced orientation angle between 0 and 
2 * pi.


### Examples of quasicrystals

The first synthetic quasicrystal, a combination of aluminium and manganese, was 
reported by [Dan Shechtman](https://en.wikipedia.org/wiki/Dan_Shechtman) and 
colleagues.  Shechtman won the 
[2011 Nobel Prize in chemistry](https://www.nobelprize.org/prizes/chemistry/2011/press-release/) 
for this work.

[Icosahedrite](https://en.wikipedia.org/wiki/Icosahedrite) is the first
naturally occuring quasicrystal to be found.  It has the composition 
Al_63 Cu_24 Fe_13 and was discovered in a meteorite by 
[Luca Bindii](https://en.wikipedia.org/wiki/Luca_Bindi) and 
[Paul J. Steinhardt](https://en.wikipedia.org/wiki/Paul_Steinhardt).

Hundreds of quasicrystals have been confirmed.  They are often found in
aluminium alloys.


## Limitations

The bottleneck in generating the animated gifs is the final step using
the [ImageMagick convert](https://imagemagick.org/script/convert.php) utility.  
This involves a surprisingly large amount of data transfer.  See this 
[stackoverflow answer for more details](https://stackoverflow.com/a/30704560/100129).

If you start having time or memory problems converting animations to gifs
then try using a black and white or greyscale colormap:
```sh
# Short options
python quasicrystals.py -cm Greys

# Long options
python quasicrystals.py --colormap Greys
```


## Gallery

Log-polar coordinates with default settings (see table above):
```sh
# Short options
python quasicrystals.py -lp

# Long options
python quasicrystals.py --log_polar
```
<img src="figures/qc_log_polar.gif" align="center" />


## Roadmap

 * Create requirements.txt file:
   * Add requirements.txt usage to README

 * quasicrystals.py:
   * Simplify handling of log-polar transformation
   * Add more colormaps
     * Particularly simple black and white color map
   * Allow specifying width and height of images
   * Include option to indicate direction of rotation
     * Currently defaults to anti-clockwise

 * Add Jupyter notebook(s):
   * Add links to run notebook(s) on NBViewer, MyBinder and Colab

 * Expand README:
   * Add more examples to gallery
     * List command line arguments used for each animation
   * Describe log-polar transform instead of using Cartesian coordinates
   * Describe rotational and translation symmetry of quasicrystals


## Alternatives

[Quasicrystals as sums of waves in the plane](http://mainisusuallyafunction.blogspot.com/2011/10/quasicrystals-as-sums-of-waves-in-plane.html)
is the earliest implementation I've been able to find.  In Haskell.

[Another early implementation](http://wealoneonearth.blogspot.com/search/label/quasicrystal).
This time in Java.  Requires post-processing with the convert tool from 
ImageMagick to produce animated gifs.

[Andrew Horchler's Matlab implementation](https://github.com/horchler/quasicrystal)
will produce animated gifs or movies.

[Mads Ohm Larsen's python gist](https://gist.github.com/omegahm/e823a68c201406d32a94)
which also requires ImageMagick post-processing.

[Trevahok's python implementation](https://github.com/Trevahok/quasicrystal-generator)
has no external dependencies.  Generates static images.

[Mike Bostock's Javascript and WebGL implementation](https://observablehq.com/@mbostock/quasicrystals)
is editable in the browser.


## See Also

[Quasicrystals on Wikipedia](https://en.wikipedia.org/wiki/Quasicrystal)

[The Second Kind of Impossible by Paul Steinhardt](https://www.amazon.co.uk/Second-Kind-Impossible-Extraordinary-Matter/dp/147672993X/)
describes the authors adventures searching for quasicrystals from meteorites
in Siberia while dodging KGB agents and much more.


## Contributing

Pull requests are welcome.  For major changes, please open an issue first to discuss what you would like to change.


## License

[GPL-2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
