gcd(X, 0, X) :- X > 0.
gcd(X, Y, GCD) :-
    Y > 0,
    R is X mod Y,
    gcd(Y, R, GCD).

lcm(A, B, LCM) :-
    gcd(A, B, GCD),
    Product is A * B,
    LCM is Product // GCD.
