def selectSort(arr:list):
    for i in range(len(arr)-1):


        for index in range(len(arr)-1):

            if arr[index]> arr[index+1]:

                min=arr[index+1]
                temp=arr[index]
                arr[index]=min
                arr[index+1]=temp
            else:
                pass
    print(arr)





selectSort([5,3,4,1,2])
