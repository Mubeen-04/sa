parent(aryaan, pradeep).
parent(pradeep, madan).
parent(aryaan, sangeeta).
parent(krina, pradeep).
parent(krina, sangeeta).
parent(pradeep, laxmi).
parent(sangeeta, javer).
parent(sangeeta, gunsi).

male(aryaan).
male(pradeep).
male(madan).
male(gunsi).
female(krina).
female(sangeeta).
female(laxmi).
female(javer).

child(X, Y) :- parent(Y, X).

sibling(X, Y) :-
    parent(X, P),
    parent(Y, P),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

father(X,F):-
    male(F), parent(X,F).

mother(X,M):-
    female(M), parent(X,M).

grandfather(X,F):-
    male(F),
    parent(X,Z),
    parent(Z,F).

grandmother(X,M):-
    female(M),
    parent(X,Z),
    parent(Z,M).

