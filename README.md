# ner-retrain

Retraining spacy's NER tagger to improve the identification of PERSON tags for certain politicians

Repository contains:

* README.md	# this readme file

Training data:
* train_json	# automatically generated training data from Wikipedia
* dev_json	# directory with the _same_ files (not optimal, but we don't have a dev set)

Training script:
* debug_and_train_ner.sh # bash script for debugging the train data and training the models

Trained models (based on 'en' and 'en_cor_web_sm'):
* models.en
* models.en_core_web_sm

Using the retrained models:
* tag.py	# example script that shows how to call the retrained models
* test.txt	# test file (but without gold annotations)

Other:
* names.txt	# list with politician's names (extracted from filefortrain.txt) 



