from enum import Enum

from fastapi import FastAPI

app = FastAPI()

class languages(str, Enum):
  Clang = 'compiled'
  Python = 'interpreter'
  Html = 'markup'

@app.get('/')
async def root():
  return {"message":"Hello World"}

@app.get('/items/{item_id}')
async def items(item_id: int):
  return {"item ": item_id}

@app.get('/models/{model}')
async def language(model: languages):
  if model.value == 'compiled':
    return {'The language is ': 'C language'}
  if model is languages.Html:
    return {'The language is ' : 'Hypertext markup language'}
  return {'The language is ' : 'Python language'}