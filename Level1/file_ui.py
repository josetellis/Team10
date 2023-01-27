from threading import *
from Level1.Findfileprj import FileFinder
def file_read():
    filname=input("Enter the file Name")
    drive=input("Enter the Drive")
    obj=FileFinder()
    print(obj.find_file(filname,drive))
def demo1():
    print("Do other task")
task1=Thread(target=file_read)
task2=Thread(target=demo1)
task1.start()
task2.start()