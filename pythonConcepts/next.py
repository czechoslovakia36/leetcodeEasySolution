#  next(iterable, default) 
#  default: optional , an default value to return if interation 
# reaches the end

listExample=[2,3,4,5,6]
listExample=iter(listExample)

'''print(type(listExample))
print(dir(list)) '''


while(True):
    next_val=next(listExample,'end')
    
    if next_val=='end':
        break
    else:
        print(next_val)
