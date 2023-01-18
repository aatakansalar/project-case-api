from fastapi import FastAPI, Body
from model import TurkishTextClassificationModel
from models import CONSTANTS, Argument, ArgumentResponse

tags_metadata = [
    {
        "name": "Status",
    },
    {
        "name": "Evaluations",
        "description": "Operations to classify Turkish text.",
    }
]

app = FastAPI(
    title= "caseAPI",
    version="1.0",
    description="A simple API for Turkish Text Classification with BERT",
    openapi_tags=tags_metadata
)

model = TurkishTextClassificationModel()

@app.get('/', include_in_schema = False, tags=["Status"])
async def status_check():
    return CONSTANTS["statusResponse"]


@app.get('/status', tags=["Status"])
async def status_check():
    return CONSTANTS["statusResponse"]

@app.post('/argument', summary = "Evaluate an argument", status_code = 200, tags=["Evaluations"])
async def evaluate_argument(argument: Argument = Body(..., example = CONSTANTS["argumentExample"])):
    """
    Evaluate an argument's label using a transformer model
    - **body**: Arguments must have a string type body

    Response will have a body and evaluation parameter
    - **body**: Input Argument's body
    - **evaluation**: The evaluation of the argument. Has label and score information
    """
    evaluation = model.classify_text(argument.body)
    response = ArgumentResponse(body = argument.body, evaluation = evaluation)
    return response
