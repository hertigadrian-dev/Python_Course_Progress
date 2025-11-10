def solve_equation(a,b,c):
    """ we solve the equation ax+b=c and return the value of x """

    if a==0:
        return None
    return (c-b)/a


def format_number(n):
    return str(int(n)) if n.is_integer() else f"{n:.2f}"


def main():

    print('Solve the next equation ax+b=c')


    while True:
        try:

            a=float(input('insert a:'))
            b=float(input('insert b:'))
            c=float(input('insert c:'))

            x=solve_equation(a,b,c)

            if x is None:
                print('a can\'t be zero!')
                continue

            sign = '+' if b>=0 else '-'
            print(f'Your ecuation is: {format_number(a)}x{sign}{format_number(abs(b))}={format_number(c)}')


            if x.is_integer():
                print(f'x={int(x)}')
            else:
                print(f'x={x:.2f}')
            break


        except ValueError:
            print('Insert only numbers!')

if __name__ == '__main__':
    main()
