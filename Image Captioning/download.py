import os
from pathlib import Path
import opendatasets as od

download_path = Path("flickr8kimagescaptions/")
data_path = Path("data/")


def download_dataset(dataset_url):
  if download_path.is_dir():
    print(f"{download_path} directory already exists!")
    print(f"Renaming the directory...........")
    os.rename(download_path, data_path)
    print("Rename complete")

  elif data_path.is_dir():
    print("Data already exists....")
    print("No Download necessary!")

  else:
    print("Downloading the dataset......")
    od.download(dataset_url)
    print("Download Complete !!!!")
    print("Renaming......")
    os.rename(download_path, data_path)
