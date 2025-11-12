
def password():
	passwd = 'lol123'
	tries = 0

	while tries < 3:
		ques = input('insert your password:')
		if ques != passwd:
			print('password wrong!')
			tries += 1
		else:
			print('Welcome!')
			return True
	else:
		print('your tries are up!')
		return False
password()
