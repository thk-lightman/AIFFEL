import re

sent = "I can do it"
pattern = re.sub("I", "You", sent)
print(pattern)
