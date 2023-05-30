# Project Name: KG construction from EFSA Health Claims

## main.ipynb
In this notebook claims present in the ClaimsKG and ClaimsKG2 datasets are annotated using OpenAI's [GPT-3.5 Turbo model](https://api.collaboratory.semanticscience.org/docs#/entity%20recognition/Extract_entities_and_relations_from_text_using_OpenAI_models_openai_extract_post) and the [Wikifier](https://wikifier.org/). The annotations are made on the basis of the food entities, phenotype, and the health relationship mentioned in the dataset. The annotated claims are then evaluated based on the predicted food terms using the precision, recall, and F1-score.

### Libraries Required
- pandas
- requests
- json
- re
- ast

### Dataset
The files ClaimsKG and ClaimsKG2, food terms, phenotype, and relationship-effect. These dataset can be found in the 'data' folder in csv format.
