import uvicorn

from fastapi import FastAPI, Request, Response
from pydantic import BaseSettings

class Settings(BaseSettings):
    confirmation_string: str
    group_id: int
    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI()

@app.post('/main')
async def authorize(req: Request):
    req_body = await req.json()
    print(req_body)
    if req_body['type'] == 'confirmation' and req_body['group_id'] == settings.group_id:
        return Response(content=settings.confirmation_string, media_type="application/json")
    elif req_body['type'] == 'message_new':
        pass
    else:
        return False

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
