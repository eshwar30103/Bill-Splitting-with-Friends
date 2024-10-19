total=int(input("enter total amt before discount:"))
friends=int(input("how many friends:"))
finalamt=int(input("final discounted amt: "))
indiv_amt=[]
for i in range(friends):
    indiv_amt.append(int(input(f"total individual amt before discount of {i+1} friend:")))
taxes=total-sum(indiv_amt)
pure_total=total-taxes
prop=[]
for j in indiv_amt:
    amm=j/pure_total*100
    prop.append(amm)
final=[]
for k in prop:
    okk=k/100*finalamt
    final.append(okk)
for friend in range(friends):
    if friend==0:
        print(f"{friend+1}st friend has to pay {final[0]} rs")
    elif friend==1:
        print(f"{friend+1}nd friend has to pay {final[1]} rs")
    elif friend==2:
        print(f"{friend+1}rd friend has to pay {final[2]} rs")
    else:
        print(f"{friend+1}th friend has to pay {final[friend]} rs")
if sum(final)==finalamt:        
    print(f'Sum of individual amts={sum(final)} is equal to final discounted amt={finalamt}')
    print("verified successfully!")

