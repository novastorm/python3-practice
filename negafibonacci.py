'''
Fibonacci with negative numbers

Closed expression for the Fibonacci series that uses integer arithmetic.

fib = lambda n:pow(2<<n,n+1,(4<<2*n)-(2<<n)-1)%(2<<n)

>> fib(1000)
4346655768693745643568852767504062580256466051737178
0402481729089536555417949051890403879840079255169295
9225930803226347752096896232398733224711616429964409
06533187938298969649928516003704476137795166849228875L

It computes the result in O(log n) arithmetic operations, each acting on
integers with O(n) bits. Given that the result (the nth Fibonacci number) is 
O(n) bits, the method is quite reasonable.

It's based on genefib4 from http://fare.tunes.org/files/fun/fibonacci.lisp, 
which in turn was based on an a less efficient closed-form integer expression 
of Paul Hankin (see: http://paulhankin.github.io/Fibonacci/).
'''

from math import sqrt

def fib(n):
    """Calculates the nth Fibonacci number"""

    sign = 1
    if n < 0:
        sign = -1
        n *= -1

    e = ((n & 1) + 1) & 1
    sign = pow(sign, e)


    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a * sign  


    # goldenRatio = (1 + sqrt(5)) / 2
    # return int( goldenRatio ** n / sqrt(5) + 0.5)


    r = pow(2<<n, n+1, (4<<2*n)-(2<<n)-1) % (2<<n)
    # print("r: ", r)
    return sign * r


# print(fib(6))
# print(fib(-6))
# print(fib(-96))
# print(fib(1000))
print(fib(1386936))