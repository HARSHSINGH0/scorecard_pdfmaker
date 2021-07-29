import pandas as pd
# read the file
xls = pd.ExcelFile('Dummy Data.xlsx')
sheet_names = xls.sheet_names
df = pd.read_excel(xls, "Sheet1")
lastrange=125#this is number of last row-1
currentstudentdata=[]
score=0
scorelist=[]
for i in range(lastrange):
    currentnumber=df.loc[i]
    registrationnumber=currentnumber[5]
    if registrationnumber in currentstudentdata:# USING IF STATEMENT SO THAT VALUES DONT GET DUPLCIATED
        score+=currentnumber[18]
        
        
    else:
        currentnumber=df.loc[i]
        fullname=currentnumber[4]
        currentstudentdata.append(fullname)
        registrationnumber=currentnumber[5]
        currentstudentdata.append(registrationnumber)
        grade=currentnumber[6]
        currentstudentdata.append(grade)
        schoolname=currentnumber[7]
        currentstudentdata.append(schoolname)
        gender=currentnumber[8]
        currentstudentdata.append(gender)
        dob=currentnumber[9]
        currentstudentdata.append(dob)
        city_of_residence=currentnumber[10]
        currentstudentdata.append(city_of_residence)
        date_and_time=currentnumber[11]
        currentstudentdata.append(date_and_time)
        country_of_residence=currentnumber[12]
        currentstudentdata.append(country_of_residence)

        score+=currentnumber[18]
        scorelist.append(score-currentnumber[18])
        print(score)
        currentstudentdata.append(score)
        final_result=currentnumber[19]
        currentstudentdata.append(final_result)
print(currentstudentdata)
scorelist.append(score)
scorelist2=[]
for i in range(len(scorelist)):
    if i==len(scorelist):
        break
    else:
        scorelist2.append(scorelist[i]-scorelist[i-1])

scorelist2.remove(scorelist2[0])

def divide_chunks(l, n):
    for i in range(0, len(l), n): 
        yield l[i:i + n]
n = 11
  
x = list(divide_chunks(currentstudentdata, n))
