#Recurence_relations
#if f(n) = O(n^a)
#time complexity is atleast n^a
# i.e. f(n) = 6n^2 + 2n + 3 the the governing factor g(n) = @(n^2)
#when a function calls itself under some argument values that is
#called recurtion

#Big O Notation (O): Describes an upper bound on time complexity. If f(n) = O(n^a), it means the time complexity of the function is at most proportional to n^a.
#Big Omega Notation (Ω): Describes a lower bound. If f(n) = Ω(n^a), it means the time complexity is at least proportional to n^a
#Theta Notation (Θ): Describes a tight bound. If f(n) = Θ(n^a), time complexity is exactly proportional to n^a (both upper and lower bounded).

#// Algorithm A: Time complexity 3n^2 + 6n + 114
#// Algorithm B: Time complexity n^2 + n
#// Both have governing term n^2, so both are Θ(n^2)
#Recurrence relations are mathematical equations defining sequences recursively, especially useful in analyzing recursive algorithms.

#They express the time complexity T(n) in terms of smaller input sizes, for example T(n) = T(n/2) + c.

#Because recursive definitions produce infinitely many equations (for each valid n), solving the general form is essential.

# Substitution method for solving recurences
#The substitution method involves repeatedly expanding the recurrence by substituting the right-hand side until the base condition is reached.

#You observe the pattern from the expansions, then use it to find the closed-form or the asymptotic time complexity.
#The substitution method involves repeatedly expanding the recurrence by substituting the right-hand side until the base condition is reached.

#You observe the pattern from the expansions, then use it to find the closed-form or the asymptotic time complexity.
#T(n) = T(n/2) + c,  T(1) = 1
#
#Expansion:
#T(n) = T(n/2) + c
#     = T(n/4) + c + c
#     = T(n/8) + c + c + c
#     ...
#After k expansions: T(n) = T(n / 2^k) + k*c
#
#Base condition reached when n / 2^k = 1  =>  k = log_2 n
#
#Therefore,
#T(n) = T(1) + c * log n = 1 + c*log n = Θ(log n)




