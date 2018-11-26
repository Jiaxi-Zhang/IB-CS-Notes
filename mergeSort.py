import random

def mergeSort(arr):

    if len(arr) > 1:
        half = len(arr)//2
        leftHalf = arr[:half]
        rightHalf = arr[half:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1
    
        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1
    
        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1

list1 = [random.randint(0,1000) for i in range(100)]
print("== Before sorting == " + ",".join(map(str,list1)))
mergeSort(list1)
print("== After sorting == " + ",".join(map(str,list1)))
