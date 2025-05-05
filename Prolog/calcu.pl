% Addition
add(X, Y, Z) :- Z is X + Y.

% Subtraction
subtract(X, Y, Z) :- Z is X - Y.

% Multiplication
multiply(X, Y, Z) :- Z is X * Y.

% Division
divide(X, Y, Z) :-
    Y \= 0,
    Z is X / Y.