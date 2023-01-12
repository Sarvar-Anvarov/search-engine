def tokenize_description(text, tokenizer):
    return tokenizer.tokenize(text)


def remove_stopwords(text, stop_words):
    filtered_text = []
    for word in text:
        if word not in stop_words:
            filtered_text.append(word)

    return filtered_text
