lst = [1,2,3]
#if you have 1 million number you need a lot of hardware
def mygen():
    for num in range(14):
        yield num**num

# for big_num in mygen():
#     print(big_num)

nums = list(mygen())    
