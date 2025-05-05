% Smallest of two numbers
min_of_two(X, Y, X) :- X =< Y.
min_of_two(X, Y, Y) :- Y < X.

% Smallest of three numbers
min_of_three(X, Y, Z, Min) :-
    min_of_two(X, Y, MinXY),
    min_of_two(MinXY, Z, Min).
