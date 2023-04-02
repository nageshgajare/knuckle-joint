import math
import streamlit as st
st.header("The problem on knuckle joint")
fos = st.number_input("enter the given value of factor of safety\n",1)
syt = st.number_input("enter the value of syt \n ",1)
gt=syt/fos
st.write(f"the value of permissible tensile stress {gt}")
c=2*syt
gc=(c)/fos
st.write(f"The value of permissible crushing stress {gc}")
t=(syt/2)/fos
st.write(f"the value of  permissible shear stress {t}")
P=st.number_input("Enter the value of Force",1)
x=4*P
y=(3.14*gt)
D=(x/y)**(1/2)
def round_up_to_nearest_even_number(D):
    return math.ceil(D/2)*2
st.write("the value of diameter is ",{round_up_to_nearest_even_number(D)})
#calculate a encharged diamter
d1=1.1*round_up_to_nearest_even_number(D)
def round_up(d1):
    return math.ceil(d1/2)*2
st.write("the value of enlarged diamter ",{round_up(d1)})
#calculate the diamensions of a and b
st.write("the value of a and b is as follows")
a=0.75*round_up_to_nearest_even_number(D)
def round_up(a):
    return math.ceil(a/2)*2
st.write("the value of a is ",{round_up(a)})
b=1.25*round_up_to_nearest_even_number(D)
def round_up(b):
    return math.ceil(b/2)*2
st.write("the value b is ",{round_up(b)})
#calculate diamter of pin
st.write("the dimater of pin")
s=2*P
y=3.14*t
e=s/y
d=(e)**(1/2)
def round_up(d):
    return math.ceil(d/2)*2
st.write("the value of shear consideration",{round_up(d)})
mk=3.14*gt
dk=32/mk
bk=b/4
ck=(round_up(a))/3
ok=(bk+ck)
kk=P/2
kt=ok*kk
d1=(dk*kt)**(1/3)
def round_up(d1):
    return math.ceil(d1/2)*2
st.write("the value for bending considertion",{round_up(d1)})
ak=round_up(d1)
pk=round_up(d)
def maximum(ak,pk):
    if ak>pk:
        return ak
    else:
        return pk
st.write("the maximum value of pin",{max(ak,pk)})
#calculate the dimensions do and d1
do=2*max(ak,pk)
st.write("the value of do",{do})
d1=1.5*max(ak,pk)
print("the value of d1")
st.write("the value of d1",{d1})
#check the tensile,shear and crushing stress in the eye
st.subheader("check the value in the eye")
mh=round_up(b)*(do-(max(ak,pk)))
bh=P/mh
st.write("the value of tensile stress in the eye",{bh})
if bh>gt:
    st.write("the design is not safe")
else:
    st.write("the design is safe")
#for crushing stress
ah=round_up(b)*(max(ak,pk))
ch=P/ah
print("the vaule of crushing stress")
print(ch)
if ch>gc:
    st.write("the design is not safe")
else:
    print("the design is safe")
dh=P/mh

# for shear
st.write("the value of shear stress",{dh})
if dh>t:
    st.write("the design is not safe")
else:
    st.write("the design is safe \n")
#check for stress in fork

st.subheader("the value for tensile crushing and shear in the fork \n ")
jk=2*round_up(a)*(do-(max(ak,pk)))

fh=P/jk
st.write("the value of tensile stress ",{fh})
if fh>gt:
    st.write("the design is not safe")
else:
    st.write("the design is safe")
jh=2*round_up(a)*(max(ak,pk))
kh=P/jh
st.write("the value of crushing stress",{kh})
if kh>gc:
    st.write("the design is not safe")
else:
    st.write("the design is safe")
jl=2*round_up(a)*(do-(max(ak,pk)))
hj=P/jl
st.write("the value of shear stress",{hj})
if hj>t:
    st.write("the design is safe")
else:
    st.write("the design is safe")
