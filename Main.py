class Widget():
    def __init__(self,title_text,x_num,y_num,):
        self.title_text=title_text
        self.x_num=x_num
        self.y_num=y_num
        def print_info(self):
            print("Напис",title_text)
            print("Розташування",x_num,y_num)

class Button(Widget):
    def __init__(self,is_clicked_bool,title_text,x_num,y_num):
        super().__init__(title_text,x_num,y_num)
        self.is_clicked=is_clicked_bool
    def click(self):
        is_clicked_bool=True
        print("Ви зареєстровані")
button1=Button(False,"Брати участь",100,100)
answer=input("Хочете зареєструватися?(так / ні):")
if answer=="так":
    button1.click()
else:
    print("Шкода")
