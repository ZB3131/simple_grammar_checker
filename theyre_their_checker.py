import nltk
from nltk import word_tokenize, pos_tag

def check_their_theyre(sentence):
    # merge "they're" into one token
    sentence = sentence.replace("They're", "Theyre").replace("they're", "theyre")

    tokens = word_tokenize(sentence)
    tags = pos_tag(tokens)
    corrections = []

    print("Tagged sentence:", tags)  # To see the tags of the words (optional)

    for i, (word, tag) in enumerate(tags):
        # Rule for "their"
        if word.lower() == "their":
            if i+1 < len(tags):
                next_word, next_tag = tags[i+1]
                allowed = {"NN", "NNS", "NNP", "JJ"}  # nouns, adjectives
                if next_tag not in allowed:
                    corrections.append(
                        f"'{word}' might be wrong here (followed by '{next_word}'/{next_tag}). Did you mean 'they’re'?"
                    )
                else:
                    # Extra rule for -ing verbs
                    if next_word.endswith("ing") and i+2 < len(tags):
                        after_next_tag = tags[i+2][1]
                        # If a noun doesn't follow, flag it
                        if after_next_tag not in {"NN", "NNS"}:
                            corrections.append(
                                f"'{word} {next_word}' looks odd. Did you mean 'They’re {next_word} ...'?"
                            )

        # Rule for "they're" (now 'theyre')
        if word.lower() in ["they're", "theyre"]:
            if i+1 < len(tags):
                next_word, next_tag = tags[i+1]
                allowed = {"JJ", "RB", "VB", "VBG", "VBN", "NNS"}  # adjectives, adverbs, verbs, participles, plural nouns
                if next_tag not in allowed:
                    corrections.append(
                        f"'{word}' might be wrong here (followed by '{next_word}'/{next_tag}). Did you mean 'their'?"
                    )

    if not corrections:
        return ["No issues found."]
    return corrections

# Test sentences
print(check_their_theyre("They're son is well-behaved"))
print(check_their_theyre("Their closing the store"))
print(check_their_theyre("They're geniuses"))
print(check_their_theyre("Their talent is incredible"))
