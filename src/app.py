import openai
import requests

def generate_image(description, quantity=1, size="1024x1024"):
    """
    Generates an image based on the provided description using the OpenAI API.

    :param description: Descriptive text to generate the image.
    :param quantity: Number of images to generate.
    :param size: Size of the generated images.
    :return: URL(s) of the generated image(s).
    """
    try:
        response = openai.images.generate(
            prompt=description,
            n=quantity,
            size=size
        )

        # Access the URLs of the generated images
        image_urls = [image.url for image in response.data]
        return image_urls
    except Exception as e:
        print(f"Error generating the image: {e}")
        return None

def download_image(url, filename):
    """
    Downloads an image from the URL and saves it to the filesystem.

    :param url: URL of the image to download.
    :param filename: Name of the file to save the image as.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Image saved as {filename}")
        else:
            print(f"Error downloading the image: {response.status_code}")
    except Exception as e:
        print(f"Error downloading the image: {e}")

# Ask the user to enter the description
description = input("Enter a description to generate the image: ")

# Generate images
image_urls = generate_image(description)

# Download and save the generated images
if image_urls:
    for i, url in enumerate(image_urls, start=1):
        filename = f"image_{i}.png"
        download_image(url, filename)
else:
    print("Unable to generate images.")
