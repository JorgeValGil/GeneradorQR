import qrcode
from datetime import datetime
import var, sys
from PyQt5 import QtWidgets

class Eventos():

    def Salir(self):
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))

    def LimpiarTexto(self):
        var.ui.lineEdit_texto.setText("")

    def ProcesarQr(self):
        texto = var.ui.lineEdit_texto.text()
        if texto != "":
            ventana_carpeta = QtWidgets.QFileDialog
            carpeta_destino = ventana_carpeta.getExistingDirectory(None, 'Selecciona la carpeta de destino')
            if ventana_carpeta.Accepted and carpeta_destino != '':
                img = qrcode.make(texto)
                now = datetime.now()
                dt_string = now.strftime("%d_%m_%Y-%H_%M_%S")
                nombre = carpeta_destino+'/'+dt_string + '.png'
                img.save(nombre)
                var.ui.labelstatusbar.setText('GENERADA IMAGEN  '+dt_string + '.png')
        else:
            var.ui.labelstatusbar.setText('DEBES INTRODUCIR TEXTO PARA GENERAR EL CÓDIGO QR')


