
def diff(code: str, user_input: str):
	
	correct = ""
	find    = ""

	for i in range(len(code)):
		if code[i] == user_input[i]: correct += code[i]
		if code[i] in user_input and code[i] != user_input[i]: find += code[i]

	return len(correct), len(find)




if __name__ == "__main__":
	
	for k in range(0, 1000):
		user_input = str(k).zfill(3)

		if diff("682", user_input) == (1, 0) and \
		   diff("614", user_input) == (0, 1) and \
		   diff("206", user_input) == (0, 2) and \
		   diff("738", user_input) == (0, 0) and \
		   diff("380", user_input) == (0, 1):
		   print(user_input)

	