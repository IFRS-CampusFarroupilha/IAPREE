'''
A collection of functions

'''

def inject(base, module) -> None:
	"""Injects a module in the main model

	function(base, module) -> None
	"""
	for i in module:
		base.append(i)