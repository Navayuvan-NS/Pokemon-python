from Tkinter import Frame
class MainWindow(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("ProgressBar example")
        self.master.minsize(200, 100)
        self.grid(sticky=E+W+N+S)

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.start_ind = Button(self, text='Start indeterminate', command=self.start_ind, activeforeground="red")
        self.start_ind.grid(row=0, column=0, pady=2, padx=2, sticky=E+W+N+S)

        self.pbar_ind = ttk.Progressbar(self, orient="horizontal", length=300, mode="indeterminate")
        self.pbar_ind.grid(row=1, column=0, pady=2, padx=2, sticky=E+W+N+S)

        self.start_det = Button(self, text='Start determinate', command=self.start_det, activeforeground="red")
        self.start_det.grid(row=2, column=0, pady=2, padx=2, sticky=E+W+N+S)

        self.pbar_det = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.pbar_det.grid(row=3, column=0, pady=2, padx=2, sticky=E+W+N+S)

        self.inside_f = Button(self, text='Start function', command=self.start_fun, activeforeground="red")
        self.inside_f.grid(row=4, column=0, pady=2, padx=2, sticky=E+W+N+S)

        self.pbar_f = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.pbar_f.grid(row=5, column=0, pady=2, padx=2, sticky=E+W+N+S)

    def foo(self, m):
        for i in xrange(m):
            i * 2
            self.pbar_det.step(1)
            self.update()
            time.sleep(0.1)
        return i


    def start_ind(self):
        for i in xrange(500):
            self.pbar_ind.step(1)
            self.update()
            # Busy-wait
            time.sleep(0.1)

    def start_det(self):
        for i in xrange(500):
            self.pbar_det.step(1)
            self.update()
            # Busy-wait
            time.sleep(0.1)

    def start_fun(self):
        res = foo(500)


if __name__=="__main__":
   d = MainWindow()
   d.mainloop()
