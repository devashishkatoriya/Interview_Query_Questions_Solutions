

def calculate(num1, num2, op):
	if op == '+':
		return num1 + num2
	if op == '-':
		return num1 - num2
	if op == '*':
		return num1 * num2
	if op == '/':
		return float(num1 / num2)


def change_op(op):
	if op == '+':
		return '-'
	if op == '-':
		return '+'
	if op == '*':
		return '/'
	if op == '/':
		return '*'

def find_digit_x(strParam):

	terms = strParam.split(' ')
	term1 = terms[0]
	term2 = terms[2]
	term3 = terms[4]
	op1 = terms[1]

	if 'x' in term1:
		RHS = calculate(int(term3), int(term2), change_op(op1))
		LHS = int(term1.replace('x', '0'))
		return RHS - LHS

	if 'x' in term2:
		RHS = calculate(int(term1), int(term3), op1)
		LHS = int(term2.replace('x', '0'))
		return RHS - LHS

	if 'x' in term3:
		RHS = calculate(int(term1), int(term2), op1)
		LHS = int(term3.replace('x', '0'))
		return RHS - LHS


print(find_digit_x("110 / 1x = 10"))
