# CMAP GENERATOR (Automatic Generation of Conceptual Maps From Text)

This repository presents an application of Natural Language Processing (NLP) methodologies to transform text into conceptual maps, aiming to aid in studying and comprehension processes. 

## Methodology
### Relation extraction
The methodology begins with the initial extraction of relations from the collected textual data. Open Information Extraction (OpenIE) is employed to extract semantic relationships between entities or concepts mentioned in the text. These relationships are represented as subject-predicate-object tuples. Before applying OpenIE, the text undergoes coreference resolution using NeuralCoref to handle pronouns and link them to their respective entities.

To ensure the quality of extracted relations, a manual analysis is conducted on a sample of extracted relations. Patterns associated with irrelevant or unsuitable extractions are identified, leading to the removal of relations that:

- Lack any noun in the first argument
- Consist of only one or two pronouns in the second argument
- Include a relation consisting of just two words, with the first being "to" (indicating an infinitive verb)
- Lack a verb in the relation
- Have either the first or second argument ending in a preposition, suggesting truncated sentences with potentially lost meaning.
- These criteria help filter out erroneous relations, ensuring the accuracy and relevance of the extracted information for constructing conceptual maps

### Pre-processing
Several pre-processing functions were developed to refine the extracted relations before constructing the final conceptual map. These functions include:

1) Filtering Duplicate Relations: A function was defined to merge tuples into single sentences, remove duplicates, and retain the longest substrings to eliminate redundancy.

2) Merging Concepts: Clusters of arguments were created based on cosine similarity, with a threshold of 0.4, to group related concepts. Clusters with common elements were merged to avoid overlaps. The title of the paragraph was chosen as the representing string if present, otherwise, the shortest argument was selected to simplify the map.

3) Concatenating Concepts: This function concatenated objects and subjects to ensure no repeated substrings in the final conceptual map. Objects and subjects sharing the same argument and relation were grouped, and common substrings were identified and merged.

4) Removing Affine Meanings: A function was defined to remove sentences with very similar meanings by comparing phrases and retaining only the longest, most informative ones.

After applying these pre-processing functions, relations were further filtered based on confidence scores assigned during extraction, with only relations exceeding the median confidence being retained. Additionally, a classifier was trained to identify and prune irrelevant or unsuitable relations from the final conceptual map.

### Classifier
Efforts to build a classifier initially focused on predicting the meaningfulness of entire sentences but encountered challenges due to the complexity of distinguishing subtle differences in structure and meaning. Despite attempts to refine the model, including manual re-annotation of additional data, the performance remained unsatisfactory.

Subsequent strategies involved training separate classifiers for the first argument, relation, and second argument. Strict annotation rules ensured the correctness and sensibility of each part of the extraction. While challenges persisted, the classifier for the first argument demonstrated promising accuracy, exceeding 81%. Integrating this classifier into the pipeline contributed to the final conceptual map creation process.

Despite attempts to enhance classifier performance through various methods, such as custom loss functions and different models, significant improvements were not achieved. The success of the classifier for the first argument suggests that meaningful distinctions are more discernible in this context.

This classifier, pretrained on carefully annotated data, was applied to prune remaining relations further after pre-processing, enhancing the quality of the final conceptual map.

### Results

In conclusion, the evaluation of the concept maps involved both a user study and objective metrics. The user study showed that while both model-generated and human-created maps were satisfactory for understanding, the baseline map was considered useless. The model-generated map was seen as useful for revising concepts but not entirely trustworthy, while the human-created map was deemed capable of comprehensively representing the paragraph. Objective metrics, including ROUGE-2 scores, indicated that the model partially retrieved relevant elements from the text similar to BART summarization. However, limitations include text repetition in concept maps and varying map lengths. Overall, the model demonstrates acceptable performance while remaining far from being perfect.

## Structure of the repo
The core functionality of our project resides in the *main_notebook.ipynb file*, where the map generation model is implemented.

In *classifier.ipynb*, the focus is on training the classifier for relation selection, a crucial aspect of map generation. Meanwhile, *graph.py* contains the class responsible for visualizing the concept map. This class constructs nodes and edges based on the resulting data frame of the most important propositions, aiding in the comprehension and analysis of the generated maps.

To enhance the accuracy of our maps, we employ NeuralCoref and the OpenIE Stanford tool ([repository of the project](https://github.com/dair-iitd/OpenIE-standalone)) to resolve coreferences and extract relations effectively. Additionally, we offer *handmade_maps.ipynb* for visualizing human-created maps, providing valuable insights for comparison.

For benchmarking purposes, *baseline_test.py* is used for the generation of baseline concept maps, while *evaluation.ipynb* outlines our model evaluation methodology, accompanied by the pertinent data frames used in the process.

We aim to provide a comprehensive framework for map generation, empowering users to explore, evaluate, and enhance their understanding of complex concepts efficiently.


```
│──📁 data: contains the dataset imported in the notebooks
│
├──📁 notebooks and util
│   ├── main_notebook.ipynb
│   ├── classifier.ipynb
│   ├── evaluation.ipynb
│   ├── import_modules.py
│   ├── graph.py
│   ├── baseline.py
│    
├── 📁 models
│
└── 📄 Report_NLP.pdf
```

## Credits

| Author             | Contact                       
| ----------------   | ------------------------------
| Domitilla Izzo | domitilla.izzo@studbocconi.it 
| Lorenzo d'Imporzano |	lorenzo.dimporzano@studbocconi.it
| Riccardo Valdo  | riccardo.valdo@studbocconi.it  
|Luca Matarazzo | luca.matarazzo@studbocconi.it
|Elena Rossi | elena.r@studbocconi.it
