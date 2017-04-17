# 1.2.1 Use the enumerate function in loops instead of creating an
# ``index''
# variable

my_container = ['Larry', 'Moe', 'Jacl']
for index, element in enumerate(my_container):
    print ('{} {}'.format(index, element))


def main():
    print('hello')
