from enum import Enum

from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class languages(str, Enum):
  Clang = 'compiled'
  Python = 'interpreter'
  Html = 'markup'

@app.get('/')
async def root():
  return {"message":"Hello World"}

@app.get("/items/annotated")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get('/items/{item_id}')
async def items(item_id: int):
  return {"item ": item_id}

@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
  return fake_items_db[skip : skip + limit]

@app.get('/models/{model}')
async def language(model: languages):
  if model.value == 'compiled':
    return {'The language is ': 'C language'}
  if model is languages.Html:
    return {'The language is ' : 'Hypertext markup language'}
  return {'The language is ' : 'Python language'}