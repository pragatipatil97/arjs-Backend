
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Replace with your GitHub Pages frontend URL
origins = [
    "https://pragatipatil97.github.io",
    "http://localhost:5500"  # Optional for local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/volume")
def calculate_volume(
    l: str = Query(..., description="Length of the box"),
    b: str = Query(..., description="Breadth of the box"),
    h: str = Query(..., description="Height of the box")
):
    """
    Calculate the volume of a rectangular box.
    Example: /volume?l=1&b=2&h=3
    """
    try:
        l_val = float(l)
        b_val = float(b)
        h_val = float(h)
        volume = l_val * b_val * h_val
        return {"volume": volume}
    except ValueError:
        return {"error": "Invalid numeric values for l, b, or h."}
    except Exception as e:
        return {"error": str(e)}
