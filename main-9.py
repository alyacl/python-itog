from tkinter import *
import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from libraries.libraries import *


window = Tk()
window.title("Проект по питону")
window.geometry('975x800')
def clearWindow():
    #список всех элементов на экране, созданных с помощью метода plase
    list2 = window.place_slaves()
    #уничтожаем все объекты, созданные с помощью plase
    for l in list2:
        l.destroy()
    list1 = window.pack_slaves()
    for l in list1:
        l.destroy()




def functionExport():
    clearWindow()
    if data.shape[1] == 0:
        welcome = Label(window,
                        text="В таблице нет никаких данных. Функция недоступна.")
        welcome.place(x=0, y=25)
    else:
        welcome = Label(window, text="Введите название сохраняемого файла без указания расширения: ")
        welcome.place(x=0, y=25)
        fileName = Entry(window, width=44)
        fileName.place(x=0, y=45)
        def saveFile():
            flName = "{}".format(fileName.get())
            global data
            varFile = IntVar()
            varFile.set(-1)
            informationfile1 = Radiobutton(window, text=".xlsx", justify=LEFT,
                                             variable=varFile, value=0)
            informationfile2 = Radiobutton(window, text=".csv", justify=LEFT,
                                           variable=varFile, value=1)
            saveInformation = Label(window, text="Выберете необходимое расширение: ",wraplength=970)
            saveInformation.place(x=0, y=90)
            informationfile1.place(x=10, y=130)
            informationfile2.place(x=10, y=160)
            def save():
                global data
                if varFile.get() != - 1:
                    informationfile1.destroy()
                    informationfile2.destroy()
                    saveBtn.destroy()
                    sprav = ""
                    for i in spravochniki:
                        sprav = sprav + str(i) + ', '
                    sprav = sprav[:len(sprav)-2]
                    if varFile.get() == 0:
                        data.to_excel(flName+".xlsx")
                        saveInformation.configure(text="Пользователем были считаны следующие справочники: "+ sprav + ". В файле " + flName + ".xlsx можно увидеть получившуюся таблицу.")
                    if varFile.get() == 1:
                        data.to_csv(flName+".csv", index=False)
                        saveInformation.configure(
                            text="Пользователем были считаны следующие справочники: " + sprav + ". В файле " + flName + ".csv можно увидеть получившуюся таблицу.")
            saveBtn = Button(window, text="Подтвердить", command=save)
            saveBtn.place(x=90, y=145)
        fileBtn = Button(window, text="Подтвердить", command=saveFile)
        fileBtn.place(x=430, y=50)
        if data.shape[1] != 0:
            def see():
                printData(data)
            fileBtn = Button(window, text="Проcмотр", command=see)
            fileBtn.place(x=880, y=750)
def functionChange():
    global data
    clearWindow()
    if data.shape[1] == 0:
        welcome = Label(window,
                        text="В таблице нет никаких данных. Функция недоступна.")
        welcome.place(x=0, y=25)
    else:
        welcome = Label(window, text="Введите число, соответсвующие значению Number той строки, данные в которой хотите изменить. Если хотите удалить какой-либо столбец, введите название столбца и нажмите кнопку удалить столбец.", wraplength=975, justify=LEFT)
        welcome.place(x=0, y=25)
        strName = Entry(window, width=44)
        strName.place(x=0, y=75)

        def chooseColumns(num):
            lst = []
            for i in np.array(data.keys()):
                if i != "Number":
                    lst.append(i)
            combo = ttk.Combobox(window, values=lst)
            combo.place(x=5, y=160)
            combo.current(0)

            def col():
                colum = "{}".format(combo.get())
                global deliterow
                if num-1 not in deliterow:
                    information = Label(window, text="В колонке " + colum +" в строчке номер " + str(num) + " введены следующие данные: " + str(data[colum][num-1]) + ". Введите новые данные или нажмите кнопку отмена.", wraplength=975)
                    information.place(x=0, y=190)
                    infEntry = Entry(window, width=44)
                    infEntry.place(x=0, y=215)
                    def change():
                        new = "{}".format(infEntry.get())
                        if len(new) > 0:
                            data[colum][num] = new
                            print(data[colum][num])
                    confBtn = Button(window, text="Подтвердить", command=change)
                    confBtn.place(x=430, y=217)
                    def cancel():
                        clearWindow()
                        functionChange()
                    cancelBtn = Button(window, text="Отмена", command=cancel)
                    cancelBtn.place(x=530, y=217)
                else:
                    information = Label(window, text="Строки номер " + str(num) + " не существует. Введите другое значение", wraplength=975)
                    information.place(x=0, y=190)
            def delite():
                global data
                global deliterow
                deliterow.append(num-1)
                try:
                    data = data.drop(num-1, axis=0)
                    information = Label(window, text="Строка номер " + str(num) + " была успешно удалена.", wraplength=975)
                    information.place(x=0, y=190)
                except IOError:
                    information = Label(window, text="Строку номер " + str(num) + " удалить невозможно.",
                                        wraplength=975)
                    information.place(x=0, y=190)

            delBtn = Button(window,text="Удалить строку", command=delite)
            delBtn.place(x=500, y=163)
            colBtn = Button(window, text="Подтвердить", command=col)
            colBtn.place(x=250, y=163)
        def chooseStr():
            flName = "{}".format(strName.get())
            if flName.isdigit() == False:
                welcome.configure(text="Введите число!")
            else:
                num = int(flName)
                print(num)
                if (num>data.shape[0] or num<1):
                    welcome.configure(text="Введите другое число!")
                else:
                    columInf = Label(window, text="Для измениния данных выберите интересующую колонку. Если хотите удалить строку полностью, нажмите удалить строку.")
                    columInf.place(x=0, y=120)
                    chooseColumns(num)
        def delColumn():
            global data
            column = "{}".format(strName.get())
            if column in data:
                if column != "Number":
                    del data[column]
                    inf = Label(window, text="Колонка " + column + " была успешно удалена.")
                    inf.place(x=0, y=120)
                else:
                    inf = Label(window, text="Колонку " + column + " удалять нельзя!")
                    inf.place(x=0, y=120)
            else:
                inf = Label(window, text="В полученной базе данных колонки с названием " + column + " нет. Перепроверьте введенные данные")
                inf.place(x=0, y=120)

        colBtn = Button(window, text="Удалить столбец", command=delColumn)
        colBtn.place(x=630, y=80)
        strBtn = Button(window, text="Изменить строку", command=chooseStr)
        strBtn.place(x=430, y=80)
        if data.shape[1] != 0:
            def see():
                printData(data)

            fileBtn = Button(window, text="Проcмотр", command=see)
            fileBtn.place(x=880, y=750)

def functionAdd():
    clearWindow()
    global data
    if data.shape[1] == 0:
        welcome = Label(window,
                        text="В таблице нет никаких данных. Функция недоступна.")
        welcome.place(x=0, y=25)
    else:
        welcome = Label(window,
                        text="Выполните указанные ниже действия для добавления строки. Ей будет присвоено слудующее значение параметра Number: " + str(data.shape[0]+1 + len(deliterow)))
        welcome.place(x=0, y=25)
        key = np.array(data.keys())
        global i
        def inValue():
            global i
            text1 = Label(window,
                          text="")
            text1.configure(text="Введите данные для поля " + key[i])
            i += 1
            text1.place(x=0, y=55)
            addName = Entry(window, width=44)
            addName.place(x=0, y=75)
            def addValue():
                global dataRow
                value = "{}".format(addName.get())
                dataAdd = pd.DataFrame({key[i-1]: [value]})
                dataRow = dataAdd.join(dataRow)
                functionAdd()
            strBtn = Button(window, text="Подтвердить", command=addValue)
            strBtn.place(x=430, y=77)

        if i == data.shape[1]:
            global dataRow
            dataRow = dataRow.join(pd.DataFrame({'Number': [data.shape[0]+1+len(deliterow)]}))


            i = 1
            lst = ""
            flag = 1
            for k, pop in dataRow.iterrows():
                for j in key:
                    if j in pop:
                        lst = lst + str(j) + ": " + str(pop[j]) + ", "
                    else:
                        flag = 0
            lst = lst[:len(lst) - 2]
            if flag == 1:
                data = pd.concat([data, dataRow], axis=0)
                dataRow = pd.DataFrame()
                welcome.configure(text="Вами была сформирована строка со следующими данными: " + lst + ". Информация сохранена в таблицу. Чтобы увидеть базу данных полностью, нажмите на кнопку Просмотр.", wraplength=975, justify=LEFT)
            else:
                dataRow = pd.DataFrame()
                welcome.configure(text="При вводе данных вами была допущена ошибка. Запустите функцию заново и следуйте указаниям")
        else:
            inValue()
        if data.shape[1] != 0:
            def see():
                printData(data)

            fileBtn = Button(window, text="Проcмотр", command=see)
            fileBtn.place(x=880, y=750)
def functionFind():
    clearWindow()
    global data
    if data.shape[1] == 0:
        welcome = Label(window,
                        text="В таблице нет никаких данных. Функция недоступна.")
        welcome.place(x=0, y=25)
    else:
        welcome = Label(window,
                        text="Введите ниже выражение, которое необходимо найти и выберете фильтры поиска")
        welcome.place(x=0, y=25)
        addValue = Entry(window, width=44)
        addValue.place(x=0, y=55)
        varFilter = IntVar()
        varFilter.set(-1)
        infFilter1 = Radiobutton(window, text="Найти Number и название столбца первого совпадающего элемента", justify=LEFT,
                                       variable=varFilter, value=0)
        infFilter2 = Radiobutton(window, text="Искать в заданном столбце", justify=LEFT,
                                       variable=varFilter, value=1)
        infFilter3 = Radiobutton(window, text="Искать в заданной строке ", justify=LEFT,
                                 variable=varFilter, value=2)
        infFilter4 = Radiobutton(window, text="Посчитать сколько раз данное значение встречается в таблице", justify=LEFT,
                                 variable=varFilter, value=3)
        filterLabel = Label(window,text="Выберете одну из функций ниже:")
        filterLabel.place(x=0, y=85)
        infFilter2.place(x=10, y=115)
        infFilter3.place(x=10, y=145)
        infFilter4.place(x=10, y=175)
        lst = []
        for i in np.array(data.keys()):
            lst.append(i)
        combo = ttk.Combobox(window, values=lst)
        combo.place(x=250, y=114)
        combo.current(0)
        rowEntry = Entry(window, width=10)
        rowEntry.place(x=250, y=145)
        if data.shape[1] != 0:
            def see():
                printData(data)
            fileBtn = Button(window, text="Проcмотр", command=see)
            fileBtn.place(x=880, y=750)
        def find():
            if varFilter.get() != -1:
                if varFilter.get() == 1:
                    value = "{}".format(addValue.get())
                    column = "{}".format(combo.get())
                    list = data[column].tolist()
                    flag = 0
                    num = -1
                    count = 0
                    for i in range(len(list)):
                        if value == list[i]:
                            if flag == 0:
                                flag = 1
                                num = i+1
                            count += 1
                    if count>0:
                        resaltText = "В колонке " + column + " было найдено " + str(count) +" совпадений. Первое находится в строчке номер " + str(num) + "."
                    else:
                        resaltText = "В колонке " + column + " совпадения не были найдены."
                    resultInf = Label(window, text=resaltText)
                    resultInf.place(x=0, y=205)
                if varFilter.get() == 2:
                    value = "{}".format(addValue.get())
                    row = "{}".format(rowEntry.get())
                    j = 0
                    flag = 0
                    if row.isdigit():
                        for i, stroka in data.iterrows():
                            if stroka['Number'] == int(row):
                                lst = stroka.to_dict()
                                flag = 1
                                break

                            else:
                                j += 1
                        if flag == 0:
                            resaltText = "Строки с номером " + row + " в текущей базе данных нет. "
                        else:
                            keyss = np.array(data.keys())
                            keys = []
                            for key in keyss:
                                keys.append(key)
                            resaltText = "В строке номер " + row + " значение " + str(value) + " не встречается."
                            for key in keys:
                                if str(lst[key]) == str(value):
                                    resaltText = "В строке номер " + row + " значение " + str(value) + " встречается в колонке " + key + "."
                                    break
                        resultLabel = Label(window, text=resaltText)
                        resultLabel.place(x=0, y=205)

                    else:
                        resultLabel = Label(window, text="Введите целое число!")
                        resultLabel.place(x=0, y=205)
                if varFilter.get() == 3:
                    value = "{}".format(addValue.get())
                    column = data.columns.tolist()
                    count = 0
                    for col in column:
                        list = data[col].tolist()
                        for i in range(len(list)):
                            if str(value) == str(list[i]):
                                count += 1
                    if count > 0:
                        resaltText = "Всего в таблице было найдено " + str(count) + " совпадений."
                    else:
                        resaltText = "В таблице совпадения найдены не были"
                    resultInf = Label(window, text=resaltText)
                    resultInf.place(x=0, y=205)
        confBtn = Button(window, text="Подтвердить", command=find)
        confBtn.place(x=500, y=132)

def functionGraphic():
    clearWindow()
    global data
    if data.shape[1] == 0:
        welcome = Label(window,
                        text="В таблице нет никаких данных. Функция недоступна.")
        welcome.place(x=0, y=25)
    else:
        if data.shape[1] != 0:
            def see():
                printData(data)

            fileBtn = Button(window, text="Проcмотр", command=see)
            fileBtn.place(x=880, y=750)
        welcome = Label(window, text="Выберете графики из списка предложенных, которые необходимо построить")
        welcome.place(x=0, y=25)
        i = 60
        graphics = []
        var1 = IntVar()
        var1.set(-1)
        var2 = IntVar()
        var2.set(-1)
        var3 = IntVar()
        var3.set(-1)
        var4 = IntVar()
        var4.set(-1)
        var5 = IntVar()
        var5.set(-1)
        var6 = IntVar()
        var6.set(-1)
        var7 = IntVar()
        var7.set(-1)
        var8 = IntVar()
        var8.set(-1)
        if 'Gender' in data and "Little_interest_or_pleasure_in_doing_things" in data:
            graphics.append("Распределение ответов на вопрос о чувстве подавленности, депрессии и усталости (у девушек)")
            choosegraphics = Checkbutton(window, text=graphics[len(graphics)-1], justify=LEFT,
                                         variable=var1, onvalue=1, offvalue=-1)
            choosegraphics.place(x=5, y=i)
            i=i+30
        if 'Thoughts_that_you_would_be_better_off_dead_or_of_hurting_yourself_in_some_way' in data and 'Your_Last_Semester_GPA' in data:
            graphics.append("Зависимость итоговых оценок от наличия суицидальных мыслей")
            choosegraphics = Checkbutton(window, text=graphics[len(graphics)-1], justify=LEFT,
                                         variable=var2, onvalue=1, offvalue=-1)
            choosegraphics.place(x=5, y=i)
            i = i + 30
        if 'How_many_hours_do_you_spend_on_social_media_per_day' in data and 'Your_Last_Semester_GPA' in data:
            graphics.append("Соотношение итоговой оценки к количеству времени,проведенном в социальных сетях")
            choosegraphics = Checkbutton(window, text=graphics[len(graphics)-1], justify=LEFT,
                                         variable=var3, onvalue=1, offvalue=-1)
            choosegraphics.place(x=5, y=i)
            i = i + 30
        if 'How_many_of_the_electronic_gadgets_do_you_have' in data and 'Age' in data and 'Your_Last_Semester_GPA' in data:
            graphics.append('Влияние количества гаджетов на успеваемость в зависимости от возраста')
            choosegraphics = Checkbutton(window, text=graphics[len(graphics)-1], justify=LEFT,
                                         variable=var4, onvalue=1, offvalue=-1)
            choosegraphics.place(x=5, y=i)
            i = i + 30
        if 'Educational_Level' in data and 'Age' in data and 'Your_Last_Semester_GPA' in data:
            graphics.append("Зависимость успеваемости от уровня получения образования в разном возрасте")
            choosegraphics = Checkbutton(window, text=graphics[len(graphics)-1], justify=LEFT,
                                         variable=var5, onvalue=1, offvalue=-1)
            choosegraphics.place(x=5, y=i)
            i = i + 30
        if 'Number' in data and 'Little_interest_or_pleasure_in_doing_things' in data and 'Feeling_down_depressed_or_hopeless' in data and 'Trouble_falling_or_staying_asleep_or_sleeping_too_much' in data and 'Feeling_tired_or_having_little_energy' in data and 'Poor_appetite_or_overeating' in data and 'Feeling_bad_about_yourself_or_that_you_are_a_failure_or_not_have_let_yourself_or_your_family_down' in data and 'Trouble_concentrating_on_things_such_as_reading_the_newspaper_or_watching_television' in data and 'Moving_or_speaking_so_slowly_that_other_people_could_have_noticed_Or_being_so_restless_that_you_have_been_moving_around_a_lot_more_than_usual' in data and 'Thoughts_that_you_would_be_better_off_dead_or_of_hurting_yourself_in_some_way' in data and 'Your_Last_Semester_GPA' in data:
            graphics.append("Heatmap для всех численных параметров")
            choosegraphics = Checkbutton(window, text=graphics[len(graphics)-1], justify=LEFT,
                                         variable=var6, onvalue=1, offvalue=-1)
            choosegraphics.place(x=5, y=i)
            i = i + 30
        if 'Poor_appetite_or_overeating' in data and 'Trouble_concentrating_on_things_such_as_reading_the_newspaper_or_watching_television' in data:
            graphics.append("Связь проблем с аппетитом и концентрации")
            choosegraphics = Checkbutton(window, text=graphics[len(graphics)-1], justify=LEFT,
                                         variable=var7, onvalue=1, offvalue=-1)
            choosegraphics.place(x=5, y=i)
            i = i + 30
        if 'How_many_hours_do_you_spend_studying_each_day' in data:
            graphics.append("Распределение учащихся по часам занятия учёбой в день")
            choosegraphics = Checkbutton(window, text=graphics[len(graphics)-1], justify=LEFT,
                                         variable=var8, onvalue=1, offvalue=-1)
            choosegraphics.place(x=5, y=i)
            i = i + 30

        var = [var1, var2, var3, var4, var5, var6, var7, var8]
        def graphicsPrint():
            count = 0

            for v in var:
                if v.get() == 1:
                    count += 1
            if count == 0:
                welcome.configure(text="Вы не выбрали ни одного графика!")
            else:
                pop = tk.Toplevel(window)
                pop.geometry('1000x820')
                pop.title("Графики")
                xx = 0
                yy = 0
                if count == 1 or count == 2:
                    fig2, ac = plt.subplots(1, 2)
                    canvas2 = FigureCanvasTkAgg(fig2, master=pop)
                    canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                    fig2.set_figwidth(10)
                    fig2.set_figheight(10)
                    fig2.subplots_adjust(wspace=0.6, hspace=0.5)
                if count > 2 and count < 5:
                    fig3, az = plt.subplots(2, 2)
                    canvas3 = FigureCanvasTkAgg(fig3, master=pop)
                    canvas3.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                    fig3.set_figwidth(10)
                    fig3.set_figheight(10)
                    fig3.subplots_adjust(wspace=0.6, hspace=0.5)
                if count > 4:
                    fig5, ab = plt.subplots(4, 2)
                    canvas5 = FigureCanvasTkAgg(fig5, master=pop)
                    canvas5.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                    fig5.set_figwidth(10)
                    fig5.set_figheight(10)
                    fig5.subplots_adjust(wspace=0.6, hspace=0.6)

                if var1.get() == 1:
                    if count == 1 or count == 2:
                        x = np.arange(1, 5)
                        grades = list(data[(data.Gender == "Female")]["Little_interest_or_pleasure_in_doing_things"])
                        y = np.array([grades.count(i) / len(grades) for i in range(1, 5)])
                        ac[xx].bar(x, y)
                        ac[xx].set_title(
                            "Распределение ответов на вопрос о чувстве\n подавленности, депрессии и усталости (у девушек)")
                        ac[xx].set_xlabel("Выбор ответа")
                        xx += 1
                    if count>2 and count<5:
                        x = np.arange(1, 5)
                        grades = list(data[(data.Gender == "Female")]["Little_interest_or_pleasure_in_doing_things"])
                        y = np.array([grades.count(i) / len(grades) for i in range(1, 5)])
                        az[xx, yy].bar(x, y)
                        az[xx, yy].set_title(
                            "Распределение ответов на вопрос о чувстве\n подавленности, депрессии и усталости (у девушек)")
                        az[xx, yy].set_xlabel("Выбор ответа")

                        if xx == 0:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1
                    if count>4:
                        x = np.arange(1, 5)
                        grades = list(data[(data.Gender == "Female")]["Little_interest_or_pleasure_in_doing_things"])
                        y = np.array([grades.count(i) / len(grades) for i in range(1, 5)])
                        ab[xx, yy].bar(x, y)
                        ab[xx, yy].set_title(
                            "Распределение ответов на вопрос о чувстве\n подавленности, депрессии и усталости (у девушек)", fontsize = 7)

                        if xx != 3:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1
                if var2.get() == 1:
                    if count == 1 or count == 2:
                        studytime2 = [list(
                            data[(data.Thoughts_that_you_would_be_better_off_dead_or_of_hurting_yourself_in_some_way == i)][
                                "Your_Last_Semester_GPA"])
                                      for i in [1, 2, 3, 4]]
                        ac[xx].boxplot(studytime2, vert=0, labels=['отсутствуют', 'иногда', 'часто', 'постоянно'])
                        ac[xx].set_title("Зависимость итоговых оценок от\n наличия суицидальных мыслей")
                        ac[xx].set_xlabel("Итоговая оценка")
                        ac[xx].set_ylabel("Наличие суицидальных мыслей")
                        xx += 1
                    if count > 2 and count < 5:
                        studytime2 = [list(
                            data[(data.Thoughts_that_you_would_be_better_off_dead_or_of_hurting_yourself_in_some_way == i)][
                                "Your_Last_Semester_GPA"])
                            for i in [1, 2, 3, 4]]
                        az[xx, yy].boxplot(studytime2, vert=0, labels=['отсутствуют', 'иногда', 'часто', 'постоянно'])
                        az[xx, yy].set_title("Зависимость итоговых оценок от\n наличия суицидальных мыслей")
                        az[xx, yy].set_xlabel("Итоговая оценка")
                        az[xx, yy].set_ylabel("Наличие суицидальных мыслей")
                        if xx == 0:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1
                    if count > 4:
                        studytime2 = [list(
                            data[(data.Thoughts_that_you_would_be_better_off_dead_or_of_hurting_yourself_in_some_way == i)][
                                "Your_Last_Semester_GPA"])
                            for i in [1, 2, 3, 4]]
                        ab[xx, yy].boxplot(studytime2, vert=0, labels=['отсутствуют', 'иногда', 'часто', 'постоянно'])
                        ab[xx, yy].set_title("Зависимость итоговых оценок от\n наличия суицидальных мыслей", fontsize = 7)

                        if xx != 3:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1

                if var3.get() == 1:
                    if count == 1 or count == 0:
                        studytime = [list(
                            data[(data.How_many_hours_do_you_spend_on_social_media_per_day == i)]["Your_Last_Semester_GPA"])
                                     for i in ['1 - 2 Hours', '2 - 4 Hours', 'More than 4 Hours']]

                        ac[xx].boxplot(studytime, vert=0, labels=['1-2 часа', '2-4 часа', 'больше 4'])
                        ac[xx].set_title(
                            "Соотношение итоговой оценки к количеству времени,\n проведенном в социальных сетях")

                        ac[xx].set_xlabel("Итоговая оценка")
                        ac[xx].set_ylabel("Количество часов в соц. сетях")
                        xx += 1
                    if count > 2 and count < 5:
                        studytime = [list(
                            data[(data.How_many_hours_do_you_spend_on_social_media_per_day == i)]["Your_Last_Semester_GPA"])
                            for i in ['1 - 2 Hours', '2 - 4 Hours', 'More than 4 Hours']]

                        az[xx, yy].boxplot(studytime, vert=0, labels=['1-2 часа', '2-4 часа', 'больше 4'])
                        az[xx, yy].set_title(
                            "Соотношение итоговой оценки к количеству времени,\n проведенном в социальных сетях")

                        az[xx, yy].set_xlabel("Итоговая оценка")
                        az[xx, yy].set_ylabel("Количество часов в соц. сетях")
                        if xx == 0:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1
                    if count > 4 :
                        studytime = [list(
                            data[(data.How_many_hours_do_you_spend_on_social_media_per_day == i)]["Your_Last_Semester_GPA"])
                            for i in ['1 - 2 Hours', '2 - 4 Hours', 'More than 4 Hours']]

                        ab[xx, yy].boxplot(studytime, vert=0, labels=['1-2 часа', '2-4 часа', 'больше 4'])
                        ab[xx, yy].set_title(
                            "Соотношение итоговой оценки к количеству времени,\n проведенном в социальных сетях", fontsize = 7)


                        if xx != 3:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1

                if var4.get()==1:
                    if count == 1 or count == 2:
                        ac[xx].scatter(data[(data.How_many_of_the_electronic_gadgets_do_you_have == "1 - 3")]["Age"],
                                         data[(data.How_many_of_the_electronic_gadgets_do_you_have == "1 - 3")][
                                             "Your_Last_Semester_GPA"],
                                         c=[[0, 0, 1, 0.3]])
                        ac[xx].scatter(data[(data.How_many_of_the_electronic_gadgets_do_you_have == "4 - 6")]["Age"],
                                         data[(data.How_many_of_the_electronic_gadgets_do_you_have == "4 - 6")][
                                             "Your_Last_Semester_GPA"],
                                         c=[[0, 1, 0, 0.3]])
                        ac[xx].scatter(
                            data[(data.How_many_of_the_electronic_gadgets_do_you_have == "More than 6")]["Age"],
                            data[(data.How_many_of_the_electronic_gadgets_do_you_have == "More than 6")][
                                "Your_Last_Semester_GPA"], c=[[1, 0, 0, 0.3]])
                        ac[xx].set_title(
                            'Влияние количества гаджетов на успеваемость\n в зависимости от возраста\n(зеленый: 1-3, синий: 4-6, красный: больше 6)')
                        ac[xx].set_xlabel("Возраст учащихся")
                        ac[xx].set_ylabel("Итоговая оценка")
                        xx += 1
                    if count > 2 and count < 5:
                        az[xx, yy].scatter(data[(data.How_many_of_the_electronic_gadgets_do_you_have == "1 - 3")]["Age"],
                                       data[(data.How_many_of_the_electronic_gadgets_do_you_have == "1 - 3")][
                                           "Your_Last_Semester_GPA"],
                                       c=[[0, 0, 1, 0.3]])
                        az[xx, yy].scatter(data[(data.How_many_of_the_electronic_gadgets_do_you_have == "4 - 6")]["Age"],
                                       data[(data.How_many_of_the_electronic_gadgets_do_you_have == "4 - 6")][
                                           "Your_Last_Semester_GPA"],
                                       c=[[0, 1, 0, 0.3]])
                        az[xx, yy].scatter(
                            data[(data.How_many_of_the_electronic_gadgets_do_you_have == "More than 6")]["Age"],
                            data[(data.How_many_of_the_electronic_gadgets_do_you_have == "More than 6")][
                                "Your_Last_Semester_GPA"], c=[[1, 0, 0, 0.3]])
                        az[xx, yy].set_title(
                            'Влияние количества гаджетов на успеваемость\n в зависимости от возраста\n(зеленый: 1-3, синий: 4-6, красный: больше 6)')
                        az[xx, yy].set_xlabel("Возраст учащихся")
                        az[xx, yy].set_ylabel("Итоговая оценка")
                        if xx == 0:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1
                    if count > 4:
                        ab[xx, yy].scatter(data[(data.How_many_of_the_electronic_gadgets_do_you_have == "1 - 3")]["Age"],
                                           data[(data.How_many_of_the_electronic_gadgets_do_you_have == "1 - 3")][
                                               "Your_Last_Semester_GPA"],
                                           c=[[0, 0, 1, 0.3]])
                        ab[xx, yy].scatter(data[(data.How_many_of_the_electronic_gadgets_do_you_have == "4 - 6")]["Age"],
                                           data[(data.How_many_of_the_electronic_gadgets_do_you_have == "4 - 6")][
                                               "Your_Last_Semester_GPA"],
                                           c=[[0, 1, 0, 0.3]])
                        ab[xx, yy].scatter(
                            data[(data.How_many_of_the_electronic_gadgets_do_you_have == "More than 6")]["Age"],
                            data[(data.How_many_of_the_electronic_gadgets_do_you_have == "More than 6")][
                                "Your_Last_Semester_GPA"], c=[[1, 0, 0, 0.3]])
                        ab[xx, yy].set_title(
                            'Влияние количества гаджетов на успеваемость\n в зависимости от возраста\n(зеленый: 1-3, синий: 4-6, красный: больше 6)', fontsize = 7)

                        if xx != 3:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1

                if var5.get() == 1:
                    if count == 1 or count == 2:
                        ac[xx].scatter(data[(data.Educational_Level == "College - Bachelor's")]["Age"],
                                         data[(data.Educational_Level == "College - Bachelor's")]["Your_Last_Semester_GPA"],
                                         c=[[0, 0, 1, 0.3]])
                        ac[xx].scatter(data[(data.Educational_Level == "High School")]["Age"],
                                         data[(data.Educational_Level == "High School")]["Your_Last_Semester_GPA"],
                                         c=[[0, 1, 0, 0.3]])
                        ac[xx].scatter(data[(data.Educational_Level == "Master")]["Age"],
                                         data[(data.Educational_Level == "Master")]["Your_Last_Semester_GPA"],
                                         c=[[1, 0, 0, 0.3]])
                        ac[xx].set_title(
                            "Зависимость успеваемости от уровня получения\n образования в разном возрасте\n(синий: Колледж или Бакалавриат, \nзелёный: Старшая школа, красный: Магистратура)")
                        ac[xx].set_xlabel("Возраст учащихся")
                        ac[xx].set_ylabel("Итоговая оценка")
                        xx += 1
                    if count > 2 and count < 5:
                        az[xx, yy].scatter(data[(data.Educational_Level == "College - Bachelor's")]["Age"],
                                       data[(data.Educational_Level == "College - Bachelor's")]["Your_Last_Semester_GPA"],
                                       c=[[0, 0, 1, 0.3]])
                        az[xx, yy].scatter(data[(data.Educational_Level == "High School")]["Age"],
                                       data[(data.Educational_Level == "High School")]["Your_Last_Semester_GPA"],
                                       c=[[0, 1, 0, 0.3]])
                        az[xx, yy].scatter(data[(data.Educational_Level == "Master")]["Age"],
                                       data[(data.Educational_Level == "Master")]["Your_Last_Semester_GPA"],
                                       c=[[1, 0, 0, 0.3]])
                        az[xx, yy].set_title(
                            "Зависимость успеваемости от уровня получения\n образования в разном возрасте\n(синий: Колледж или Бакалавриат, \nзелёный: Старшая школа, красный: Магистратура)")
                        az[xx, yy].set_xlabel("Возраст учащихся")
                        az[xx, yy].set_ylabel("Итоговая оценка")
                        if xx == 0:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1
                    if count > 4:
                        ab[xx, yy].scatter(data[(data.Educational_Level == "College - Bachelor's")]["Age"],
                                           data[(data.Educational_Level == "College - Bachelor's")][
                                               "Your_Last_Semester_GPA"],
                                           c=[[0, 0, 1, 0.3]])
                        ab[xx, yy].scatter(data[(data.Educational_Level == "High School")]["Age"],
                                           data[(data.Educational_Level == "High School")]["Your_Last_Semester_GPA"],
                                           c=[[0, 1, 0, 0.3]])
                        ab[xx, yy].scatter(data[(data.Educational_Level == "Master")]["Age"],
                                           data[(data.Educational_Level == "Master")]["Your_Last_Semester_GPA"],
                                           c=[[1, 0, 0, 0.3]])
                        ab[xx, yy].set_title(
                            "Зависимость успеваемости от уровня получения\n образования в разном возрасте\n(синий: Колледж или Бакалавриат, \nзелёный: Старшая школа, красный: Магистратура)", fontsize = 7)

                        if xx != 3:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1

                if var6.get()==1:
                    if count == 1 or count == 2:
                        ac[xx].imshow(data.corr(), cmap='hot', interpolation='nearest')
                        heat = ["Number", "Первый вопрос", "Второй вопрос", "Третий вопрос", "Четвертый вопрос",
                                "Пятый вопрос", "Шестой вопрос", "Седьмой вопрос", "Восьмой вопрос", "Девятый вопрос",
                                "Средний балл"]
                        heat2 = ["Number", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Балл"]
                        ac[xx].set_xticks(range(len(heat2)), heat2, fontsize=5)
                        ac[xx].set_yticks(range(len(heat)), heat)
                        ac[xx].set_title('Heatmap для всех численных параметров')
                        xx += 1
                    if count > 2 and count <5:
                        az[xx, yy].imshow(data.corr(), cmap='hot', interpolation='nearest')
                        heat = ["Number", "Первый вопрос", "Второй вопрос", "Третий вопрос", "Четвертый вопрос",
                                "Пятый вопрос", "Шестой вопрос", "Седьмой вопрос", "Восьмой вопрос", "Девятый вопрос",
                                "Средний балл"]
                        heat2 = ["Number", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Балл"]
                        az[xx, yy].set_xticks(range(len(heat2)), heat2, fontsize=5)
                        az[xx, yy].set_yticks(range(len(heat)), heat)
                        az[xx, yy].set_title('Heatmap для всех численных параметров')
                        if xx == 0:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1
                    if count > 4:
                        ab[xx, yy].imshow(data.corr(), cmap='hot', interpolation='nearest')
                        heat = ["Number", "Первый вопрос", "Второй вопрос", "Третий вопрос", "Четвертый вопрос",
                                "Пятый вопрос", "Шестой вопрос", "Седьмой вопрос", "Восьмой вопрос", "Девятый вопрос",
                                "Средний балл"]
                        heat2 = ["Number", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Балл"]

                        ab[xx, yy].set_title('Heatmap для всех численных параметров', fontsize = 7)
                        if xx != 3:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1

                if var7.get() == 1:
                    if count == 1 or count == 2:
                        answer = [list(data[(data.Poor_appetite_or_overeating == i)][
                                           "Trouble_concentrating_on_things_such_as_reading_the_newspaper_or_watching_television"])
                                  for i in [1, 2, 3, 4]]

                        ac[xx].boxplot(answer, vert=0, labels=['нет проблем', 'иногда', 'часто', 'постоянно'])
                        ac[xx].set_title(
                            "Связь проблем с аппетитом и концентрации \n(1-проблем нет, 4-концентрация отсутствует вовсе)")
                        ac[xx].set_xlabel("Проблемы с концентрацией")
                        ac[xx].set_ylabel("Отсутствие аппетита или переедания")
                        xx += 1
                    if count > 2 and count < 5:
                        answer = [list(data[(data.Poor_appetite_or_overeating == i)][
                                           "Trouble_concentrating_on_things_such_as_reading_the_newspaper_or_watching_television"])
                                  for i in [1, 2, 3, 4]]

                        az[xx, yy].boxplot(answer, vert=0, labels=['нет проблем', 'иногда', 'часто', 'постоянно'])
                        az[xx, yy].set_title(
                            "Связь проблем с аппетитом и концентрации \n(1-проблем нет, 4-концентрация отсутствует вовсе)")
                        az[xx, yy].set_xlabel("Проблемы с концентрацией")
                        az[xx, yy].set_ylabel("Отсутствие аппетита/переедания")
                        if xx == 0:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1
                    if count > 4:
                        answer = [list(data[(data.Poor_appetite_or_overeating == i)][
                                           "Trouble_concentrating_on_things_such_as_reading_the_newspaper_or_watching_television"])
                                  for i in [1, 2, 3, 4]]

                        ab[xx, yy].boxplot(answer, vert=0, labels=['нет проблем', 'иногда', 'часто', 'постоянно'])
                        ab[xx, yy].set_title(
                            "Связь проблем с аппетитом и концентрации \n(1-проблем нет, 4-концентрация отсутствует вовсе)", fontsize = 7)

                        if xx != 3:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1

                if var8.get() == 1:
                    if count == 1 or count == 2:
                        ac[xx].hist(data["How_many_hours_do_you_spend_studying_each_day"])
                        ac[xx].set_title("Распределение учащихся по часам\n занятия учёбой в день")
                        ac[xx].set_xlabel("Количество часов, которое занимает учёба")
                        ac[xx].set_ylabel("Количество учащихся")
                        xx += 1
                    if count > 2 and count < 5:
                        az[xx, yy].hist(data["How_many_hours_do_you_spend_studying_each_day"])
                        az[xx, yy].set_title("Распределение учащихся по часам\n занятия учёбой в день")
                        az[xx, yy].set_xlabel("Количество часов, которое занимает учёба")
                        az[xx, yy].set_ylabel("Количество учащихся")
                        if xx == 0:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1
                    if count > 4:
                        ab[xx, yy].hist(data["How_many_hours_do_you_spend_studying_each_day"])
                        ab[xx, yy].set_title("Распределение учащихся по часам\n занятия учёбой в день", fontsize = 7)

                        if xx != 3:
                            xx += 1

                        else:
                            xx = 0
                            yy += 1




        printButn = Button(window, text="Вывести", command=graphicsPrint)
        printButn.place(x=0, y=i)
        if len(graphics) == 0:
            welcome.configure(text="По полученой базе данных никаких графиков построить нельзя, испортируйте ещё данные.")
            printButn.destroy()

def functionManagment():
    clearWindow()
    manag = "Добро пожаловать в программу, анализирующую базу данных! " \
            "В данной программе реализовано 6 основных функций, вызываемых при нажатии на соответсвующие кнопки. Расмотрим каждую из них поподробнее.\n" \
            "\n\tИМПОРТ\n\n" \
            "Данная функцию импортирует справочники в программу. Ей можно воспользоваться в случае необходимости начального добавления базы данных или же при случайном удалении какого-то столбца. Формат импортируемых данных: .xlsx\n" \
            "\n\tЭКСПОРТ\n\n" \
            "Функцию экспорта сохраняет текущую базу данных со всеми изменениями. Пользователь может указать название сохраняемого файла и указать расширение.\n" \
            "\n\tИЗМЕНИТЬ\n\n" \
            "Нажав на кнопку изменить пользователь может редактировать текущую базу данных. Необходимо будет следовать командам на экране.\n" \
            "\n\tДОБАВИТЬ\n\n" \
            "Пользователь может добавить в текущую базу данных новую строку.\n" \
            "\n\tНАЙТИ\n\n" \
            "В поле для ввода необходимо будет ввести слова, которые нужно искать и также выбрать параметры поиска.\n" \
            "\n\tГРАФИКИ\n\n" \
            "Пользователь может воспользоваться это функцией для визуализации каких-либо зависимостей. Программа может построить 8 разнообразных графиков\n" \
            "\nТакже в программе есть кнопка просмотр. Нажав на неё, пользователь может увидеть текущую базу данных.\n" \
            "\nПримечание. В случае возникновения каких-либо ошибок пользователю необходимо вызвать функцию заново, путём нажатия на интересующую его кнопку."
    welcome = Label(window, text=manag, wraplength=975, justify=LEFT)
    welcome.place(x=0, y=25)


def moveData(data):
    file = Label(window, text="Файл был успешно считан, нажмите на кнопку Просмотр, чтобы увидеть базу данных целиком. Для загрузки следующего справочника введите его название в поле выше.", wraplength=975, justify=LEFT)
    file.place(x=0, y=100)
    def see():
        printData(data)
    fileBtn = Button(window, text="Проcмотр", command=see)
    fileBtn.place(x=880, y=750)

def functionImport():

    clearWindow()
    welcome = Label(window, text="Здравствуйте! Введите название файла на английском языке: ")
    welcome.place(x=0, y=25)
    fileName = Entry(window, width=44)
    fileName.place(x=0, y=45)
    def findFile():
        try:
            flName = "{}".format(fileName.get())
            print(flName)
            global data
            spravochniki.append(flName)
            dataNew = pd.read_excel(flName)
            dataKey = np.array(data.keys())
            dataNewKey = np.array(dataNew.keys())
            dataKey = set(dataKey) & set(dataNewKey)
            if data.shape[1] != 0:
                for key in dataKey:
                    del dataNew[key]
                data = data.join(dataNew)
            else:
                data = dataNew.join(data)
            moveData(data)
        except IOError:
            print('Файл недоступен')
            welcome.configure(text="Файл с данным названием не доступен. Введите, пожалуйста, другой.")
    fileBtn = Button(window, text="Продолжить", command=findFile)
    fileBtn.place(x=430, y=50)
    if data.shape[1] != 0:
        def see():
            printData(data)
        fileBtn = Button(window, text="Проcмотр", command=see)
        fileBtn.place(x=880, y=750)



def printData(data):
    pop =tk.Toplevel(window)
    pop.geometry('850x600')
    pop.title("Таблица")
    table = ttk.Treeview(pop, show='headings')
    index = np.array(data.keys())
    table['columns'] = index
    lst = []
    for i in range(data.shape[1]):
        table.heading(table['columns'][i], text=index[i], anchor='center')
        table.column(table['columns'][i], anchor='center')
    for i, str in data.iterrows():
        for row in index:
            lst.append(str[row])
        table.insert('', tk.END, values=lst)
        lst.clear()

    table.pack(side=tk.LEFT, fill=tk.BOTH, pady=100, padx=15)
    scroll = ttk.Scrollbar(pop, command=table.yview)
    scrollx= ttk.Scrollbar(pop, command=table.xview, orient=HORIZONTAL)
    table.configure(yscrollcommand=scroll.set, xscrollcommand=scrollx.set)
    scrollx.place(x=20, y=500, width=800)
    scroll.place(x=0, y=100, height=396)
    tableText = Label(pop, text="Таблица, загруженная в программу на данный момент. Чобы вернуться к функциям нажмите закрыть.")
    tableText.place(x=0, y=30)
    def backFunction():
        pop.destroy()
    back = Button(pop, text="Закрыть", command=backFunction)
    back.place(x=680, y=30)

def functionButton():
    importButton = Button(window, text="Импорт", command=functionImport, width=15)
    importButton.grid(column=0, row=0, sticky='nw')
    exportButton = Button(window, text="Экспорт", command=functionExport, width=15)
    exportButton.grid(column=1, row=0, sticky='nw')
    changeButton = Button(window, text="Изменить", command=functionChange, width=15)
    changeButton.grid(column=2, row=0, sticky='nw')
    addButton = Button(window, text="Добавить", command=functionAdd, width=15)
    addButton.grid(column=3, row=0, sticky='nw')
    findButton = Button(window, text="Найти", command=functionFind, width=15)
    findButton.grid(column=4, row=0, sticky='nw')
    graphicButton = Button(window, text="Графики", command=functionGraphic, width=15)
    graphicButton.grid(column=5, row=0, sticky='nw')
    managmentButton = Button(window, text="Руководство", command=functionManagment, width=15)
    managmentButton.grid(column=6, row=0, sticky='nw')
    if data.shape[1] != 0:
        def see():
            printData(data)
        fileBtn = Button(window, text="Проcмотр", command=see)
        fileBtn.place(x=880, y=750)

i = 1
dataRow = pd.DataFrame()
deliterow = []
spravochniki = []
data = pd.DataFrame()
functionButton()
window.mainloop()

