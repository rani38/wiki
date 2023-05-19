from sklearn.feature_extraction.text import TfidfVectorizer

# Define the question
question = "What is the capital of France?"

# Create a TfidfVectorizer instance
vectorizer = TfidfVectorizer()

# Fit the vectorizer on the question
vectorizer.fit([question])

# Vectorize the question
question_vector = vectorizer.transform([question])

# Print the vector representation
print(question_vector.toarray())
