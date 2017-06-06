import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi

from initializeCommunications import *

def comboboxListener():
    mobile_id = ui.ComboBoxNumber.currentText()
    ui.LabelTextOVSF.setText(bin(listMobile[int(mobile_id)].ovsfCode))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = loadUi('gui.ui')
    ui.show()

    MOBILE_NUMBER = 250

    # generate Codes
    listCodes = ovsfGenerator(MOBILE_NUMBER)
    # generate a testing list of mobile phones
    listMobile = [Mobile(str(i), listCodes[i]) for i in range(0, MOBILE_NUMBER)]
    print(listMobile)
    for mobile in listMobile:
        print(mobile)
        ui.ComboBoxNumber.insertItem(0, mobile.identifier)

    ui.ComboBoxNumber.activated.connect(comboboxListener)

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

    # cheating function in order to test if the demodulation fuction works
    # Actualy, with this signal the function may return 1 -1 -1 1, 1 is 1 and -1 is 0 and 0 is nothing
    #
    for i in listMobile:
        print(demodulateSignal(signal, i))

    sys.exit(app.exec_())