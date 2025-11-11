#TimeComplexity

#Linear Search vs Binary Search
#Works on both sorted and unsorted arrays.
#Time complexity is O(n) because, in the worst case, all elements need to be checked.
#Simple and easy to understand, but inefficient for large datasets.
#Binary Search:

#Time complexity is O(log n).
#Can be implemented iteratively or recursively.
#Iterative implementation uses O(1) space as it maintains only a few variables (low, high, mid).
#Recursive implementation requires O(log n) space due to the recursive call stack.
#Requires a sorted array; otherwise, it doesn’t function correctly.

#space complexity

#Space complexity depends on the implementation (iterative vs recursive).
#Iterative binary search requires constant space O(1).
#Recursive binary search requires O(log n) space.
#Linear search requires O(1) space since it only needs a few variables for iteration.


#Sorting Algorithms and Their Time Complexity

#Sorting is prerequisite for binary search, so understanding sorting complexities is essential.
#Several sorting techniques exist: Selection sort, Merge sort, Quick sort, etc


#Selection Sort: Time complexity O(n²) because it iteratively finds the smallest element and places it at the beginning.
#Merge Sort: Time complexity O(n log n), uses divide and conquer strategy.

#LINEAR SEARCH : TIME COMPLEXITY IS O(n)space complexity O(1)
#binary search : Time complexity is O(logn) space complexity:
#iteravive binary O(1)
#recursive binary O(log(n))
#sorting algo:
#selection,merge,quike

#Time complexity analysis often involves formulating and solving recurrence relations.
#Understanding recurrence relations and solving them (via methods like Master’s method and substitution) is key to analyzing algorithm complexities.


#Recurrence Relations and Complexity Analysis
#Algorithms, especially recursive ones, can be expressed using recurrence relations to analyze their complexity.
#Master’s theorem and substitution method are common techniques to solve recurrence relations and find time complexity.
#Proper understanding of these mathematical tools is important for mastering algorithm analysis.


#Arrays allow direct indexing which enables efficient binary search.
#Linked lists do not support indexing since nodes are scattered in memory and connected via pointers, making binary search inefficient or impractical on linked lists.
#Choice of data structure affects the complexity and feasibility of algorithms.



