import suffixtree

def fibonacci(n):
    fib = []
    for i in xrange(n+1):
        if i == 0:
            fib.append("b")
        if i == 1:
            fib.append("a")
        if i > 1:
            fib.append(fib[i-1] + fib[i-2])
    return fib
    
if __name__ == "__main__":
    
    #Simulate 10 fibonacci strings
    strings = fibonacci(10)
    
    #init result lists
    res = {}
    failed = [0] * len(strings)
    
    for i in xrange(len(strings)):
        tree = suffixtree.SuffixTree(strings[i])
        try:
            res[len(strings[i])] = tree.find_tandem_repeats()
            
        except Exception:
            failed[i] = "failed"
            pass
    print "failed"
    print failed
    print "results"
    print res
        