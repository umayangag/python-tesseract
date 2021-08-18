#!/bin/bash


sudo docker build -f Dockerfile -t ldflk/ocr_service .
sudo docker push ldflk/ocr_service:latest
sudo docker pull ldflk/ocr_service
sudo docker kill local_ocr_service
sudo docker run --rm -p 8082:8082 -d --name local_ocr_service ldflk/ocr_service
sudo docker logs local_ocr_service