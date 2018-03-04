from swampy.Gui import *

g=Gui()

def com():
  g.la(text='Thanku there!!')
  canvas=g.ca(width='500',height='500')
  canvas.config(bg='red')
  item=canvas.circle([0,0],20,fill='blue',outline='yellow',width='5')
  canvas.polygon([[1,2],[4,3],[44,33],[200,300]],fill='green',outline='white')

def com1():
  g.en(text='Default Text')
  text=g.te(width='100',height=100)
  for i in range(4):
   text.insert(END,'A line hai yee\n')
  text.insert(2.4,'Ghussa')
  text.delete(0.0,END)
def create():
  g.row()
  g.col()
  g.ca(width=100,height=100)
  g.endcol()
  g.col()
  g.gr(cols=2)
  g.bu(text='hi')
  g.bu(text='hi')
  g.bu(text='hi')
  g.bu(text='hi')
  g.endgr()
  g.row([1200,1],pady=30)
  g.bu(text='click')
  g.la(text='Yipee')
  g.endrow()
  g.endcol()
  g.endrow()

def switch_color(color,mb):
  mb.config(bg=color)
  mb.config(text=color)
def menu():
  colors=['red','blue','green']
  mb=g.mb(text=colors[0])
  for color in colors:
    g.mi(mb,text=color,command=Callable(switch_color,color,mb))
     
g.la(text='Click The Fucking Button')
g.bu(text='Click Me',command=menu)
g.mainloop() 
