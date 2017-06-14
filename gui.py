import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QImage

from initializeCommunications import *
import signalplot

MOBILE_NUMBER = 20
listMobile=[]
def comboboxListener():
    mobile_id = int(ui.ComboBoxNumber.currentText())
    ui.LabelTextOVSF.setText(bin(listMobile[mobile_id].ovsfCode))
    ui.LabelTextDecodeMessage.setText(str(demodulateSignal(signal,listMobile[mobile_id])))
    ui.LabelTextDesiredMessage.setText(str(listMobile[mobile_id].message))

def buttonNewSimulationListener():
    #ui.LineEditInterferencesAmplitude.setText(ui.LineEditNbPhone.displayText())
    listMobileGenerator(int(ui.LineEditNbPhone.displayText()))
    #printSignal(signal)

def comboBoxGenerate():
    ui.ComboBoxNumber.clear()
    for mobile in listMobile:
        print(mobile)
        ui.ComboBoxNumber.insertItem(0, mobile.identifier)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    listMobile = listMobileGenerator(MOBILE_NUMBER)
    ui = loadUi('gui.ui')
    ui.show()
    comboBoxGenerate()
    signal = generateGlobalSignal(listMobile)
    comboboxListener()

    ui.ComboBoxNumber.activated.connect(comboboxListener)
    ui.ButtonNewSimulation.clicked.connect(buttonNewSimulationListener)
    signalplot.plot(signal)
    qimg = QImage("plot.png")
    pixmap = QPixmap(qimg)
    ui.plotLabel.setPixmap(pixmap)

    sys.exit(app.exec_())
