import time 
import httpx

SERVER_URL = "http://localhost:8000"

while True:
    try:
        resp = httpx.get(SERVER_URL)
        print(resp.json())
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)