import spacy
nlp = spacy.load('en_core_web_md')

description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""
# Movie description for comparisons.

def watch_next(info): # Define the watch_next function. 
    movies = open("movies.txt", "r")  # Open the movie.txt file and read contents.
    split_movie_list = [] # Create an empty list which will store our similarities.
    for i in movies:     # Split movies in the file into title and description. 
        split_movie_list.append(i.split(':')) 
    count = len(split_movie_list) # Count the number of movies in text file.
    sim_list = [] # This list will store similar similarity values for the movies. 
    my_model_sentence = nlp(info)
    for i in range(0, count): 
        sim_list.append(nlp(split_movie_list[i][1]).similarity(my_model_sentence))
        # Check similarity between movie description and descriptions of recently watched movies.
    max_similarity = max(sim_list) # This gives us the max similarity value. 
    max_similarity_movie = sim_list.index(max_similarity)  # Produce an index of highest similarity values. 
    return split_movie_list[max_similarity_movie][0] # And return movie title with highest similarity to the watched movie. 

print("We recommend you watch this next: " + watch_next(description))
# Print a recommendation for the movie in the .txt file with the highest similarity to the watched movie. 