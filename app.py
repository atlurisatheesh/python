from fastapi import FastAPI, HTTPException
from schemas import PredictionRequest, PredictionResponse
from predictor import predict_confirmation
from decision_engine import decide_confirm_only
from logger import logger

app = FastAPI(title="Tatkal Confirm AI")

@app.get("/")
def health():
    logger.info("Health check called")
    return {"status": "running"}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: PredictionRequest):

    class_type = data.class_type.lower()
    logger.info(f"Request received | class={class_type} | weekend={data.is_weekend}")

    if class_type not in ["sleeper", "ac"]:
        logger.warning("Invalid class_type received")
        raise HTTPException(
            status_code=400,
            detail="class_type must be 'sleeper' or 'AC'"
        )

    probability = predict_confirmation(
        class_type=class_type,
        is_weekend=data.is_weekend
    )

    confirm_only = decide_confirm_only(
        class_type=class_type,
        is_weekend=data.is_weekend,
        probability=probability
    )

    logger.info(
        f"Decision | probability={probability}% | confirm_only={confirm_only}"
    )

    return {
        "confirmation_probability": probability,
        "book_only_if_confirm": confirm_only
    }
