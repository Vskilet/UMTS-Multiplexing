import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QImage

from initializeCommunications import *
import signalplot

MOBILE_NUMBER = 5

def comboboxListener(listMobile):
    mobile_id = int(ui.ComboBoxNumber.currentText())
    ui.LabelTextOVSF.setText(bin(listMobile[mobile_id].ovsfCode))
    ui.LabelTextDecodeMessage.setText(str(listMobile[mobile_id].message))

def buttonNewSimulationListener():
    #ui.LineEditInterferencesAmplitude.setText(ui.LineEditNbPhone.displayText())
    listMobileGenerator(int(ui.LineEditNbPhone.displayText()))
    #printSignal(signal)

def comboBoxGenerate(listMobile):
    ui.ComboBoxNumber.clear()
    for mobile in listMobile:
        print(mobile)
        ui.ComboBoxNumber.insertItem(0, mobile.identifier)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = loadUi('gui.ui')
    ui.show()

    listMobile = listMobileGenerator(MOBILE_NUMBER)
    comboBoxGenerate(listMobile)
    signal = generateGlobalSignal(listMobile)
    # cheating function in order to test if the demodulation fuction works
    # Actualy, with this signal the function may return 1 -1 -1 1, 1 is 1 and -1 is 0 and 0 is nothing
    #
    for i in listMobile:
        print(demodulateSignal(signal, i))

    comboboxListener(listMobile)

    ui.ComboBoxNumber.activated.connect(comboboxListener(listMobile))
    ui.ButtonNewSimulation.clicked.connect(buttonNewSimulationListener)

    #printSignal(signal)
    signalplot.plot(signal)
    qimg = QImage("plot.png")
    pixmap = QPixmap(qimg)
    ui.plotLabel.setPixmap(pixmap)

    sys.exit(app.exec_())
