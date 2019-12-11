TEMP_VARS = "11" #20
EAX = "21" #return values
EBX = "22" #halt
ECX = "23" #loop counter
EDX = "24" #temp var/general purpose
ESI = "25" #goto pointer
EDI = "26" #pointer
EBP = "27" #literal loader
ESP = "28" #stack pointer
EIP = "29" #instruction pointer
PERM_VARS = "30" #50
PRINT_INT = "51"
STRING_VARS = "52" #61
PRINT_STRING = "62"
FLOAT_VARS = "63" #72
PRINT_FLOAT = "73"
INC = "74"
DEC = "73"
CMP = "329" #583
perm_vars = {}
labels = {}


def run1(al):
  o = open("out.bc",'a')
  for i in al.split("\n"):
    cells = i.split(";")
    if(cells[0]=="add"):
      lin = i.split(";")
      x = str(lin[1])
      y = str(lin[2])
      o.write(">"+x+", "+TEMP_VARS+", 0, "+EBP+", 0, 0\n")
      o.write(">"+y+", "+ECX+", 0, "+EBP+", 0, 0\n")
      o.write("lbl;"+x+"+"+y+"\n")
      o.write("if;"+ECX+";0\n")
      o.write("goto;"+x+"+"+y+"T\n")
      o.write("goto;"+x+"+"+y+"F\n")
      o.write("lbl;"+x+"+"+y+"F\n")
      o.write(">0, "+TEMP_VARS+", 0, "+TEMP_VARS+", "+INC+", 0\n")
      o.write(">0, "+ECX+", 0, "+ECX+", "+DEC+", 0\n")
      o.write("goto;"+x+"+"+y+"\n")
      o.write("lbl;"+x+"+"+y+"T\n")
      o.write(">0, "+EAX+", 0, "+TEMP_VARS+", 0, 0\n")

    elif(cells[0]=="sub"):
      lin = i.split(";")
      x = str(lin[1])
      y = str(lin[2])
      o.write(">"+x+", "+TEMP_VARS+", 0, "+EBP+", 0, 0\n")
      o.write(">"+y+", "+ECX+", 0, "+EBP+", 0, 0\n")
      o.write("lbl;"+x+"+"+y+"\n")
      o.write("if;"+ECX+";0\n")
      o.write("goto;"+x+"-"+y+"T\n")
      o.write("goto;"+x+"-"+y+"F\n")
      o.write("lbl;"+x+"-"+y+"F\n")
      o.write(">0, "+TEMP_VARS+", 0, "+TEMP_VARS+", "+DEC+", 0\n")
      o.write(">0, "+ECX+", 0, "+ECX+", "+DEC+", 0\n")
      o.write("goto;"+x+"-"+y+"\n")
      o.write("lbl;"+x+"-"+y+"T\n")
      o.write(">0, "+EAX+", 0, "+TEMP_VARS+", 0, 0\n")
    else:
      o.write(i+"\n")
  o.close()

def run2(al):
  for i in al.split("\n"):
    cells = i.split(";")
    if(cells[0]=="print"):

    elif(cells[0]=="if"):
    elif(cells[0]=="nop"):
    elif(cells[0]=="goto"):

o = open("out.bc","w") #clear the out file
o.write("")
o.close()

a = open("in.mitc","r")
al = a.read()
a.close()
lines = al.split("\n")

run1(al)

a = open("")
