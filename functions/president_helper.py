import os
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords, inaugural
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Stop words
stop_words = set(stopwords.words('english'))



def read_file(file_name):
  with open(file_name, 'r+', encoding='utf-8') as file:
    file_text = file.read()
  return file_text

def process_speeches(speeches):
  word_tokenized_speeches = list()
  for speech in speeches:
    sentence_tokenizer = PunktSentenceTokenizer()
    sentence_tokenized_speech = sentence_tokenizer.tokenize(speech)
    word_tokenized_sentences = list()
    for sentence in sentence_tokenized_speech:
      word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!') for word in sentence.replace(",","").replace("-"," ").replace(":","").split()]
      # ---------------- Removes stopwords from sentences
      word_tokenized_sentence = [word for word in word_tokenized_sentence if word not in stop_words]
      word_tokenized_sentences.append(word_tokenized_sentence)
    word_tokenized_speeches.append(word_tokenized_sentences)
  return word_tokenized_speeches

def merge_speeches(speeches):
  all_sentences = list()
  for speech in speeches:
    for sentence in speech:
      all_sentences.append(sentence)
  return all_sentences

def get_president_sentences(president):
  # Get the file IDs for the inaugural speeches
  file_ids = inaugural.fileids()

  # Initialize a dictionary to store the president's name and the original file name
  president_names = {}

  # Extract the president's name from the file name
  for file_id in file_ids:
      # Map the name to the corresponding president name using the custom function
      president_name = map_president_name(file_id)
      # Store the president's name as the key and the original file name as the value
      president_names[president_name] = file_id
  
  # Extract the president's name from the file name
  # for file_id in file_ids:
  #     # Extract the name between the year and .txt
  #     name = file_id.split("-")[1].split(".")[0]
  #     # Store the president's name as the key and the original file name as the value
  #     president_names[name] = file_id

  # Create a list to store the speeches
  speeches = [inaugural.raw(president_names[president])]

  processed_speeches = process_speeches(speeches)
  all_sentences = merge_speeches(processed_speeches)
  return all_sentences

def get_presidents_sentences(presidents):
  all_sentences = list()
  for president in presidents:
    # Get the file IDs for the inaugural speeches
    file_ids = inaugural.fileids()

    # Initialize a dictionary to store the president's name and the original file name
    president_names = {}

    # Extract the president's name from the file name
    for file_id in file_ids:
        # Map the name to the corresponding president name using the custom function
        president_name = map_president_name(file_id)
        # Store the president's name as the key and the original file name as the value
        president_names[president_name] = file_id
    
    # # Extract the president's name from the file name
    # for file_id in file_ids:
    #     # Extract the name between the year and .txt
    #     name = file_id.split("-")[1].split(".")[0]
    #     # Store the president's name as the key and the original file name as the value
    #     president_names[name] = file_id

    # Create a list to store the speeches
    speeches = [inaugural.raw(president_names[president])]
    processed_speeches = process_speeches(speeches)
    all_prez_sentences = merge_speeches(processed_speeches)
    all_sentences.extend(all_prez_sentences)
  return all_sentences

def most_frequent_words(list_of_sentences):
  all_words = [word for sentence in list_of_sentences for word in sentence]
  return Counter(all_words).most_common()


def create_wordcloud(most_frequent_words):
    # Create a dictionary from the list of most frequent words
    word_freq_dict = {word: freq for word, freq in most_frequent_words}

    # Define a color function to map word frequencies to colors
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        # Define a colormap
        colormap = plt.get_cmap("viridis_r")  # choose colormaps 
        # Normalize word frequencies between 0 and 1
        normalized_freq = (word_freq_dict[word] - min(word_freq_dict.values())) / (max(word_freq_dict.values()) - min(word_freq_dict.values()))
        # Map normalized frequency to a color in the colormap
        color = colormap(normalized_freq)
        return "rgb" + str(tuple(int(255 * x) for x in color[:3]))

    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white', color_func=color_func)

    # Generate the word cloud from the word frequency dictionary
    wordcloud.generate_from_frequencies(word_freq_dict)

    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


# Define a custom function to map file names to president names
def map_president_name(file_id):
    if file_id == '1797-Adams.txt':
        return 'John-Adams'
    elif file_id == '1825-Adams.txt':
        return 'John-Q-Adams'
    elif file_id == '1841-Harrison.txt':
        return 'William-Harrison'
    elif file_id == '1889-Harrison.txt':
        return 'Benjamin-Harrison'
    elif file_id == '1905-Roosevelt.txt':
        return 'Theodore-Roosevelt'
    elif file_id in ['1933-Roosevelt.txt', '1937-Roosevelt.txt', '1941-Roosevelt.txt', '1945-Roosevelt.txt']:
        return 'Franklin-D-Roosevelt'
    elif file_id == '1965-Johnson.txt':
        return 'Lyndon-Johnson'
    elif file_id == '1989-Bush.txt':
        return 'George-HW-Bush'
    elif file_id in ['2001-Bush.txt', '2005-Bush.txt']:
        return 'George-W-Bush'
    else:
        # Extract the name between the year and .txt
        return file_id.split("-")[1].split(".")[0]

