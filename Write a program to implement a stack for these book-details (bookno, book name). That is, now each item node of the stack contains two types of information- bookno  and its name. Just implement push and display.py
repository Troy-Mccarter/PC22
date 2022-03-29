def isEmpty(stk):
  if stk==[]: 
     return True
  else:
     return False

def Push(stk,item):
  stk.append(item)
  top=len(stk)-1

def Display(stk):
  if isEmpty(stk):
    print("stack empty")
  else:
    top=len(stk)-1
    print(stk[top], "<-top")
    for a in range (top-1,-1,-1):
      print(stk[a])

Stack=[]
top=None
while True:
  print("select stack operation:")
  print("1.Push")
  print("2.Display stack")
  print("3.Exit")
  ch=int(input("enter your choice:"))

  if ch==1:
    BookNo=int(input"Enter bookno: ))
    BookName= input("Enter book name: )
    item=(BookNo,BookName)
    Push(Stack,item)

  elif ch==2:
    Display(Stack)

  elif ch==3:
    break

  else:
    print("Invaild choice!")
