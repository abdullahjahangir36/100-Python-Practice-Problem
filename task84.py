# Write a function that accepts a list of strings and 
# performs Bag of words and convert it to numerical vectors.
from sklearn.feature_extraction.text import CountVectorizer

def bag_of_words_from_user():
    # Prompt the user to enter a list of strings
    print("Enter each string followed by pressing Enter. Type 'done' when you are finished:")
    
    strings = []
    while True:
        user_input = input()
        if user_input.lower() == 'done':
            break
        strings.append(user_input)
    
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the data
    X = vectorizer.fit_transform(strings)
    
    # Get the vocabulary
    vocabulary = vectorizer.get_feature_names_out()
    
    # Convert to a dense matrix and then to a list of lists
    dense_matrix = X.toarray()
    
    # Create a list of dictionaries to represent each string's vector
    vectors = []
    for row in dense_matrix:
        vector_dict = {vocabulary[i]: row[i] for i in range(len(vocabulary))}
        vectors.append(vector_dict)
    
    return vocabulary, vectors

# Example usage
if __name__ == "__main__":
    vocab, vectors = bag_of_words_from_user()
    print("Vocabulary:", vocab)
    print("Vectors:", vectors)
