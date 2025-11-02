def sumOrProduct(n, q):

    sum_of_numbers = 0
    product_of_numbers = 1
    if(q==1):
        return (n*(n+1))//2
    if(q==2):
        for j in range(1,n+1):
            product_of_numbers*=j
        return product_of_numbers%(10**9+7)
n, q = map(int, input().split())
print(sumOrProduct(n, q))