import re

partisan_phrases = [
   		
		# From https://www.theatlantic.com/politics/archive/2016/07/why-democrats-and-republicans-literally-speak-different-languages/492539/
		
		# Democratic phrases
		'immigrants',
		'undocumented workers',
		'comprehensive health reform',
		'estate taxes',
		'tax breaks for the wealthy',
				
		# Republican phrases
		'radical Islamic terrorism',
		'illegal aliens',
		'Washington takeover of health care',
		'death taxes',
		'tax reform',
		
		# From the 2005 paper "What Drives Media Slant?" by Gentzkow and Shapiro http://faculty.chicagobooth.edu/jesse.shapiro/research/biasmeas.pdf

    # Democratic phrases
		'private accounts',
		'trade agreement',
		'American people',
		'tax breaks',
		'trade deficit',
		'oil companies',
		'credit card',
		'nuclear option',
		'war in Iraq',
		'middle class',
		'President budget',
		'Republican party',
		'change the rules',
		'minimum wage',
		'budget deficit',
		'Republican senators',
		'wildlife refuge',
		'card companies',
		'worker\'s rights',
		'poor people',
		'Republican leader',
		'cut funding',
		'American workers',
		'living in poverty',
		'Senate Republicans',
		'fuel efficiency',
		'national wildlife',
		'veterans health care',
		'congressional black caucus',
		'billion in tax cuts',
		'security trust fund',
		'social security trust',
		'privatize social security',
		'American free trade',
		'central American free',
		'corporation for public broadcasting',
		'additional tax cuts',
		'pay for tax cuts',
		'tax cuts for people',
		'oil and gax companies',
		'prescription drug bill',
		'caliber sniper rifles',
		'increase the minimum wage',
		'system of checks and balances',
		'middle class families',
		'cut health care',
		'civil rights movement',
		'cuts to child support',
		'drilling in the Arctic National',
		'victims of gun violence',
		'solvency of social security',
		'Voting Rights Act',
		'war in Iraq and Afghanistan',
		'civil rights protections',
		'credit card debt',
		'Affordable Care Act',

		# Republican phrases
		'stem cell',
		'natural gas',
		'death tax',
		'illegal aliens',
		'class action',
		'war on terror',
		'embryonic cell',
		'tax relief',
		'illegal immigration',
		'personal account',
		'pass the bill',
		'private property',
		'border security',
		'human life',
		'human embryos',
		'increase taxes',
		'retirement accounts',
		'government spending',
		'national forest',
		'minority leader',
		'urge support',
		'cell lines',
		'cord blood',
		'action lawsuits',
		'economic growth',
		'food program',
		'hate crimes legislation',
		'adult stem cells',
		'oil for food',
		'personal retirement accounts',
		'energy and natural resources',
		'hate crimes law',
		'change hearts and minds',
		'global war on terrorism',
		'death tax repeal',
		'housing and urban affairs',
		'million jobs created',
		'national flood insurance',
		'private property rights',
		'temporary worker program',
		'class action reform',
		'growth and job creation',
		'natural gas',
		'reform social security',
		'Obamacare'
]

def test(self, content, result):
    partisan_mentions = content.contains_any_of(partisan_phrases)
    if (len(partisan_mentions) > 0):
        result.add_warning('Partisan vocabulary is used', partisan_mentions)
        result.add_partisanship_fail_points(len(partisan_mentions))

def define_bias_types(detector):
    detector.add_bias_type({
        'name': 'Partisan Vocabulary',
        'desc': 'Commonly used terms in Republican or Democratic discourse.',
        'test': test
    })
