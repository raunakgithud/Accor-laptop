#Asymptotic_Notations

# f(n) = o.g(n)
# after n0 some value of n where g(n) >= f(n)

#An algorithm is a finite sequence of well-defined instructions required to solve a given computational problem. It can be thought of like a recipe that tells you step by step what to do to reach a desired output.
#
#Two essential properties of an Algorithm:
#
#It must have a finite number of steps.
#It must terminate in finite time, meaning it should not run forever without producing an output.
#If both these conditions are satisfied, the sequence of steps can be called an algorithm.
#
#Example:
#
#A simple algorithm to find the sum of two numbers:
#
## Algorithm to add two numbers a and b
#1. Take inputs a and b
#2. Compute sum = a + b
#3. Output sum

#Why do we need efficient algorithms despite very fast processors?
#
#Even with super-fast computers (like GPUs, quantum computers), the speed alone cannot solve highly complex problems quickly if the algorithm is inefficient.
#For example, sorting 10 million numbers using different algorithms varies drastically in performance:
#Using Selection Sort (inefficient): might take hours.
#Using Merge Sort (efficient): might take seconds.
#In real-life critical applications (like aircraft control systems), timely output generation is crucial for safety and reliability.
#
#Hence, efficiency in algorithms—measured in terms of time and space complexity—is vital.

#Time Complexity refers to the amount of time an algorithm takes to produce an output as a function of the size of the input.
#
#Space Complexity refers to the amount of memory or space an algorithm requires during its execution based on the input size.
#
#These complexities help measure the efficiency of an algorithm, independent of the hardware it's run on.
#
#Assumption: The time taken for each basic operation (addition, multiplication, assignment) is constant.
#
#Example:
#
#Simple addition operation:
#x = n + 1
#return x
## time complexity is O(1) as only a constant number of operations are performed
#Loop running n times:
#for i in range(n):
#    y = y + n
## time complexity is O(n) since the operation inside the loop runs n times


#As input size grows, exact time measurements are less meaningful. Instead, we analyze the growth rate of the time complexity using Asymptotic Notations. These notations describe the upper bound, lower bound, or tight bound of an algorithm's time/computational complexity.
#
#The main asymptotic notations are:
#
#Big O notation (O): Upper bound
#Big Omega notation (Ω): Lower bound
#Big Theta notation (Θ): Tight bound (both upper and lower)
#Each notation compares two functions f(n) and g(n) representing time complexities.

#Big O notation, denoted O(g(n)), describes an upper bound on the growth of the function f(n). It means the function f(n) grows at most as fast as g(n) multiplied by a positive constant for sufficiently large n.
#
#Mathematical Definition:
#
#f(n) = O(g(n)) if there exist positive constants c and n₀ such that:
#
#f(n) ≤ c * g(n) for all n ≥ n₀
#
#Intuition: f(n) does not grow faster than g(n) beyond some threshold.
#
#Example 1:
#
#20n² = O(n²) because 20n² ≤ 20 * n² for all n ≥ 1
#
#Example 2:
#
#100n + 60 = O(n²) because for large n (e.g., n ≥ 160), 100n + 60 ≤ n²
#
#Example in Python:
#
#def example_linear(n):
#    # Runs in O(n) time
#    total = 0
#    for i in range(n):
#        total += i
#    return total

#Big Omega notation, denoted Ω(g(n)), describes a lower bound on the growth of the function f(n). It means the function f(n) grows at least as fast as g(n) multiplied by some positive constant for sufficiently large n.
#
#Mathematical Definition:
#
#f(n) = Ω(g(n)) if there exist positive constants c and n₀ such that:
#
#f(n) ≥ c * g(n) for all n ≥ n₀
#
#Intuition: f(n) grows at least as fast as g(n) beyond some threshold.
#
#Example:
#
#20n² = Ω(n²) because 20n² ≥ 1 * n² for all n ≥ 1
#
#Python Example:
#
#def example_at_least_n_square(n):
#    # Hypothetical function that takes at least n² time
#    for i in range(n):
#        for j in range(n):
#            pass

#Big Theta notation, denoted Θ(g(n)), means f(n) is bounded both above and below by g(n) multiplied by positive constants.
#
#Mathematical Definition:
#
#f(n) = Θ(g(n)) if there exist positive constants c1, c2 and n₀ such that:
#
#c1 * g(n) ≤ f(n) ≤ c2 * g(n) for all n ≥ n₀
#
#Intuition: f(n) grows at the same rate as g(n) beyond some threshold.
#
#Example:
#
#f(n) = 4n³ + 6n² is Θ(n³) because the dominant term n³ governs the growth.
#
#Illustrating with Python:
#
#def example_theta_n3(n):
#    # Double nested loop with some additional computation
#    total = 0
#    for i in range(n):
#        for j in range(n):
#            total += i * j
#    return total

#The governing term or dominant term in a function is the term that grows the fastest as n becomes very large and therefore dictates the asymptotic complexity.
#
#When comparing time complexities, only the highest-order term is considered, and constants or lower-order terms are ignored.
#
#Example:
#
#For f(n) = 3n² + 6n + 148, the governing term is n² because as n grows large, n² dominates n and constants.
#
#Thus, f(n) = Θ(n²).
#
#Example code:
#
## Suppose this function takes time 3n² + 6n + 148
## For large n, time ~ 3n²
#
#def function_example(n):
#    for i in range(n):
#        for j in range(n):
#            pass  # inner loop runs n times
#    for k in range(6 * n + 148):
#        pass  # additional operations which are less significant as n grows
#The complexity is dominated by the nested loop giving Θ(n²).

#When comparing algorithms, the main criterion is the order of their governing term in time complexity.
#
#Algorithms with smaller governing term powers are considered more efficient as input size grows.
#Constant factors and lower order terms don't affect the asymptotic complexity class.
#Example:
#
#Consider three algorithms with time complexities:
#
#f1(n) = 2n
#f2(n) = 4n + 10
#f3(n) = 100n + 20
#All have governing term n, so all are Θ(n).
#
#Hence, none of these algorithms is asymptotically better than the others despite different constant factors.
#
#If an algorithm A has time complexity Θ(n) and algorithm B has Θ(n²), A is asymptotically better than B as it grows slower as n increases.




