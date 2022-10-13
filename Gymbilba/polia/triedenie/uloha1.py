from tkinter import *
from random import randint

arr = [randint(1,100) for i in range(100)]
arr1 = arr

root = Tk()
root.geometry("1000x400")

canvas=Canvas(root, width=1000, height=400)
canvas.pack()

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i + 1] < arr[i]: arr[i], arr[i+1] = arr[i+1], arr[i]
        canvas.delete("all")
        for e in range(len(arr)):
            canvas.create_line(e*10,0,e*10,arr[e] * 4, fill="green", width=10)
        canvas.update()
    return arr
    
bubble_sort(arr)
    
def quick_sort(array):
    pivot = randint(0, len(arr1) - 1)
    array = bubble_sort(array[0:pivot]) + bubble_sort(array[pivot:])
    
quick_sort(arr1)

root.mainloop()