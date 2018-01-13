def drawTable(array):
	# Print a pretty table that supports Unicode strings
	#     Accepts an array of arrays as rows of columns
	numRows = len(array)
	numCols = len(array[0])
	
	# Iterate through rows to verify the same # of columns / row
	for i in range(0,numRows):
		if len(array[i]) != numCols:
			raise Exception('Each row doesn\'t have the same number\
			 of columns')
	
	# Find column widths and convert contents to str at the same time
	colwidths = [0]*numCols
	for r in range(0,numRows):
		for c in range(0,numCols):
			array[r][c] = unicode(array[r][c])
			
			cellLen = len(array[r][c])
			if cellLen > colwidths[c]:
				colwidths[c] = cellLen
	
	# Return a separator line (like +------+---+ for args [6,3],'-','+'
	#     We make this a function so we can do headers, etc, if we want
	def separatorLine(widths,linechar,cornerchar):
		line = cornerchar
		for n in widths:
			line += linechar*n
			line += cornerchar
		return line + '\n'
	
	
	prettyTable = '' # Here's the start of the table we want to return
	sepLine = separatorLine(colwidths,'-','+') # Here's a separator line
	
	prettyTable += sepLine # First line, rest filled in below
	
	# Fill the data
	for r in range(0,numRows):
		row = '|' # reset the row so we can += again below
		for c in range(0,numCols):
			data = array[r][c] # Data to put in this cell
			padding = ((colwidths[c] - len(data)) / 2)*' ' # Padding
			row += padding
			row += data # add the data
			# Add more padding to end
			row += ' ' * (colwidths[c] - (len(data)+len(padding)))
			row += '|' # Divider
		prettyTable += row + '\n' + sepLine  # Add newest row
	return prettyTable
