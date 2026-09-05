# C Samsung TV Remote Control

A small networking project written in **C and Python** that allows me to control my Samsung Smart TV from another device on my local network.

The main goal of this project was to practice and understand **C socket programming and networking**.

## Features

The server can receive commands from another device and control the TV.

Current commands include:

- Turn the TV on using Wake-on-LAN
- Turn the TV off
- Increase volume
- Decrease volume
- Mute the TV

A TCP server written in C runs on my Windows PC and listens for commands from another device on the local network.

The TV is turned on using a **Wake-on-LAN magic packet** sent with UDP.

Other controls use Python and the `samsungtvws` library to communicate with the Samsung TV through its WebSocket interface.

## Technologies Used

- C
- Python
- TCP sockets
- UDP
- Wake-on-LAN
- Winsock2
- Samsung TV WebSocket API
- Termux

To use this:

Download Termux on you phone

fix put your ip address in line   68: 192.xxx.x.255 ( only where the x's are) leave the 255 alone

to find your ip address 
Run this app on your computer within the same network as your phone 
