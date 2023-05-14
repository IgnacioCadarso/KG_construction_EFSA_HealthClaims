Project Name: Claim Annotation using OpenAI GPT-3.5 Turbo Model
This project aims to annotate claims present in the ClaimsKG and ClaimsKG2 datasets using OpenAI's GPT-3.5 Turbo model. The annotations are made on the basis of the food entities, phenotype, and the health relationship mentioned in the dataset. The annotated claims are then evaluated based on the predicted food terms using the precision, recall, and F1-score.

Libraries Required
pandas
requests
json
re
ast
wikifier
Installation
The libraries can be installed using pip.

python
Copy code
!pip install pandas requests json re ast wikifier
Dataset
Two datasets are used in this project: ClaimsKG and ClaimsKG2. These datasets contain the claims, food terms, phenotype, and relationship-effect. These datasets can be found in the 'data' folder in csv format.

Steps to Run
First, import the required libraries and load the data from the csv files present in the 'data' folder.
Combine the data from the two datasets using pd.concat() function.
Filter out the required columns using the dataframe indexing.
Remove the rows with missing values using the dropna() function.
Reset the index of the dataframe using the range() function.
Annotate the claims using the annotateClaimsKG() function. The results are saved in 'data/annotated_claims.csv'.
Evaluate the annotations of the OpenAI GPT3.5-Turbo model on food terms using the evaluateAnnotations() function.
Finally, evaluate the annotations of OpenAI GPT3.5-Turbo model + Wikifier on food terms using the queryWikifier() function.
Functions
1. annotateClaimsKG()
This function takes no input parameters. It sends the text present in the 'Claim' column to the OpenAI GPT-3.5 Turbo model for annotation. The function extracts the entities, classifies them, and extracts an association between those entities. The entities to extract are of the types: "Food Entity", "Phenotype". The function returns the results as a YAML object with the following fields:

entities: the list of entities in the text, each entity is an object with the fields: label, type
association: a list with the most important association between entities in the text, an association is an object with the fields: "subject" for the subject entity, "predicate" for the relation (maintenance of function, enhancing a function, reducing a risk factor), "object" for the object entity
The function saves the annotated results in 'data/annotated_claims.csv' file.

2. evaluateAnnotations()
This function takes no input parameters. It evaluates the annotations of the OpenAI GPT3.5-Turbo model on food terms using the precision, recall, and F1-score. The function returns the confusion matrix, precision, recall, and F1-score.

3. queryWikifier()
This function takes no input parameters. It uses the DBpedia IRI to query Wikifier and get the Wikidata ID of the entity. The function accepts the entity if it is of type Food or ChemicalSubstance. The function returns the annotations of OpenAI GPT3.5-Turbo model + Wikifier on food terms. The annotations are saved in 'data/wiki_iris.csv' file.

Conclusion
This project provides a step-by-step guide to annotate the claims using OpenAI GPT-3.5 Turbo model, evaluate the annotations on food terms, and finally use Wikifier to get