from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Replace with your GitHub Pages URL
origins = [
    #"https://username.github.io",
    "https://pragatipatil97.github.io/WebAR_Cube/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/volume")
def calculate_volume(l: float, b: float, h: float):
    volume = l * b * h
    return {"volume": volume}
