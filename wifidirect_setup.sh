#!/bin/sh
sudo ifdown --force wlan0
sudo rm /etc/network/interfaces
sudo cp /etc/network/interfaces_wifidirect /etc/network/interfaces
sudo /etc/init.d/networking restart
sudo ifup wlan0
service isc-dhcp-server start
