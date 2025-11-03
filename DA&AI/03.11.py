import torch
from transformers import pipeline
from typing import Literal

classifier = pipeline(Literal["sentiment-analysis"])
classifier(
    [
        "I've been ready for a HuggingFace course my whole life.",
        "I hate this so much!",
    ]
)
