from tkinter import *
from tkinter import messagebox
import sqlite3


# *********************************************************************************

class Db:
    '''Klasa zawierajaca polaczenie z baza danych i metody oparte na tym polaczeniu'''

    conn = sqlite3.connect('employee.db')
    c = conn.cursor()

    # c.execute("""CREATE TABLE employees (
    #             name text,
    #             lastname text,
    #             position text,
    #             salary integer
    #             )""")

    # Dla klasy User:

    def insert_emp(self, emp):
        '''Metoda dodaje nowego pracownika'''

        with self.conn:
            self.c.execute("INSERT INTO employees VALUES (:name, :lastname, :position, :salary)",
                           {'name': emp.name, 'lastname': emp.lastname, 'position': emp.position, 'salary': emp.salary})
            # self.conn.commit()

    def get_emps(self):
        '''Metoda wyswietla wszystkich pracownikow'''

        self.c.execute("SELECT * FROM employees ORDER BY lastname")
        return self.c.fetchall()

    def remove_emp(self, emp):
        '''Metoda usuwa konkretnego pracownika'''

        with self.conn:
            self.c.execute(
                "DELETE from employees WHERE name = :name AND lastname = :lastname AND position = :position AND salary = :salary",
                {'name': emp.name, 'lastname': emp.lastname, 'position': emp.position, 'salary': emp.salary})

    # Dla klasy HR:

    def get_emp(self, emp):
        self.c.execute(
            "SELECT * FROM employees WHERE name = :name AND lastname = :lastname AND position = :position AND salary = :salary",
            {'name': emp.name, 'lastname': emp.lastname, 'position': emp.position, 'salary': emp.salary})
        return self.c.fetchone()

    def get_emp_by_name(self, name):
        '''Metoda podaje pracownika o danym imieniu'''

        self.c.execute("SELECT * FROM employees WHERE name =:name", {'name': name})
        return self.c.fetchone()  # fetchone

    def get_emps_by_name(self, name):
        '''Metoda podaje wszystkich pracownikow o danym imieniu'''

        self.c.execute("SELECT * FROM employees WHERE name =:name", {'name': name})
        return self.c.fetchall()

    def get_emp_by_lastname(self, lastname):
        '''Metoda podaje pracownika o danym nazwisku'''

        self.c.execute("SELECT * FROM employees WHERE lastname =:lastname", {'lastname': lastname})
        return self.c.fetchone()

    def get_emps_by_lastname(self, lastname):
        '''Metoda podaje wszystkich pracownikow o danym nazwisku'''

        self.c.execute("SELECT * FROM employees WHERE lastname =:lastname", {'lastname': lastname})
        return self.c.fetchall()

    def get_emp_by_name_and_lastname(self, name, lastname):
        '''Metoda podaje pracownika o danym imieniu i nazwisku'''

        self.c.execute("SELECT * FROM employees WHERE name =:name AND lastname =:lastname",
                       {'name': name, 'lastname': lastname})
        return self.c.fetchone()

    def get_emps_by_name_and_lastname(self, name, lastname):
        '''Metoda podaje wszystkich pracownikow o danym imieniu i nazwisku'''

        self.c.execute("SELECT * FROM employees WHERE name =:name AND lastname =:lastname",
                       {'name': name, 'lastname': lastname})
        return self.c.fetchall()

    def get_emp_by_position(self, position):
        '''Metoda podaje pracownika o danym staowisku'''

        self.c.execute("SELECT * FROM employees WHERE position =:position", {'position': position})
        return self.c.fetchone()

    def get_emps_by_position(self, position):
        '''Metoda podaje wszystkich pracownikow o danym staowisku'''

        self.c.execute("SELECT * FROM employees WHERE position =:position", {'position': position})
        return self.c.fetchall()

    def get_emp_by_salary(self, salary):
        '''Metoda podaje wszystkich pracownikow o danej pensji'''

        self.c.execute("SELECT * FROM employees WHERE salary =:salary", {'salary': salary})
        return self.c.fetchone()

    def get_emps_by_salary(self, salary):
        '''Metoda podaje wszystkich pracownikow o danej pensji'''

        self.c.execute("SELECT * FROM employees WHERE salary =:salary", {'salary': salary})
        return self.c.fetchall()

    def get_emps_order_by_salary(self):
        '''Metoda podaje wszystkich pracownikow sortujac po pensji'''

        self.c.execute("SELECT * FROM employees ORDER BY salary")
        return self.c.fetchall()

    def emp_info(self):
        '''Metoda zwraca jakie informacje o pracownikach sa przechowywane w tabeli'''

        self.c.execute("SELECT * FROM employees")
        r = self.c.fetchone().keys()

        return r

    # Dla klasy Admin:

    def update_salary_by_position(self, position, salary):
        '''Metoda zmienia pensje wszystkich pracownikow na tym samym stanowisku'''

        with self.conn:
            self.c.execute("""UPDATE employees SET salary = :salary
                        WHERE position = :position""",
                           {'position': position, 'salary': salary})
            self.conn.commit()

    def update_emp_salary(self, emp, salary):
        '''Metoda zmienia pensje konkretnego pracownika'''

        with self.conn:
            self.c.execute("""UPDATE employees SET salary = :salary
                        WHERE name = :name AND lastname = :lastname AND position = :position""",
                           {'name': emp.name, 'lastname': emp.lastname, 'position': emp.position, 'salary': salary})
            self.conn.commit()

    def update_emp_lastname(self, emp, lastname):
        '''Metoda zmienia nazwisko konkretnego pracownika'''

        with self.conn:
            self.c.execute("""UPDATE employees SET lastname = :lastname
                        WHERE name = :name AND position = :position AND salary = :salary""",
                           {'name': emp.name, 'lastname': lastname, 'position': emp.position, 'salary': emp.salary})
            self.conn.commit()

    def update_emp(self, emp, name, lastname):
        '''Metoda zmienia imie i nazwisko danego pracownika'''

        with self.conn:
            self.c.execute("""UPDATE employees SET lastname = :lastname, name = :name
                        WHERE position = :position AND salary = :salary""",
                           {'name': name, 'lastname': lastname, 'position': emp.position, 'salary': emp.salary})
            self.conn.commit()

    def update_emp_position_and_salary(self, emp, position, salary):
        '''Metoda zmienia stanowisko i pensje danego pracownika'''

        with self.conn:
            self.c.execute("""UPDATE employees SET position = :position, salary = :salary
                        WHERE name = :name AND lastname = :lastname""",
                           {'name': emp.name, 'lastname': emp.lastname, 'position': position, 'salary': salary})
            self.conn.commit()

    def update_emp_position(self, position, position1):
        '''Metoda zmienia nazwe stanowiska'''

        with self.conn:
            self.c.execute("""UPDATE employees SET position = ? WHERE position = ?""", (position1, position))
            self.conn.commit()

    def remove_emps(self):
        '''Metoda usuwa wszystkich pracownikow z bazy danych'''
        with self.conn:
            self.c.execute("DELETE from employees")

    def remove_emps_by_position(self, position):
        '''Metoda usuwa wszystkich pracownikow z danego stanowiska'''

        with self.conn:
            self.c.execute("DELETE from employees WHERE position = :position",
                           {'position': position})


class Employee:
    '''Klasa, której obiekty odzwierciedlają rzędy w tabeli employees'''

    def __init__(self, name, lastname, position, salary):
        self.name = name
        self.lastname = lastname
        self.position = position
        self.salary = salary

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.lastname)

    def __repr__(self):
        return "Pracownik: {} {}, pracujacy na satnowisku {}, dostajacy pensje w wysokosci {}".format(self.name,
                                                                                                      self.lastname,
                                                                                                      self.position,
                                                                                                      self.salary)


class User:
    '''Klasa defaultowego uzytkownika, zawierajaca metody uzywane przez Admina i Pracownika HR'''

    user_type = ""
    objects = {}

    def __init__(self):
        self.name = Entry(frame)
        self.lastname = Entry(frame)
        self.position = Entry(frame)
        self.salary = Entry(frame)

    def create_user_view(self):

        Label(frame, text="Dodaj pracownika: ").grid(row=0, column=0)
        Button(frame, text="Dodaj", command=lambda: self.emp_info_add()).grid(row=0, column=1)

        Label(frame, text="Wyswietl wszystkich pracownikow: ").grid(row=1, column=0)
        Button(frame, text="Wyswietl", command=lambda: self.show_emps()).grid(row=1, column=1)

        Label(frame, text="Usun pracownika: ").grid(row=3, column=0)
        Button(frame, text="Usun", command=lambda: self.emp_info_del()).grid(row=3, column=1)

        Label(frame, text="Wyloguj: ").grid(row=12, column=0)
        Button(frame, text="Wyloguj", command=lambda: loginView.init_view(loginView())).grid(row=12, column=1)

    def clear(self):

        for widget in frame.winfo_children():
            widget.destroy()

    def view(self):

        a = loginView()

        if a.user_type.get() == 'Admin':
            Admin().admin_view()
        else:
            HR().hr_view()
        self.create_user_view()

    def emp_info(self):

        self.clear()

        Label(frame, text="Imie pracownika: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)

        Label(frame, text="Nazwisko pracownika: ").grid(row=2, column=0)
        self.lastname = Entry(frame)
        self.lastname.grid(row=2, column=1)

        Label(frame, text="Stanowisko pracownika: ").grid(row=3, column=0)
        self.position = Entry(frame)
        self.position.grid(row=3, column=1)

        Label(frame, text="Pensja pracownika: ").grid(row=4, column=0)
        self.salary = Entry(frame)
        self.salary.grid(row=4, column=1)

    def emp_info_name(self):

        self.clear()

        Label(frame, text="Podaj imie pracownika: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)

    def emp_info_add(self):

        self.emp_info()
        Button(frame, text="Wprowadz", command=lambda: self.emp_added()).grid(row=5, column=1)

    def emp_added(self):

        emp = Employee(self.name.get(), self.lastname.get(), self.position.get(), self.salary.get())
        Db().insert_emp(emp)
        messagebox.showinfo("Sukces", "Dodano nowego pracownika")
        self.view()

    def emp_info_del(self):

        self.emp_info()
        Button(frame, text="Wprowadz", command=lambda: self.emp_del()).grid(row=5, column=1)

    def emp_del(self):

        emp = Employee(self.name.get(), self.lastname.get(), self.position.get(), self.salary.get())

        if Db().get_emp(emp) is None:
            messagebox.showinfo("Blad", "Brak takiego pracownika")
        else:
            Db().remove_emp(emp)
            messagebox.showinfo("Sukces", "Usunieto pracownika z bazy danych")

        self.view()

    def show_emps(self):

        self.clear()

        rows = Db().get_emps()
        i = 0
        for row in rows:
            Label(frame, text=row).grid(row=i, column=0)
            i += 1

        Button(frame, text="Powrot", command=lambda: self.view()).grid(row=i, column=0)


class Admin(User):
    '''Klasa zawierajaca metody dostepne dla Admina'''

    def __init__(self):
        self.name1 = Entry(frame)
        self.lastname1 = Entry(frame)
        self.position1 = Entry(frame)
        self.salary1 = Entry(frame)
        super().__init__()

    def admin_view(self):

        self.clear()
        self.create_user_view()

        Label(frame, text="Zmien pensje wszystkich na stanowisku: ").grid(row=4, column=0)
        Button(frame, text="Zmien", command=lambda: self.salary_position_info()).grid(row=4, column=1)

        Label(frame, text="Zmien pensje pracownika: ").grid(row=5, column=0)
        Button(frame, text="Zmien", command=lambda: self.salary_info()).grid(row=5, column=1)

        Label(frame, text="Zmien nazwisko pracownika: ").grid(row=6, column=0)
        Button(frame, text="Zmien", command=lambda: self.lastname_info()).grid(row=6, column=1)

        Label(frame, text="Zmien imie i nazwisko pracownika: ").grid(row=7, column=0)
        Button(frame, text="Zmien", command=lambda: self.name_lastname_info()).grid(row=7, column=1)

        Label(frame, text="Zmien stanowisko i pensje pracownika: ").grid(row=8, column=0)
        Button(frame, text="Zmien", command=lambda: self.position_salary_info()).grid(row=8, column=1)

        Label(frame, text="Zmien nazwe stanowiska: ").grid(row=9, column=0)
        Button(frame, text="Zmien", command=lambda: self.position_info()).grid(row=9, column=1)

        Label(frame, text="Usun stanowisko wraz z pracownikami: ").grid(row=10, column=0)
        Button(frame, text="Usun", command=lambda: self.position_info_del()).grid(row=10, column=1)

        Label(frame, text="Usun wszystkich pracownikow: ").grid(row=11, column=0)
        Button(frame, text="Usun", command=lambda: self.del_emps()).grid(row=11, column=1)

    def salary_position_info(self):

        self.clear()

        Label(frame, text="Podaj stanowisko: ").grid(row=0, column=0)
        self.position = Entry(frame)
        self.position.grid(row=0, column=1)

        Label(frame, text="Podaj nowa pensje: ").grid(row=1, column=0)
        self.salary = Entry(frame)
        self.salary.grid(row=1, column=1)

        Button(frame, text="Zmien", command=lambda: self.upd_salary_by_position()).grid(row=2, column=0)

    def upd_salary_by_position(self):

        if Db().get_emp_by_position(self.position.get()) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma takiego stanowiska")
        else:
            Db().update_salary_by_position(self.position.get(), self.salary.get())
            messagebox.showinfo("Sukces", "Zmieniono pensje pracownikow na danym stanowisku")

        self.admin_view()

    def salary_info(self):

        self.emp_info()
        Label(frame, text="Podaj nowa pensje: ").grid(row=5, column=0)
        self.salary1 = Entry(frame)
        self.salary1.grid(row=5, column=1)

        Button(frame, text="Zmien", command=lambda: self.upd_salary()).grid(row=6, column=0)

    def upd_salary(self):

        emp = Employee(self.name.get(), self.lastname.get(), self.position.get(), self.salary.get())
        if Db().get_emp(emp) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma takiego pracownika")
        else:
            Db().update_emp_salary(emp, self.salary1.get())
            messagebox.showinfo("Sukces", "Zmieniono pensje pracownika")
        self.admin_view()

    def lastname_info(self):

        self.emp_info()

        Label(frame, text="Podaj nowe nazwisko: ").grid(row=5, column=0)
        self.lastname1 = Entry(frame)
        self.lastname1.grid(row=5, column=1)

        Button(frame, text="Zmien", command=lambda: self.upd_lastname()).grid(row=6, column=0)

    def upd_lastname(self):

        emp = Employee(self.name.get(), self.lastname.get(), self.position.get(), self.salary.get())
        if Db().get_emp(emp) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma takiego pracownika")
        else:
            Db().update_emp_lastname(emp, self.lastname1.get())
            messagebox.showinfo("Sukces", "Zmieniono nazwisko pracownika")
        self.admin_view()

    def name_lastname_info(self):

        self.emp_info()

        Label(frame, text="Podaj nowe imie: ").grid(row=5, column=0)
        self.name1 = Entry(frame)
        self.name1.grid(row=5, column=1)

        Label(frame, text="Podaj nowe nazwisko: ").grid(row=6, column=0)
        self.lastname1 = Entry(frame)
        self.lastname1.grid(row=6, column=1)

        Button(frame, text="Zmien", command=lambda: self.upd_name_lastname()).grid(row=7, column=0)

    def upd_name_lastname(self):

        emp = Employee(self.name.get(), self.lastname.get(), self.position.get(), self.salary.get())

        if Db().get_emp(emp) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma takiego pracownika")
        else:
            Db().update_emp(emp, self.name1.get(), self.lastname1.get())
            messagebox.showinfo("Sukces", "Przypisano nowego pracownika na istniejace stanowisko")
        self.admin_view()

    def position_salary_info(self):

        self.emp_info()

        Label(frame, text="Podaj nowe stanowisko: ").grid(row=5, column=0)
        self.position1 = Entry(frame)
        self.position1.grid(row=5, column=1)

        Label(frame, text="Podaj nowa pensje: ").grid(row=6, column=0)
        self.salary1 = Entry(frame)
        self.salary1.grid(row=6, column=1)

        Button(frame, text="Zmien", command=lambda: self.upd_position_salary()).grid(row=7, column=0)

    def upd_position_salary(self):

        emp = Employee(self.name.get(), self.lastname.get(), self.position.get(), self.salary.get())

        if Db().get_emp(emp) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma takiego pracownika")
        else:
            Db().update_emp_position_and_salary(emp, self.position1.get(), self.salary1.get())
            messagebox.showinfo("Sukces", "Nadano nowe stanowisko i pensje dla pracownika")

        self.admin_view()

    def position_info(self):

        self.clear()

        Label(frame, text="Podaj stara nazwe stanowiska: ").grid(row=5, column=0)
        self.position = Entry(frame)
        self.position.grid(row=5, column=1)

        Label(frame, text="Podaj nowa nazwe stanowiska: ").grid(row=6, column=0)
        self.position1 = Entry(frame)
        self.position1.grid(row=6, column=1)

        Button(frame, text="Zmien", command=lambda: self.upd_position()).grid(row=7, column=0)

    def upd_position(self):

        if Db().get_emp_by_position(self.position.get()) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma takiego stanowiska")
        else:
            Db().update_emp_position(self.position.get(), self.position1.get())
            messagebox.showinfo("Sukces", "Zmieniono nazwe stanowiska")

        self.admin_view()

    def del_emps(self):

        Db().remove_emps()
        messagebox.showinfo("Sukces", "Tabela zostala wyczyszczona")

    def position_info_del(self):

        self.clear()

        Label(frame, text="Podaj nazwe stanowiska ktore chcesz usunac: ").grid(row=1, column=0)
        self.position = Entry(frame)
        self.position.grid(row=2, column=0)

        Button(frame, text="Usun", command=lambda: self.del_position()).grid(row=3, column=0)

    def del_position(self):

        if Db().get_emp_by_position(self.position.get()) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma takiego stanowiska")
        else:
            Db().remove_emps_by_position(self.position.get())
            messagebox.showinfo("Sukces", "Usunieto stanowisko wraz z pracownikami")

        self.admin_view()


class HR(User):
    '''Klasa zawierajaca metody dostepne dla Pracownika HR'''

    def hr_view(self):

        self.clear()
        self.create_user_view()

        Label(frame, text="Sprawdz czy pracownik jest w bazie: ").grid(row=4, column=0)
        Button(frame, text="Sprawdz", command=lambda: self.check()).grid(row=4, column=1)

        Label(frame, text="Wyswietl pracownikow o danym imieniu: ").grid(row=5, column=0)
        Button(frame, text="Wyswietl", command=lambda: self.emps_name()).grid(row=5, column=1)

        Label(frame, text="Wyswietl pracownikow o danym nazwisku: ").grid(row=6, column=0)
        Button(frame, text="Wyswietl", command=lambda: self.emps_lastname()).grid(row=6, column=1)

        Label(frame, text="Wyswietl pracownika: ").grid(row=7, column=0)
        Button(frame, text="Wyswietl", command=lambda: self.emps_name_lastname()).grid(row=7, column=1)

        Label(frame, text="Wyswietl pracownikow na danym stanowisku: ").grid(row=8, column=0)
        Button(frame, text="Wyswietl", command=lambda: self.emps_position()).grid(row=8, column=1)

        Label(frame, text="Wyswietl pracownikow o danej pensji: ").grid(row=9, column=0)
        Button(frame, text="Wyswietl", command=lambda: self.emps_salary()).grid(row=9, column=1)

        Label(frame, text="Podaj liczbe pracownikow w bazie: ").grid(row=10, column=0)
        Button(frame, text="Podaj", command=lambda: self.employees_number()).grid(row=10, column=1)

        Label(frame, text="Uszereguj pracownikow wedlug pensji: ").grid(row=11, column=0)
        Button(frame, text="Wyswietl", command=lambda: self.emps_order_by_salary()).grid(row=11, column=1)

    def check(self):

        self.emp_info()
        Button(frame, text="Wprowadz", command=lambda: self.emp_checked()).grid(row=5, column=1)

    def emp_checked(self):

        emp = Employee(self.name.get(), self.lastname.get(), self.position.get(), self.salary.get())
        if Db().get_emp(emp) is None:
            messagebox.showinfo("Brak", "W bazie danych nie ma takiego pracownika")
        else:
            messagebox.showinfo("Sukces", "W bazie danych istnieje taki pracownik")
        self.hr_view()

    def emps_name(self):

        self.clear()

        Label(frame, text="Podaj imie pracownika: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=2, column=0)

        Button(frame, text="Wyszukaj", command=lambda: self.view_emps_name()).grid(row=3, column=0)

    def view_emps_name(self):

        if Db().get_emp_by_name(self.name.get()) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma pracownika o takim imieniu")
            self.hr_view()
        else:
            Label(frame, text=Db().get_emps_by_name(self.name.get())).grid(row=4)
            Button(frame, text="Powrot", command=lambda: self.hr_view()).grid(row=5)

    def emps_lastname(self):

        self.clear()

        Label(frame, text="Podaj nazwisko pracownika: ").grid(row=1, column=0)
        self.lastname = Entry(frame)
        self.lastname.grid(row=2, column=0)

        Button(frame, text="Wyszukaj", command=lambda: self.view_emps_lastname()).grid(row=3, column=0)

    def view_emps_lastname(self):

        if Db().get_emp_by_lastname(self.lastname.get()) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma pracownika o takim nazwisku")
            self.hr_view()
        else:
            Label(frame, text=Db().get_emps_by_lastname(self.lastname.get())).grid(row=4)
            Button(frame, text="Powrot", command=lambda: self.hr_view()).grid(row=5)

    def emps_name_lastname(self):

        self.clear()

        Label(frame, text="Podaj imie pracownika: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.grid(row=1, column=1)

        Label(frame, text="Podaj nazwisko pracownika: ").grid(row=2, column=0)
        self.lastname = Entry(frame)
        self.lastname.grid(row=2, column=1)

        Button(frame, text="Wyszukaj", command=lambda: self.view_emps_name_lastname()).grid(row=3, column=0)

    def view_emps_name_lastname(self):

        if Db().get_emp_by_name_and_lastname(self.name.get(), self.lastname.get()) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma pracownika o takim imieniu i nazwisku")
            self.hr_view()
        else:
            Label(frame, text=Db().get_emps_by_name_and_lastname(self.name.get(), self.lastname.get())).grid(row=4)
            Button(frame, text="Powrot", command=lambda: self.hr_view()).grid(row=5)

    def emps_position(self):

        self.clear()

        Label(frame, text="Podaj stanowisko pracownika: ").grid(row=1, column=0)
        self.position = Entry(frame)
        self.position.grid(row=2, column=0)
        Button(frame, text="Wyszukaj", command=lambda: self.view_emps_position()).grid(row=3, column=0)

    def view_emps_position(self):

        if Db().get_emp_by_position(self.position.get()) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma takiego stanowiska")
            self.hr_view()
        else:
            Label(frame, text=Db().get_emps_by_position(self.position.get())).grid(row=4)
            Button(frame, text="Powrot", command=lambda: self.hr_view()).grid(row=5)

    def emps_salary(self):

        self.clear()

        Label(frame, text="Podaj pensje pracownika: ").grid(row=1, column=0)
        self.salary = Entry(frame)
        self.salary.grid(row=2, column=0)

        Button(frame, text="Wyszukaj", command=lambda: self.view_emps_salary()).grid(row=3, column=0)

    def view_emps_salary(self):

        if Db().get_emp_by_salary(self.salary.get()) is None:
            messagebox.showinfo("Blad", "W bazie danych nie ma pracownika o takiej pensji")
            self.hr_view()
        else:
            Label(frame, text=Db().get_emps_by_salary(self.salary.get())).grid(row=4)
            Button(frame, text="Powrot", command=lambda: self.hr_view()).grid(row=5)

    def emps_order_by_salary(self):

        self.clear()

        rows = Db().get_emps_order_by_salary()
        i = 0
        for row in rows:
            Label(frame, text=row).grid(row=i, column=0)
            i += 1

        Button(frame, text="Powrot", command=lambda: self.view()).grid(row=i, column=0)

    def employees_number(self):

        rows = Db().get_emps()
        i = 0
        for row in rows:
            i += 1

        messagebox.showinfo("Sukces", "Liczba pracownikow: " + str(i))


class loginView:
    '''Klasa ekranu logowania'''

    def __init__(self):
        self.user_type = StringVar()
        self.login = Entry(frame)
        self.password = Entry(frame)

    def log_in_a(self):

        def validate_user_type():
            if self.user_type.get() == "Admin" or self.user_type.get() == "Pracownik HR":
                return True
            else:
                messagebox.showinfo("Blad", "Wybierz typ uzytkownika!")
                return False

        def verify_admin():

            if self.login.get() != logowanie_admin["login"] or self.password.get() != logowanie_admin["password"] or self.user_type.get() != "Admin":
                return False
            else:
                return True

        def verify_hr():

            if self.login.get() != logowanie_hr["login"] or self.password.get() != logowanie_hr["password"] or self.user_type.get() != "Pracownik HR":
                return False
            else:
                return True

        if validate_user_type():
            if verify_hr():
                hr = HR()
                hr.hr_view()
            elif verify_admin():
                admin = Admin()
                admin.admin_view()
            else:
                messagebox.showinfo("Blad", "Dane logowania nieprawidlowe")

    def init_view(self):

        for widget in frame.winfo_children():
            widget.destroy()

        self.user_type.set("--Wybierz typ uzytkownika--")
        OptionMenu(frame, self.user_type, "Pracownik HR", "Admin").grid(row=0, column=1)

        Label(frame, text="Login: ").grid(row=1, column=0)
        self.login = Entry(frame)
        self.login.grid(row=1, column=1)

        Label(frame, text="Haslo: ").grid(row=2, column=0)
        self.password = Entry(frame)
        self.password.grid(row=2, column=1)

        Button(frame, text="Zaloguj sie", command=self.log_in_a).grid(row=3, column=1)


root = Tk()
root.title("Pracownicy")
frame = Frame(root)
frame.grid()

logowanie_admin = {"login": "admin", "password": "1234"}
logowanie_hr = {"login": "hr", "password": "4321"}

loginView.init_view(loginView())

root.mainloop()
