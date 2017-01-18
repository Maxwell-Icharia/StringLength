def string_length(d):
	if (isinstance(d, (list))) & (len(d) > 1):
		for x in d:
  			return [len(x[0:-1])]
  	elif len(d) >= 1:
  		return [len(d)]
  	else:
  		return 'Invalid input'