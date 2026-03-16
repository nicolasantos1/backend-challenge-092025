from fastapi import FastAPI
from fastapi.responses import JSONResponse

from sentiment_analyzer import analyze_feed

app = FastAPI()


@app.post("/analyze-feed")
def analyze_feed_endpoint(payload: dict):
    result = analyze_feed(payload)

    status = result.pop("_status", 200)
    if status != 200:
        return JSONResponse(status_code=status, content=result)

    return {"analysis": result}
