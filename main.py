from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "https://pragatipatil97.github.io",
    "http://localhost:5500"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/volume")
def calculate_volume(l: str = Query(...), b: str = Query(...), h: str = Query(...)):
    try:
        volume = float(l) * float(b) * float(h)
        return {"volume": volume}
    except ValueError:
        return {"error": "Invalid numeric values for l, b, or h."}
