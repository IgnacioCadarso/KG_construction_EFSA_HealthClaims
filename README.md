# Project Name: KG construction from EFSA Health Claims

## main.ipynb
In this notebook claims present in the ClaimsKG and ClaimsKG2 datasets are annotated using OpenAI's [GPT-3.5 Turbo model](https://api.collaboratory.semanticscience.org/docs#/entity%20recognition/Extract_entities_and_relations_from_text_using_OpenAI_models_openai_extract_post) and [Wikifier](https://wikifier.org/). The annotations are made on the basis of the food entities, phenotype, and the health relationship mentioned in the dataset. The annotated claims are then evaluated based on the predicted food terms using the precision, recall, and F1-score.

### Libraries Required
- pandas
- requests
- json
- re
- ast


### Dataset
The files ClaimsKG.csv and ClaimsKG2.csv contain all information taken from EFSA health claims. ClaimsKG.csv contains [art. 13](https://www.efsa.europa.eu/en/topics/topic/general-function-health-claims-under-article-13) claims and ClaimsKG2.csv contain [art.14](https://www.efsa.europa.eu/en/topics/topic/claims-disease-risk-reduction-and-child-development-or-health-under) claims. These files can be found in the 'data' folder in csv format.

### NER Task
The NER task involves annotating the claims using the OpenAI GPT-3.5 Turbo model. The function annotateClaimsKG() sends each claim text to the model, extracts entities of types "Food Entity" and "Phenotype," and returns the results as a YAML object with the fields "entities" and "association." The annotated results are saved in the 'annotated_claims.csv' file.

Evaluation of NER Annotations
The annotations of the OpenAI GPT-3.5 Turbo model on food and phenotypes are evaluated using nervaluate. The evaluation calculates metrics such as precision, recall, and F1-score based on the true and predicted labels.

EL Task
The project includes two approaches to evaluate Entity Linking (EL) using the Wikifier API.

Approach 1:

In the first approach, the Wikifier API is called for each claim, and the relevant entities are annotated. The food terms are extracted by filtering the entities based on their dbpedia iris. If the entities are not of the types "FOOD," "CONDIMENT," or "BEVERAGE," they are removed. The precision, recall, and F1-score of the entity linking are calculated based on the comparison of the Wikifier URLs with the true URLs.
Approach 2:

In the second approach, the Wikifier API is called separately for each predicted food entity in the dataset. The dbpedia iris and Wikipedia URLs of the predicted food entities are obtained and compared to the true URLs. The precision, recall, and F1-score of the entity linking are calculated based on this comparison.
Relation Extraction (REL) Task
The relationship labels in the dataset are mapped to the predefined relationship categories: "Maintenance of a function," "Reducing a risk factor," and "Enhancing of a function." This mapping is performed to align the predicted relationship labels with the task's defined categories.

The accuracy of the predicted relationship labels is calculated by comparing them with the true relationship labels in the dataset.



