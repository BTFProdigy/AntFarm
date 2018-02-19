from tqdm import tqdm


for i in tqdm(range(10000)):
    i


def func(x):
    for i in tqdm(range(x)):
        i


func(100000)


'''
# tqdm supports nested progress bars. Here's an example:
from tqdm import trange
from time import sleep

for i in trange(10, desc='1st loop'):
    for j in trange(5, desc='2nd loop', leave=False):
        for k in trange(100, desc='3nd loop'):
            sleep(0.01)
'''
