def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

print(order('4of Fo1r pe6ople g3ood th5e the2'))