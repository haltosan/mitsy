
def read(f):
  a = open("new","r")
  red = a.read()
  a.close()
  if(f):
    al = red
  else:
    a = open("config.txt",'r')
    al = a.read()
  lines = al.split("\n")

  out =[]
  for i in lines:

    comment = i.find("# ")
    if(not comment==-1):
      i = i[:comment-1]
    cells = i.replace("=","").replace("#", "").replace("  "," ").replace('"',"").split(" ")
    out.append(cells)
  return(out)

def edit(target,amount,f):
  table = read(f)
  cascade = False
  out= []
  for i in table:
    c = 0
    for l in i:
      if(cascade and c==1):
        i[1] = str( int(i[1])+amount )
      elif(cascade and c==2):
        i[2] = str( int(i[2])+amount )
      elif(l==target):
        i[1]=str(int(i[1])+amount)
        i[2]=str(int(i[2])+amount)
        cascade = True
      c+=1
    out.append(i)
  return(out)

def change(new):
  a = open("new","w")
  a.write("")
  a.close()

  a = open("new","a")
  for i in new:
    s=""
    for l in range(len(i)):
      if(l==0):
        s+=i[l]+" = "
      elif(l==1):
        s+=('"'+i[l]+'"')
      elif(l==2):
        s+=" #"+i[l]
    a.write(s+"\n")

dynamic = ["TEMP_VARS","INT_VARS","STRING_VARS","FLOAT_VARS"]

def run():
  a = open("new","w")
  a.write("")
  a.close()
  first = False
  while(True):
    print("What do you want to change?")
    print("1) Temp vars\n2) Int vars\n3) String vars\n4) Float vars")
    print("99) Exit")
    choice = (input("> "))
    if(choice == "99"):
      break
    choice = int(choice)
    print("Increase by how much?")
    ammount = int(input("> "))
    new = edit(dynamic[choice],ammount,first)
    change(new)
    first = True
    
    
