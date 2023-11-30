# EDBT 2024 Demonstration Submission
 This repository includes the KG data generator, the datasets and the code of the verbalizer module that we present in the paper "Interactive Generation of Business Reports in a Neuro-Symbolic Datalog-based Environment" submitted to EDBT 2024 - Demo Track


## Synthetic KG Generator
The folder ***data_generator*** contains the script to generate an artifical KG of ownership, similar to the real one and of arbitrary dimension. It leverages a list of random companies, available in the csv file ***company.csv*** and generates the KG edges in a new csv file: ***syntethic_kg.csv***.

## Dataset Description

***synthetic_kgs*** are artifially generated graphs that show structural similarities with realistics company network; the number n of nodes in the graph can be chosen by setting the ***number_of_edges*** variable.

## Authors
