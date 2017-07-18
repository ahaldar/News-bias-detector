import sys
import svo
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

sentences = []
	
def splitSentences():
	paragraph = sys.argv[1]
	lines_list = tokenize.sent_tokenize(paragraph)
	sentences.extend(lines_list)


def getSVOs(sentence):
	svo.parser = svo.English()
	#parse = parser(u'Trump defends son in Paris.')

	f = sentence.decode('utf-8')
	#print type(f)
	parse = svo.parser(f)
	#print f

	print "SVOs: ",
	print(svo.findSVOs(parse))
	#for word in parse:
	#	  print(word.text, word.pos_, word.dep_)
	
	print "Noun phrases: ",	
	for np in parse.noun_chunks:
			print('{0}, '.format(np.text)),
	print

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
	

def main():
	splitSentences()
	for sentence in sentences:
		print(sentence)
		getSVOs(sentence)
		getSentiments(sentence)
		print

if __name__ == "__main__":
	main()

