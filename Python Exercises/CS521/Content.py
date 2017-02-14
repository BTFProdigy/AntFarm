my_global_var = 3

def math_example(x=3):
    return 3*x + my_global_var if x % 2 else x // 2

my_str = "This is an example of {}"
my_new_string = my_str.format('formatting')

my_string = "This is the %dnd example of %s" % (2, 'formmating')

def args_example(*args):
    for arg in args:
        print("another arg {} in the arg list".format(arg))

split_string = my_string.split()


for item in split_string:
    print(item)

for index in range(4,len(split_string)):
    print(index)

if __name__ == '__main__':

    with open('demo.txt', 'w') as f:

        for num in range(5):
            f.write(str(num) + '\r')


    with open('demo.txt') as f:

        x = f.readline()
        print(x)
        print(math_example(int(x)))

