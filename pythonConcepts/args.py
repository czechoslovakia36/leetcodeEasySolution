def sum(*values):
    result=0
    len1=len(values)
    i=0

    while(i<len1):
        result=result+values[i]
        i=i+1
    return result


print(sum(1,2,3))