from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# initialize app
app = FastAPI()

# urls whitelist
origins = ["http://localhost:3000", "http://localhost:3000"]

# middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes
@app.get("/test", tags=["test"])
async def root() -> dict:
    return {"message": "hello from your friendly FastAPI"}
