import requests

url = "https://www.googleapis.com/customsearch/v1"

params = {
    "key" : "AIzaSyDvyoQLO8pV6kGALBGeSs-NHTG62t5ZT6I",
    "cx" : "35501b3f4d7f54ea7",
    "q" : "Model Context Protocol MCP"
}

responce=requests.get(url,params=params)

print(responce.json())