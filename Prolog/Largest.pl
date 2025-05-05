% Maximum of two numbers
max_of_two(X, Y, X) :- X >= Y.
max_of_two(X, Y, Y) :- Y > X.

% Maximum of three numbers
max_of_three(X, Y, Z, Max) :-
    max_of_two(X, Y, MaxXY),
    max_of_two(MaxXY, Z, Max).
