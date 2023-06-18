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
from tqdm import tqdm

url = "https://huggingface.co/TheBloke/koala-7B-GGML/resolve/main/koala-7B.ggmlv3.q5_1.bin"

# Define a custom callback function for the progress bar
def progress_bar_callback(current, total, width=80):
    progress = current / total
    progress_bar_width = int(progress * width)
    progress_bar = '#' * progress_bar_width + '-' * (width - progress_bar_width)
    print(f"Downloading: [{progress_bar}] {progress * 100:.2f}%", end='\r')

# Download the file using wget with the progress bar

# URL of the file to download

# Download the file using wget
downloaded_file = wget.download(url, bar=progress_bar_callback)
print()
# Get the full path of the downloaded file
downloaded_file_path = os.path.join(os.getcwd(), downloaded_file)

# Print the full path of the downloaded file
print("Downloaded file path:", downloaded_file_path)