from fpdf import FPDF
from main import *
import os
class PDF(FPDF):
    def lines(self):
        self.set_fill_color(255,99,71) # color for outer rectangle
        self.rect(5.0, 5.0, 200.0,287.0,'DF')
        self.set_fill_color(255,255,255) # color for inner rectangle
        self.rect(8.0, 8.0, 194.0,281.0,'FD')
    
    def imagex(self,sctplt,x,y,width,height):
        self.set_xy(x,y)
        self.image(sctplt, type='', w=width, h=height)
    def titles(self,txt):
        self.set_xy(10,10.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt=txt, border=0)
    def texts(self,text,x,y,ln,fntsize):
        
        self.set_xy(x,y)    
        self.set_text_color(0,0,0)
        self.set_font('Arial', '', fntsize)
        
        self.cell(0,10,text,ln=ln)
        

namelist=[]
for k in range(len(x)):
    namelist.append(x[k][0])

d={}

for i in range(len(namelist)):
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.lines()
    image1="wisdom test/1.png"
    image2="wisdom test/2.png"
    
    pdf.imagex(image2,20.0,50.0,4000/50,3840/50)
    pdf.imagex(image1,070.0,10,3900/50,2000/50)
    currstudent=namelist[i]
    pdf.imagex("pics/{}.jpg".format(currstudent),27.0,51.5,4000/60,4000/55)
    pdf.texts("Name:"+x[i][0],105,60,1,20)
    pdf.texts("Registration Number:{}".format(x[i][1]),105,70,1,15)
    pdf.texts("Grade:{}".format(x[i][2]),105,80,1,15)
    pdf.texts("School:{}".format(x[i][3]),105,90,1,15)
    pdf.texts("Gender:{}".format(x[i][4]),105,100,1,15)
    pdf.texts("Date of birth:{}".format(x[i][5]),105,110,1,15)
    pdf.texts("City of Residence:{}".format(x[i][6]),105,120,1,15)
    pdf.texts("Date of test:{}".format(x[i][7]),10,130,1,15)
    pdf.texts("Country:{}".format(x[i][8]),10,140,1,15)
    pdf.texts("Score:{}/100".format(scorelist2[i]),10,150,1,15)
    pdf.texts("Final Result:{}".format(x[i][10]),10,160,1,15)
    
    
    
    
    
    
    

    pdf.output(f"{namelist[i]}.pdf",'F')
    