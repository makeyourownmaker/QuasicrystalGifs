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
python quasicrystals.py -fn qc.fig
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

All of the above arguments are optional.

Setting the waves option to 4 or 6 will produce an animation but it will not be
quasiperiodic.  No warning is given.

A colormap is a matrix of values that define the colors for graphics objects.
All the matplotlib colormaps are supported but I've not tested all of them.
Here is a list of the
[matplotlib version 3.3.3 colormaps](https://matplotlib.org/3.3.3/tutorials/colors/colormaps.html).

The only required argument is -fn or --filename.

| Name       | Short | Long         | Description                                     |
|------------|-------|--------------|-------------------------------------------------|
| Filename   | -fn   | --filename   | Filename for animation                          |

The filename must use the gif file extension and should not use any sub-directories.

There is one more optional argument:

| Name  | Short | Long    | Description       | Default |
|-------|-------|---------|-------------------|---------|
| Quiet | -q    | --quiet | Turn off messages | False   |

Check the -h or --help options for further details like acceptable values for 
each command line option.


## Installation

Requires:
 * Recent version of [python 3](https://www.python.org/)
 * [numpy](https://numpy.org/) package
 * [matplotlib](https://matplotlib.org/) package
 * [ImageMagick](https://imagemagick.org/) program

To install the two python packages:
```sh
pip install -r requirements.txt
```
ImageMagick will also need to be installed.


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
python quasicrystals.py -fn qc.gif
```

Alternatively, clone the repository and run the script:
```sh
git clone https://github.com/makeyourownmaker/QuasicrystalGifs
cd QuasicrystalGifs
python quasicrystals.py -fn qc.gif
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
a crystal.
Quasicrystal patterns or ordered but not periodic and can continuously
fill all available space, but lack
[translational symmetry](https://en.wikipedia.org/wiki/Translational_symmetry).

Classic crystals can possess only two, three, four, and six-fold
[rotational symmetries](https://en.wikipedia.org/wiki/Rotational_symmetry);
as seen in their diffraction patterns.
The [diffraction patterns](https://en.wikipedia.org/wiki/Diffraction) of
quasicrystals show peaks with other symmetry orders.

Quasicrystals can be thought of as the 3 dimensional generalisation of a
[Penrose tiling](https://en.wikipedia.org/wiki/Penrose_tiling).


### How does this quasicrystal animation work?

Each frame of the animation is a simulation of the diffraction pattern produced
by the vertices of an aperiodic tiling.

Each frame of the animation is a summation of five or more waves at evenly-spaced
rotations.  That is, every point in each animation frame is colored according 
to the sum of sines and cosines depending on the x and y coordinates.  The
animation is determined by an evenly-spaced orientation angle between 0 and 
2 * pi.  The number of wave cycles in the animation is determined by
changing "stripes".  Larger numbers of stripes leads to finer structures.


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
The -q or --quiet option will disable the Saving animation progress animation
and reduce runtime a little.

If you start having time or memory problems converting animations to gifs
then try using a black and white or greyscale colormap:
```sh
# Short options
python quasicrystals.py -fn qc.gif -cm binary

# Long options
python quasicrystals.py --filename qc.gif --colormap binary
```
Other black and white/greyscale colormaps include: binary, gist_yarg, gist_gray,
gray and Greys.

Reducing the resolution is also helpful:
```sh
# Short options
python quasicrystals.py -fn qc.gif -cm binary -rs 400

# Long options
python quasicrystals.py --filename qc.gif --colormap binary -rs 400
```


## Gallery

Log-polar coordinates with default settings (see table above):
```sh
# Short options
python quasicrystals.py -fn qc.gif -lp

# Long options
python quasicrystals.py --filename qc.gif --log_polar
```
<img src="figures/qc_log_polar.gif" align="center" />

```sh
python quasicrystals.py -wa 7 -st 128 -rs 800 -cm spectral -fn wa_7_st_128_rs_800_cm_spectral.gif
```
<img src="figures/wa_7_st_128_rs_800_cm_spectral.gif" align="center" />

```sh
python quasicrystals.py -wa 7 -st 128 -rs 800 -cm hsv -fn wa_7_st_128_rs_800_cm_hsv.gif
```
<img src="figures/wa_7_st_128_rs_800_cm_hsv.gif" align="center" />


## Roadmap

 * Speed up saving animations:
   * Compare speed of generating gifs with PIL
     * Retain matplotlib colormaps if possible

 * quasicrystals.py:
   * Simplify handling of log-polar transformation
   * Allow specifying width and height of images
   * Include option to indicate direction of rotation
     * Currently defaults to anti-clockwise

 * Explore matplotlib [LightSource](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html):
   * Apply a light source coming from specified azimuth and elevation
   * Hope this will make animations a little less planar looking
   * [Shading example](https://matplotlib.org/stable/gallery/images_contours_and_fields/shading_example.html)
   * [Hillshading example](https://matplotlib.org/stable/gallery/specialty_plots/advanced_hillshading.html)

 * Expand README:
   * Add more examples to gallery
     * List command line arguments used for each animation
   * Describe log-polar transform instead of using Cartesian coordinates
   * Describe rotational and translational symmetry of quasicrystals

 * Add Jupyter notebook(s):
   * Add links to run notebook(s) on NBViewer, MyBinder and Colab


## Alternatives

[Quasicrystals as sums of waves in the plane](http://mainisusuallyafunction.blogspot.com/2011/10/quasicrystals-as-sums-of-waves-in-plane.html)
is the earliest implementation I've been able to find.  In Haskell.

[Another early implementation](http://wealoneonearth.blogspot.com/search/label/quasicrystal).
This time in Java.  Requires post-processing with the convert tool from 
ImageMagick to produce animated gifs.  Code is readable but not vectorised.

[Andrew Horchler's Matlab implementation](https://github.com/horchler/quasicrystal)
will produce animated gifs or movies.

[Mads Ohm Larsen's python gist](https://gist.github.com/omegahm/e823a68c201406d32a94)
which also requires ImageMagick post-processing.

[Trevahok's python implementation](https://github.com/Trevahok/quasicrystal-generator)
has no external dependencies.  Generates static greyscale images but code is
short and very readable.

[Mike Bostock's Javascript and WebGL implementation](https://observablehq.com/@mbostock/quasicrystals)
is editable in the browser.

[Quasicrystals on shadertoy](https://www.shadertoy.com/results?query=quasicrystal)
by multiple authors.


## See Also

[Quasicrystals on Wikipedia](https://en.wikipedia.org/wiki/Quasicrystal)

[The Second Kind of Impossible by Paul Steinhardt](https://www.amazon.co.uk/Second-Kind-Impossible-Extraordinary-Matter/dp/147672993X/)
describes the authors adventures searching for quasicrystals from meteorites
in Siberia while dodging KGB agents and much more.

[Quasicrystals and Geometry by Marjorie Senechal](https://www.amazon.com/Quasicrystals-Geometry-Marjorie-Senechal/dp/0521575419)
starts with the history of crystallography and then covers methods for generating aperiodic tilings.

[Alan Mackay predicted quasicrystals in a 1981 paper](https://en.wikipedia.org/wiki/Alan_Lindsay_Mackay)

[Quasicrystalline Medieval Islamic Architectural Tilings](https://www.peterlu.com/research/islamic_tilings)

[Diffraction pattern of a penrose tiling](http://sato.issp.u-tokyo.ac.jp/ibuka/penrose.html)


## Contributing

Pull requests are welcome.  For major changes, please open an issue first to discuss what you would like to change.


## License

[GPL-2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
