from fastapi import FastAPI
import pyjokes
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


@app.get("/multi/{friend}")
def multi_friends_joke(
friend: Annotated[str, Field(min_length=3)],
jokes_number: Annotated[int, Field(gt=0, le=12)]):
	result = ""
	for i in range(jokes_number):
		result += friend + f" tells his joke #{i + 1}: " +pyjokes.get_joke() + " "
	return result