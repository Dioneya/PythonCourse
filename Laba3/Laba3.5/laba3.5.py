import wx
from StringFormater import StringFormater 

class StringFrame(wx.Frame):
    ''' Класс окна работы со строками '''

    def __init__(self):
        self.formater = StringFormater()

        wx.Frame.__init__(
            self, None, -1, "Обработка строк", size=(400, 320))

        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, "Строка:", pos=(5, 20))
        self.entry_text = wx.TextCtrl(
            panel, -1, "", size=(300, -1), pos=(70, 20))
        wx.StaticText(panel, -1, "Результат:", pos=(5, 230))
        self.result_text = wx.TextCtrl(
            panel, -1, "", size=(300, -1), pos=(70, 230))

        self.delete_cnt = sc = wx.SpinCtrl(panel, -1, "", (295, 55), (40, -1))
        sc.SetRange(1, 20)
        sc.SetValue(5)

        self.delete_check = wx.CheckBox(panel, -1, "Удалить слова размером меньше",
                    (70, 60), (250, 20))
        wx.StaticText(panel, -1, "букв", pos=(340, 62))
        self.replace_check = wx.CheckBox(panel, -1, "Заменить все цифры на *", (70, 80), (220, 20))
        self.space_check = wx.CheckBox(panel, -1, "Вставить пробелы между символами",
                    (70, 100), (280, 20))
        self.sort_checkbox = wx.CheckBox(panel, -1, "Сортировать слова в строке",
                                         (70, 120), (220, 20))

        self.radio_by_size = wx.RadioButton(
            panel, -1, "По размеру", (100, 140), (150, 20))
        self.radio_by_lex = wx.RadioButton(
            panel, -1, "Лексикографически", (100, 160), (150, 20))
        self.radio_by_size.Disable()
        self.radio_by_size.SetValue(True)
        self.radio_by_lex.Disable()

        format_button = wx.Button(panel, -1, "Форматирование",
                                  size=(300, 30), pos=(70, 190))

        self.Bind(wx.EVT_BUTTON, self.on_format_click, format_button)
        self.Bind(wx.EVT_CHECKBOX, self.on_check, self.sort_checkbox)

    def on_format_click(self, event):
        # кое-что реализуем...
        input = self.entry_text.GetValue()
        if self.delete_check.GetValue(): 
            input = self.formater.delete_words_less(input, self.delete_cnt.GetValue())
        
        if self.replace_check.GetValue():
            input = self.formater.replace_numbers(input)
        
        if self.space_check.GetValue():
            input = self.formater.add_space_between_letters(input)
        
        if self.sort_checkbox.GetValue():
            input = self.formater.get_sorted_by_lexgraph(input) if self.radio_by_lex.GetValue() else self.formater.get_sorted_by_len(input)
                
        self.result_text.Value = input

    def on_check(self, event):
        if self.sort_checkbox.IsChecked():
            self.radio_by_size.Enable()
            self.radio_by_lex.Enable()
        else:
            self.radio_by_size.Disable()
            self.radio_by_lex.Disable()

if __name__ == '__main__':
    # создаем объект приложения
    app = wx.App()
    # создаем объект окна MainFrame
    string_frame = StringFrame()
    # и показываем
    string_frame.Show()
    # запускаем главный цикл обработки сообщений
    app.MainLoop()