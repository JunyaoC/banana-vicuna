# This is a potassium-standard dockerfile, compatible with Banana

# Must use a Cuda version 11+
# FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime
FROM nvidia/cuda:11.6.2-devel-ubuntu20.04

WORKDIR /

# Install git
RUN apt-get update && apt-get install -y git
RUN apt-get update && apt-get install -y build-essential
# Install python packages
RUN pip install --upgrade pip
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python

RUN wget https://huggingface.co/TheBloke/stable-vicuna-13B-GGML/resolve/main/stable-vicuna-13B.ggmlv3.q5_1.bin

# # Add your model weight files 
# # (in this case we have a python script)
# ADD download.py .
# RUN python3 download.py

ADD . .

EXPOSE 8000

CMD python3 -u app.py