import torch
import transformers

from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier(
    [
        "I've been ready for a HuggingFace course my whole life.",
        "I hate this so much!",
    ]
)