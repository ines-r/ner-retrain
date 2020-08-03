import spacy

"""
This script shows how to read in the retrained models and predict tags for some text file.
"""


"""
Read a text file and return as a list
"""
def read_docs(infile):
    text = []
    with open(infile, "r") as fh:
        for line in fh:
            text.append(line.strip())
    return text


"""
Pick the model you want to use:
"""

#####
### Before running the script, select the model you want to use:
###   use spacy's original en (English) model
# model_name = "en"  
###   use retrained en model
# model_name = "./retrained.en/model-best" 
###   use spacy's original en_core_web_sm model
#model_name = "en_core_web_sm" 
###   use retrained en_core_web_sm model
model_name = "./retrained.en_core_web_sm/model-best" 


# load model
nlp = spacy.load(model_name)

# read test file
texts = read_docs('test.txt')

# iterate over text and predict NER tags
for i in range(len(texts)):
    doc = nlp(texts[i])
    print([(ent.text, ent.label_) for ent in doc.ents]) 
    

