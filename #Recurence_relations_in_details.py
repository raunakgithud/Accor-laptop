#Recurence_relations_in_details

print('Recurence_relations_in_details')

#8902497302
#
#A recurrence relation is a mathematical equation that expresses a term of a sequence or function in terms of its previous terms. In computer science, recurrence relations are used to describe the time complexity of recursive algorithms by defining the time needed to solve a problem of size ( n ) based on the time to solve smaller subproblems.
#
#In a general form, a recurrence relation can be written as:
#
#[ T(n) = f(T(n-1), T(n-2), ..., T(n-k)) + g(n) ]
#
#where ( T(n) ) depends on the previous terms and possibly some function of ( n ).
#
#Example:
#
#Arithmetic Progression: ( a_n = a_{n-1} + d )
#Geometric Progression: ( a_n = r \times a_{n-1} )
#Fibonacci sequence: ( F_n = F_{n-1} + F_{n-2} )
#Factorial: ( n! = n \times (n-1)! )
#These recurrence relations also represent dependencies between terms similarly to dependencies in recursive algorithms.
#
#Recurrence relations can be categorized based on their structure:
#
#Linear Recurrence Relation: Each term is a linear combination of previous terms.
#
#Example: ( T(n) = 2T(n-1) + 3T(n-2) )
#Homogeneous Recurrence Relation: These relations do not include additional functions of ( n ) (like constants or expressions involving ( n )). They rely solely on previous terms.
#
#Example: ( T(n) = 3T(n-1) - 2T(n-2) )
#Non-Homogeneous Recurrence Relation: These include extra terms such as constants or functions of ( n ).
#
#Example: ( T(n) = 2T(n-1) + n )

#Recurrence relations often arise from recursive algorithms, where the time complexity ( T(n) ) depends on the time for solving smaller input sizes. For example, in divide and conquer algorithms like Merge Sort or Binary Search, the recurrence relation helps express the time complexity precisely.
#
#Binary Search recurrence might look like:
#
#[ T(n) = T(\frac{n}{2}) + c ]
#
#Merge Sort recurrence:
#
#[ T(n) = 2T(\frac{n}{2}) + cn ]
#
#Solving these recurrences provides a mathematical way to evaluate time complexity, offering precise asymptotic behavior rather than rough estimates.
#
#While you can estimate time complexity by counting lines of code or loops, recurrence relations give an exact framework, especially for recursive algorithms

