#!/bin/bash


montage aggregated_2020.png aggregated_2021.png aggregated_2022.png -mode concatenate -tile x1 aggregated_stich1.png
montage aggregated_2017.png aggregated_2018.png aggregated_2019.png -mode concatenate -tile x1 aggregated_stich2.png
montage aggregated_2014.png aggregated_2015.png aggregated_2016.png -mode concatenate -tile x1 aggregated_stich3.png
montage aggregated_stich3.png aggregated_stich2.png aggregated_stich1.png -mode concatenate -tile 1x aggregated_stich_complete.png



montage heatmap_2020.png heatmap_2021.png heatmap_2022.png -mode concatenate -tile x1 heatmap_stich1.png
montage heatmap_2017.png heatmap_2018.png heatmap_2019.png -mode concatenate -tile x1 heatmap_stich2.png
montage heatmap_2014.png heatmap_2015.png heatmap_2016.png -mode concatenate -tile x1 heatmap_stich3.png
montage heatmap_stich3.png heatmap_stich2.png heatmap_stich1.png -mode concatenate -tile 1x heatmap_stich_complete.png
