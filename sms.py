import tkinter as tk
from tkinter import ttk 
from PIL import ImageTk
from tkinter import messagebox
from tkinter import filedialog
import ttkthemes
import pymysql
import time
import pandas as pd


def clock():
    global current_date, current_time
    
    current_date = time.strftime('%m/%d/%Y')
    current_time = time.strftime('%I:%M:%S %p')
    
    datetime_label.config(text=f'Date: {current_date}\nTime: {current_time}')
    datetime_label.after(1000,clock)
    
    
# common function for adding, searching, and updateing       
def label_entry_data(title, button_text, cmd):
    global regno_entry, name_entry, dob_entry, gender_entry, bloodgroup_entry, dept_entry, batch_entry, batch_entry, contact_entry, mail_entry, address_entry, window_screen
    
    # create window
    window_screen = tk.Toplevel()
    window_screen.geometry('620x728+300+120')
    window_screen.grab_set()
    window_screen.resizable(0,0)
    window_screen.title(title)
    window_screen.configure(bg='#a713da')
    window_screen.iconphoto(False, icon)
    
    # registraion number label and entry
    regno_label = tk.Label(window_screen, text='Registration Number', font=('Comic Sans MS', 15, 'bold'), bg='#a713da', fg='#080808')
    regno_label.grid(row=0, column=0, padx=30, pady=15)
    regno_entry = tk.Entry(window_screen, font=('Comic Sans MS', 13, 'bold'), fg='#a713da',  width=30)
    regno_entry.grid(row=0, column=1, padx=10, pady=15)
    
    # name label and entry
    name_label = tk.Label(window_screen, text='Name', font=('Comic Sans MS', 15, 'bold'), bg='#a713da', fg='#080808')
    name_label.grid(row=1, column=0, padx=30, pady=15)
    name_entry = tk.Entry(window_screen, font=('Comic Sans MS', 13, 'bold'), fg='#a713da',  width=30)
    name_entry.grid(row=1, column=1, padx=10, pady=15)
    
    # date of birth label and entry
    dob_label = tk.Label(window_screen, text='Date of Birth', font=('Comic Sans MS', 15, 'bold'), bg='#a713da', fg='#080808')
    dob_label.grid(row=2, column=0, padx=30, pady=15)
    dob_entry = tk.Entry(window_screen, font=('Comic Sans MS', 13, 'bold'), fg='#a713da',  width=30)
    dob_entry.grid(row=2, column=1, padx=10, pady=15)
    
    # gender label and entry
    gender_label = tk.Label(window_screen, text='Gender', font=('Comic Sans MS', 15, 'bold'), bg='#a713da', fg='#080808')
    gender_label.grid(row=3, column=0, padx=30, pady=15)
    gender_entry = tk.Entry(window_screen, font=('Comic Sans MS', 13, 'bold'), fg='#a713da',  width=30)
    gender_entry.grid(row=3, column=1, padx=10, pady=15)
    
    # blood group label and entry
    bloodgroup_label = tk.Label(window_screen, text='Blood Group', font=('Comic Sans MS', 15, 'bold'), bg='#a713da', fg='#080808')
    bloodgroup_label.grid(row=4, column=0, padx=30, pady=15)
    bloodgroup_entry = tk.Entry(window_screen, font=('Comic Sans MS', 13, 'bold'), fg='#a713da',  width=30)
    bloodgroup_entry.grid(row=4, column=1, padx=10, pady=15)
    
    #department label and entry
    dept_label = tk.Label(window_screen, text='Department', font=('Comic Sans MS', 15, 'bold'), bg='#a713da', fg='#080808')
    dept_label.grid(row=5, column=0, padx=30, pady=15)
    dept_entry = tk.Entry(window_screen, font=('Comic Sans MS', 13, 'bold'), fg='#a713da',  width=30)
    dept_entry.grid(row=5, column=1, padx=10, pady=15)
    
    # batch label and entry
    batch_label = tk.Label(window_screen, text='Batch', font=('Comic Sans MS', 15, 'bold'), bg='#a713da', fg='#080808')
    batch_label.grid(row=6, column=0, padx=30, pady=15)
    batch_entry = tk.Entry(window_screen, font=('Comic Sans MS', 13, 'bold'), fg='#a713da',  width=30)
    batch_entry.grid(row=6, column=1, padx=10, pady=15)
    
    # contact label and entry
    contact_label = tk.Label(window_screen, text='Contact', font=('Comic Sans MS', 15, 'bold'), bg='#a713da', fg='#080808')
    contact_label.grid(row=7, column=0, padx=30, pady=15)
    contact_entry = tk.Entry(window_screen, font=('Comic Sans MS', 13, 'bold'), fg='#a713da',  width=30)
    contact_entry.grid(row=7, column=1, padx=10, pady=15)
    
    # mail label and entry
    mail_label = tk.Label(window_screen, text='Mail', font=('Comic Sans MS', 15, 'bold'), bg='#a713da', fg='#080808')
    mail_label.grid(row=8, column=0, padx=30, pady=15)
    mail_entry = tk.Entry(window_screen, font=('Comic Sans MS', 13, 'bold'), fg='#a713da',  width=30)
    mail_entry.grid(row=8, column=1, padx=10, pady=15)
    
    # address label and entry
    address_label = tk.Label(window_screen, text='Address', font=('Comic Sans MS', 15, 'bold'), bg='#a713da', fg='#080808')
    address_label.grid(row=9, column=0, padx=30, pady=15)
    address_entry = tk.Entry(window_screen, font=('Comic Sans MS', 13, 'bold'), fg='#a713da',  width=30)
    address_entry.grid(row=9, column=1, padx=10, pady=15)
    
    # button
    button = ttk.Button(window_screen, text=button_text, command=cmd)
    button.grid(row=10,column=1, padx=10, pady=20)
    
    # only for updating purpose
    if  title == 'Update Student Details':
        try:
            index_row = student_table.focus()
            content = student_table.item(index_row)
            content_data = content['values']
        
            regno_entry.insert(0, content_data[0])
            regno_entry.configure(state='disabled')
            name_entry.insert(0, content_data[1])
            dob_entry.insert(0, content_data[2])
            gender_entry.insert(0, content_data[3])
            bloodgroup_entry.insert(0, content_data[4])
            dept_entry.insert(0, content_data[5])
            batch_entry.insert(0, content_data[6])
            contact_entry.insert(0, content_data[7])
            mail_entry.insert(0, content_data[8])
            address_entry.insert(0, content_data[9])
        
        except:
            messagebox.showerror('ERROR', 'To update a student data, select a record from the database',parent=window_screen)
            window_screen.destroy()
           
           
# function for adding students
def add_student():
    if (regno_entry.get()=='' or name_entry.get()=='' or dob_entry.get()=='' or  gender_entry.get()=='' or bloodgroup_entry.get()=='' or 
        dept_entry.get()=='' or batch_entry.get()=='' or contact_entry.get()=='' or mail_entry.get()=='' or address_entry.get()==''):
        messagebox.showerror('ERROR', 'To add a student to the database, all fields must be filled out.', parent=window_screen)
    else:
        try:
            # sql query for inserting or adding students data
            query = 'INSERT INTO student (regno, name, dob, gender, bloodgroup, dept, batch, contact, mail, address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            my_cursor.execute(query, (regno_entry.get(), name_entry.get(), dob_entry.get(), gender_entry.get(), bloodgroup_entry.get(), dept_entry.get(), 
                                    batch_entry.get(), contact_entry.get(), mail_entry.get(), address_entry.get()))
            conn.commit()
            result = messagebox.askyesno('WARNING','Data added successfully. Do you want to clean?', parent=window_screen)

            # to clear the current data in table
            if result:
                regno_entry.delete(0, 'end')
                name_entry.delete(0, 'end')
                dob_entry.delete(0, 'end')
                gender_entry.delete(0, 'end')
                bloodgroup_entry.delete(0, 'end')
                dept_entry.delete(0, 'end')
                batch_entry.delete(0, 'end')
                contact_entry.delete(0, 'end')
                mail_entry.delete(0, 'end')
                address_entry.delete(0, 'end')
            else:
                pass
            
        except:
            messagebox.showerror('ERROR', 'Registration Number already exists', parent=window_screen)
            return
        
        # sql query for showing the table
        query = 'SELECT * FROM student'
        my_cursor.execute(query)
        
        fetched_data = my_cursor.fetchall()
        
        student_table.delete(*student_table.get_children())
        
        for data in fetched_data:
            student_table.insert('', 'end', values=data)
    

# for deleting a student data
def delete_student():
    try:
        index_row = student_table.focus()
        content = student_table.item(index_row)
        content_regno = content['values'][0]
    
    except:
        messagebox.showerror('ERROR', 'To delete a student data, select a record from the database')
        return

    # sql query for deleting a selected student from the table
    query = 'DELETE FROM student WHERE regno=%s'
    my_cursor.execute(query, content_regno)
    conn.commit()
            
    messagebox.showinfo('DELETED', f'Registration Number {content_regno} was successfully erased.')
    
    # sql query for showing the table        
    query = 'SELECT * FROM student'
    my_cursor.execute(query)
    fetch_data = my_cursor.fetchall()
            
    student_table.delete(*student_table.get_children())
            
    for data in fetch_data:
        student_table.insert('', 'end', values=data)
    
    
# for searching student data
def search_student():
    # sql query for searching student in the table for a given data
    query = 'SELECT * FROM student WHERE regno=%s or name=%s or dob=%s or gender=%s or bloodgroup=%s or dept=%s or batch=%s or contact=%s or mail=%s or address=%s' 
    my_cursor.execute(query, (regno_entry.get(), name_entry.get(), dob_entry.get(), gender_entry.get(), bloodgroup_entry.get(), dept_entry.get(),
                                batch_entry.get(), contact_entry.get(), mail_entry.get(), address_entry.get()))
    
    fetched_data = my_cursor.fetchall()
    
    student_table.delete(*student_table.get_children())
    
    for data in fetched_data:
        student_table.insert('', 'end', values=data)
        
    if len(fetched_data) == 0:
        messagebox.showerror('ERROR', 'There was no record found in the database', parent=window_screen)


# for updating student data
def update_student():
    # sql query for updating the data of a selected student in the table
    query = 'UPDATE student SET name=%s, dob=%s, gender=%s, bloodgroup=%s, dept=%s, batch=%s, contact=%s, mail=%s, address=%s WHERE regno=%s'
    my_cursor.execute(query, (name_entry.get(), dob_entry.get(), gender_entry.get(), bloodgroup_entry.get(), dept_entry.get(),
                                batch_entry.get(), contact_entry.get(), mail_entry.get(), address_entry.get(), regno_entry.get()))
    conn.commit()
    
    messagebox.showinfo('SUCCES', f'Registration Number {regno_entry.get()} is successfully updated', parent=window_screen)
    
    window_screen.destroy()
    
    show_student()
        
        
 # for showing the whole data       
def show_student():
    # sql query for showing the table
    query = 'SELECT * FROM student'
    my_cursor.execute(query)
    fetch_data = my_cursor.fetchall()
    
    student_table.delete(*student_table.get_children())
    
    for data in fetch_data:
        student_table.insert('', 'end', values=data)
        
    if len(fetch_data) == 0:
        messagebox.showerror('ERROR', 'There are no records in the database', parent=window)
      
      
 # for clearing the table       
def clear_table():
        student_table.delete(*student_table.get_children())
        

# for exporting the data into .csv format   
def export_data():
    path = filedialog.asksaveasfilename(defaultextension='.csv')
    index = student_table.get_children()
    list = []
    
    for data in index:
       content = student_table.item(data)
       data_list = content['values']
       list.append(data_list)
     
     # using pandas to convert the aq table to a dataframe(in tabular format)  
    df = pd.DataFrame(list, columns=['Registration Number', 'Name', 'Date of Birth', 'Gender', 'Blood Group', 
                                     'Deptartment', 'Batch','Contact', 'Mail', 'Address'])  
    df.to_csv(path, index=False)
    
    messagebox.showinfo('SUCCESS', 'Data successfully exported', parent=window)


# for exiting the window
def exit():
    ans = messagebox.askyesno('WARNING', 'Are you sure you want to exit?', parent=window)
    
    if ans:
        window.destroy()
    else:
        pass


# for connecting the mysql server and creating database and table
def connect_database():
    def connect():
        global my_cursor, conn
        
        try:
            conn = pymysql.connect(host = hostname_entry.get(), user = username_entry.get(), password = password_entry.get())
            my_cursor = conn.cursor()
            
        except:
            messagebox.showerror('ERROR', 'Please Enter Correct Credentials', parent=connect_window)
            
        try:
            # sql query for creating the database
            query = 'CREATE DATABASE students_management_database'
            my_cursor.execute(query)
            # sql query to set the database as default
            query = 'USE students_management_database'
            my_cursor.execute(query)
            # sql query for creating the  table
            query = 'CREATE TABLE student ( regno VARCHAR(20) NOT NULL PRIMARY KEY,' \
                                    'name VARCHAR(50) NOT NULL,' \
                                    'dob VARCHAR(20) NOT NULL,' \
                                    'gender VARCHAR(20) NOT NULL,' \
                                    'bloodgroup VARCHAR(15) NOT NULL,' \
                                    'dept VARCHAR(30) NOT NULL,' \
                                    'batch VARCHAR(10) NOT NULL,' \
                                    'contact VARCHAR(10) NOT NULL,' \
                                    'mail VARCHAR(50) NOT NULL,' \
                                    'address VARCHAR(100) NOT NULL )'
            my_cursor.execute(query)
            
        except:
            # sql query to set the database as default
            query = 'USE students_management_database'
            my_cursor.execute(query)
        
        # when we connect to the database the left frame button will be visible(nornal to use)
        connect_window.destroy()    
        add_student_button.config(state='normal')
        delete_student_button.config(state='normal')
        search_student_button.config(state='normasl')
        update_student_button.config(state='normal')
        show_student_button.config(state='normal')
        export_student_button.config(state='normal')
        clear_student_button.config(state='normal')
     
     # create a window to connect mysql server            
    connect_window = tk.Toplevel()
    connect_window.grab_set()
    connect_window.geometry('470x250+700+350')
    connect_window.configure(bg='#a713da')
    connect_window.title('Database Connection')
    connect_window.resizable(0,0)
    connect_window.iconphoto(False, icon)
    
    

    # host name label
    hostname_label = tk.Label(connect_window, text='Host Name', font=('Comic Sans MS', 13, 'bold'), bg='#a713da', fg='#080808')
    hostname_label.grid(row=0, column=0, padx=30)

    hostname_entry = tk.Entry(connect_window, font=('Comic Sans MS', 13, 'bold'), bd=2, fg='#a713da')
    hostname_entry.grid(row=0, column=1, padx=40, pady=20)
    
    # user name label
    username_label = tk.Label(connect_window, text='User Name', font=('Comic Sans MS', 13, 'bold'), bg='#a713da', fg='#080808')
    username_label.grid(row=1, column=0, padx=30)

    username_entry = tk.Entry(connect_window, font=('Comic Sans MS', 13, 'bold'), bd=2, fg='#a713da')
    username_entry.grid(row=1, column=1, padx=40, pady=20)
    
    # password label
    password_label = tk.Label(connect_window, text='Password', font=('Comic Sans MS', 13, 'bold'), bg='#a713da', fg='#080808')
    password_label.grid(row=3, column=0, padx=30)

    password_entry = tk.Entry(connect_window, font=('Comic Sans MS', 13, 'bold'), bd=2, fg='#a713da')
    password_entry.grid(row=3, column=1, padx=40, pady=20)

    # connect button
    connect_button2 = ttk.Button(connect_window, text='Connect', command=connect)
    connect_button2.grid(row=4, column=1) 
    
    
    
# create a main window
window = ttkthemes.ThemedTk()

window.get_themes()
window.set_theme('breeze')

# create window
window.geometry('1280x768+275+100')
window.resizable(0,0)
window.title('Student Management System')
window.configure(bg='#9f00c5')

# icon for the window
global icon
icon = ImageTk.PhotoImage(file=r'icon.png')
window.iconphoto(False, icon)

# create date and time label
datetime_label = tk.Label(window, font=('Comic Sans MS', 15, 'bold'), bg='#9f00c5', fg='#080808')
datetime_label.place(x=47, y=10)
clock()

# create name label
name_label = tk.Label(window, text='STUDENT MANAGEMENT SYSTEM', font=('Microsoft Sans Serif', 20,'bold'), width=30, bg='#9f00c5', fg='#080808')
name_label.place(x=300, y=20)

# create a connect button for database
connect_button = ttk.Button(window, text='Connect Database', cursor='hand2', command=connect_database)
connect_button.place(x=1100, y=20)


# create left frame
left_frame = tk.Frame(window, bg='#9f00c5')
left_frame.place(x=25, y=80, width=300, height=650)

# create logo image
logo_img = ImageTk.PhotoImage(file=r'logo.png')
logo_label = tk.Label(left_frame, image=logo_img, bg='#9f00c5')
logo_label.grid(row=0, column=0, padx=20, pady=10)

# add student button
add_student_button = ttk.Button(left_frame, text='Add Student', cursor='hand2', width=25, state='disabled', 
                                command = lambda:label_entry_data('Add Student Details', 'ADD', add_student))
add_student_button.grid(row=1, column=0, padx=20, pady=20)

# delete student button
delete_student_button = ttk.Button(left_frame, text='Delete Student', cursor='hand2', width=25, state='disabled', 
                                   command=delete_student)
delete_student_button.grid(row=2, column=0, padx=20, pady=20)

# search student button
search_student_button = ttk.Button(left_frame, text='Search Student', cursor='hand2', width=25, state='disabled', 
                                   command = lambda:label_entry_data('Search Student Details', 'SEARCH', search_student))
search_student_button.grid(row=3, column=0, padx=20, pady=20)

# update student button
update_student_button = ttk.Button(left_frame, text='Update Student', cursor='hand2', width=25, state='disabled', 
                                   command = lambda:label_entry_data('Update Student Details', 'UPDATE', update_student))
update_student_button.grid(row=4, column=0, padx=20, pady=20)

# show student button
show_student_button = ttk.Button(left_frame, text='Show Student', cursor='hand2', width=25, state='disabled', 
                                 command=show_student)
show_student_button.grid(row=5, column=0, padx=20, pady=20)

# clear table
clear_student_button = ttk.Button(left_frame, text='Clear Table', cursor='hand2', width=25, state='disabled', 
                                    command=clear_table)
clear_student_button.grid(row=6, column=0, padx=20, pady=20)

# export data button
export_student_button = ttk.Button(left_frame, text='Export Student', cursor='hand2', width=25, state='disabled',
                                   command=export_data)
export_student_button.grid(row=7, column=0, padx=20, pady=20)

# exit button
exit_student_button = ttk.Button(left_frame, text='EXIT', cursor='hand2', width=25,
                                 command=exit)
exit_student_button.grid(row=8, column=0, padx=20, pady=40)



# create right frame
right_frame = tk.Frame(window, bg='white')
right_frame.place(x=300, y=80, width=950, height=650)

# create scroll bar for horizontal and vertical
scroll_Bar_x = tk.Scrollbar(right_frame, orient='horizontal') 
scroll_Bar_y = tk.Scrollbar(right_frame, orient='vertical') 

# create student table
student_table = ttk.Treeview(right_frame, columns=('Reg', 'Name', 'D.O.B', 'Gender', 'Blood Group', 'Dept', 'Batch','Contact', 'Mail', 'Address'),
                             xscrollcommand=scroll_Bar_x.set, yscrollcommand=scroll_Bar_y.set)

# scroll bar for horizontal and vertical scrolling purposes
scroll_Bar_x.config(command=student_table.xview, width=23)
scroll_Bar_y.config(command=student_table.yview, width=23)

scroll_Bar_x.pack(side='bottom', fill='x')
scroll_Bar_y.pack(side='right', fill='y')

student_table.pack(fill='both', expand=1)

# specifying a name
student_table.heading('Reg', text='Registration Number')
student_table.heading('Name', text='Name')
student_table.heading('D.O.B', text='Date of Birth')
student_table.heading('Gender', text='Gender')
student_table.heading('Blood Group', text='Blood Group')
student_table.heading('Dept', text='Department')
student_table.heading('Batch', text='Batch')
student_table.heading('Contact', text='Contact')
student_table.heading('Mail', text='Mail ID')
student_table.heading('Address', text='Address')

student_table.config(show='headings')

# configuring the column of the table
student_table.column('Reg',anchor='center',width=250)
student_table.column('Name',anchor='center',width=300)
student_table.column('D.O.B',anchor='center',width=170)
student_table.column('Gender',anchor='center',width=170)
student_table.column('Blood Group',anchor='center',width=170)
student_table.column('Dept',anchor='center',width=170)
student_table.column('Batch',anchor='center',width=170)
student_table.column('Contact',anchor='center',width=190)
student_table.column('Mail',anchor='center',width=300)
student_table.column('Address',anchor='center',width=600)

# styling the table
style = ttk.Style()
style.configure('Treeview', rowheight=35, font=('aerial', 13, 'bold'), foreground='#9f00c5', background='#f5f5f5')
style.configure('Treeview.Heading', font=('Comic Sans MS', 15, 'bold'), foreground='#080808')


window.mainloop()
