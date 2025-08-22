# simple_grammar_checker
This project is a simple grammar checker built in Python using NLTK.
It focuses on detecting common mistakes between “their” (possessive) and “they’re” (contraction of "they are"). 

It is still a work in progress because, for example, “their” can also be followed by adverbs, as in, “their fabulously made home.” So it needs a rule to check whether, for instance, `i+3` is `NN`.

I used the `.replace()` method to normalize contractions, because the NLTK `word_tokenize` splits “they’re” into “they” and “’re”, so “they’re” is not flagged if it’s used incorrectly. I also tried the `TreebankWordTokenizer`, but it still splits it.

I had to add a separate rule for verbs ending in -ing because NLTK’s `pos_tag` can tag -ing verbs as `NN`; for example, “their running late” wouldn’t be flagged as incorrect because the following verb is tagged as an `NN`.

Features:
- Detects when “their” is used incorrectly (e.g., “Their ” should be “They’re running late”).
- Detects when “they’re” is used incorrectly (e.g., “They’re teacher is nice” should be “Their teacher is nice”).
- Provides suggestions for corrections.
- Prints the POS tags for easier development.

Installation:
1.	Clone the repository:
```bash
 git clone https://github.com/ZB3131/simple_grammar_checker.git
cd simple_grammar_checker 
```

2.	Install NLTK:
```bash
pip install nltk
```

3.	Download NLTK resources (first run only):
```bash
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```
5.	After cloning, you can open `theyre_their_checker.py` in your desired code editor and change the test sentences (also add more). Then run the script:
```bash
python theyre_their_checker.py
```
Or on Python:
```bash
from theyre_their_checker import check_their_theyre
print(check_their_theyre("Their story is captivating."))
print(check_their_theyre("They're geniuses."))
print(check_their_theyre("They're mother is a doctor."))
print(check_their_theyre("Their closing the store."))
```
Output
```bash
['No issues found.']
['No issues found.']
["'Theyre' might be wrong here (followed by 'mother'/NN). Did you mean 'their'?"]
["'Their closing' looks odd. Did you mean 'They’re closing ...'?"]
```
How it Works:
-	The model tokenizes each sentence and assigns a part-of-speech (POS) tag to each word.
-	It applies simple rules to check if “their” and “they’re” are used correctly, based on the POS tags of the following word(s).
-	If a potential misuse is detected, it outputs a suggested correction.

Future Improvements:
-	Improve the tokenizer so that “they’re” is recognized as a single token in its original form, without needing to replace it with “theyre”
-	Extend checker to other commonly confused words (your vs you’re, its vs it’s, etc.)
-	Improve POS-based context rules

