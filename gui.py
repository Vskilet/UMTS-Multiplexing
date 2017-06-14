import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QImage
from initializeCommunications import *
import signalplot

global MOBILE_NUMBER
global listMobile
global signal
global ui
MOBILE_NUMBER = 5
listMobile=[]
signal=[]
def comboboxListener():
    global signal
    global listMobile
    mobile_id = int(ui.ComboBoxNumber.currentText())
    ui.LabelTextOVSF.setText(bin(listMobile[mobile_id].ovsfCode))
    print(signal)
    ui.LabelTextDecodeMessage.setText(str(demodulateSignal(signal,listMobile[mobile_id])))
    ui.LabelTextDesiredMessage.setText(str(listMobile[mobile_id].message))

def buttonListener():
    simulation(MOBILE_NUMBER)

def spinnerListener():
    MOBILE_NUMBER = ui.mobileNumber.value()

def comboBoxGenerate():
    global listMobile
    ui.ComboBoxNumber.clear()
    for mobile in listMobile:
        print(mobile)
        ui.ComboBoxNumber.insertItem(0, mobile.identifier)

def simulation(mobileNumber):
    global MOBILE_NUMBER
    global listMobile
    global signal
    MOBILE_NUMBER=mobileNumber
    listMobile = listMobileGenerator(MOBILE_NUMBER)
    signal = generateGlobalSignal(listMobile)
    ui.LabelSignal.setText("Signal : " + str(signal) )
    comboBoxGenerate()
    comboboxListener()
    ui.ComboBoxNumber.activated.connect(comboboxListener)
    signalplot.plot(signal)
    qimg = QImage("plot.png")
    pixmap = QPixmap(qimg)
    ui.plotLabel.setPixmap(pixmap)
    ui.mobileNumber.setValue(MOBILE_NUMBER)
    ui.mobileNumber.valueChanged.connect(spinnerListener)
    ui.buttonBitSimulation.clicked.connect(buttonListener)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = loadUi('gui.ui')
    simulation(10)

    ui.show()

    sys.exit(app.exec_())
