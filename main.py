import os

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database.data_manipulation import get_jobs_by_type, return_all_jobs

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/api/info/tech/{type}")
def get_type(tech_type):
    response = get_jobs_by_type(tech_type)
    print(response)
    if response:
        return response
    raise HTTPException(404, f"0")


@app.get("/api/info")
def get_info():
    response = return_all_jobs()
    if response:
        return response
    raise HTTPException(404, f"0")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=5000), log_level="info")