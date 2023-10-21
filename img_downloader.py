#Code to download images from google
import requests
import os

def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded image from {url} and saved it as {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_url = input("Enter the URL of the image you want to download: ")
    save_directory = input("Enter the folder where you want to save the image: ")
    image_name = input("Enter the name for the image file: ")

    # Ensure the save_directory exists
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    save_path = os.path.join(save_directory, image_name)

    download_image(image_url, save_path)
