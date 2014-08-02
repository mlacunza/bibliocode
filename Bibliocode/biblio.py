#!/usr/bin/env python
# -*- coding: utf-8 -*-#

__author__ = 'Mario Lacunza <mlacunza@gmail.com>'
__version__ = '0.1'

"""
Archivo inicial para BiblioCode.

Equivale al EXE - 02

"""
import wx
#import tools.errores

class biblio(wx.App):

    def OnInit(self):

        self.Inicio()
        return True

    def Inicio(self):
        pass
        
def main():
    application = biblio()
    application.MainLoop()

if __name__ == '__main__':
    main()