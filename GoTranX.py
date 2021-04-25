import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from googletrans import Translator

_ca = ('af', 'sq', 'ar', 'be', 'bg', 'ca', 'zh',
       'hr', 'cs', 'da', 'nl', 'en', 'et', 'tl', 'fi', 'fr', 'gl', 'de', 'el', 'iw',
       'hi', 'hu', 'is', 'id', 'ga', 'it', 'ja', 'ko', 'lv', 'lt', 'mk', 'ms', 'mt',
       'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk', 'sl', 'es', 'sw', 'sv', 'th',
       'tr', 'uk', 'vi', 'cy', 'yi')
_cb = ('Afrikaans', 'Albanian', 'Arabic',
       'Belarusian', 'Bulgarian', 'Catalan', 'Chinese', 'Croatian', 'Czech',
       'Danish', 'Dutch', 'English', 'Estonian', 'Filipino', 'Finnish', 'French',
       'Galician', 'German', 'Greek', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic',
       'Indonesian', 'Irish', 'Italian', 'Japanese', 'Korean', 'Latvian',
       'Lithuanian', 'Macedonian', 'Malay', 'Maltese', 'Norwegian', 'Persian',
       'Polish', 'Portuguese', 'Romanian', 'Russian', 'Serbian', 'Slovak',
       'Slovenian', 'Spanish', 'Swahili', 'Swedish', 'Thai', 'Turkish', 'Ukrainian',
       'Vietnamese', 'Welsh', 'Yiddish')


def info(self):
    _va = """
GoTranX is a simple text translator, which uses the Google Translate service to do the translation.

To keep GoTranX usable for you, after translating, make sure you give it enough delay time (at least 5 seconds)
before the next translation. Tho this is not too necessary since module i use here, already supports bulk-translation which is botproof.

Im using (for this open-source version) googletrans module from https://github.com/ssut/py-googletrans.
So please put star for the repo if you found it useful, or if you have modify this project.

Version : 1.0
Programmer : Arachmadi Putra (https://me.cimosoft.com)
"""
    messagebox.showerror("About", _va)


class GoTranX:

    # setout : filling output text (_wge) with result text
    def setout(self, _va):
        self._wge.configure(state='normal')
        self._wge.delete(1.0, "end")
        self._wge.insert("end", _va)
        self._wge.configure(state='disabled')

    # trans : translation process start here
    def trans(self):
        try:
            _va = Translator()
            _vb = self._wgd.get("1.0", "end-1c")
            if len(_vb) != 0:
                _vc = _va.translate(
                    str(_vb), src=_ca[self._wgb.current()], dest=_ca[self._wgc.current()]).text
            self.setout(_va=_vc)
        except Exception as _vd:
            messagebox.showwarning("Ouch !", _vd)

    def __init__(self, master=None):
        # draw Frame : for container
        self._wga = ttk.Frame(master)
        # draw Combobox : for source language selection
        self._wgb = ttk.Combobox(self._wga)
        self._wgb.place(anchor='nw', relx='0.05', rely='0.05', x='0', y='0')
        # draw Combobox : for destination language selection
        self._wgc = ttk.Combobox(self._wga)
        self._wgc.place(anchor='nw', relx='0.51', rely='0.05', x='0', y='0')
        # draw Text : for source text entry
        self._wgd = tk.Text(self._wga)
        self._wgd.configure(
            blockcursor='false', font='{Consolas} 8 {}', height='10', insertunfocussed='none', wrap='word')
        self._wgd.configure(takefocus=False, width='50')
        self._wgd.place(anchor='nw', height='100', relx='0.05',
                        rely='0.15', width='283', x='0', y='0')
        # draw Text : for result text output
        self._wge = tk.Text(self._wga)
        self._wge.configure(
            blockcursor='false', font='{Consolas} 8 {}', height='10', insertunfocussed='none', wrap='word')
        self._wge.place(anchor='nw', height='100', relx='0.05',
                        rely='0.55', width='283', x='0', y='0')
        # draw Button : for translation execution
        self._wgf = ttk.Button(self._wga, command=self.trans)
        self._wgf.configure(cursor='hand2', text='TRANSLATE')
        self._wgf.place(anchor='nw', bordermode='outside',
                        relx='0.05', rely='0.46', width='150', x='0', y='0')
        # draw Label : for information
        self._wgg = ttk.Label(self._wga)
        self._wgg.configure(anchor='center', font='{Segoe UI} 8 {}',
                            justify='center', text='© 2021 Cimosoft Codelicious, Org')
        self._wgg.place(anchor='nw', relx='0', rely='0.9',
                        width='320', x='0', y='0')
        self._wgg.bind("<Button>", info)
        self._wga.configure(height='340', width='320')
        self._wga.pack(side='top')
        # define Frame as mainwindow
        self.mainwindow = self._wga
        # fill up combobox with language names (_cb)
        _va = list()
        for _vb in _cb:
            _va.append(_vb)
        self._wgb['values'] = _va
        self._wgc['values'] = _va
        # setting default selection on each combobox
        self._wgb.current(11)
        self._wgc.current(23)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    import tkinter as tk
    _va = tk.Tk()
    _va.resizable(0, 0)
    _va.winfo_toplevel().title("GoTranX 1.0")
    _vb = GoTranX(_va)
    _vb.run()
