import json
import subprocess

cmds = [
    "pip install sentence-transformers",
    "pip install torch",
    "pip install numpy"
]
for i in cmds:
    subprocess.run(i, shell=True)

import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/e5-small")

with open("data_set.json", "r") as file:
    data = json.load(file)

sentences = list(data.values())

embeddings = model.encode(sentences)

print("embedding shape:", embeddings.shape)

np.save("embeddings.npy", embeddings)


with open("sentences.json", "w") as f:
    json.dump(sentences, f)

print("embeddings saved to embeddings.npy")