#http://docs.python-requests.org/en/master/
import requests, json, threading
from Tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("HTTP CLIENT")

        self.label = Label(master, text="", bg="green")
        self.label.place(height=100, width=200, x=10, y=10)

        self.btnGetString = Button(master, text="Get String", command=self.threadGetString)
        self.btnGetString.place(height=40, width=120, x=10, y=120)

        self.btnSendString = Button(master, text="Send String", command=self.threadSendString)
        self.btnSendString.place(height=40, width=120, x=10, y=170)

        self.btnGetJson = Button(master, text="Get JSON", command=self.threadGetJson)
        self.btnGetJson.place(height=40, width=120, x=10, y=220)

        self.btnSendJson = Button(master, text="Send JSON", command=self.threadSendJson)
        self.btnSendJson.place(height=40, width=120, x=10, y=270)

        self.btnGetJsonArray = Button(master, text="Get JSON Array", command=self.threadGetJsonArray)
        self.btnGetJsonArray.place(height=40, width=120, x=10, y=320)

        self.btnSendJsonArray = Button(master, text="Send JSON Array", command=self.threadSendJsonArray)
        self.btnSendJsonArray.place(height=40, width=120, x=10, y=370)

    def getString(self):
        try:
            r = requests.get("http://213.82.212.147:90")
            x = r.text
            self.label.config(text=x)
        except Exception:
            self.label.config(text="Error get string")

    def sendString(self):
        try:
            requests.post("http://213.82.212.147:90/getstring", data="Python")
        except Exception:
            print "Error send string"

    def getJson(self):
        try:
            r = requests.post("http://213.82.212.147:90/sendjson")
            result = json.loads(r.text)
            x = result["Name"]
            self.label.config(text=x)
        except Exception:
            self.label.config(text="Error get json")

    def sendJson(self):
        try:
            data = {}
            data['Name'] = "Nuria"
            data['Car'] = "Ferrari"
            data['Country'] = "Spain"
            jsonData = json.dumps(data)
            requests.post("http://213.82.212.147:90/getjson", jsonData)
        except Exception:
            print "Error send json"

    def getJsonArray(self):
        try:
            r = requests.post("http://213.82.212.147:90/sendjsonarray")
            result = json.loads(r.text)
            str = []
            for x in result:
                str.append(x["Name"] + "\n")
            self.label.config(text=" ".join(str))
        except Exception:
            self.label.config(text="Error get json array")

    def sendJsonArray(self):
        try:
            xa = {}
            xa['Name'] = "Nuria"
            xa['Car'] = "Ferrari"
            xa['Country'] = "Spain"
            xb = {}
            xb['Name'] = "Natalia"
            xb['Car'] = "Porsche"
            xb['Country'] = "Spain"
            lisx = []
            lisx.append(xa)
            lisx.append(xb)
            jsonData = json.dumps(lisx)
            requests.post("http://213.82.212.147:90/getjsonarray", jsonData)
        except Exception:
            print "Error send json array"

    def threadGetString(self):
        self.thread = threading.Thread(target=self.getString)
        self.thread.start()

    def threadSendString(self):
        self.thread = threading.Thread(target=self.sendString)
        self.thread.start()

    def threadGetJson(self):
        self.thread = threading.Thread(target=self.getJson)
        self.thread.start()

    def threadSendJson(self):
        self.thread = threading.Thread(target=self.sendJson)
        self.thread.start()

    def threadGetJsonArray(self):
        self.thread = threading.Thread(target=self.getJsonArray)
        self.thread.start()

    def threadSendJsonArray(self):
        self.thread = threading.Thread(target=self.sendJsonArray)
        self.thread.start()

root = Tk()
root.resizable(0, 0)
root.geometry("400x500+20+20")
my_gui = MyFirstGUI(root)
root.mainloop()