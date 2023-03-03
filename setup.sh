#!/bin/bash

pkg update -y && pkg install apt -y && apt install wget -y && apt install git -y && apt install python2 -y && pip2 install requests && pip2 install pyyaml
mkdir assets && curl https://github.com/MySploitX/packages/blob/main/msg.yml -o assets/msg.yml