import openai
import gradio as gr
import pandas as pd
import spacy
import app

# Load the spaCy pre-trained model for English language
nlp = spacy.load('en_core_web_sm')

# Load the embeddings file
df = pd.read_csv("embeddings.csv")

# Set the OpenAI API key
openai.api_key = "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"

# Define the function to generate embeddings for given text
def generate_embedding(text):
    tokens = [token for token in nlp(text) if not token.is_stop and token.is_alpha]
    lemmas = [token.lemma_ for token in tokens]
    embedding = []
    for lemma in lemmas:
        try:
            row = df[df['sentence'] == lemma].iloc[0].tolist()[1:]
            embedding.extend(row)
        except IndexError:
            continue
    return embedding


# Define a function to search for an answer in the embeddings file
def get_answer_from_embeddings(input):
    # Get the embedding vector for the input message
    input_embedding = generate_embedding(input)

    # If embedding is present for the input message, find the most similar message from the embeddings file
    if len(input_embedding) > 0:
        similarity_scores = []
        for i, row in df.iterrows():
            score = 0
            for j, val in enumerate(input_embedding):
                score += (row[j+1] - val)**2
            similarity_scores.append(score)
        closest_row = df.loc[similarity_scores.index(min(similarity_scores))]
        return closest_row['sentence_response']

    # If no matching embedding is found, use OpenAI API to generate response
    else:
        messages = [
            {"id": "1", "text": input},
            {"id": "2", "text": "Hi, how can I help you today?"},
            {"role": "system", "content": "You are a helpful and kind AI Assistant, who is an expert on the ROM Global project."}
        ]
        prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])
        completion = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.85,
            max_tokens=1000,
            n=1,
            stop=None,
            # Set the presence_penalty and frequency_penalty to encourage more diverse responses
            presence_penalty=0.6,
            frequency_penalty=0.6,
        )
        response = completion["choices"][0]["text"]
        return response


# Define the Gradio interface for the chatbot
inputs = gr.inputs.Textbox(lines=7, label="ROMBot-AI")
outputs = gr.outputs.Textbox(label="Reply")

title = "ROMBot-AI"
description = "Ask anything you want!"

# Launch the interface
gr.Interface(fn=get_answer_from_embeddings, inputs=inputs, outputs=outputs, title=title, description=description, theme="compact").launch(share=True)

if __name__ == "__main__":
    app.run()