# News Bias Detector

A program to test for biased language and subjectivity, with focus on partisan vocabulary in news text snippets.

## Dependencies

Install nltk, spaCy, and vaderSentiment in order for svo-senti.py to work:
```
sudo pip install -U nltk
sudo pip install -U spacy
sudo python -m spacy download en
sudo pip install vaderSentiment
```

## Run

`python detect_bias.py "[block of text]"` in terminal.  
`python svo-senti.py "[block of text]"` in terminal.

## Examples

```
$ python detect_bias.py "Grenfell disaster victims murdered by political decisions"

NEWS BIAS DETECTOR

Sensationalism issues: 1
Partisanship issues: 0

* Sensationalist vocabulary is used

Mentioned: disaster


$ python detect_bias.py "If Republican efforts to repeal and replace Obamacare are successful, one of the biggest winners would be the wealthy. The Senate's bill -- released this week -- differs in key ways from the House-passed version. But proposals eliminate the taxes imposed on high-income Americans to help pay for an expansion of health benefits under the Affordable Care Act. The legislation also would let people contribute more to certain tax-advantaged accounts."

NEWS BIAS DETECTOR

Sensationalism issues: 0
Partisanship issues: 2

* Partisan vocabulary is used

Mentioned: Obamacare, Affordable Care Act
```


```
$ python svo-senti.py "Trump defends son in Paris. The President's son has shown astonishingly poor judgement."

Trump defends son in Paris.
SVOs:  [(u'trump', u'defends', u'son')]
Noun phrases:  Trump,  son,  Paris, 
Polarity scores:  compound: 0.0  neg: 0.0  neu: 1.0  pos: 0.0 

The President's son has shown astonishingly poor judgement.
SVOs:  [(u'son', u'shown', u'judgement')]
Noun phrases:  The President's son,  astonishingly poor judgement, 
Polarity scores:  compound: -0.4767  neg: 0.307  neu: 0.693  pos: 0.0 
```

## Credits

detect_bias.py based on the JavaScript [joblint](https://github.com/rowanmanning/joblint) project and its Python modification [newslint](https://github.com/Xeus/newslint).  
svo-senti.py using the help of [spaCy tutorials](https://nicschrading.com/project/Intro-to-NLP-with-spaCy/).
