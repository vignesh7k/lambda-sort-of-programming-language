language_history = [
	{'language': 'Python', 'first_release': 1991},
	{'language': 'C', 	   'first_release': 1972},
	{'language': 'Java',   'first_release': 1995},
	{'language': 'C++',    'first_release': 1985},
	{'language': 'Go',     'first_release': 2009},
]

language_history.sort(reverse=False, key=lambda x: x['first_release']) 

for language_history in language_history:
    print(language_history)
	
# ['C', 'C++', 'Python', 'Java', 'Go']








