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
INT_VARS = "30" #50
PRINT_INT = "51"
STRING_VARS = "52" #61
STRING_EBP = "62"
PRINT_STRING = "63"
FLOAT_VARS = "64" #73
PRINT_FLOAT = "74"
PRINT_ACTIVATE = "75"
INC = "77"
DEC = "76"
CMP = "331" #585
MAX = 600
perm_vars = {}
labels = {}
strings = []

def run0(al):
  a = open("r0",'a')
  for i in al.split("\n"):
    cells = i.split(";")
    if(cells[0]=="add"):
      lin = i.split(";")
      x = str(lin[1])
      y = str(lin[2])
      a.write(">"+x+", "+TEMP_VARS+", 0, "+EBP+", 0, 0\n")
      a.write(">"+y+", "+ECX+", 0, "+EBP+", 0, 0\n")
      a.write("lbl;"+x+"+"+y+"\n")
      a.write("if;"+ECX+";0\n")
      a.write("goto;:"+x+"+"+y+"T\n")
      a.write("goto;:"+x+"+"+y+"F\n")
      a.write("lbl;"+x+"+"+y+"F\n")
      a.write(">0, "+TEMP_VARS+", 0, "+TEMP_VARS+", "+INC+", 0\n")
      a.write(">0, "+ECX+", 0, "+ECX+", "+DEC+", 0\n")
      a.write("goto;:"+x+"+"+y+"\n")
      a.write("lbl;"+x+"+"+y+"T\n")
      a.write(">0, "+EAX+", 0, "+TEMP_VARS+", 0, 0\n")

    elif(cells[0]=="sub"):
      lin = i.split(";")
      x = str(lin[1])
      y = str(lin[2])
      a.write(">"+x+", "+TEMP_VARS+", 0, "+EBP+", 0, 0\n")
      a.write(">"+y+", "+ECX+", 0, "+EBP+", 0, 0\n")
      a.write("lbl;"+x+"+"+y+"\n")
      a.write("if;"+ECX+";0\n")
      a.write("goto;"+x+"-"+y+"T\n")
      a.write("goto;"+x+"-"+y+"F\n")
      a.write("lbl;"+x+"-"+y+"F\n")
      a.write(">0, "+TEMP_VARS+", 0, "+TEMP_VARS+", "+DEC+", 0\n")
      a.write(">0, "+ECX+", 0, "+ECX+", "+DEC+", 0\n")
      a.write("goto;"+x+"-"+y+"\n")
      a.write("lbl;"+x+"-"+y+"T\n")
      a.write(">0, "+EAX+", 0, "+TEMP_VARS+", 0, 0\n")
    else:
      a.write(i+"\n")
  a.close()

def run1(al):
  global labels
  a = open("r1","a")
  ids = 0
  fi = False
  for i in al.split("\n"):
    cells = i.split(";")
    if(cells[0]=="if"):
      ids+=1
      a.write(">0, "+CMP+", "+cells[2]+", "+EBP+", 0, 0\n")
      a.write(">1, "+CMP+", ["+cells[1]+"], "+EBP+", 0, 0\n")
      a.write(">0, "+EAX+", 0, "+CMP+", "+cells[2]+", 0\n")
      a.write("goto;["+EAX+"]\n")
      a.write("goto;:"+str(ids)+"t\n")
      a.write("goto;:"+str(ids)+"f\n")
      a.write("lbl;"+str(ids)+"t\n")
      fi = True
    else:
      a.write(i+"\n")
      if(fi):
        a.write("lbl;"+str(ids)+"f\n")
        fi=False

def run2(al):
  a = open("r2","a")
  for i in al.split("\n"):
    cells = i.split(";")
    if(cells[0]=="print"):
      if(cells[1]=="int"):
        a.write(">"+cells[2]+", "+PRINT_INT+", 0, "+EBP+", 0, 0\n")
        a.write(">1, "+PRINT_ACTIVATE+", 0, "+EBP+", 0, 0\n")
      elif(cells[1]=="string"):
        a.write('>"'+cells[2]+'", '+PRINT_STRING+", 0, "+STRING_EBP+", 0, 0\n")
        a.write(">2, "+PRINT_ACTIVATE+", 0, "+EBP+", 0, 0\n")
    elif(cells[0]=="nop"):
      a.write(">0, "+EAX+", 0, "+EAX+", 0, 0\n")
    elif(cells[0]=="goto"):
      a.write(">0, "+EAX+", 0, "+EAX+", 0, "+cells[1]+"\n")
    elif(cells[0]=="halt"):
      a.write(">0, 0, 0, "+EBP+", 0, 0\n")
    elif(cells[0]=="dec"):
      a.write(">0, "+cells[1]+", 0, "+DEC+", ["+cells[1]+"], 0\n")
    elif(cells[0]=="inc"):
      a.write(">0, "+cells[1]+", 0, "+INC+", ["+cells[1]+", 0\n")
    else:
      a.write(i+"\n")
  a.close()

def run3(al):
  a = open("r3","a")
  global perm_vars, labels
  c = 0
  varC = 0
  for i in al.split("\n"):
    c+=1
    cells = i.split(";")
    if(cells[0]=="lbl"):
      labels[cells[1]]=c
      a.write(">0, "+EAX+", 0, "+EAX+", 0, 0\n") #nop
    elif(cells[0]=="var"):
      if(cells[2]=="int"):
        perm_vars[cells[1]]=int(INT_VARS)+varC
        a.write(">"+cells[3]+", "+INT_VARS+", "+str(varC)+", "+EBP+", 0, 0\n")
        varC+=1
    else:
      a.write(i+"\n")

def run4(al):
  global perm_vars, labels, strings
  lineCount = 0
  a = open("out.bc","a")
  for i in al.split("\n"):
    lineCount+=1
    splitCells = i.split(";")
    if(splitCells[0]=="pvar"):
      if(splitCells[1]=="int"):
        splitCells[2] = splitCells[2].replace("/","")
        a.write(">0, "+PRINT_INT+", 0, "+str(perm_vars[splitCells[2]])+", 0, 0\n")
        a.write(">1, "+PRINT_ACTIVATE+", 0, "+EBP+", 0, 0\n")
    else:
      if("/" in i):
        for cell in i.split(", "):
          if('/' in cell):
            cell = cell.replace("/","").replace(" ","").replace("[","").replace("]","").replace(">","")
            location = perm_vars[cell]
            i = i.replace("/"+cell, str(location))
      if("[" in i):
        for cell in i.split(", "):
          if("[" in cell):
            cell = cell.replace("/","").replace(" ","").replace("[","").replace("]","").replace(">","")
            ncell = str( int(cell)+MAX )
            i = i.replace("["+cell+"]",ncell)
      if(":" in i):
        for cell in i.split(", "):
          if(":" in cell):
            cell = cell.replace("/","").replace(" ","").replace("[","").replace("]","").replace(">","")
            targetLn = labels[cell.replace(":","")]
            delta = targetLn - lineCount - 1 #decrease 1 for goto
            i = i.replace(cell,str(delta))
      if('"' in i):
        for cell in i.split(", "):
          if('"' in cell):
            cell = cell.replace("/","").replace(" ","").replace("[","").replace("]","").replace(">","").replace('"',"")
            strings.append(cell)
            i = i.replace('"'+cell+'"',str(strings.index(cell)-MAX))
            #TODO: finish replacing strings
      a.write(i+"\n")

def clear():
  files = ["out.bc","r0","r1","r2","r3"]
  for i in files:
    a = open(i,"w")
    a.write("")
    a.close()

def makeAl(f):
  a = open(f,"r")
  al = a.read()
  a.close()
  return(al)

def makeAr(al):
  a = open("out.bc","w")
  al = al.replace("\n>",", ")
  al = al.replace(">","{")
  al = al.replace("\n","}")
  a.write(al)

clear()

run0(makeAl("in.mitc"))

run1(makeAl("r0"))

run2(makeAl("r1"))

run3(makeAl("r2"))

run4(makeAl("r3"))

print("var",perm_vars)
print("lbl",labels)
print("strings",strings)
