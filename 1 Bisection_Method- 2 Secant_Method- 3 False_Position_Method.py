import math 
from tabulate import tabulate
from sympy import *
class NonLinear():
    def __init__(self,expr,lower,higher):
        self.higher_interval=0
        self.lower_interval=0
        self.exp=expr
        Temp=lower
        if '/' in Temp:
            nume , deno  = Temp.split('/')
            nume=float(eval(nume))
            deno=float(deno)
            self.lower_interval=round(nume/deno,9)
        else:
            self.lower_interval=float(eval(Temp))

        Temp=higher
        if '/' in Temp:
            nume , deno  = Temp.split('/')
            nume=float(eval(nume))
            deno=float(deno)
            self.higher_interval=round(nume/deno,9)
        else:
            self.higher_interval=float(eval(Temp))
        

    def f(self,num):
        x = num
        return float(eval(self.exp))


    def BisectionMethod(self,tolerence,round_to):
        error_bound=float(tolerence)
        round_to=int(round_to)
        flag=0
        if self.f(self.lower_interval)*self.f(self.higher_interval)>0:
            print("Bisection Method inapplicable!")
            return 
            
        else:
            header = ["a","b","p=(a+b)/2","f(p)","Error"]
            if self.f(self.lower_interval)<0:
                a=self.lower_interval
                b=self.higher_interval
            else:
                flag=1
                a=self.lower_interval
                b=self.higher_interval
        p=round((a+b)/2,round_to)
        fp=self.f(p)
        fp=round(fp,round_to)
        err=1
        data = [(a, b, p, fp, "NULL")]
        tuple = ()

        if fp < 0:
            if flag==1:
                b=p
            else:    
                a = p
        else:
            if flag!=1:
                b=p
            else:
                a=p    

        while err>=error_bound and err!=0.0:
            prevp=p
            p = round((a+b)/2,round_to)
            fp = self.f(p)
            fp = round(fp,round_to)
            err=round(abs(p-prevp),round_to)
            tuple = tuple + (a,) + (b,) + (p,) + (fp,) + (err,)
            data.append(tuple)
            tuple = ()

            if fp < 0:
                if flag==1:
                    b = p
                else:
                    a=p  
            else:
                if flag!=1:
                    b=p
                else:
                    a=p
        print(tabulate(data,header,tablefmt="simple"))
        return
    

    def Secant_Method(self,tolerence,round_to):
        error_bound = float(tolerence)
        round_to=int(round_to)
        p0 =self.lower_interval
        p1 =self.higher_interval
        a=self.f(p0)
        b=self.f(p1)
        p2 = round(p1 - ((b * (p1 - p0)) / (b - a)),round_to)
        err=1
        header = ["N  ","A   ","B   ","C   ","  Error"]
        data=[(1,p0,p1,p2,"NULL")]
        tuple=()
        p0 = p1
        p1 = p2
        count=2
        while err>=error_bound and err!=0:
            prevp = p2
            a = self.f(p0)
            b = self.f(p1)
            p2=round(p1 - ((b * (p1 - p0)) / (b - a)),round_to)
            err=round(abs(prevp-p2),round_to)
            tuple=tuple+(count,)+(p0,)+(p1,)+(p2,)+(err,)
            data.append(tuple)
            count+=1
            tuple=()
            p0 = p1
            p1 = p2
        print(tabulate(data,header,tablefmt="simple"))
        return

        
    def False_Position_Method(self,tolerence,round_to):
        error_bound = float(tolerence)
        round_to=int(round_to)
        flag=0
        if self.f(self.lower_interval) * self.f(self.higher_interval) > 0:
            print("False Reguli Method inapplicable!")
            return
            
        else:
            if self.f(self.lower_interval) < 0:
                a = self.lower_interval
                b = self.higher_interval
            else:
                flag=1
                a = self.lower_interval
                b = self.higher_interval
        upper =(a*self.f(b))-(b * self.f(a))
        lower = (self.f(b)-self.f(a))
        p=round(upper/lower,round_to)
        fp = self.f(p)
        fp=round(fp,round_to)
        err =1
        header = ["A   ","B   ","P   ","f(P)  ","  Error"]
        data=[(a, b, p, fp,"NULL")]
        tuple=()
        if fp < 0:
            if flag==1:
                b=p
            else:    
                a = p
        else:
            if flag!=1:
                b=p
            else:
                a=p


        while err>=error_bound and err!=0.0:
            prevp=p
            upper = (a * self.f(b)) - (b * self.f(a))
            lower = (self.f(b) - self.f(a))
            p = round(upper / lower, round_to)
            fp = self.f(p)
            fp=round(fp,round_to)
            err = round(abs(p-prevp),round_to)
            tuple=tuple+(a,) + (b,) + (p,) + (fp,) + (err,)
            data.append(tuple)
            tuple = ()
            if fp < 0:
                if flag==1:
                    b=p
                else:    
                    a = p
            else:
                if flag!=1:
                    b=p
                else:
                    a=p 
        print(tabulate(data,header,tablefmt="simple"))
        return

print("Starting")
print("If you want to write 'x^2' you have to write 'x**2'\nIf you want to write 'e^2' you have to write 'math.exp(2)'\nIf you want to write 'cos(x)' you have to write 'math.cos(x)'\nIf you want to write 'ln(x)' you have to write 'math.log(x)'\nIf you want to write 'pi' you have to write 'math.pi'\n")
val = input ("Enter 1 to implement Bisection Method\nEnter 2 to implement Secant Method\nEnter 3 to implement False Position Method\n")
val=int(val)
expression = input("Enter the equation\n")
low_inter = input("Enter Lower Interval\n")
upr_inter = input("Enter Upper Interval\n")
tol = input("Enter tolerence Value\n")
tol=float(eval(tol))
rou = input("Enter round of place\n")
obj = NonLinear(expression,low_inter,upr_inter)
if val==1:
    obj.BisectionMethod(tol,rou)
elif val==2:
    obj.Secant_Method(tol,rou)
elif val==3:
    obj.False_Position_Method(tol,rou)
else:
    print("Invalid Input")
