
nums =[1,2,3,4]
#how something is iteratable  it should have __iter()__
print (dir(nums))
#print (next (nums)) list operator is not a iterator
#i_nums = nums.__iter__() same as below
i_nums = iter(nums)
print (dir(i_nums))

"""
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break
"""
# pratical example is to make class iteratable

class MyRange:
    def __init__(self,start,end):
        self.value =start
        self.end = end

    def __iter__(self):
        return self
    def __next__(self):
        if self.value>= self.end:
            raise StopIteration
        current = self.value
        self.value +=1
        return current

num = MyRange(1, 10)
print(next(num))
print(next(num))
#generators used to createing extremly useful easy to read iterators ,
# look like normal functions but instead of return they yeid the value, keep this value and use agian

def my_range(start):
    current =start
    while True:
        yield current
        current+=1

nums=my_range(1)

for nu in num:
    print(nu)