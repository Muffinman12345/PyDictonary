#Import the module
from PyDictionary import PyDictionary

#Make a dictonary
dict_=PyDictionary()

#Here are some commands:

print(dict_.synonyms('little'))
#This returns a list of synonyms of little


print(dict_.meaning("indentation"))
#Returns the definition of indentation

print(dict_.translate('Word', 'en'))
#First thing in the '' is the word you want to translate, and the second is the language code.
#If you are not familiar with language codes, check this out:
#https://www.loc.gov/standards/iso639-2/php/code_list.php
