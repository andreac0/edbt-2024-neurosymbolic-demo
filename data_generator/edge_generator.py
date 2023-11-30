import random
import numpy as np
import pandas as pd

# Read a list of companies - nodes of the graph
df = pd.read_csv('company.csv')

# Define number of edges to produce
number_of_edges = 1000

################
def generate_edges(entities, num_edges):
    edges = []

    for _ in range(num_edges):
        node1, node2 = random.sample(entities, 2)
        edges.append(sorted([node1, node2]))

    return edges


edges = generate_edges(list(df['name']), number_of_edges)

df = pd.DataFrame(edges).drop_duplicates().reset_index(drop=True)
df.columns = ['controller','controlled']

s = []
for i in range(len(df)):
    if i % 2 > 0:
        x = df.loc[i,'controlled']
        df.loc[i,'controlled'] = df.loc[i,'controller']
        df.loc[i,'controller'] = x
    s.append(np.random.uniform(size = 1)[0])


df['share'] = s
df = df[df['share']>0]


entities = df['controlled'].drop_duplicates()

for ent in entities:
    exp_values = np.exp(df[df['controlled'] == ent]['share'])
    softmax_values = exp_values / exp_values.sum()
    df.loc[df['controlled'] == ent,'share'] = softmax_values

for i in range(len(df)):
    df.loc[i,"share"] = round(df.loc[i,"share"],2)
df = df[df['share']>0]

df.to_csv('syntethic_kg.csv', index=False)

