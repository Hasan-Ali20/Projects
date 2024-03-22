# Loads the spaCy library for natural language processing tasks
import spacy 

# Loads the advanced English language model provided by spaCy
nlp = spacy.load("en_core_web_md")

# Loads the pandas library 
import pandas as pd

# Reading text file as a DataFrame with ':' as the separator
df = pd.read_csv('movies.txt',sep=':', header=None, names=['Movie', 'Description'])

print(df)

Movie = str(input("""Please enter a movie description of your choice, based on the description
we will look through our movies database, and provide you a movie which has 
a high similarity to that description you provided, so you can enjoy a recommend movie!: """))

# Defining a function to recommend a movie based on a given description
def recommend_movie(description):
    # Process the input description with nlp
    doc = nlp(description)
    # Initialize variables to track the movie title and its similarity score
    recommended_movie = None
    max_similarity = -1
    
    # Iterate over each movie description in the DataFrame
    for index, row in df.iterrows():
        # Process the movie description
        movie_doc = nlp(row['Description'])
        # Calculate the similarity between the input description and the current movie description
        similarity = doc.similarity(movie_doc)
        
        # Update the recommended movie if the current movie has higher similarity
        if similarity > max_similarity:
            max_similarity = similarity
            recommended_movie = row['Movie']
    
    # Return the recommended movie and its similarity score
    return recommended_movie, max_similarity

# Call the function to recommend a movie based on the description provided by user
recommended_movie_title, similarity_score = recommend_movie(Movie)

# Print the recommended movie and its similarity score
print("Recommended Movie:", recommended_movie_title)
print("Similarity Score:", similarity_score)
print (f"The recommended movie is {recommended_movie_title} because it has the similarity score of {similarity_score}, which is the highest similarity to the movie description you have provided!")