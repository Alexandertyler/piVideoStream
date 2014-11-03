#!/bin/sh

cd piracast/scripts
sudo nice -n -20 ./core &
sudo python piracast.py 
cd ~/
