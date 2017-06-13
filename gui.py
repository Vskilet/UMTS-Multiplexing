import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QImage

from initializeCommunications import *
import signalplot

MOBILE_NUMBER = 5

def comboboxListener():
    mobile_id = ui.ComboBoxNumber.currentText()
    ui.LabelTextOVSF.setText(bin(listMobile[int(mobile_id)].ovsfCode))
    ui.LabelTextDecodeMessage.setText(str(listMobile[int(mobile_id)].message))

def buttonNewSimulationListener():
    #ui.LineEditInterferencesAmplitude.setText(ui.LineEditNbPhone.displayText())
    initialization(ui.LineEditNbPhone.displayText())

def initialization(total_nb_mob):
    # generate Codes
    listCodes = ovsfGenerator(total_nb_mob)
    # generate a testing list of mobile phones
    listMobile = [Mobile(str(i), listCodes[i]) for i in range(0, total_nb_mob)]

    print(listMobile)
    ui.ComboBoxNumber.clear()
    for mobile in listMobile:
        print(mobile)
        ui.ComboBoxNumber.insertItem(0, mobile.identifier)

    signal = [0 for x in range(0, len(bitToString(listMobile[0].ovsfCode)))]
    # generate the global signal with the mobiles ovsf codes (all mobiles send 1 for the moment
    print(len(bitToString(listMobile[0].ovsfCode)))
    for i in range(0, len(bitToString(listMobile[0].ovsfCode))):
        for mobile in listMobile:
            if (mobile.message != 0):
                if (mobile.message == 1):
                    bits = bitToString(mobile.ovsfCode)
                if (mobile.message == -1):
                    bits = conjugue(bitToString(mobile.ovsfCode))
                if (bits[i] == '0'):
                    signal[i] -= 1
                else:
                    signal[i] += 1
    # signal=signal[::-1]
    print(signal)
    return signal, listMobile

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = loadUi('gui.ui')
    ui.show()

    signal, listMobile = initialization(MOBILE_NUMBER)

    # cheating function in order to test if the demodulation fuction works
    # Actualy, with this signal the function may return 1 -1 -1 1, 1 is 1 and -1 is 0 and 0 is nothing
    #
    for i in listMobile:
        print(demodulateSignal(signal, i))
    
    
    comboboxListener()

    ui.ComboBoxNumber.activated.connect(comboboxListener)
    ui.ButtonNewSimulation.clicked.connect(buttonNewSimulationListener)

    # Affichage du signal

    signalplot.plot(signal)
    qimg = QImage("plot.png")
    pixmap = QPixmap(qimg)
    ui.plotLabel.setPixmap(pixmap)


    sys.exit(app.exec_())
