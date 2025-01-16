#!/bin/bash

# Crear regla udev para RPLidar
echo 'KERNEL=="ttyUSB*", ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", MODE:="0777", SYMLINK+="rplidar"' | sudo tee /etc/udev/rules.d/rplidar.rules

# Recargar reglas udev
sudo udevadm control --reload-rules && sudo udevadm trigger

# Dar permisos al puerto USB
sudo chmod 777 /dev/ttyUSB0
