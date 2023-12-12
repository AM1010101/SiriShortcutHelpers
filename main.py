from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
async def root():
    # redirect to docs
    response = RedirectResponse(url='/docs')
    return response


@app.get("/google_search_list")
async def google_search_list(query):
    return 'not implemented yet'

@app.get("/image_search")
async def google_search_list():
    return 'not implemented yet'

@app.get("/google_search_list_content")
async def google_search_list_content():
    return 'not implemented yet'

@app.get("/youtube_transcript_timestamps")
async def youtube_transcript_timestamps(video_url:str):
    parsed_url = urlparse(video_url)
    video_id = parsed_url.query.split("=")[1]
    return YouTubeTranscriptApi.get_transcript(video_id)

@app.get("/youtube_transcript")
async def youtube_transcript(video_url:str):
    parsed_url = urlparse(video_url)
    video_id = parsed_url.query.split("=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_string = ""
    for line in transcript:
        transcript_string += line['text'] + " "
    return transcript_string

@app.get("/url_as_text")
async def scrape_webpage(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        response.raise_for_status()  # Raise an exception for bad requests

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # You can now work with the parsed HTML, for example, print the title
        title = soup.title.string
        print(f"Title of the webpage: {title}")

        content = soup.get_text()

        # Return the entire HTML content if needed
        return content

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions, e.g., connection error, timeout
        print(f"Error: {e}")
        return None


@app.get("/generate_image")
async def generate_image():
    return 'not implemented yet'
