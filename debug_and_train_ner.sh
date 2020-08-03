#! /bin/bash

# debug the train/dev data
#python -m spacy debug-data -b en -p ner en train_json dev_json --verbose



# train a model
# python -m spacy train [lang] [output_path] [train_path] [dev_path]
#[--base-model] [--pipeline] [--vectors] [--n-iter] [--n-early-stopping]
#[--n-examples] [--use-gpu] [--version] [--meta-path] [--init-tok2vec]
#[--parser-multitasks] [--entity-multitasks] [--gold-preproc] [--noise-level]
#[--orth-variant-level] [--learn-tokens] [--textcat-arch] [--textcat-multilabel]
#[--textcat-positive-label] [--verbose]

python -m spacy train en models.en_core_web_sm train_json dev_json --base-model en_core_web_sm --pipeline ner --verbose
