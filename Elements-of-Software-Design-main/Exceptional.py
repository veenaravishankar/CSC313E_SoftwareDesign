
def isfloat(value):
    try:
        #print(float(value))
        float(value)
        return True
    except ValueError as exec:
        print(value, exec)
        return False
    except SyntaxError as se:
        print(se)
    except ZeroDivisionError as zd:
        print(zd)
    #finally:
     #   print('processed all the input')

print('enter your series of input')
my_list = input().split()

for num in my_list:
    if isfloat(num):
        print(num)


#print('enter inputs')
#inp = input()
#print(float(inp))