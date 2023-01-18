from pydantic import BaseModel
from typing import List, Dict


CONSTANTS = {
    "statusResponse": {"status": "ProjectAPI is up and running!"},
    "argumentExample": {"body": "Bu harika bir filmdi."}
}

class Argument(BaseModel):
    body: str


class ArgumentResponse(BaseModel):
    body: str
    evaluation: Dict

