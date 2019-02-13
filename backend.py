ops = {
	'+': 5,
	'-': 4,
	'*': 3,
	'/': 2
}

def solve(nums):
	
	# Array initialization
	nums = [int(num) for num in nums]
	nums.sort(reverse = True)
	expr = str(nums.pop(0))
	
	# First done is for putting A(B@C) parentheses
	first_done = False
	
	for num in nums:
		max_local_pts = -1e9
		local_expr = expr
		
		# Last number position for 3rd parentheses expression type
		if not first_done:
			last_num_pos = 0
		elif expr[-2] in ops:
			last_num_pos = -1
		else:
			last_num_pos = -2
		
		for op, score in ops.items():
			exprs = [
				# AB@C
				expr + op + str(num),
				#(AB)@C
				'(' + expr + ')' + op + str(num),
				# A(B@C)
				expr[:last_num_pos] + '(' + expr[last_num_pos:] + op + str(num) + ')'
			]
			for i in range(2):
				try:
					# Absolute difference to 24 is multiplied by 10, as the main focus is on getting 24 first
					local_pts = score - 10 * abs(24 - eval(exprs[i])) - min(i, 1)
					if local_pts > max_local_pts:
						local_expr = exprs[i]
						max_local_pts = local_pts
				except ZeroDivisionError:
					pass
		
		expr = local_expr
		first_done = True
	
	return expr
