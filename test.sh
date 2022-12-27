#!/bin/bash

cp ~/Documents/GitHub/keydge-backend/Journal/data/3m.csv ./
rm -rf _deepscatter_tmp/
rm -rf tile
quadfeather --files 3m.csv --tile_size 100000 --destination tile