# Write a program that can find the most used word in a bollywood song
from collections import Counter
import re

def find_most_used_word(song_lyrics):
    # Remove punctuation and convert to lowercase
    cleaned_lyrics = re.sub(r'[^\w\s]', '', song_lyrics).lower()
    
    # Split the lyrics into words
    words = cleaned_lyrics.split()
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Find the most common word
    most_common_word, most_common_count = word_count.most_common(1)[0]
    
    return most_common_word, most_common_count

def main():
    # Input lyrics from the user
    song_lyrics = input("Enter the lyrics of the song: ")
    
    # Find the most used word
    most_common_word, most_common_count = find_most_used_word(song_lyrics)
    
    # Print the result
    print(f"The most used word is '{most_common_word}' with {most_common_count} occurrences.")

if __name__ == "__main__":
    main()
