# News Bias Detector

A program to test for biased language and subjectivity, with focus on partisan vocabulary in news text snippets.

## Run

`python detect_bias.py "[block of text]"` in terminal.

## Examples

```
$ python detect_bias.py "On Tuesday House Speaker Paul Ryan, speaking at the National Association of Manufacturers, reiterated his call for the need for tax reform. Tax reform is urgent because the gap in corporate tax rates between the United States and our competitors is wide and increasing."

NEWS BIAS DETECTOR

Sensationalism issues: 0
Partisanship issues: 2

* Partisan vocabulary is used

Mentioned: tax reform, Tax reform


$ python detect_bias.py "If Republican efforts to repeal and replace Obamacare are successful, one of the biggest winners would be the wealthy. The Senate's bill -- released this week -- differs in key ways from the House-passed version. But proposals eliminate the taxes imposed on high-income Americans to help pay for an expansion of health benefits under the Affordable Care Act. The legislation also would let people contribute more to certain tax-advantaged accounts."

NEWS BIAS DETECTOR

Sensationalism issues: 0
Partisanship issues: 2

* Partisan vocabulary is used

Mentioned: Obamacare, Affordable Care Act
```


## Credits

Based on the JavaScript [joblint](https://github.com/rowanmanning/joblint) project and its Python modification [newslint](https://github.com/Xeus/newslint).
