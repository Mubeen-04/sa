% Predicate to check if a number is prime
is_prime(2).  % Base case: 2 is prime
is_prime(N) :-
    N > 2,
    \+ has_factor(N, 2).

% Helper predicate to check if N has a factor
has_factor(N, F) :-
    F * F =< N,  % Only check up to sqrt(N)
    N mod F =:= 0.
has_factor(N, F) :-
    F * F =< N,
    F2 is F + 1,
    has_factor(N, F2).
