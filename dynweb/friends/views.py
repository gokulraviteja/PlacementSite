from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from friends.models import Object,Url,Mate
from getpass import getpass
import requests
import collections
usr='personalbgokulravi1999@gmail.com'
pwd='gokulraviB1'
#options=webdriver.ChromeOptions()
#options.add_argument('--headless')
#driver=webdriver.Chrome('C:\\Users\\bellapukonda\\Desktop\\auto\\chromedriver.exe',options=options)




# Create your views here.


def friendspage(request):
    d1={}
    username= request.POST['username']
    mobileno=request.POST['mobno']
    bran=request.POST['dropdown']
    q=bran.split('-')
    q1=q[0]
    q2=q[1]
    st="DATA INVALID"
    temp=0
    for ij in 'qwertyuiopasdfghjklzxcvbnm':
        if(ij in mobileno):
            temp=1
            break
    if(temp==0):
        if(len(mobileno)==10):
            ma=Mate.objects.all()
            se=set()
            for ij in ma:
                se.add(ij.mobno )
            print(se)
            if(mobileno in se):
                st="MOBILE NUMBER ALREADY REGISTERED"
            else:
                st="USER "+str(username)+" SUCCESSFULLY REGISTERED"
                m=Mate(name=username,category=q1,branch=q2,mobno=mobileno)
                m.save()
    return render(request,"friends/friendspage.html",{"st":st})


def display(request):
    bran=request.POST['dropdown']
    q=bran.split('-')
    q1=q[0]
    q2=q[1]
    ma=Mate.objects.filter(category=q1,branch=q2)
    return render(request,"friends/display.html",{'ma':ma})


def direct(request):
    d={}
    for i in Object.objects.all():

        if(i.category in d):
            d[i.category].append(i.branch)
        else:
            d[i.category]=[i.branch]
    categories=list(d.keys())
    for i in d:
        p=d[i]
        q=[]
        for j in p:
            q.append(i+'-'+j)
        d[i]=q
    kk={}
    kk["categories"]=categories
    others=[]
    for i in d:
        for j in d[i]:
            others.append(j)
    kk["others"]=others

    return render(request,"friends/direct.html",kk)

def register(request):
    d={}
    for i in Object.objects.all():

        if(i.category in d):
            d[i.category].append(i.branch)
        else:
            d[i.category]=[i.branch]
    categories=list(d.keys())
    for i in d:
        p=d[i]
        q=[]
        for j in p:
            q.append(i+'-'+j)
        d[i]=q
    kk={}
    kk["categories"]=categories
    others=[]
    for i in d:
        for j in d[i]:
            others.append(j)
    kk["others"]=others

    return render(request,"friends/register.html",kk)




def test(request):
    #driver=webdriver.Chrome('C:\\Users\\bellapukonda\\Desktop\\auto\\chromedriver.exe')
    u=Url.objects.get(id='1')
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver=webdriver.Chrome('C:\\Users\\bellapukonda\\Desktop\\auto\\chromedriver.exe',options=options)
    driver.get('http://placement.bitmesra.ac.in/')
    username_box=driver.find_element_by_id('txtUsername')
    username_box.send_keys(usr)
    pass_box=driver.find_element_by_id('txtPassword')
    pass_box.send_keys(pwd)
    login_box=driver.find_element_by_id('imgSubmit')
    login_box.click()
    driver.get("http://placement.bitmesra.ac.in/Student/Jobs.aspx")
    d={}
    url=driver.find_element_by_id("cname1").get_attribute("href")
    urls=driver.find_elements_by_id("cname1")
    b=[]
    for i in urls:
        k=i.get_attribute("href")
        if(k==u.recent):
            break
        b.append(k)
    if(b!=[]):
        u.recent=b[0]
        u.save()
    for i in b:
        driver.get(i)
        a=driver.find_elements_by_class_name('col-xs-3 ')
        for i in a:
            s=i.text
            if('-' in s):
                s=s.split('-')
                if(s[0] in d):
                    d[s[0]].append(s[1])
                else:
                    d[s[0]]=[s[1]]
    driver.quit()
    d1={}
    for i in d:
        p=i.find('\n')
        if(p!=-1):
            p=i[p+1:-1]
            cc=collections.Counter(d[i])
            if(p in d1):
                for j in cc:
                    if(j in d1[p]):
                        d1[p][j]+=cc[j]
                    else:
                        d1[p][j]=cc[j]
            else:
                d1[p]=cc
    st=[]
    for i in d1:
        for j in d1[i]:
            a1=i.strip()
            a2=j.strip()
            a3=d1[i][j]
            st.append(str(a2)+' brach of '+str(a1)+' are applicable to '+str(a3)+' new companies')
            ma=Mate.objects.filter(category=a2,branch=a1)
            mobs=[]
            for i in ma:
                mobs.append(int(i.mobno))



            q=Object.objects.filter(category=a1,branch=a2)
            if(len(q)!=0):
                q=Object.objects.get(category=a1,branch=a2)
                q.comcount+=int(a3)
                q.save()
            else:
                q=Object(category=a1,branch=a2,comcount=a3)
                q.save()

    return render(request,"friends/index.html",{"obj":Object.objects.all(),"url":Url.objects.get(id='1'),'st':st})
