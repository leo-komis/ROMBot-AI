import csv

class EmbeddingHelper:

    def __init__(self, embedding_path):
        # load embeddings from CSV file
        with open('embeddings.csv', newline='') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            self.embedding_dict = {rows[0]: list(map(float, rows[1:])) for rows in reader}

    def get_embedding(self, word):
        """
        Returns the embedding vector for a given word.

        Args:
        - word (str): The word to get the embedding for.

        Returns:
        - embedding (list[float]): A list of floats representing the word's embedding vector.
        """
        if word in self.embedding_dict:
            return self.embedding_dict[word]
        else:
            return None