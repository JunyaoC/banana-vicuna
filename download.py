# # This file runs during container build time to get model weights built into the container

# # In this example: A Huggingface BERT model
# from transformers import pipeline

# def download_model():
#     # do a dry run of loading the huggingface model, which will download weights
#     # pipeline('fill-mask', model='bert-base-uncased')
    

# if __name__ == "__main__":
#     download_model()

import os
import wget

# URL of the file to download
url = "https://huggingface.co/TheBloke/stable-vicuna-13B-GGML/resolve/main/stable-vicuna-13B.ggmlv3.q5_1.bin"

# Download the file using wget
downloaded_file = wget.download(url)

# Get the full path of the downloaded file
downloaded_file_path = os.path.join(os.getcwd(), downloaded_file)

# Print the full path of the downloaded file
print("Downloaded file path:", downloaded_file_path)