#Frontend

from tkinter import *
import tkinter.messagebox
import pshop_backend
import mysql.connector


root = Tk()
root.title("Petshop Database Management System")
root.geometry("1200x700")
#root.config(bg="grey")

TitleFrame = Frame(root, bd=2, padx=5, pady=8, relief=RIDGE)
TitleFrame.pack(side = TOP)

Label(TitleFrame ,font=('arial', 20, 'bold'), text="Petshop Database Management").grid()


#===============================================================================
def est_conn():
    pshop_backend.connect_to_database(hostname.get(), username.get(), password.get(), databasename.get())
    tkinter.messagebox.showinfo("Register", "Connected to database")
    ConnectFrame.destroy()
    DisplayData()

def connect_to_database():
    global ConnectFrame
    ConnectFrame = Toplevel(root)
    ConnectFrame.title("Connect to database")
    ConnectFrame.geometry("300x300")

    global hostname, username, password, databasename

    hostname = StringVar()
    username = StringVar()
    password = StringVar()
    databasename = StringVar()

    hostname.set("localhost")
    databasename.set("my_petshop_gui2")   # sets the default value


    Label(ConnectFrame, text = "Please enter details below").pack()
    Label(ConnectFrame, text ="").pack()
    Label(ConnectFrame, text ="Mysql server address").pack()
    mysql_add = Entry(ConnectFrame, textvariable = hostname)
    mysql_add.pack()
    Label(ConnectFrame, text =" Mysql Username").pack()
    mysql_uname = Entry(ConnectFrame, textvariable = username)
    mysql_uname.pack()
    Label(ConnectFrame, text ="Mysql Password").pack()
    mysql_pass = Entry(ConnectFrame, textvariable = password, show="*")
    mysql_pass.pack()
    Label(ConnectFrame, text ="Database Name").pack()
    mysql_pass = Entry(ConnectFrame, textvariable = databasename)
    mysql_pass.pack()
    Label(ConnectFrame, text ="").pack()
    Button(ConnectFrame, text="Connect", command = est_conn).pack()

#=========================Functions======================================
def DisplayData():
    info_list.delete(0,END)
    #info_list.insert(0, "PetID     PetType            NumInStock      NumSold     Price                 PetSubType")
    rows = pshop_backend.viewDataAll()
    #info_list.insert(END, rows[0][1], rows[2])
    for row in rows:
        info_list.insert(END, str(row[0]) + '%15s' % str(row[1]) + '%15s' % str(row[2])\
                         + '%15s' % str(row[3]) + '%18s' % str(row[4]) + '%15s' % str(row[5]) + '%25s' % str(row[6]) + '%15s' % str(row[7])\
                         + '%15s' % str(row[8]) + '%15s' % str(row[9]), str(""))


def m_exit():
    root.destroy()


#====================================================================================

MesgFrame = LabelFrame(root, font=('arial', 20, 'bold'), text="Pet & Client Info\n")
MesgFrame.pack(side = TOP)

info_list = Listbox(MesgFrame, width = 100, height = 20)
info_list.grid(row = 0, column = 0, padx = 20)

#================================Pet Table=============================================
#========================================================================================================
#========================================================================================================
#========================================================================================================
def pet_table():

    PetFrame = Toplevel(root)
    PetFrame.title("Pet Info")
    PetFrame.geometry("600x700")

    Label(PetFrame).grid(row=0, column=1)
    Label(PetFrame).grid(row=1, column=1)
    Label(PetFrame, text = "Pet Input").grid(row=2, column=2)
    lblPetType = Label(PetFrame, text = "Pet Type")
    lblPetType.grid(row=3, column = 0, columnspan = 2)
    txtPetType = Entry(PetFrame, width = 20)
    txtPetType.grid(row=3, column = 2, columnspan = 2)

    lblPetSubType = Label(PetFrame, text = "Pet Sub Type")
    lblPetSubType.grid(row=4, column = 0, columnspan = 2)
    txtPetSubType = Entry(PetFrame, width = 20)
    txtPetSubType.grid(row=4, column = 2, columnspan = 2)

    lblNumStock = Label(PetFrame, text = "Number In Stock")
    lblNumStock.grid(row=5, column = 0, columnspan = 2)
    txtNumStock = Entry(PetFrame, width = 20)
    txtNumStock.grid(row=5, column = 2, columnspan = 2)

    lblNumSold = Label(PetFrame, text = "Number Sold")
    lblNumSold.grid(row=6, column = 0, columnspan = 2)
    txtNumSold = Entry(PetFrame, width = 20)
    txtNumSold.grid(row=6, column = 2, columnspan = 2)

    lblPetPrice = Label(PetFrame, text = "Price in USD")
    lblPetPrice.grid(row=7, column = 0, columnspan = 2)
    txtPetPrice = Entry(PetFrame, width = 20)
    txtPetPrice.grid(row=7, column = 2, columnspan = 2)

    Label(PetFrame).grid(row=8, column=1)
    Label(PetFrame).grid(row=9, column=1)
    Label(PetFrame, text = "Pet Table").grid(row=10, column=2)

    #=======Functions for the Function===============
    def display_pet():
        pet_list.delete(0,END)
    #info_list.insert(0, "PetID     PetType            NumInStock      NumSold     Price                 PetSubType")
        rows = pshop_backend.viewData('pet_info')
    #info_list.insert(END, rows[0][1], rows[2])
        for row in rows:
            #pet_list.insert(END, str(row[0]) + '%15s' % str(row[1]) + '%15s' % str(row[2])\
                       #  + '%15s' % str(row[3]) + '%18s' % str(row[4]) + '%15s' % str(row[5]), str(""))
            pet_list.insert(END, row)


    def clearData():
     txtPetType.delete(0,END)
     txtPetSubType.delete(0,END)
     txtNumStock.delete(0,END)
     txtNumSold.delete(0,END)
     txtPetPrice.delete(0,END)

     def add_data():
         pass

    def pet_Rec(event):
            global psd
            searchStd = pet_list.curselection()[0]
            psd = pet_list.get(searchStd)

            txtPetType.delete(0,END)
            txtPetType.insert(END, psd[1])
            txtPetSubType.delete(0,END)
            txtPetSubType.insert(END,psd[2])
            txtNumStock.delete(0,END)
            txtNumStock.insert(END,psd[3])
            txtNumSold.delete(0,END)
            txtNumSold.insert(END,psd[4])
            txtPetPrice.delete(0,END)
            txtPetPrice.insert(END,psd[5])

    def addData():
        if(len(txtPetType.get())!=0):
            pshop_backend.addPetRec(txtPetType.get(), txtPetSubType.get(), txtNumStock.get(), txtNumSold.get(), txtPetPrice.get())
            pet_list.delete(0,END)
            pet_list.insert(END, (txtPetType.get(), txtPetSubType.get(), txtNumStock.get(), txtNumSold.get(), txtPetPrice.get()))
        print(txtPetType.get())

    def DeleteData():
        if(len(txtPetSubType.get())!=0):
            pshop_backend.deleteRec('pet_info', 'pet_id', psd[0])
            clearData()
            display_pet()


    def searchDatabase():
        pet_list.delete(0,END)
        for row in pshop_backend.searchData(txtPetType.get(), txtPetSubType.get(), txtNumStock.get(), txtNumSold.get(), txtPetPrice.get()):
            pet_list.insert(END, row, str(""))


    def update():
        if len(txtPetType.get()) != 0:
            pshop_backend.dataUpdate(psd[0], txtPetType.get(), txtPetSubType.get(), txtNumStock.get(), txtNumSold.get(), txtPetPrice.get())
            display_pet()



#===========Listbox & ScrollBar=======================

    scrollbar = Scrollbar(PetFrame)
    scrollbar.grid(row=11, column=9, sticky='ns')

    pet_list = Listbox(PetFrame, width = 60, height = 20, yscrollcommand = scrollbar.set)
    pet_list.bind('<<ListboxSelect>>', pet_Rec)
    pet_list.grid(row=11, column=0, columnspan=9, padx=15)
    scrollbar.config(command = pet_list.yview)


    #=========Buttons=============================
    petAddData = Button(PetFrame, text="Add New", command = addData)
    petAddData.grid(row=12, column=0)

    petDisplayData = Button(PetFrame, text="Display", command = display_pet)
    petDisplayData.grid(row=12, column=1)

    petClearData = Button(PetFrame, text="Clear", command = clearData)
    petClearData.grid(row=12, column=2)

    petDeleteData = Button(PetFrame, text="Delete", command = DeleteData)
    petDeleteData.grid(row=12, column=3)

    petSearchData = Button(PetFrame, text="Search", command = searchDatabase)
    petSearchData.grid(row=12, column=4)

    petUpdateData = Button(PetFrame, text="Update", command = update)
    petUpdateData.grid(row=12, column=5)

    petExit = Button(PetFrame, text="Exit", command = lambda: pshop_backend.close_win(PetFrame))
    petExit.grid(row=12, column=6)


#================================Transaction Table=============================================
#========================================================================================================
#========================================================================================================
#========================================================================================================
def tran_table():

    tranFrame = Toplevel(root)
    tranFrame.title("Transaction Info")
    tranFrame.geometry("600x700")

    Label(tranFrame).grid(row=0, column=1)
    Label(tranFrame).grid(row=1, column=1)
    Label(tranFrame, text = "Transaction Input").grid(row=2, column=2)
    lblDate = Label(tranFrame, text = "Date")
    lblDate.grid(row=3, column = 0, columnspan = 2)
    txtDate = Entry(tranFrame, width = 20)
    txtDate.grid(row=3, column = 2, columnspan = 2)

    lblCustomer = Label(tranFrame, text = "Customer Name")
    lblCustomer.grid(row=4, column = 0, columnspan = 2)
    txtCustomer = Entry(tranFrame, width = 20)
    txtCustomer.grid(row=4, column = 2, columnspan = 2)

    lblPetId = Label(tranFrame, text = "PetId")
    lblPetId.grid(row=5, column = 0, columnspan = 2)
    txtPetId = Entry(tranFrame, width = 20)
    txtPetId.grid(row=5, column = 2, columnspan = 2)

    lblQuantity = Label(tranFrame, text = "Quantity")
    lblQuantity.grid(row=6, column = 0, columnspan = 2)
    txtQuantity = Entry(tranFrame, width = 20)
    txtQuantity.grid(row=6, column = 2, columnspan = 2)

    lblTotalPrice = Label(tranFrame, text = "Total Price in USD")
    lblTotalPrice.grid(row=7, column = 0, columnspan = 2)
    txtTotalPrice = Entry(tranFrame, width = 20)
    txtTotalPrice.grid(row=7, column = 2, columnspan = 2)

    Label(tranFrame).grid(row=8, column=1)
    Label(tranFrame).grid(row=9, column=1)
    Label(tranFrame, text = "Transaction Table").grid(row=10, column=2)


    #=============================Functions============================
    #=======Functions for the Function===============
    def display_tran():
        tran_list.delete(0,END)
    #info_list.insert(0, "PetID     PetType            NumInStock      NumSold     Price                 PetSubType")
        rows = pshop_backend.viewData('transaction_info')
    #info_list.insert(END, rows[0][1], rows[2])
        for row in rows:
            #tran_list.insert(END, str(row[0]) + '%15s' % str(row[1]) + '%15s' % str(row[2])\
            #             + '%15s' % str(row[3]) + '%18s' % str(row[4]) + '%15s' % str(row[5]), str(""))
            tran_list.insert(END, row)


    def clearData():
        txtDate.delete(0,END)
        txtCustomer.delete(0,END)
        txtPetId.delete(0,END)
        txtQuantity.delete(0,END)
        txtTotalPrice.delete(0,END)



    def tran_Rec(event):
        global sd
        searchStd = tran_list.curselection()[0]
        sd = tran_list.get(searchStd)

        txtDate.delete(0,END)
        txtDate.insert(END, sd[1])
        txtCustomer.delete(0,END)
        txtCustomer.insert(END,sd[2])
        txtPetId.delete(0,END)
        txtPetId.insert(END,sd[3])
        txtQuantity.delete(0,END)
        txtQuantity.insert(END,sd[4])
        txtTotalPrice.delete(0,END)
        txtTotalPrice.insert(END,sd[5])


    def addData():
        if(len(txtCustomer.get())!=0):
            pshop_backend.addTranRec(str(txtDate.get()), txtCustomer.get(), txtPetId.get(), txtQuantity.get(), txtTotalPrice.get())
            tran_list.delete(0,END)
            tran_list.insert(END, (txtDate.get(), txtCustomer.get(), txtPetId.get(), txtQuantity.get(), txtTotalPrice.get()))


    def DeleteData():
        if(len(txtCustomer.get())!=0):
            pshop_backend.deleteRec('transaction_info', 'tran_id', sd[0])
            clearData()
            display_tran()

    def searchDatabase():
        tran_list.delete(0,END)
        for row in pshop_backend.searchTranData(txtDate.get(), txtCustomer.get(), txtPetId.get(), txtQuantity.get(), txtTotalPrice.get()):
            tran_list.insert(END,row,str(""))

    def update():
        if len(txtDate.get()) != 0:
            pshop_backend.tran_dataUpdate(sd[0], txtDate.get(), txtCustomer.get(), txtPetId.get(), txtQuantity.get(), txtTotalPrice.get())
            display_tran()


    #===========Listbox & ScrollBar=======================

    scrollbar = Scrollbar(tranFrame)
    scrollbar.grid(row=11, column=9, sticky='ns')

    tran_list = Listbox(tranFrame, width = 60, height = 20, yscrollcommand = scrollbar.set)
    tran_list.bind('<<ListboxSelect>>', tran_Rec)
    tran_list.grid(row=11, column=0, columnspan=9, padx=15)
    scrollbar.config(command = tran_list.yview)

    #===================Buttons=========================
    tranAddData = Button(tranFrame, text="Add New", command = addData)
    tranAddData.grid(row=12, column=0)

    tranDisplayData = Button(tranFrame, text="Display", command = display_tran)
    tranDisplayData.grid(row=12, column=1)

    tranClearData = Button(tranFrame, text="Clear", command = clearData)
    tranClearData.grid(row=12, column=2)

    tranDeleteData = Button(tranFrame, text="Delete", command = DeleteData)
    tranDeleteData.grid(row=12, column=3)

    tranSearchData = Button(tranFrame, text="Search", command = searchDatabase)
    tranSearchData.grid(row=12, column=4)

    tranUpdateData = Button(tranFrame, text="Update", command = update)
    tranUpdateData.grid(row=12, column=5)

    tranExit = Button(tranFrame, text="Exit", command = lambda: pshop_backend.close_win(tranFrame))
    tranExit.grid(row=12, column=6)
    #========================================================================================================
    #========================================================================================================
    #========================================================================================================





#===========================================================================
BotFrame = Frame(root)
BotFrame.pack(side=TOP)
bot0 = Button(BotFrame, text="Connect to Database", command = connect_to_database)
bot0.grid(row=0, column=0)
bot4 = Button(BotFrame, text="Display Database", command = DisplayData)
bot4.grid(row=0, column=1)
bot1 = Button(BotFrame, text="Show Pet Database", command = pet_table)
bot1.grid(row=0, column=2)
bot2 = Button(BotFrame, text="Show Customer Database", command = tran_table)
bot2.grid(row=0, column=3)
bot3 = Button(BotFrame, text="Exit", command = m_exit)
bot3.grid(row=0, column=4)



root.mainloop()
