#you are given an m*n integer grid accounts where account of ij is the amount of money of ith customer has jth bank.the customers wealth is the amount of they have in all there bank accounts.the richest cusomer isthe customer that has the maximum well.
def find_richest_customer(accounts):
    max_wealth=0
    for cus in accounts:
        wealth=sum(cus)
        if wealth > max_wealth:
            max_wealth=wealth
    return max_wealth

if __name__=="__main__":
    m=int(input("Enter the number of customer\n"))
    n=int(input("enter number of banks"))
    
    account=[]
    for i in range(m):
        print("enter wealth for customer {} in {} banks".format(i+1,n))
        customer_wealth=list(map(int,input().split()))
        account.append(customer_wealth)
    print(find_richest_customer(account))     

        