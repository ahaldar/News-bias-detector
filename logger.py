import math

def report(result, opts):
    print('\nNEWS BIAS DETECTOR\n')
    if (result.is_clean()):
    		print('No issues found with the content!')
    if (result.has_fail_points()):
				log_fails(result.fail_points)
    print
    if (result.has_messages()):
    		for msg in result.warnings:
        		log_message('warning', 'yellow', opts['verbose'], msg)
    print
    mentions = []
    for msg in result.warnings:
        mentions.append(msg['evidence'])
    mentions = filter(len, mentions)
    log_mentions(set(mentions))

def log_fails(points):
		data_set = [
		    {'label': 'Sensationalism', 'value': points['sensationalism']},
		    {'label': 'Partisanship', 'value': points['partisanship']}
		]
	 
		for datum in data_set:
				print(datum['label'] + ' issues: ' + str(int(datum['value'])))

def log_mentions(mentions):
    if len(mentions) > 0:
        print('Mentioned: ' + ', '.join(mentions))
        print

def log_message(type_cat, color, verbose, message):
    print('* ' + message['message'])
    if (verbose):
        print(message['detail'])
