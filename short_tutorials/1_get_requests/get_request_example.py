# API GET request example
import requests # needed to make GET request
import os # needed obtain a value of specific env variable
from dotenv import load_dotenv # needed load .env variables
# the below are needed to process and display an image
from PIL import Image 
from io import BytesIO

config = load_dotenv() # load variables from .env file
my_api_key = os.environ.get("MY_API_KEY") # obtain API key value

# url to obtain Astronomy Picture of the Day
apod_url = 'https://api.nasa.gov/planetary/apod'

# parameter: date of the APOD
picture_date = '2023-11-01'

# Form request URL by inserting API key and date parameter
request_url = f'{apod_url}?api_key={my_api_key}&date={picture_date}'

# Make the GET request
response = requests.get(request_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    apod_data = response.json()

    # Display the astronomy picture of the day information
    print(f"Title: {apod_data['title']}")
    print(f"Date: {apod_data['date']}")
    print(f"Explanation: {apod_data['explanation']}")
    print(f"URL: {apod_data['url']}")
    # Display the image
    image_url = apod_data['url']
    response_image = requests.get(image_url)
    
    if response_image.status_code == 200:
        # Open and display the image using PIL
        image = Image.open(BytesIO(response_image.content))
        image.show()
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response_image.status_code}, {response_image.text}")
else:
    print(f"Error: {response.status_code}, {response.text}")
