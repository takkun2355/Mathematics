def quad(Y=None, A=None, X=None):
    # What $y=ax^2$?

    Calc = float(0)

    hnbs = "has not been set."

    if not X == None:
        X **= 2
    
    # "Y", "A", "X"のいずれか2つが設定されてなかったらprintする
    if Y == A == X == None:
        raise ValueError(
            "None of Y, A, X have been set, so the calculation cannot be performed.\n            Please set any two of Y, A or X."
        )

    # Yを求める
    if Y == None:
        if A == None:
            raise ValueError(
                "Y or A " + hnbs
            )
            
        elif X == None:
            raise ValueError(
                "Y or X " + hnbs,
            )
            
        else:
            Calc = A * X

    # Aを求める
    elif A == None:

        if X == None:
            raise ValueError(
                "A or X " + hnbs
            )
        else:
            Calc = X / Y

    elif A == 0:
        if Y == 0:
            raise ValueError(
                # 「A」がゼロであるため、2次関数に関する計算を行うことができません。
                "I am unable to perform calculations on quadratic functions because A is zero.\n            The solutions to X are all real numbers."
            )

    # Xを求める
    else:
        CalcX = Y / A

        #sqrt(CalcX)
        if CalcX < 0:
            raise ValueError(
                f"Since X^2 is a negative number ({CalcX}), there are no solutions within the set of real numbers."
            )

    return Calc

def sqrt(X, f=10):
    ortnb = 0
    trtnb = 1

    for i in range(int(X*10)):
        ortnb += 1
        ortnbt = ortnb**2

        trtnb += 1
        trtnbt = trtnb**2
        if trtnbt >= X > ortnbt:
            if trtnbt == X:
                rtnb = trtnb
            else:
                rtnb = ortnb
            break
    
    Newton = (rtnb + 10/rtnb)/2
    for j in range(f):
        Newton = (Newton + 10/Newton)/2

    X_pos = absol(Newton)
    X_neg = X_pos * -1
    return X_pos, X_neg

def factorial(X):
    Calc = 1

    if not X == int(X):
        raise FunctionInvalidError("The value is not an integer. \n Please use gamma().")
    if 0 > X:
        raise ValueError("Calculations involving negative numbers cannot be performed. \n Please use gamma().")

    for i in range(X):
        Calc *= i+1
    return Calc

def absol(X):
    if X < 0:
        X = -X
    return X

def BSJudge(X, Y, retum="both", nominus=False):
    if Y <= X:
        small = Y
        big = X
    elif X < Y:
        small = X
        big = Y

    if nominus is True:
        if big < 0:
            big *= -1
        if small < 0:
            small *= -1
    
    match retum:
        case "big":
            return int(big)
        case "small":
            return int(small)
        case "both":
            return int(big), int(small)
        case _:
            raise TypeError("The value is not an integer. \n Example: test.sqrt(10, 20)")
    


def gcd(X, Y):
    if X is Y is None:
        raise ValueError("No value has been set. \n Example: test.sqrt(10, 20)")
    elif X is None or Y is None:
        raise ValueError("The value is insufficient. \n Example: test.sqrt(10, 20)")

    if X != int(X) or Y != int(Y):
        raise TypeError("The value is not an integer. \n Example: test.sqrt(10, 20)")
    
    big, small = BSJudge(X, Y, "big", True), BSJudge(X, Y, "small", True)

    if small != 0:
        Calc = big % small
        BSJudge(X, Y, "both", True)

        for i in range(big):
            if Calc == 0:
                Calc = small
                break
            big = small
            small = Calc
            Calc = big % small
            BSJudge(X, Y, "both", True)

    if small == 0:
        return big
    else:
        return Calc



class FunctionInvalidError(TypeError):
    pass

N = -10.12

factorial(N)
print(factorial(N))