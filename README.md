# Visualizing Sorting Algorithms
Data is always nice to work with when it is neat and orderly; however, raw data is not usually in order. Sorting algorithms are used to organize data so that you do not need to do it yourself. These two programs use pygame to visualize the insertion sort and selection sort algorithms. Each column is a class in a list. A sorting algorithm organizes it and it is displayed on the screen.

## Insertion Sort
Insertion sort is a sorting algorithm where elements are sorted into two groups—sorted and unsorted. Elements in the unsorted group is organized within the sorted group. <br/><br/>
The unsorted elements are in white, and the sorted elements are in yellow. The cursor (orange) starts at the first unsorted element. It then traverses the list backwards until it finds a spot where the element to the left of it is shorterand the element on the right is taller.<br/>
![](images/insertion_sort.GIF)

## Selection Sort 
Selection sort is a sorting algorithm where elements are sorted into two groups—sorted and unsorted. The cursor repeatedly finds the smallest element within the unsorted elements and swaps it with the unsorted element immediatly to the right of the sorted group. <br/><br/>
The unsorted elements are in white, and the sorted elements are in yellow. The cursor (orange) goes through all the unsorted columns. When the cursor finds the shortest element, it highlights it in green. Once the cursor reaches the end, the program swaps the next unsorted element and the green element. <br/>
![](images/selection_sort.GIF)


