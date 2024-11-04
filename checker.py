# from pack import getlatlong
import csv
# l = {}
# rows =[]
f1 = open (r"bot/plugins/database/profile.csv", "r") 
f2 = open (r"bot/plugins/database/profile.csv", "w") 
reader = csv.DictReader(f1)
writer = csv.writer(f2)

# count=2
# for i in reader:
#     print(i)
        
#     main = i['MapURL']
#     print(main)
#     d = getlatlong(main)
#     lat = d[0]
#     long=d[1]
#     print(lat,long)
#     l[count]=[lat,long]
#     rows.append(i)
#     count+=1
#     print(count)


# print(rows)        
# f1.close()
# f2 = open (r"bot/plugins/database/profile.csv", "w")
# writer = csv.writer(f2)
# try:
#     rows[count][4]=l[count][0]
#     rows[count][5]=l[count][1]
#     print(rows)
#     writer.writerows(rows)
# except:
#     pass




 

    