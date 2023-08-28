import transformers

from transformers import pipeline

classifier = pipeline("sentiment-analysis")
classifier("I've been waiting for a HuggingFace course my whole life.")


# alemdar, yerebatan cd. 38 34110 fatih istanbul
