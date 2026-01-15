from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    class_type: str = Field(..., example="sleeper")
    is_weekend: bool = Field(..., example=True)


class PredictionResponse(BaseModel):
    confirmation_probability: float
    book_only_if_confirm: bool
