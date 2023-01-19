#!/bin/bash

python3 create_csv.py $1
rm -rf _deepscatter_tmp/
rm -rf tile
quadfeather --files newest.csv --tile_size 100000 --destination tile