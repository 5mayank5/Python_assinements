def recfib(n):
    if n <= 1 :
        return n
    else:
        return(recfib(n-1)+ recfib(n-2))
    n_term = 10
    if n_term <= 0:
        print("invalid input ! please input a positive value")
    else:
         print("fibonacci series:")
    for i in range (n_terms):
          print(recfib(i))
    
