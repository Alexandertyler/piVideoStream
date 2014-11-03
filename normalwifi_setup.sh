#!/bin/sh

sudo ifdown --force wlan0
sudo rm /etc/network/interfaces
sudo cp /etc/network/interfaces_normal /etc/network/interfaces
sudo /etc/init.d/networking restart
sudo ifup wlan0
