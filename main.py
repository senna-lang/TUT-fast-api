from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()


@app.get("/countries/japan")  # 上から順にマッチングされる
async def japan():
    return {"country_name": "japan"}


@app.get("/countries/{country_name}")
async def country(country_name: str):
    return {"country_name": country_name}


"""
http://twiter.com/search?query=python&src=typded_query  ?移行がクエリパラメータで&で複数のパラメータを指定できる
"""


@app.get(
    "/countries/"
)  # クエリパラメータはデフォルト値が無ければ必須 Optionalで必須でなくできる
async def country2(country_name: Optional[str], country_code: int = 1):
    return {"country_name": country_name, "country_code": country_code}


# パスパラメーターとクエリパラメーターを組み合わせる
@app.get("/countries/{country_name}")
async def country3(country_name: Optional[str] = None, country_code: int = 1):
    return {"country_name": country_name, "country_code": country_code}


# リクエストボディの定義
class ShopInfo(BaseModel):
    name: str
    address: str


class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12) # バリデーションの付け方
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Data(BaseModel):
    shop: Optional[ShopInfo] = None
    item: List[Item]


@app.post("/items/")
async def index(data: Data):  # リクエストボディを受け取る
    return {"data": data}
