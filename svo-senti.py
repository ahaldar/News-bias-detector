import os
import sys
import csv
import svo
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

sentences = []

def recursive_file_gen(mydir):
    for root, dirs, files in os.walk(mydir):
        for file in files:
            #print (file[-3:])
            if file[-3:] == "txt":
                print (file)
                yield os.path.join(root, file)

def splitSentences():
	paragraph = sys.argv[1]
	lines_list = tokenize.sent_tokenize(paragraph)
	sentences.extend(lines_list)

def splitSentences2():
	path = '/home/triya/Desktop/cnn/cnn_cleaned/'
	l = list(recursive_file_gen(path))
	for filename in l:
		with open (filename) as f:
			paragraph = f.read()
			lines_list = tokenize.sent_tokenize(paragraph)
			sentences.extend(lines_list)

def writeCSV(f, svo_list, np, ss):
	with open('data.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([f, svo_list, np, ss['compound'], ss['neg'], ss['neu'], ss['pos']])


def getSVOs(sentence):
	svo.parser = svo.English()
	#parse = parser(u'Trump defends son in Paris.')

	f = sentence.decode('utf-8')
	#print type(f)
	parse = svo.parser(f)
	#print f

	print "SVO: ",
	#print(svo.findSVOs(parse))
	svo_list = svo.findSVOs(parse)
	if not svo_list:
		svo_list = svo.findSVs(parse)
	print(svo_list)
	#for word in parse:
	#	  print(word.text, word.pos_, word.dep_)
	
	print "Noun phrases: ",	
	npset = ''
	for np in parse.noun_chunks:
			print(np.text),
			npset = npset + ',' + np.text
	print
	
	return(f, svo_list, npset)

def getSentiments(sentence):
	#sentences = ["Trump defends son in Paris.",
	#"Two close confidants of Pope Francis have written an article in a Jesuit journal that strongly criticizes some American religious supporters of President Donald Trump for their fundamentalist views.",
	#"The President's son has shown astonishingly poor judgment."
	#]

	#paragraph = "Trump's dealings with Russia are a never-ending stream of controversy. \
	#	As President, Trump has the authority to declassify any material he wishes to, but the move was shocking. Critics called it \"reckless\" and \"dangerous\". \
	#	Trump has gone out on a thin limb, risking charges of obstruction of justice to protect Mike Flynn, who lost his White House job after lying about contacts with Russians."

	#lines_list = tokenize.sent_tokenize(paragraph)
	#sentences.extend(lines_list)

	sid = SentimentIntensityAnalyzer()

	ss = sid.polarity_scores(sentence)
	print "Polarity scores: ",
	for k in sorted(ss):
		print('{0}: {1} '.format(k, ss[k])),
	print
	
	return ss
	

def main():
	#splitSentences()
	splitSentences2()
	for sentence in sentences:
		print(sentence)
		f, svo_list, np = getSVOs(sentence)
		ss = getSentiments(sentence)
		writeCSV(f, svo_list, np, ss)
		print

if __name__ == "__main__":
	main()

