from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from typing import List
from endpoints import router

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, tags=["database"], prefix="/endpoints")

@app.get("/")
async def root():
    response = RedirectResponse(url='/docs')
    return response

@app.get("/example")
async def get_example(reall_long_name_for_a_person_variable:str,  height:float, hobbies:List[str], address:dict,age:int=10, is_married:bool=True,) -> str:
    '''this function gets an example of the API call'''
    
    return 'response'

@app.get("/example/{reall_long_name_for_a_person_variable}")
async def get_example(reall_long_name_for_a_person_variable:str,  height:float, hobbies:List[str], address:dict,age:int=10, is_married:bool=True,) -> str:
    '''this function gets an example of the API call'''
    
    return 'response'

@app.post("/example")
async def post_example(name:str, age:int, height:float, is_married:bool, hobbies:List[str], address:dict) -> str:
    '''this function posts an example'''
    
    return 'response'

@app.delete("/example")
async def delete_example(name:str, address:dict) -> str:
    '''this function deletes an example '''
    
    return 'response'

@app.put("/example")
async def put_example(name:str, address:dict) -> str:
    '''this function puts an example '''
    
    return 'response'

@app.get("/youtube_transcript_timestamps")
async def youtube_transcript_timestamps(video_url:str):
    parsed_url = urlparse(video_url)
    video_id = parsed_url.query.split("=")[1]
    return YouTubeTranscriptApi.get_transcript(video_id)

@app.get("/youtube_transcript")
async def youtube_transcript(video_url:str)->str:
    '''this function returns the transcript of a youtube video as a string'''
    parsed_url = urlparse(video_url)
    video_id = parsed_url.query.split("=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_string = ""
    for line in transcript:
        transcript_string += line['text'] + " "
    return transcript_string

@app.get("/url_as_text")
async def scrape_webpage(url:str)->str:
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
        return ''





# @app.get("/generate_image")
# async def generate_image():
#     return 'not implemented yet'

# @app.get("/google_search_list")
# async def google_search_list(query):
#     return 'not implemented yet'

# @app.get("/image_search")
# async def google_search_list():
#     return 'not implemented yet'

# @app.get("/google_search_list_content")
# async def google_search_list_content():
#     return 'not implemented yet'