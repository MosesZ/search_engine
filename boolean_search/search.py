import ast, csv, os, re, webbrowser
from nltk.tokenize import word_tokenize
from pymystem3 import Mystem

def intersection(lst1, lst2): 

    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def sorted_aphanumeric(data):

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

with open('C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\inverted_index\\inverted_index.csv', 'r', newline='') as f:

	reader = csv.reader(f)
	data = [row for row in reader]
	words = data[0]
	inverted_indicies = data[1]

request = "вынести Всевозможный минус"

lemmatizer = Mystem() 
lemmatized_request = lemmatizer.lemmatize(request)
lemmatized_request = [w for w in lemmatized_request if w not in [" ", "\n"]]

doc_sets = []

for index, item in enumerate(lemmatized_request):

	doc_sets.append(ast.literal_eval(inverted_indicies[words.index(item)]))

sets_intersection = []

for index, item in enumerate(doc_sets):

	if (index == 0):

		sets_intersection = item
	else:

		sets_intersection = intersection(sets_intersection, item)

path = 'C:\\Users\\Moses\\Documents\\GitHub\\search_engine\\scraper\\URLs_list.txt'
main_page = 'http://mathprofi.ru/'

for i in sets_intersection:

	with open(path) as f:

	    content = f.readlines()
	    content = [x.strip() for x in content]
	    page = word_tokenize(content[3])[1]
	    print(main_page + page)
	    url = main_page + page
	    webbrowser.open(url,new=2)