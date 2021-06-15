# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:35:03 2021

@author: alpha
"""


# import the sorting package from library
from algovis import sorting
# importing random module to shuffle the list
import random
# GUI lib
import tkinter
import tkinter.font as font

def getdata():
    # Making a list of 100 integers from 1-100
    # using list comprehension
    my_list = [i+1 for i in range(100)]
    
    # shuffling the list
    random.shuffle(my_list)
    
    return(my_list)


def BubbleSort():
    my_list=getdata()
    # making a BubbleSort class object by passing the shuffled list
    Sort_object = sorting.BubbleSort(my_list)
    # calling the visualize method
    Sort_object.visualize(interval= 100)
def InsertionSort():
    my_list=getdata()
    # making a BubbleSort class object by passing the shuffled list
    Sort_object = sorting.InsertionSort(my_list)
    # calling the visualize method
    Sort_object.visualize(interval= 100)
def SelectionSort():
    my_list=getdata()
    # making a BubbleSort class object by passing the shuffled list
    Sort_object = sorting.SelectionSort(my_list)
    # calling the visualize method
    Sort_object.visualize(interval= 100)
def MergeSort():
    my_list=getdata()
    # making a BubbleSort class object by passing the shuffled list
    Sort_object = sorting.MergeSort(my_list)
    # calling the visualize method
    Sort_object.visualize(interval= 100)
def QuickSort():
    my_list=getdata()
    # making a BubbleSort class object by passing the shuffled list
    Sort_object = sorting.QuickSort(my_list)
    # calling the visualize method
    Sort_object.visualize(interval= 100)





window = tkinter.Tk()

myFont = font.Font(size=30)

BubbleSort = tkinter.Button(window,font=myFont, text ="BubbleSort", command = BubbleSort)
InsertionSort = tkinter.Button(window,font=myFont, text ="InsertionSort", command = InsertionSort)
SelectionSort = tkinter.Button(window,font=myFont, text ="SelectionSort", command = SelectionSort)
MergeSort = tkinter.Button(window,font=myFont, text ="MergeSort", command = MergeSort)
QuickSort = tkinter.Button(window,font=myFont, text ="QuickSort", command = QuickSort)

BubbleSort.grid(column=1,row=1)
BubbleSort.config( height = 5, width = 10)
InsertionSort.grid(column=2,row=1)
InsertionSort.config( height = 5, width = 10)
SelectionSort.grid(column=3,row=1)
SelectionSort.config( height = 5, width = 10)
MergeSort.grid(column=1,row=2)
MergeSort.config( height = 5, width = 10)
QuickSort.grid(column=2,row=2)
QuickSort.config( height = 5, width = 10)


window.mainloop()





