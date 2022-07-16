from datetime import datetime
import qrcode
from PyQt5 import QtWidgets
import sys
import var


class Eventos:

    def salir(self):
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))

    def limpiar_texto(self):
        var.ui.lineEdit_texto.setText("")

    def procesar_qr(self):
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
