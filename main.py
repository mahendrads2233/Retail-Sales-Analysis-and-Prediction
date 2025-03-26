from fastapi import FastAPI

app = FastAPI()
@app.get("/")

async def sample():
    return {'Hello':'World'}

@app.get ("/version/{'Version_ID'}")

async def get_version(Version_id : int):
    return {"Version_Id": Version_id}
