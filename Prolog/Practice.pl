gcd(X,0,X) :-  X>0.
gcd(X,Y,GCD) :-
    Y > 0,
    R is X mod Y,
    gcd(Y,R,GCD).

lcm(A,B,LCM) :-
    gcd(A,B,GCD),
    Product is A*B,
    LCM is Product //GCD.

fact(0,1).
fact(N,F) :-
    N > 0,
    N1 is N - 1,
    fact(N1,F1),
    F is N * F1.

is_prime(2).
is_prime(N) :-
    N > 2,
    \+ has_factor(N,2).

has_factor(N,F) :-
    F * F =< N,
    N mod F =:= 0.

has_factor(N,F) :-
    F * F =< N,
    F2 is F + 1,
    has_factor(N,F2).

even(Number) :-
   Number mod 2 =:= 0.

odd(Number) :-
   Number mod 2 =:= 1.


