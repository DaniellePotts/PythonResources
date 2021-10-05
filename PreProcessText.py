import string 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 

class PreProcessText:
    def __init__(self):
        nltk.download('wordnet')
        nltk.download('stopwords')
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.punc = string.punctuation
    def lemmatize(self, text):
        split = text.split()
        lemmatized = [self.lemmatizer.lemmatize(word) for word in split]
    
        return self.rejoin_sentence(lemmatized)

    def is_punc(self, text):
        if text in self.punc:
            return True
        elif "'" in text:
            return True
        else:
            return False
    def remove_punc(self, text):
        for punc in self.punc:
            text = text.replace(punc,"")
        return text
    def remove_stop_words(self, text):
        word_tokens = word_tokenize(text)
        filtered_sentence = [w for w in word_tokens if not w.lower() in self.stop_words]
        filtered_sentence = []

        filtered_sentence = [w for w in word_tokens if w not in self.stop_words]

        return word_tokens, filtered_sentence

    def rejoin_sentence(self, word_tokens):
        sentence = ""
        total_words = len(word_tokens)
        for i in range(0, total_words):

            if (i + 1) == total_words: sentence = sentence + word_tokens[i]
            else:
                if total_words > (i +1) and self.is_punc(word_tokens[i + 1]): 
                    sentence = sentence + word_tokens[i]
                else:
                    sentence = sentence + word_tokens[i] + " "
        return sentence
