from fastapi import FastAPI

from fastapi import status

app = FastAPI()

@app.get('/healthcheck', status_code = status.HTTP_200_OK)
async def healthcheck():
    return {'healthcheck': 'Healthy'}
