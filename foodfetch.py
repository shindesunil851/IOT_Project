import random

#r=random.randint(0,50)
r=5

file=open('new_food.csv','r')

food_glucose={}
li =[]
for line in file:
    li.append(line.split(',')[0])
    #print(line.split(',')[0])

    food_glucose[line.split(',')[0]]=line.split(',')[1].strip()+','+line.split(',')[2].strip()

#print(food_glucose)

a=[]
k=-1
a_sum=0


for i in food_glucose:
    k = k+1
    if k< 262 and len(a)<1:
        ran=random.randint(k,262)
        if a_sum<r:
            p=a_sum+int(food_glucose[li[ran]].split(',')[0])


            if p<r:
                a.append(li[ran])
                a_sum=a_sum+int(food_glucose[li[ran]].split(',')[0])


            else:

                while 1:

                    ran=ran+1
                    p=a_sum+int(food_glucose[li[ran]].split(',')[0])

                    if p<r:
                        a.append(li[ran])
                        a_sum=a_sum+int(food_glucose[li[ran]].split(',')[0])
                        break

    elif k>263 and k<4605 and len(a)<9:
        ran=random.randint(k,4604)
        if a_sum<r:
            p=a_sum+int(food_glucose[li[ran]].split(',')[0])


            if p<r:
                a.append(li[ran])
                a_sum=a_sum+int(food_glucose[li[ran]].split(',')[0])


            else:

                while 1:

                    ran=ran+1
                    p=a_sum+int(food_glucose[li[ran]].split(',')[0])

                    if p<r:
                        a.append(li[ran])
                        a_sum=a_sum+int(food_glucose[li[ran]].split(',')[0])
                        break

# for i in food_glucose:
#     print(food_glucose[i].split(',')[0])



# print(li[10])
print(a_sum)
print(a)