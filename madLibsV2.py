''' Mahmud Hasan
    madLibs v2 '''

import random

names = ['Jack', 'Kate', 'Mom', 'Dad', 'Bubby', 'Steven']
places = ['attic', 'basement', 'bathroom', 'bedroom', 'closet', 'room', 'yard', 'hallway']
things = ['bed', 'stove', 'computer', 'dresser', 'sink', 'sofa', 'telephone', 'toilet']
animals = ['bat', 'gorrilla', 'cat', ' monkey', 'dog', 'bird']
adjective = ['smart', 'cool', 'hot', 'nice', 'pink', 'white', 'powdery']
adverb = ['slowly', 'quickly', 'noisily', 'rudely', 'silently', 'smoothly']
presVerb = ['run', 'swim', 'eat', 'jump','watch', 'bake', 'crack', 'place']
pastVerb = ['ran', 'swam', 'ate', 'jumped', 'watched', 'baked', 'cracked', 'placed']

def fillBlanks(story):
	i = 0
	story = story.split()
	for word in story:
		# replaces with a random name
		if word[:6] == '<NAME>':
			story[story.index(word)] = str(names[random.randrange(len(names))]) + word[6:len(word)]
		# replaces with a random place
		elif word[:7] == '<PLACE>':
			story[story.index(word)] = str(places[random.randrange(len(verb))]) + word[7:len(word)]
		# replaces with a random thing
		elif word[:7] == '<THING>':
			story[story.index(word)] = str(things[random.randrange(len(things))]) + word[7:len(word)]
		# replaces with a random animal
		elif word[:8] == '<ANIMAL>':
			story[story.index(word)] = str(animals[random.randrange(len(animals))]) + word[8:len(word)]
		# replaces with a random past tense verb
		elif word[:11] == '<PAST-VERB>':
			story[story.index(word)] = str(pastVerb[random.randrange(len(pastVerb))]) + word[11:len(word)]
		# replaces with a random present tense verb
		elif word[:11] == '<PRES-VERB>':
			story[story.index(word)] = str(presVerb[random.randrange(len(presVerb))]) + word[11:len(word)]
		# replaces with a random adverb
		elif word[:8] == '<ADVERB>':
			story[story.index(word)] = str(adverb[random.randrange(len(adverb))]) + word[8:len(word)]
		# replaces with a random adjective
		elif word == '<ADJECTIVE>':
			story[story.index(word)] = str(adjective[random.randrange(len(adjective))])
		
		if (story[i-1])[-1] in '?.!':
			story[i] = (story[i]).capitalize()
		i += 1
	
	story = ' '.join(story)
	print story

fillBlanks("Today, <NAME> and I <PAST-VERB> a <THING> for my <NAME>'s brithday. \
	We <ADVERB> <PAST-VERB> an egg into a <ADJECTIVE> <THING>. \
	We <ADVERB> <PAST-VERB> and add them to the <THING>. \
	<ADJECTIVE> <THING> <PRES-VERB> <THING> while we <PRES-VERB> it.")
