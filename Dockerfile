FROM python:3.8-slim-buster
WORKDIR /python-tesseract$

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ocr_server.py ocr_server.py

EXPOSE 8082
CMD [ "python3.8", "ocr_server.py"]
