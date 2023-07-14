from transformers import pipeline

# # Initialize the classifier
# classifier = pipeline("sentiment-analysis")
# Initialize the classifier with a specific model
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Use the model to classify a piece of text
result = classifier("I love this movie!")[0]

# Output the classification results
print(f"label: {result['label']}, with score: {result['score']}")

from transformers import pipeline
