#!/usr/bin/env python
# -*- coding: utf-8 -*-#

__author__ = 'Mario Lacunza <mlacunza@gmail.com>'
__version__ = '0.9.1'

"""
Archivo inicial para Velantur.

Equivale al EXE

"""
import wx
import db.sq

import tools.errores

class pyMeGestor(wx.App):

    def OnInit(self):
        self.oDB = db.sq.cSqlite()
        self.oError = tools.errores.Error()
        
        self.Inicio()
        return True

    def Inicio(self):
        #Prueba datos
        test = self.oDB.testConn()
        #TODO: Mejorar esta verificacion
        if (test==None):
            #Ingrese Coneccion    
            import frm.frmBD as fBD
            bd = fBD.clsBD(None)
            bd.Show()
        else:
            #Carga Coneccion a la BD Principal
            self.oDB.CargaConn()
            #TODO: aqui deberia redirigir al Login
            import frm.frmMain as fMain  # @UnresolvedImport
            m = fMain.clsMain(None)
            m.Show()

        
def main():
    application = pyMeGestor()
    application.MainLoop()

if __name__ == '__main__':
    main()