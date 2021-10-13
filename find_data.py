def spot_term(texts, term):
  return [t for t in texts if term.lower() in t.lower()]

def term_exists(text, term):
  return term.lower() in text
