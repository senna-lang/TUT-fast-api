from fastapi import FastAPI

app = FastAPI()

@app.get("/countries/japan") #上から順にマッチングされる
async def japan():
      return {"country_name": "japan"}

@app.get("/countries/{country_name}")
async def country(country_name: str):
      return {"country_name": country_name}



