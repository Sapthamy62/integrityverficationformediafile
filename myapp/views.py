from django.shortcuts import render
from django.shortcuts import render
from .forms import upload,VerifyForm,AdminForm,Register
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Document,Actors
import hashlib
from .deployment import Addblock,verify
from .deployment import verify
from web3 import Web3
import mysql.connector as sql
def home(request):
     return render(request,'myapp/home.html')
def about(request):
     return render(request,'myapp/about.html')
def mediafile(request):
     st=Document.objects.all() # Collect all records from table 
     return render(request,'myapp/display.html',{'st':st})  

def loginaction(request):      
        global em,pwd,utype,status
        if request.method=="POST":
                form=AdminForm(request.POST)
                if form.is_valid():
                        em=form.cleaned_data['email']
                        pwd=form.cleaned_data['password']
                m=sql.connect(host="localhost",user="root",passwd="spojith9656160925",database="web")
                cursor=m.cursor() 
                c="select * from myapp_actors where email='{}' and password='{}'".format(em,pwd)
                cursor.execute(c)
                t=tuple(cursor.fetchall())
                s=t[0][5]
                ut=t[0][6]
                print(t)
                if t==():
                        return HttpResponseRedirect("error")            
                elif ut==1 and s=='enable':
                        # st=Actors.objects.all() 
                        st=Actors.objects.filter(Typeid=2) 
                        return render(request,'myapp/welcome.html',{'st':st})
                elif ut==2 and s=='enable':
                        form=upload()
                        return render(request,'myapp/index.html',{'forms':form})
                        
        form=AdminForm()
        return render(request,'myapp/login.html',{'forms':form})
# def welcomeaction(request):
                # m=sql.connect(host="localhost",user="root",passwd="spojith9656160925",database="web")
                # cursor=m.cursor() 
                # c="select firstname,lastname from actor where Typeid=2"
                # cursor.execute(c)
                # st=cursor.fetchall()
                # print(st)
                

fn=''
ln=''
em=''
pwd=''
status=''
def registeraction(request):
        # c="insert into users Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
        # cursor.execute(c)
        # m.commit()
        if request.method=="POST":
              
           form=Register(request.POST)           
           if form.is_valid():
              firstname=form.cleaned_data['firstname']
              lastname=form.cleaned_data['lastname']
              email=form.cleaned_data['email']
              passw=form.cleaned_data['password']
              member = Actors(lastname=lastname,Typeid=2,status='disable',Firstname=firstname,email=email,password=passw)
              form=Register()
              member.save()
        form=Register()      
        return render(request,"myapp/register.html",{'form':form})
def uploadfile(request):
    if request.method=='POST':
        form=upload(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            filename="media/documents/"+str(form.cleaned_data['document'])
            o_filename=filename.replace(' ','_')
            # message = hash_file("media/documents/"+str(form.cleaned_data['document']))
            lastid=(Document.objects.last()).id
            message=hash_file(o_filename)
            # return HttpResponse(message)
            Addblock(lastid,message)
            return HttpResponse("Block added Successfully")
    else:
            form=upload()
            return render(request,'myapp/index.html',{'forms':form})
def display(request):

	st=Document.objects.all() # Collect all records from table 
	return render(request,'myapp/display.html',{'st':st})   
def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()
def verifyfile(request):
        if request.method=='POST':
           form=VerifyForm(request.POST)  
           if form.is_valid():
                idoffile=form.cleaned_data['id']             
                m=sql.connect(host="localhost",user="root",passwd="spojith9656160925",database='web')
                cursor=m.cursor()
                c="select document from myapp_document where id='{}'".format(idoffile)
                cursor.execute(c)
                t=tuple(cursor.fetchall())
                fname=t[0][0]
                o_fname="media/"+fname
                hash=hash_file(o_fname)
                print(hash)
                status=verify(idoffile,hash)
                print(status)
                # return HttpResponse(status)
                return render(request,'myapp/conformation.html',{'s':status})
        form=VerifyForm()
        return render(request,'myapp/verify.html',{'forms':form})

def action(request,id):       
                m=sql.connect(host="localhost",user="root",passwd="spojith9656160925",database="web")
                cursor=m.cursor() 
                # c="update table myapp_actors set status='{}' where id='{}'".format(st,id)
                c=Actors.objects.get(id=id)
                c.status='enable'
                c.save()
                st=Actors.objects.filter(Typeid=2) 
                return render(request,'myapp/welcome.html',{'st':st}) 
                
def disable(request,id):
                c=Actors.objects.get(id=id)
                c.status='disable'
                c.save()
                st=Actors.objects.filter(Typeid=2) 
                return render(request,'myapp/welcome.html',{'st':st}) 
                
               
      
                
      