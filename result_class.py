import math

class Result(object):

    def __init__(self):
        self.mentions = []
        self.warnings = []
        self.fail_points = dict({
            'sensationalism': 0,
            'partisanship': 0
        })

    def set_current_bias_type(self, bias_type):
        self.current_bias_type = bias_type

    def clear_current_bias_type(self):
        del self.current_bias_type

    def _add_mentions(self, mentions):
        self.mentions += mentions
        self.mentions = list(set(self.mentions))

    def _add_message(self, type_cat, msg, evidence):
        self.add_mentions(evidence)
        new_msg = {
            'message': msg,
            'detail': self.current_bias_type['desc'] if self.current_bias_type != None else '',
            'evidence': ', '.join(set(evidence)) if evidence != None else []
        }

        if type_cat == 'warnings':
            self.warnings.append(new_msg)

    def add_mentions(self, mentions):
        self._add_mentions(mentions)

    def add_warning(self, msg, evidence):
        self._add_message('warnings', msg, evidence)

    def _add_fail_points(self, type_cat, amount):
        self.fail_points[type_cat] += math.ceil(1 if amount is None else amount)

    def add_sensationalism_fail_points(self, amount):
        self.fail_points['sensationalism'] += math.ceil(1 if amount is None else amount)

    def add_partisanship_fail_points(self, amount):
        self.fail_points['partisanship'] += math.ceil(1 if amount is None else amount)

    def has_messages(self):
        return (len(self.warnings) > 0)

    def has_fail_points(self):
        return (
            self.fail_points['sensationalism'] > 0 or
            self.fail_points['partisanship'] > 0
        )

    def is_clean(self):
        return (
            not self.has_messages() and
            not self.has_fail_points()
        )

def create():
    return Result()
