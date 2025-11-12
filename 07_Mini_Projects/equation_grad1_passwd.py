
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

def access_level():
	level = password()
	if level:
		print('Welcome to level 2 !')
		print('--------------------------------')
		main()

	else:
		print('\nAccess denied, try later!')

''' We solve equation ax + b = c '''

def solve_equation(a,b,c):
	if a == 0:
		return None
	return (c-b)/a

def format_number(n):
	return str(int(n)) if n.is_integer() else f'{n:.2f}'

def main():
	print('Solve equation ax + b = c')
	print('-----------------------------------')

	while True:
		try:
			a = float(input('insert the value of a:'))
			b = float(input('insert the value of b:'))
			c = float(input('insert the value of c:'))

			x = solve_equation(a,b,c)

			if x == None:
				print('a can\'t be zero !')
				continue

			sign = '+' if b > 0 else '-'

			print(f'your equation is: {format_number(a)}x{sign}{format_number(abs(b))} = {format_number(c)}')

			if x.is_integer():
				print(f'x={int(x)}')
			else:
				print(f'x={x:.2f}')
		except ValueError:
			print('Insert only numbers not letters !')
if __name__ == '__main__':
	access_level()



