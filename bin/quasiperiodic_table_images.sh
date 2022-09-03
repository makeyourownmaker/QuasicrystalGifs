#!/bin/sh
#
# Generate images for quasiperiodic table of quasicrystal patterns

it=1         # iterations
rs=128       # resolution
cm='binary'  # colormap
dir='figures'

for wa in `seq 4 2 14`; do 
    for st in `seq 2 2 12`; do 
        echo "$wa $st"; 
        fn=`echo "wa_"$wa"_st_"$st"_rs_"$rs"_cm_"$cm".gif"`; 
        python3 quasicrystals.py -fn $dir/$fn -wa $wa -st $st -rs $rs -it $it -cm $cm; 
    done; 
done

