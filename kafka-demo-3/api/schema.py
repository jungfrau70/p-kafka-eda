from pydantic import BaseModel

class REQUEST(BaseModel):
    request_id: str
    region: str
    az: str
    tennant: str
    command: str

class RESPONSE(BaseModel):
    request_id: str    
    region: str
    az: str
    tennant: str    
    result: str