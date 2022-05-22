def add(datatype,*args):
    if datatype=='int':
        answer=0

    if datatype=='str':
        answer=''

    for item in args:
        answer+=item
    print(answer)



add('int',9,5)
add('str','hi  ','world')