# ROMBot-AI

![ROMBot-AI](https://github.com/leo-komis/ROMBot-AI/raw/dev/AdobeStock_AI_Python.jpeg)

## Introduction

The code is designed to be a webapp that creates a chatbot, with a very simple interface. The chatbot in this code is capable of answering questions. It has a memory of previous answers, and if it receives a question that it has already answered, it can quickly retrieve the answer from its memory. If it receives a new question, it can generate an answer using the OpenAI API.

Based on a previous implementation built in .NET, I ultimately decided to continue my work in Python. The result seems to perform much better, at least locally, and it has the benefit of having access to a pleuthora of libraries that one could employ to enrich their application. 

The program is organized in a way that makes it easy to use and understand. It has a number of methods that allow you to interact with the chatbot, such as retrieving answers and storing answers and their related information. Additionally, the program uses a number of advanced techniques to generate answers, such as generating embeddings for answers, which are mathematical representations of the answers that capture their meaning in a high-dimensional space.

Overall, the program is designed to provide a conversational experience for users. It is capable of understanding questions and generating answers, making it an ideal solution for those who want to create a chatbot that can interact with users in a natural and intuitive manner.

The program also includes a training mode, where it trains a text classification model on the list of question-answer pairs. This model can then be used to improve the accuracy of the program's answer generation over time. The program is deployed as an Azure web app and includes a simple interface for users to enter their questions.

## The plan

1. Create a ChatBot class with:

   1a. A constructor that initializes the OpenAIApiClient instance and the Embeddings concurrent dictionary.

   1b. A LoadEmbeddingsFromDatabase method that loads the embeddings from a database into the Embeddings dictionary.

   1c. A SaveEmbeddingToDatabase method that saves an embedding to a database.

   1d. A GenerateEmbeddingAsync method that generates embeddings using the OpenAI API.

   1e. A GetClosestEmbedding method that finds the closest embedding to a given question.

   1f. A GetAnswerAsync method that generates an answer given a question.

2. Create a EmbeddingHelper class that contains the CosineSimilarity method used for comparing embeddings.

3. Create a EmbeddingData class that contains the LoadEmbeddingsAsync and LoadQAPairsAsync methods for loading embeddings and QA pairs from files.

4. Create a simple but functional web interface in Flask that uses the ChatBot class to generate answers.

5. Develop it further by attaching a database and adding a UI.

6. Add a method to the ChatBot class that allows specific users to feed it raw text, from which the bot would generate embeddings

## Still under development: 

7. Add a module which would allow the bot to transpose its knowledge from one domain to another, as long as the criteria is the same.
