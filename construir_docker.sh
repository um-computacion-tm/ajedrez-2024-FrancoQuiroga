#!/bin/bash
sudo docker build --no-cache -t ajedrez . && sudo docker run -it ajedrez
exit