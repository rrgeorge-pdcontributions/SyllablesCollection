## Project Description

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) [![Version](https://badge.fury.io/gh/tterb%2FHyde.svg)](https://badge.fury.io/gh/tterb%2FHyde)

### SyllablesCollection

A repository of possible syllables of 2 or 3 word length that can be used to create new possibly sane words or any other uses that you can think of.

The syllables are extracted from the [Dictionary List](https://github.com/rrgeorge-pdcontributions/Dictionary-List) data source.

### Why should I use this?

This repository can be used to create new words, get inspiration for a organization or team original names, analyzing topics etc. The usage can be varied depending upon your requirements. 

### Data Format

`syllables.json` is the main file containing the data. The main json object has a key "data" that contains a list of json objects of syllables and other properties. Each json object in list has four keys

* `syllable` : The syllable itself.
* `cnt_score` : Number of words that contains syllable.
* `start` : Number of words that contains syllable as starting element
* `middle` : Number of words that contains syllable as middle element.
* `end` : Number of words that contains syllable as ending element

The `start`, `middle` and `end` keys are referred to as positional scores for the syllable.

The `syllable_word_creator.py` script contains an example of using the dataset to generate new words in Python.

### Examples


1. Word generation without using positional scores

![Alt text](https://github.com/rrgeorge-pdcontributions/SyllablesCollection/blob/main/syl_1.PNG?raw=true "Word generation without using positional scores")

2. Word generation using positional scores

![Alt text](https://github.com/rrgeorge-pdcontributions/SyllablesCollection/blob/main/syl_2.PNG?raw=true "Word generation using positional scores")
