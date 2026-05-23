from fastapi import FastAPI, Depends, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "X-API-KEY"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

api = FastAPI()

# Add CORS middleware
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )



@api.get("/")
def read_root():
    return {"Hello": "World"}

## This is a protected route that requires authentication by X-API-Key
@api.post("/protected")
def protected_route(api_key: str = Depends(get_api_key)):
    return {"message": "Welcome to the protected route!", "api_key": api_key}

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)
