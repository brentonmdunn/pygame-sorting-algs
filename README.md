# Visualizing Sorting Algorithms
Data is always nice to work with when it is nice and orderly. Sorting algorithms are used to organize data. These two programs use pygame to visualize the insertion sort and selection sort algorithms respectively. Each column is a class in a list. A sorting algorithm organizes it and it is displayed on the screen.

## Insertion Sort
Insertion sort is a sorting algorithm where elements are sorted into two groups—sorted and unsorted. Elements in the unsorted group is organized within the sorted group. <br/><br/>
The unsorted elements are in white, and the sorted elements are in yellow. The cursor (orange) starts at the first unsorted element. It then traverses the list backwards until it finds a spot where the element to the left of it is shorter than the orange element and taller on the right side.<br/>
![](images/insertion_sort.GIF)

## Selection Sort 
Selection sort is a sorting algorithm that repeatedly finds the smallest element and swaps it with the next unsorted element. <br/><br/>
The unsorted elements are in white, and the sorted elements are in yellow. The cursor (orange) goes through all the unsorted columns. When the cursor finds the shortest element, it highlights it in green. Once the cursor reaches the end, the program swaps the next unsorted element and the green element. <br/>
![](images/selection_sort.GIF)


