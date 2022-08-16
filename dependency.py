import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from dotenv import load_dotenv
import os

security = HTTPBearer()

load_dotenv()

async def has_access(credentials: HTTPBasicCredentials = Depends(security)):
    """
        Function that is used to validate the token in the case that it requires it
    """
    token = credentials.credentials
    hash_key = os.environ.get("HASH_KEY")

    try:
        decode_token = jwt.decode(token, hash_key, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token expired.")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="Invalid token.")