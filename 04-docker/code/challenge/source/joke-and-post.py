import requests
import json
import os
from rich import print as pprint

JOKE_API_BASE_URL="https://api.chucknorris.io/jokes"
WEBEX_BASE_API="https://webexapis.com/v1/"
ROOM_ID = os.getenv("WEBEX_ROOM")
TOKEN = os.getenv("WEBEX_TOKEN")

def get_chuck_joke():
  url = JOKE_API_BASE_URL+"/random"

  headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
  }
  
  response = requests.request("GET",url, headers=headers)
  json_joke = response.json()
  return(json_joke["value"])

def post_to_webex(message):
  url = WEBEX_BASE_API + "/messages"

  payload = json.dumps({
    "roomId": ROOM_ID,
    "markdown": f"*{message}*"
  })

  HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
  }

  response = requests.request("POST", url, headers=HEADERS, data=payload)

  return(response)

def get_room_name():
  
  url = WEBEX_BASE_API + f"/rooms/{ROOM_ID}"

  headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
  }

  response = requests.request("GET", url, headers=headers)

  json_response = response.json()
  room_name = json_response["title"]

  return(room_name)

def main():
  joke = get_chuck_joke()
  pprint()
  response_obj = post_to_webex(joke)
  room_name = get_room_name()
  pprint(f":dromedary_camel: [bold]Status code:[/bold] {response_obj.status_code}")
  pprint(f":speaker: [bold]Message sent in room: [cyan]{room_name}[/bold][/cyan]")

if __name__ == "__main__":
    main()