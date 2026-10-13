# Accessing data from database
from fastapi import FastAPI
import asyncio
app = FastAPI()

tourist_places =  {
    "India": ["Taj Mahal", "Jaipur", "Goa", "Kerala"],
    "USA": ["Statue of Liberty", "Grand Canyon", "Hollywood", "Times Square"],
    "UK": ["Big Ben", "Buckingham Palace", "Tower of London", "Stonehenge"],
    "France": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral", " Palace of Versailles"],
    "Japan": ["Tokyo Tower", "Mount Fuji", "Hiroshima Peace Memorial", "Osaka Castle"],
    "Australia": ["Sydney Opera House", "Great Barrier Reef", "Uluru", "Bondi Beach"],
    
}
@app.get("/get_places/{country}")
async def get_places(country: str):
    await asyncio.sleep(20)  # Simulating a delay for database access
    places = tourist_places.get(country.capitalize())
    if places:
        return {"country": country, "places": places}
    else:
        return {"error": "Country not found"}