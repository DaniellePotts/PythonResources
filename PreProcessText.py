import string 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from spellchecker import SpellChecker
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from bs4 import BeautifulSoup

class PreProcessText:
    def __init__(self):
        nltk.download('wordnet')
        nltk.download('stopwords')
        nltk.download('punkt')
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.punc = string.punctuation
        self.spell = SpellChecker()
        self.porter = PorterStemmer()
        self.lancaster=LancasterStemmer()
    def lemmatize(self, text):
        split = text.split()
        lemmatized = [self.lemmatizer.lemmatize(word) for word in split]
    
        return self.rejoin_sentence(lemmatized)
#     def spell_check(self, )
    
    def stem(self, text, stemmer_type):
        split = text.split()
        stemmed = []
        if stemmer_type.upper() == "PORTER":
            stemmed = [self.porter.stem(word) for word in split]
        elif stemmer_type.upper() == "LANCASTER":
            stemmed = [self.lancaster(word) for word in split]
        else:
            raise "Valid stemmer not provided"
        return self.rejoin_sentence(stemmed)
   
# spell = Speller(lang='en')
    def is_punc(self, text):
        if text in self.punc:
            return True
        elif "'" in text:
            return True
        else:
            return False
    
    def remove_punc(self, text):
        for punc in self.punc:
            if punc == "/" or punc == "-" or punc == ".":
                text = text.replace(punc, " ")
            else:
                text = text.replace(punc,"")
        return text
    def remove_stop_words(self, text):
        word_tokens = word_tokenize(text)
        filtered_sentence = [w for w in word_tokens if not w.lower() in self.stop_words]
        filtered_sentence = []

        filtered_sentence = [w for w in word_tokens if w not in self.stop_words]

        return self.rejoin_sentence(filtered_sentence)
    def add_stop_words(self, words):
      for w in words:
        self.stop_words.add(w)
    def remove_single_digits(self,text):
        split = text.split()
        final = []
        for s in split:
            if not s.isdigit():
                final.append(s)
        return self.rejoin_sentence(final)
    def remove_email(self, text):
        items = text.split()
        filtered = [i for i in items if '@' not in i]
        
        return self.rejoin_sentence(filtered)
    def strip_html_tags(self, text):
        soup = BeautifulSoup(text, "html.parser")
        stripped_text = soup.get_text()
        return stripped_text
    def remove_numbers(self, text):
        return ''.join([i for i in s if not i.isdigit()])
    def remove_alpha_numeric_terms(self, text):
        cleaned = []
        for s in text.split():
            includes_numbers = any(char.isdigit() for char in s)
            if not includes_numbers:
                cleaned.append(s)
        return self.rejoin_sentence(cleaned)
    def remove_terms(self, text, terms):
        for t in terms:
            text = text.replace(t, "")
        return text
    def remove_trailing_spaces(self, text, remove_preifx_space, remove_suffix_space):
      if remove_preifx_space:
        if text:
            if text[0] == " ":
              text = text[1:]
      if remove_suffix_space:
        if text[(len(text) -1)] == " ":
          text = text[:(len(text)-1)]
      return text
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
