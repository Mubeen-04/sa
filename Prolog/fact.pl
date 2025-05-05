factorial(0, 1).  % Base case: factorial of 0 is 1
factorial(N, F) :-
    N > 0,
    N1 is N - 1,         % Decrement N
    factorial(N1, F1),   % Recursively calculate factorial of N-1
    F is N * F1.         % Multiply N with the result of N-1 factorial
