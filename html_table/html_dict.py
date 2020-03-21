
import bs4
import re

path="C:\\Users\\jsm\\Downloads\\Humesh_sheets.html.html"

f=open(path,'r')
html_page = f.read()
f.close()


soup = bs4.BeautifulSoup(html_page,'lxml')

main= soup.find('body',{'class':"awr"})

table1=main.find('table',attrs={'summary':re.compile("BDAM")})

t1=table1.find_all(class_="awrbg")
cnames_table1=[]
for cnames in t1:
    cnames_table1.append(cnames.text)
cn_t1=cnames_table1
print("-"*120)
print("'Sample BDAM Findings by Average Sessions' Table Column Names : {}" .format(cn_t1))
print("-"*120)

t2=table1.find_all(class_="awrc")
t3=table1.find_all(class_="awrnc")
cvalues_table1=[]
for cvalues in t2:
    cvalues_table1.append(cvalues.text)
cvalues_table2=[]
for cvalues in t3:
    cvalues_table2.append(cvalues.text)
    
#print(cvalues_table1)
cv1=cvalues_table1[:6]
cv2=cvalues_table2[:6]
cv3=cvalues_table1[6:12]
cv4=cvalues_table2[6:12]
cv5=cvalues_table1[12:18]

print("Record1: {}".format(cv1))
print("Record2: {}".format(cv2))
print("Record3: {}".format(cv3))
print("Record4: {}".format(cv4))
print("Record5: {}".format(cv5))

table2=main.find('table',attrs={'summary':re.compile("broad")})

cnames_table2=[]
t2=table2.find_all(class_="awrnobg")
cnames_table2.append(" ")
t3=table2.find_all(class_="awrbg")
for cnames in t3:
    cnames_table2.append(cnames.text)
cn_t2=cnames_table2
print("-"*100)
print("'Load Profile' Table Column Names: {}" .format(cn_t2))
print("-"*100)
cvalues_table3=[]
t4=table2.find_all(class_="awrc")
t5=table2.find_all(class_="awrnc")
for cvalues in t4:
    cvalues_table3.append(cvalues.text)
cvalues_table4=[]
for cvalues in t5:
    cvalues_table4.append(cvalues.text)
cv1_t2=cvalues_table3[:5]
cv2_t2=cvalues_table4[:5]
cv3_t2=cvalues_table3[5:10]
cv4_t2=cvalues_table4[5:8]
cv5_t2=cvalues_table4[10:12]

print("Record1: {}".format(cv1_t2))
print("Record2: {}".format(cv2_t2))
print("Record3: {}".format(cv3_t2))
print("Record4: {}".format(cv4_t2))
print("Record5: {}".format(cv5_t2))




        




















    

