def get_number(exponent, mantissa):
    return mantissa + 10**exponent
 
 
# not distributed
# a x ( b + c )
def not_dist(a, b, c):
    return a * (b + c)
 
 
# distributed
# a x b + a x c
def dist(a, b, c):
    return a * b + a * c
 
 
def main():
    mant_a = 0.200
    exp_a = 1
    mant_b = -0.600
    exp_b = 0
    mant_c = 0.602
    exp_c = 0
    a = get_number(exp_a, mant_a)
    b = get_number(exp_b, mant_b)
    c = get_number(exp_c, mant_c)
 
    print("Distributed: {0}".format(dist(a, b, c)))
    print("Not Distributed: {0}".format(not_dist(a, b, c)))
 
if __name__ == '__main__':
    main()
