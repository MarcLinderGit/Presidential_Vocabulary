# Exploring U.S. Presidential Inaugural Speeches

In this project, I leverage the power of natural language processing (NLP) and word embeddings to uncover the linguistic patterns, common themes, and unique insights hidden within the inaugural addresses of U.S. presidents, spanning from 1789 to 2017.

## Project Overview

### Preprocessing the Data

1. **Data Reading**: I read and store all the text data from these files, creating a list of speeches to analyze.

2. **Text Tokenization**: The speeches are broken down into words and sentences to facilitate analysis.

### Analyzing the Inaugural Addresses

3. **Exploring Common Words**: I begin by identifying the most frequently used words across all the inaugural addresses, shedding light on common themes and topics.

4. **Word Embeddings**: Next, I create word embeddings using the Gensim library, enabling me to represent words in a multidimensional space. I build a model that learns the context and relationships between words in the entire corpus of inaugural addresses.

5. **Words Similar to "Freedom"**: I investigate the words most similar to the term "freedom" in the context of all inaugural addresses, uncovering related concepts and ideas.

### Individual Presidents

6. **Focus on a Single President**: I shift my attention to a specific president, Franklin D. Roosevelt, to explore how his inaugural addresses differ from the collective speeches of all presidents.

7. **Frequent Words of the President**: I identify the most frequently used words in Roosevelt's inaugural speeches, gaining insights into his recurring themes.

8. **Roosevelt's Word Embeddings**: I create a new word embedding model tailored to Roosevelt's inaugural addresses and examine words similar to "freedom" in his context.

### Selection of Presidents

9. **Mount Rushmore Presidents**: I expand my analysis to include the inaugural addresses of four iconic presidents featured on Mount Rushmore: Washington, Jefferson, Lincoln, and Theodore Roosevelt. This allows me to compare their language and themes.

10. **Frequent Words of Mount Rushmore Presidents**: I determine the most commonly used words in the speeches of these presidents, providing a unique perspective on their leadership.

11. **Mount Rushmore Presidents' Word Embeddings**: A specialized word embedding model is trained on the inaugural addresses of these four presidents. I investigate words similar to "freedom" in their speeches.

### Custom Presidential Selection

12. **Personalized Analysis**: I offer you the opportunity to choose your favorite presidents, controversial figures, or political party affiliations for a more tailored analysis. You can create a custom word embedding model and explore words and themes of interest.

## Conclusion

This project combines the historical significance of U.S. presidential inaugural addresses with cutting-edge NLP techniques to unveil insights, trends, and nuances in presidential communication. By examining common words, word embeddings, and the language of individual presidents, I gain a deeper understanding of the values and visions that have shaped the nation's leadership over centuries. It's a fascinating journey through both language and history. Let's dive in and explore the rich tapestry of U.S. presidential speeches!