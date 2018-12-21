import Tkinter
from Tkinter import *
import ttk
import urllib2
import os, sys
import urllib
import time

class main:

	def __init__(self):
		self.gui()

	def getresult(self):

		a = self.listbox.get(self.listbox.curselection())
		#print a
		self.dire.set(a)		

		a = a + "\n"
		self.nume.set("#" + self.dictn[a]['Num'])

		imge = PhotoImage(file=self.dictn[a]['Img'])
		self.canvas.create_image(0,0, image=imge, anchor = "nw")

		self.mw2.grid(row = 0, column = 1, columnspan = 1)
		self.mww.geometry("1200x800")


	def search(self): 
		self.listbox.delete(0, END)

		op = open("example.txt","r")
		st = self.entry.get().lower()
		vl = self.cb.get().lower()
		if st == "":
			if vl != "All types":
				for x in op:
					#n = x[:-1]
					va = self.dictn[x]['Type']
					if ", " in va:
						va = va.split(", ")
					for j in va:
						if j == vl:
							self.listbox.insert(0,x[:-1])

		elif st != "":
			if vl != "All types":
				for x in op:
					if st in x.lower():
						#n = x[:-1]
						va = self.dictn[x]['Type']
						if ", " in va:
							va = va.split(", ")
						for j in va:
							if j == vl:
								self.listbox.insert(0,x[:-1])

		elif st != "":
			if vl == "All types":
				for x in op:
					if st in x.lower():
						self.listbox.insert(0,x[:-1])




	def getUrl(self):

		self.dictn = {}
		self.typel = []

		op = open("example.txt", "r")
		i = 0
		for name in op:
			self.progressbar.step(1)
			self.mw.update()
			time.sleep(0.1)
			response = urllib2.urlopen("https://www.pokemon.com/us/pokedex/"+name)

			page = response.read()

			out = open("html.txt", "w")
			out.write(page)
			out.close()
			name1 = name[:-2]
			#name = name[:-4]
			self.dictn[name] = {}
			q = 0
			inq = open("html.txt", "r")
			for x in inq:
				search = "<span class=\"attribute-title\">Height</span>"

				if search in x:
					q = q + 1
				if search in x and q == 1:
					a =  next(inq)
					a = ' '.join(a.split())
					# print a
					a = a[30:-7]
					self.dictn[name]['Height'] = a
					#print "Height = " + a
			inq.close()

			q = 0
			inq = open("html.txt", "r")
			for x in inq:
				search = "<span class=\"attribute-title\">Category</span>"
				if search in x:
					q = q + 1
				if search in x and q == 1:
					a =  next(inq)
					a = ' '.join(a.split())
					# print a
					a = a[30:-7]
					#print "Catogory = " + a
					self.dictn[name]['Category'] = a
			inq.close()

			q = 0
			inq = open("html.txt", "r")
			for x in inq:
				search = "<span class=\"attribute-title\">Weight</span>"
				if search in x:
					q = q + 1
				if search in x and q == 1:
					a =  next(inq)
					a = ' '.join(a.split())
					# print a
					a = a[30:-7]
					#print "Weight = " + a
					self.dictn[name]['Weight'] = a
			inq.close()


			inq = open("html.txt", "r")
			q = 0
			t = ""
			for x in inq:
				search = "<span class=\"attribute-title\">Abilities</span>"
			  	if search in x:
					q = q + 1
				
				searcht = "<span class=\"attribute-value\">"
				if searcht in x and q == 1:
					a = ' '.join(x.split())
					a = a[30:-7]
					#print "Abilities " + a
					t = t + a + ", "
				if( q == 1) and (' '.join(next(inq).split()) == "</div>"):
					break
			t = t[:-2]
			self.dictn[name]['Abilities'] = t
			inq.close()

			inq = open("html.txt", "r")
			q = 0
			t = ""
			for x in inq:
				search = "<div class=\"dtm-type\">"
			  	if search in x:
			  		q = q + 1
				
				searcht = "<a href=\"/us/pokedex/?type"
				if searcht in x and q == 1:
					a1 = ' '.join(x.split())
					a1 = a1[27:-4]
					a = ""
					for w in range(len(a1)):
						if a1[w] == "\"":
							break
						else:
							a = a+a1[w]
					if a not in self.typel:
						self.typel.append(a)
					#print "Type " + a
					t = t + a + ", "
				if( q == 1) and (' '.join(next(inq).split()) == "</div>"):
					break
			t = t[:-2]
			self.dictn[name]['Type'] = t
			inq.close()

			inq = open("html.txt", "r")
			q = 0
			t= ""
			for x in inq:
				search = "<div class=\"dtm-weaknesses\">"
			  	if search in x:
					q = q + 1

				searcht = "<span>"
				if searcht in x and q == 1:
					
					a1 = ' '.join(x.split())
					a1 = a1[6:]
					#print "Weakness " + a1 
					t = t + a1 + ", "

				if( q == 1) and ("</div>" in ' '.join(next(inq).split())):
					break
			t = t[:-2]
			self.dictn[name]['Weakness'] = t
			inq.close()

			path = os.getcwd()+"/Images"

			if not os.path.exists(path):
				os.mkdir(path)
			


			inq = open("html.txt", "r")
			for x in inq:
				search = "<img class=\"active\" src=\"https://assets.pokemon.com/assets/cms2/img/pokedex/full/"

				if search in x:
					a = ""
					a1 = x[33:]
					for f in range(len(a1)):
						if a1[f] == "\"":
							break
						else:
							a = a + a1[f]

					#print a
					urllib.urlretrieve(a, "Images/"+name1+".png")
					self.dictn[name]['Img'] = "Images/"+name1+".png"
					a = a[56:-4]
					#print a
					self.dictn[name]['Num'] = a
					break 	
			inq.close()
			self.cb['values'] = self.typel
		op.close()



	def gui(self):

		self.mww = Tkinter.Tk()
		self.mww.title("Pokedex")
		self.mww.geometry("600x800")


		self.mw = Frame(self.mww, height = 800, width = 600)
		self.mw.grid(row = 0, column = 0, columnspan = 1)
		self.mw.grid_propagate(0)

		self.frame1 = Frame(self.mw, bg = "red", width = 600, height = 80, highlightbackground="black", highlightcolor="black", highlightthickness=2)
		self.frame1.grid(row=0, column=0, columnspan=1)
		self.frame1.pack_propagate(0)

		self.head_l = Label(self.frame1, bg="red", fg="white", text="Pokedex")
		self.head_l.config(font=("Arial", 28))
		self.head_l.pack(side=TOP, expand=YES)

		self.frame2 = Frame(self.mw, bg = "red", width = 600, height = 120, highlightbackground="black", highlightcolor="black", highlightthickness=2)
		self.frame2.grid(row=1, column=0, columnspan=1)
		self.frame2.grid_propagate(0)

		self.subframe1 = Frame(self.frame2, width=200, height=120,bg="red")
		self.subframe1.grid(row=0,column=0,columnspan=1)
		self.subframe1.pack_propagate(0)

		self.btn_fpd = Button(self.subframe1, width = 12, height=3, text="Fetch \n Pokemon Data", bg="yellow", fg="black", command = self.getUrl)
		self.btn_fpd.pack(side=TOP, expand=YES)

		self.subframe2 = Frame(self.frame2, width=400, height=120,bg="red")
		self.subframe2.grid(row=0,column=1,columnspan=1)
		self.subframe2.pack_propagate(0)

		self.s = ttk.Style()
		self.s.theme_use('clam')
		self.s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
		self.progressbar = ttk.Progressbar(self.subframe2,style="green.Horizontal.TProgressbar", orient = "horizontal", length = 300, mode="indeterminate")
		self.progressbar.pack(side=TOP, expand=YES)

		self.frame3 = Frame(self.mw, width = 600, height = 220, bg= "red",highlightbackground="black", highlightcolor="black", highlightthickness=2)
		self.frame3.grid(row=2, column=0, columnspan=1)
		self.frame3.grid_propagate(0)

		self.subframe3 = Frame(self.frame3, width=600, height = 60, bg = "red")
		self.subframe3.grid(row=0, column = 0, columnspan = 1)
		self.subframe3.pack_propagate(0)

		self.filter_l = Label(self.subframe3, text="Searching & Filtering", bg="red", fg="black")
		self.filter_l.config(font=("Arial", 24))
		self.filter_l.pack(side=TOP, expand=YES)

		self.subframe4 = Frame(self.frame3, width = 600, height = 80, bg="red")
		self.subframe4.grid(row = 1, column = 0, columnspan = 1)
		self.subframe4.pack_propagate(0)

		self.entry = Entry(self.subframe4,bd = 2, width = 50)
		self.entry.pack(side=TOP, expand=YES)

		self.subframe5 = Frame(self.frame3, width = 600, height = 80, bg="red")
		self.subframe5.grid(row = 2, column = 0, columnspan = 1)
		self.subframe5.grid_propagate(0)

		self.subframe6 = Frame(self.subframe5, width = 400,height = 80, bg="red")
		self.subframe6.grid(row=0, column=0, columnspan = 1)
		self.subframe6.pack_propagate(0)

		self.cb = ttk.Combobox(self.subframe6,state="readonly", width = 40)
		self.cb.set("All types")
		self.cb.pack(side=TOP, expand=YES)

		self.subframe7 = Frame(self.subframe5, width = 200, height = 80, bg="red")
		self.subframe7.grid(row = 0, column = 1, columnspan = 1)
		self.subframe7.pack_propagate(0)

		self.btn_search = Button(self.subframe7, width = 8, height = 2, bg = "yellow", fg = "black", text = "Search", command = self.search) 
		self.btn_search.pack(side = TOP, expand = YES)

		self.frame4 = Frame(self.mw, width = 600, height= 380, bg="red", highlightbackground="black", highlightcolor="black", highlightthickness=2)
		self.frame4.grid(row = 3, column = 0, columnspan = 1)
		self.frame4.grid_propagate(0)

		self.subframe8 = Frame(self.frame4, width = 600, height = 80, bg="red")
		self.subframe8.grid(row = 0, column = 0, columnspan = 1)
		self.subframe8.pack_propagate(0)

		self.tot_res_l = Label(self.subframe8,bg="red", fg = "black")
		self.tot_res_l.config(text="Total")
		self.tot_res_l.config(font=("Arial", 24))
		self.tot_res_l.pack(side = TOP, expand = YES)

		self.subframe9 = Frame(self.frame4, width=600, height = 300, bg="red")
		self.subframe9.grid(row = 1, column = 0, columnspan = 1)
		self.subframe9.grid_propagate(0)

		self.subframe10 = Frame(self.subframe9, width = 350, height = 300, bg="red")
		self.subframe10.grid(row = 0, column = 0, columnspan = 1)
		self.subframe10.pack_propagate(0)

		self.listbox = Listbox(self.subframe10, width = 40, height = 14)
		self.listbox.pack(side = TOP, expand = YES)

		self.subframe11 = Frame(self.subframe9, width = 250, height = 300, bg="red")
		self.subframe11.grid(row = 0, column = 1, columnspan = 1)
		self.subframe11.pack_propagate(0)

		self.btn_gpd = Button(self.subframe11, width = 10, height = 2, bg="yellow", fg="black", text = "Search \n Pokemon Data", command = self.getresult)
		self.btn_gpd.pack(side = TOP, expand = YES)



		self.mw2 = Frame(self.mww, width=600, height = 800, bg="blue")
		self.mw2.grid(row = 0, column = 1, columnspan = 1)
		self.mw2.grid_propagate(0)
		self.mw2.grid_forget()

		self.tframe1 = Frame(self.mw2, width = 600, height = 80, bg="red")
		self.tframe1.grid(row = 0, column = 0, columnspan = 1)
		self.tframe1.pack_propagate(0)

		self.dire = StringVar()
		self.dire.set("")
		self.name = Label(self.tframe1, bg="red", fg = "black", textvariable= self.dire)
		self.name.config(font=("Airal", 28))
		self.name.pack(side = TOP, expand = YES)

		self.tframe2 = Frame(self.mw2, width = 600, height = 80, bg="red")
		self.tframe2.grid(row = 1, column = 0, columnspan = 1)
		self.tframe2.pack_propagate(0)

		self.nume = StringVar()
		self.nume.set("")
		self.name = Label(self.tframe2, bg="red", fg = "black", textvariable= self.nume)
		self.name.config(font=("Airal", 20))
		self.name.pack(side = TOP, expand = YES)

		self.tframe3 = Frame(self.mw2, width = 600, height = 500)
		self.tframe3.grid(row = 2, column = 0, columnspan = 1)
		self.tframe3.pack_propagate(0)

		self.canvas = Canvas(self.tframe3, width=475, height=475)
		self.canvas.pack(side = TOP, expand = YES)


		self.tframe4 = Frame(self.mw2, width = 600, height = 20, bg="blue")
		self.tframe4.grid(row = 3, column = 0, columnspan = 1)

		self.tframe5 = Frame(self.mw2, width = 600, height = 20, bg="red")
		self.tframe5.grid(row = 4, column = 0, columnspan = 1)

		self.tframe6 = Frame(self.mw2, width = 600, height = 20, bg="blue")
		self.tframe6.grid(row = 5, column = 0, columnspan = 1)

		self.tframe7 = Frame(self.mw2, width = 600, height = 20, bg="red")
		self.tframe7.grid(row = 6, column = 0, columnspan = 1)

		self.tframe8 = Frame(self.mw2, width = 600, height = 40, bg="blue")
		self.tframe8.grid(row = 7, column = 0, columnspan = 1)

		self.tframe9 = Frame(self.mw2, width = 600, height = 20, bg="green")
		self.tframe9.grid(row = 8, column = 0, columnspan = 1)











m = main()
m.mww.mainloop()
#print m.dictn

