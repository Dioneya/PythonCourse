import wx
import re
import datetime
import os.path
from os import path, getcwd
class LogFrame(wx.Frame):
    ''' Класс окна отображения лога '''

    def __init__(self):
        wx.Frame.__init__(
            self, None, -1, "Искатель строк", size=(500, 400))
        self.create_menu()
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([-3, -2])
        self.create_log_file()

        self.sample_list = []
        self.list_box = wx.ListBox(self, -1, (20, 20), (80, 120),
                              self.sample_list, wx.LB_SINGLE)

        self.statusbar.SetStatusText('')
        self.statusbar.SetStatusText("", 1)

    def create_log_file(self):
        log_file_path = os.path.join(os.path.dirname(
                                    __file__), 'script18.log')
        print(log_file_path)
        if not path.exists(log_file_path):
            print('work')
            message = wx.MessageDialog(self,'Файл лога не найден. Файл будет создан автоматически')
            message.ShowModal()
            with open(log_file_path,'w') as f:
                pass
            pass
        else:
            print('gg')


    def menu_data(self):
        data = (("&Файл",
                 ({"&Открыть...": self.on_open_file},)),
                ("&Лог",
                 ({"&Экспорт...": self.on_save_log},
                  {"&Добавить в лог": self.add_to_log},
                  {"&Просмотр лога": self.read_log})
                 ))
        return data

    def create_menu(self):
        menu = wx.MenuBar()

        for item in self.menu_data():
            menu_item = self.create_sub_menu(item[1])
            menu.Append(menu_item, item[0])

        self.SetMenuBar(menu)

    def create_sub_menu(self, itemgroup):
        groupmenu = wx.Menu()
 
        for items in itemgroup:
            for item in items.keys():
                title = item
                handler = items[item]
                menu_item = groupmenu.Append(-1, title)
                if handler:
                    self.Bind(wx.EVT_MENU, handler, menu_item)

        return groupmenu

    def on_open_file(self, event):
        dlg = wx.FileDialog(self, message="Выберите файл", defaultDir="",
                            defaultFile="", wildcard="*.*", style=wx.FD_OPEN)

        # при открытии файла просто обновляем строку состояния

        if dlg.ShowModal() == wx.ID_CANCEL:
            return  

        self.statusbar.SetStatusText('Обработан файл '+dlg.GetPath())
        self.statusbar.SetStatusText(
                                    '{0:,}'.format(
                                        os.path.getsize(dlg.GetPath())
                                        ).replace(',', ' ')+' байт',
                                    1)
        self.__find_matches_in_lines(self.__get_text_in_file(dlg.GetPath()),dlg.GetPath())
        
    def __get_text_in_file(self,name):
        try:
            with open (name, 'r') as f:
                return f.readlines()
        except IOError as err:
            print(err)
            return []
        pass

    def __find_matches_in_lines(self,lines,path):
        regex = r'[(]\d{3}[)](\d{7}|\d{3}([-]\d{2}){2})' # (000)1234567 или (000)111-22-33
        self.list_box.InsertItems(['Файл {} был обработан {} \n'.format(path,datetime.datetime.now()),'\n'], self.list_box.GetCount())
        line_cnt = 1
        for i in lines:
            data = ['Строка {}, позиция {} : найдено \'{}\'\n'.format(line_cnt, match.start(), match.group()) for match in re.finditer(regex, i)]
            data.append('')
            self.list_box.InsertItems(data,self.list_box.GetCount())
            line_cnt+=1
            pass
        pass

    def on_save_log(self, event):
        dlg = wx.FileDialog(self, message="Выберите файл", defaultDir="",
                            defaultFile="", wildcard="*.*", style=wx.FD_SAVE)

        if dlg.ShowModal() == wx.ID_CANCEL:
            return  
        
        self.save_log(dlg.GetPath())
    
    def save_log(self,path):
        f = open(path,'w')
        f.writelines(self.list_box.Items)
        f.close()

        
    def add_to_log(self,event):
        log_file_path = os.path.join(os.path.dirname(
                                    __file__), 'script18.log')
        f = open(log_file_path,'a')
        f.writelines(self.list_box.Items)
        f.close()

    def read_log(self,event):
        dlg = wx.MessageDialog(self,'Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!','Warning',wx.OK | wx.CANCEL)
        dlg.SetOKCancelLabels('Да','Нет')
        
        if dlg.ShowModal() == wx.ID_CANCEL:
            return
        log_file_path = os.path.join(os.path.dirname(
                                    __file__), 'script18.log')
        f = open(log_file_path,'r')
        text = f.readlines() 
        self.list_box.Clear()
        self.list_box.InsertItems(text,self.list_box.GetCount())

if __name__ == '__main__':
    # создаем объект приложения
    app = wx.App()
    # создаем объект окна MainFrame
    log_frame = LogFrame()
    # и показываем
    log_frame.Show()

    # запускаем главный цикл обработки сообщений
    app.MainLoop()