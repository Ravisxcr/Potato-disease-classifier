from fastapi import FastAPI

li = {
    1 : 'Newuser',
    2 : 'Login',
    3 : 'Github'
}

app = FastAPI()
@app.get("/hello")
async def hello():
    return 'welcome'

@app.get("/news/{all}")
async def news(all : int):
    a = li.get(all)
    return f'The news that you are searching in {a} section is not available'