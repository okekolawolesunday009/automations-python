import re
print(re.search(r"[Pp]ython", "Python"))

import re
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

import re
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

import re
print(re.search(r"o+l+", "goldfish")) #ol
print(re.search(r"o+l+", "woolly")) #ool
print(re.search(r"o+l+", "boil")) nil

import re
print(re.search(r"p?each", "To each their own")) #each ( p is optional) 
print(re.search(r"p?each", "I like peaches")) #peach
import re
print(re.search(r".com", "welcome")) any match
print(re.search(r"\.com", "welcome")) exact match
print(re.search(r"\.com", "mydomain.com"))

import re
print(re.search(r"\w*", "This is an example")) none
print(re.search(r"\w*", "And_this_is_another")) all string