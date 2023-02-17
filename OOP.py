import customtkinter as CTk
from PIL import Image



class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("250x320")
        self.title("Cal")
        self.resizable(False, False)

        #self.logo = CTk.CTkImage(dark_image=Image.open("i.png"), size=(450, 150))
        #self.logo_lbl = CTk.CTkLabel(master=self, text='', image=self.logo)
        #self.logo_lbl.grid(row=0, column=0)

        


if __name__ == '__main__':
    app = App()
    app.mainloop()