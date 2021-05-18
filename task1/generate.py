import numpy as np

count = 2 * 1024**3 // 4 # how many 32bit integers in 2 GB
max_value = np.iinfo(np.uint32).max
file_name = f'{os.path.dirname(os.path.realpath(__file__))}/numbers.txt'

def generate(count, file_name):
    ary = np.random.randint(2, max_value, size = count, dtype = np.dtype('uint32').newbyteorder('B')).byteswap()

    with open(file_name, 'wb') as file:
        file.write(ary.data)

generate(count, file_name)
