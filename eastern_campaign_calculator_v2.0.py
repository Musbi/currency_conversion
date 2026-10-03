from tkinter import *

class myGui:
    def __init__(self):
        #create main window
        self.main_window = Tk()
        self.main_window.title("Eastern Campaign Currency Calculator v2.0")

        #create list for header
        self.header = ["Currency", "Amount held", "Total Funds", 
                       "Tamba", "Candi", "Sona", "Tongbi", "Yinbi", "Jinbi", "Tamra", "Rajat", "Svarnam",
                         "Doka", "Ginka", "Kinka", "Nodokoin", "Rodokoin", "Huaqian", "Bulawan"]
        #add header to grid
        self.organizeRow(self.header)
        
        #create list for first column
        self.column1 = ["Tamba", "Candi", "Sona", "Tongbi", "Yinbi", "Jinbi", "Tamra", "Rajat", "Svarnam",
                         "Doka", "Ginka", "Kinka", "Nodokoin", "Rodokoin", "Huaqian", "Bulawan"]
        #add column to grid
        self.organizeColumn(self.column1)

        #create list for currency hard values
        self.currency = [1.0, 32.0, 100.0, 0.5, 5.0, 500.0, 1.0, 50.0, 1000.0, 0.8, 8.0, 800.0, 0.75, 100.0, 20.0, 5.0]

        #create list for user input values
        self.user_values = [0.0] *16

        #create and add entries to grid
        self.createEntries()
        
        #create button to calculate
        self.calculate_button = Button(self.main_window, text="Calculate", command=self.calculate).grid(row=17, column=8)
        #create button to quit
        self.quit_button = Button(self.main_window, text="Quit", command=self.main_window.destroy).grid(row=17, column=9)


        mainloop()

    def calculate(self):
       #collect all user values
       self.user_values[0] = self.tamba.get()
       self.user_values[1] = self.candi.get()
       self.user_values[2] = self.sona.get()
       self.user_values[3] = self.tongbi.get()
       self.user_values[4] = self.yinbi.get()
       self.user_values[5] = self.jinbi.get()
       self.user_values[6] = self.tamra.get()
       self.user_values[7] = self.rajat.get()
       self.user_values[8] = self.svarnam.get()
       self.user_values[9] = self.doka.get()
       self.user_values[10] = self.ginka.get()
       self.user_values[11] = self.kinka.get()
       self.user_values[12] = self.nodokoin.get()
       self.user_values[13] = self.rodokoin.get()
       self.user_values[14] = self.huanqian.get()
       self.user_values[15] = self.bulawan.get()

       #multiply corresponding values together 
       totalValueCoin = 0
       for i in range(len(self.currency)):
           #total value of coin calculated
           totalValueCoin += self.user_values[i] * self.currency[i]
       for i in range(len(self.currency)):
           #calculate and print total funds in the column
           temp = totalValueCoin / self.currency[i]
           labTotalFund = Label(self.main_window, text=str(round(temp, 2)), relief=SUNKEN, justify=CENTER, width=10, height=2, anchor=CENTER)
           labTotalFund.grid(row=1+i, column=2)
       for i in range(len(self.currency)):
           #divide hard value by other currencies, multiply by amount held and print across row
           for j in range(len(self.currency)):
               temp2 = self.currency[i] / self.currency[j] * self.user_values[i]
               labConvertedValue = Label(self.main_window, text=str(round(temp2, 2)), relief=SUNKEN, justify=CENTER, width=10, height=2, anchor=CENTER)
               labConvertedValue.grid(row=i+1, column=j+3)

           pass

    def organizeRow(self, list1):
        #format the rows in the table
        for i in range(len(list1)):
            lab1 = Label(self.main_window, text=list1[i], relief=SUNKEN, justify=CENTER, width=10, height=2)
            lab1.grid(row=0, column=i)

    def organizeColumn(self, list1):
        #format the columns in the table
        for i in range(len(list1)):
            lab2 = Label(self.main_window, text=list1[i], relief=SUNKEN, justify=CENTER, width=10, height=2)
            lab2.grid(row=i+1, column=0)

    def createEntries(self):
             #create variables for the 16 currencies
     self.tamba = DoubleVar()
     self.candi = DoubleVar()
     self.sona = DoubleVar()
     self.tongbi = DoubleVar()
     self.yinbi = DoubleVar()
     self.jinbi = DoubleVar()
     self.tamra = DoubleVar()
     self.rajat = DoubleVar()
     self.svarnam = DoubleVar()
     self.doka = DoubleVar()
     self.ginka = DoubleVar()
     self.kinka = DoubleVar()
     self.nodokoin = DoubleVar()
     self.rodokoin = DoubleVar()
     self.huanqian = DoubleVar()
     self.bulawan = DoubleVar()
     
     
     #create entries for the currencies
     self.tamba_entry = Entry(self.main_window, textvariable=self.tamba, width=10).grid(row=1, column=1)
     self.candi_entry = Entry(self.main_window, textvariable=self.candi, width=10).grid(row=2, column=1)
     self.sona_entry = Entry(self.main_window, textvariable=self.sona, width=10).grid(row=3, column=1)
     self.tongbi_entry = Entry(self.main_window, textvariable=self.tongbi, width=10).grid(row=4, column=1)
     self.yinbi_entry = Entry(self.main_window, textvariable=self.yinbi, width=10).grid(row=5, column=1)
     self.jinbi_entry = Entry(self.main_window, textvariable=self.jinbi, width=10).grid(row=6, column=1)
     self.tamra_entry = Entry(self.main_window, textvariable=self.tamra, width=10).grid(row=7, column=1)
     self.rajat_entry = Entry(self.main_window, textvariable=self.rajat, width=10).grid(row=8, column=1)
     self.svarnam_entry = Entry(self.main_window, textvariable=self.svarnam, width=10).grid(row=9, column=1)
     self.doka_entry = Entry(self.main_window, textvariable=self.doka, width=10).grid(row=10, column=1)
     self.ginka_entry = Entry(self.main_window, textvariable=self.ginka, width=10).grid(row=11, column=1)
     self.kinka_entry = Entry(self.main_window, textvariable=self.kinka, width=10).grid(row=12, column=1)
     self.nodokoin_entry = Entry(self.main_window, textvariable=self.nodokoin, width=10).grid(row=13, column=1)
     self.rodokoin_entry = Entry(self.main_window, textvariable=self.rodokoin, width=10).grid(row=14, column=1)
     self.huanqian_entry = Entry(self.main_window, textvariable=self.huanqian, width=10).grid(row=15, column=1)
     self.bulawan_entry = Entry(self.main_window, textvariable=self.bulawan, width=10).grid(row=16, column=1)


if __name__ == "__main__":
    myGui()