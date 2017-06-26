import re

class Content(object):

    content = ''

    def __init__(self, content):
        self.content = content.encode('ascii', 'ignore')
        
    def contains_any_of(self, phrases):
        return filter(
            lambda x: len(x) != 0 or x == '',
            flatten(
                map(
                    lambda x:
                        re.findall(prepare_phrase(x), self.content),
                        phrases
                )
            )
        )

def prepare_phrase(phrase):
    return phrase if isinstance(phrase, re._pattern_type) else re.compile('\\b' + phrase + '\\b', re.I)
    
def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)

def create(content):
    return Content(content)

