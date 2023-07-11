from transformers import pipeline

# # Initialize the text generator
# generator = pipeline("text-generation")
# Initialize the classifier with a specific model
generator = pipeline("text-generation", model="gpt2")

# Use the model to generate a continuation of the given text
result = generator("In a world where", max_new_tokens=100)[0]

# Output the generated text
print(result['generated_text'])
