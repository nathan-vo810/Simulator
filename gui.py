import main
import tkHyperlinkManager
from tkinter import *
from PIL import Image, ImageTk

from const import Const

root = Tk()
root.title(Const.ROOT_TITLE)
root.configure(bg=Const.ROOT_COLOR)
backgroundImage = Image.open(Const.ROOT_BACKGROUND_URL)
backgroundPhoto = ImageTk.PhotoImage(backgroundImage)
backgroundLabel = Label(root, image=backgroundPhoto)
backgroundLabel.place(x=0, y=0, relwidth=1.0, relheight=1.0, anchor=CENTER)
backgroundLabel.pack()
root.update()
root.geometry(Const.ROOT_GEOMETRY)
root.minsize(Const.ROOT_MIN_WIDTH, Const.ROOT_MIN_HEIGHT)
root.maxsize(Const.ROOT_MAX_WIDTH, Const.ROOT_MAX_HEIGHT)

topFrame = Frame(backgroundLabel, bg=Const.ROOT_COLOR)
topFrame.pack(side=TOP, fill=BOTH)
middleFrame = Frame(backgroundLabel, bg=Const.ROOT_COLOR)
middleFrame.pack(side=TOP, anchor=W)
bottomFrame = Frame(backgroundLabel, bg=Const.ROOT_COLOR)
bottomFrame.pack(side=TOP)

title = Label(topFrame,
              text=Const.TOP_LABEL,
              font=Const.COURIER_24_BOLD,
              bg=Const.ROOT_COLOR
              )
title.pack()
subTitle = Label(topFrame,
                 text="v " + Const.VERSION + "      ",
                 font=Const.TIMESNEWROMAN_10,
                 bg=Const.ROOT_COLOR
                 )
subTitle.pack(side=RIGHT)


def convertSeason(tog=[0]):
    if tog[0]:
        summerToogle.config(text='', state=DISABLED,
                            bg=Const.COLOR_RED)
        winterToogle.config(text=Const.SEASON_WINTER, state=NORMAL,
                            bg=Const.COLOR_LIGHTGREEN)
        computerCheckbox.config(state=DISABLED, variable=IntVar(0))
    else:
        summerToogle.config(text=Const.SEASON_SUMMER, state=NORMAL,
                            bg=Const.COLOR_LIGHTGREEN)
        winterToogle.config(text='', state=DISABLED,
                            bg=Const.COLOR_RED)
        computerCheckbox.config(state=NORMAL)
    tog[0] = not tog[0]


def convertWeek(week=[0]):
    if week[0]:
        weekendToogle.config(text='', state=DISABLED,
                             bg=Const.COLOR_RED)
        weekdayToogle.config(text=Const.DAYTYPE_WEEKDAYS, state=NORMAL,
                             bg=Const.COLOR_LIGHTGREEN)
    else:
        weekendToogle.config(text=Const.DAYTYPE_WEEKENDS, state=NORMAL,
                             bg=Const.COLOR_LIGHTGREEN)
        weekdayToogle.config(text='', state=DISABLED,
                             bg=Const.COLOR_RED)
    week[0] = not week[0]


toogleFrame = Frame(middleFrame, bg=Const.ROOT_COLOR)
toogleFrame.pack(padx=(100, 20), pady=20)
seasonLabel = Label(toogleFrame, text=Const.SEASON_LABEL,
                    font=Const.COURIER_12_BOLD, anchor=W,
                    bg=Const.ROOT_COLOR)
seasonLabel.grid(row=0, column=0, sticky=W)
summerToogle = Button(toogleFrame, text='',
                      command=convertSeason,
                      width=8,
                      state=DISABLED,
                      bg=Const.COLOR_RED)
summerToogle.grid(row=0, column=2)
winterToogle = Button(toogleFrame, text=Const.SEASON_WINTER,
                      command=convertSeason,
                      width=8,
                      state=NORMAL,
                      bg=Const.COLOR_LIGHTGREEN)
winterToogle.grid(row=0, column=3)
emptyLabel = Label(toogleFrame, text='', bg=Const.ROOT_COLOR).grid(row=1)
dayTypeLabel = Label(toogleFrame, text=Const.DAYTYPE_LABEL,
                     font=Const.COURIER_12_BOLD, anchor=W,
                     bg=Const.ROOT_COLOR)
dayTypeLabel.grid(row=2, column=0, sticky=W)
weekendToogle = Button(toogleFrame, text='',
                       command=convertWeek,
                       width=8,
                       state=DISABLED,
                       bg=Const.COLOR_RED)
weekendToogle.grid(row=2, column=2)
weekdayToogle = Button(toogleFrame, text=Const.DAYTYPE_WEEKDAYS,
                       command=convertWeek,
                       width=8,
                       state=NORMAL,
                       bg=Const.COLOR_LIGHTGREEN)
weekdayToogle.grid(row=2, column=3)

applianceFrame = Frame(middleFrame, bg=Const.ROOT_COLOR)
applianceFrame.pack(padx=(100, 20), pady=5, anchor=W)
applianceLabel = Label(applianceFrame, text=Const.APPLIANCE_LABEL,
                       font=Const.COURIER_12_BOLD, anchor=W,
                       bg=Const.ROOT_COLOR)
applianceLabel.grid(row=0, column=0, sticky=W)

isAllChosen = IntVar(value=0)
isKettle = IntVar(value=0)
isFreezer = IntVar(value=0)
isFridge = IntVar(value=0)
isComputer = IntVar(value=0)
isWasher = IntVar(value=0)
isDryer = IntVar(value=0)
kettleCheckbox = Checkbutton(applianceFrame,
                             text=Const.APPLIANCE_KETTLE, variable=isKettle,
                             bg=Const.ROOT_COLOR)
kettleCheckbox.grid(row=1, column=2, sticky=W)
freezerCheckbox = Checkbutton(applianceFrame,
                              text=Const.APPLIANCE_FREEZER, variable=isFreezer,
                              bg=Const.ROOT_COLOR)
freezerCheckbox.grid(row=1, column=3, sticky=W)
fridgeCheckbox = Checkbutton(applianceFrame,
                             text=Const.APPLIANCE_FRIDGE, variable=isFridge,
                             bg=Const.ROOT_COLOR)
fridgeCheckbox.grid(row=2, column=2, sticky=W)
computerCheckbox = Checkbutton(applianceFrame,
                               text=Const.APPLIANCE_COMPUTER, variable=isComputer,
                               bg=Const.ROOT_COLOR)
computerCheckbox.grid(row=2, column=3, sticky=W)
washerCheckbox = Checkbutton(applianceFrame,
                             text=Const.APPLIANCE_WASHER, variable=isWasher,
                             bg=Const.ROOT_COLOR)
washerCheckbox.grid(row=3, column=2, sticky=W)
dryerCheckbox = Checkbutton(applianceFrame,
                            text=Const.APPLIANCE_DRYER, variable=isDryer,
                            bg=Const.ROOT_COLOR)
dryerCheckbox.grid(row=3, column=3, sticky=W)
checkboxs = [kettleCheckbox, freezerCheckbox, fridgeCheckbox, computerCheckbox, washerCheckbox, dryerCheckbox]


def checkAll():
    if isAllChosen.get():
        for cb in checkboxs:
            cb.select()
            cb.config(state=DISABLED)
            if cb == computerCheckbox and (winterToogle.cget('text') != '') is True:
                cb.deselect()
    else:
        for cb in checkboxs:
            cb.deselect()
            cb.config(state=NORMAL)


allCheckbox = Checkbutton(applianceFrame, text=Const.APPLIANCE_ALL,
                          variable=isAllChosen, command=checkAll,
                          bg=Const.ROOT_COLOR)
allCheckbox.grid(row=0, column=2, sticky=W)


def getChosenAppliances():
    if isAllChosen.get():
        return [Const.APPLIANCE_KETTLE, Const.APPLIANCE_FREEZER,
                Const.APPLIANCE_FRIDGE, Const.APPLIANCE_COMPUTER,
                Const.APPLIANCE_WASHER, Const.APPLIANCE_DRYER]
    else:
        appliaces = []
        if isKettle.get():
            appliaces.append(Const.APPLIANCE_KETTLE)
        if isFreezer.get():
            appliaces.append(Const.APPLIANCE_FREEZER)
        if isFridge.get():
            appliaces.append(Const.APPLIANCE_FRIDGE)
        if isComputer.get():
            appliaces.append(Const.APPLIANCE_COMPUTER)
        if isWasher.get():
            appliaces.append(Const.APPLIANCE_WASHER)
        if isDryer.get():
            appliaces.append(Const.APPLIANCE_DRYER)
        return appliaces


def argParse():
    """
    Function to connect to the backend
    ****Input:
            Season in boolean (0: Summer, 1: Winter)
            DayType in boolean (0: Weekday, 1: Weekend)
            Array of Appliance, by name.
    """
    season = (winterToogle.cget('text') != '')
    dayType = (weekendToogle.cget('text') != '')
    appliances = getChosenAppliances()
    main.Main.simulateData(season, dayType, appliances)


simulateButton = Button(bottomFrame, text=Const.BUTTON_TEXT,
                        fg=Const.COLOR_GREEN, font=Const.ARIAL_16_BOLD,
                        command=argParse)
simulateButton.pack(pady=(Const.PADDING_Y_AXIS_TYPE_3, 8))


def openInfoWindow():
    infoWindow = Toplevel(root)
    infoWindow.title(Const.SUBWINDOW_TITLE)
    infoWindow.configure(bg=Const.ROOT_COLOR)
    backgroundLabelForSubWindow = Label(infoWindow, image=backgroundPhoto)
    backgroundLabelForSubWindow.place(x=0, y=0, relwidth=1.0, relheight=1.0, anchor=CENTER)
    backgroundLabelForSubWindow.pack()
    infoWindow.update()
    infoWindow.geometry(Const.SUBWINDOW_GEOMETRY)
    infoWindow.minsize(Const.SUBWINDOW_MIN_WIDTH, Const.SUBWINDOW_MIN_HEIGHT)
    infoWindow.maxsize(Const.SUBWINDOW_MAX_WIDTH, Const.SUBWINDOW_MAX_HEIGHT)
    # infoWindow.resizable(width=False, height=False)


moreInfoText = Text(backgroundLabel, bg=Const.ROOT_COLOR, relief=FLAT)
moreInfoText.config(width=17, height=1)
hyperlink = tkHyperlinkManager.HyperlinkManager(moreInfoText)
moreInfoText.insert(INSERT, "About ECS", hyperlink.add(openInfoWindow))
moreInfoText.config(state=DISABLED)
moreInfoText.pack(anchor=W)

root.mainloop()
