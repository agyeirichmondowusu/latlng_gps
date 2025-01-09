import fastapi
from fastapi import FastAPI, Request
import uvicorn


app = FastAPI()

latlng_data = []

@app.post("/update-location")
async def updateLocation(latlng: Request):
    global latlng_data
    data = await latlng.json()
    latlng_data.append(data)

    print("received data: ", latlng_data)

    return "received"

@app.get("/get-lat-lng")
async def getLatLng():
	global latlng_data
	return {"lat-lng": latlng_data}


if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)


