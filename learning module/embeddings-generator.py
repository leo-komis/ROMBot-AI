import csv
import spacy
import PyPDF2

# Load the spaCy pre-trained model for English language
nlp = spacy.load('en_core_web_sm')

# Ask user to input the PDF file name/path
pdf_file = input("Enter the path to the PDF file: ")

# Open the PDF file in read-binary mode
with open(pdf_file, 'rb') as f:
    pdf_reader = PyPDF2.PdfReader(f)

    # Concatenate all pages into a single string
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Preprocess the text with spaCy
    doc = nlp(text)
    tokens = [token for token in doc if not token.is_stop and token.is_alpha]
    lemmas = [token.lemma_ for token in tokens]

    # Generate embeddings for each lemma using spaCy's pre-trained model
    embeddings = []
    for lemma in lemmas:
        embedding = nlp(lemma).vector.tolist()
        # Add the original sentence as the first column of the embedding matrix
        embedding.insert(0, lemma)
        embeddings.append(embedding)

    # Get the dimensions of the embedding vector from spaCy
    dim_names = ['sentences'] + [f'dim_{i}' for i in range(len(embeddings[0])-1)]

    # Save the embeddings to a CSV file
    with open('embeddings.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(dim_names)
        writer.writerows(embeddings)