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
listMobile = []
signal = []


def comboboxListener():
    global signal
    global listMobile
    mobile_id = int(ui.ComboBoxNumber.currentText())
    ui.LabelTextOVSF.setText(bin(listMobile[mobile_id].ovsfCode))
    # print(signal)
    ui.LabelTextDecodeMessage.setText(str(demodulateSignal(signal, listMobile[mobile_id])))
    ui.LabelTextDesiredMessage.setText(str(listMobile[mobile_id].message))


def comboboxStrListener():
    global signal
    global listMobile
    mobile_id = int(ui.ComboBoxNumber.currentText())
    ui.LabelTextOVSF.setText(bin(listMobile[mobile_id].ovsfCode))
    # print(signal)
    ui.LabelTextDesiredMessage.setText(str(listMobile[mobile_id].ascii))
    try:
        ui.LabelTextDecodeMessage.setText(str(listMobile[mobile_id].unbin()))
    except:
        ui.LabelTextDecodeMessage.setText("errors due to noises...")


def buttonListener():
    simulation(MOBILE_NUMBER)


def buttonStrListener():
    # print("###### test ######")
    simulationSTR(MOBILE_NUMBER)
    comboboxStrListener()


def spinnerListener():
    global MOBILE_NUMBER
    MOBILE_NUMBER = ui.mobileNumber.value()


def sliderListener():
    ui.LabelTextInterferencesRate.setText(str(ui.SliderInterferencesRate.value()))


def comboBoxGenerate():
    global listMobile
    ui.ComboBoxNumber.clear()
    for mobile in listMobile:
        # print(mobile)
        ui.ComboBoxNumber.insertItem(0, mobile.identifier)


def printErrorRate():
    ui.LabelErrorRate.setText(str(calculErrorRate(signal, listMobile) * 100 / len(listMobile)))


def printErrorRateStr():
    ui.LabelErrorRate.setText(str(calculErrorRateStr(signal, listMobile) * 100 / len(listMobile)))


def simulation(mobileNumber):
    global MOBILE_NUMBER
    global listMobile
    global signal
    signalplot.clear()
    MOBILE_NUMBER = mobileNumber
    listMobile = listMobileGenerator(MOBILE_NUMBER)

    clean_signal = generateGlobalSignal(listMobile)

    degraded_signal = addRandomNoises(clean_signal, ui.SpinInterferencesAmplitude.value(),
                             ui.SliderInterferencesRate.value())
    printErrorRate()

    ui.LabelSignal.setText("Original signal : " + str(clean_signal) + "\nDegraded signal : " + str(degraded_signal))
    comboBoxGenerate()
    comboboxListener()
    ui.ComboBoxNumber.activated.connect(comboboxListener)
    signalplot.plot(clean_signal, degraded_signal)
    qimg = QImage("plot.png")
    pixmap = QPixmap(qimg)
    ui.plotLabel.setPixmap(pixmap)
    codeSize = (len(str(bin(listMobile[0].ovsfCode))) - 2)
    ui.codeLengthLabel.setText(str(codeSize))
    ui.LabelThroughput.setText(str(3840 / codeSize) + "kbps")


def simulationSTR(mobileNumber):
    global MOBILE_NUMBER
    global listMobile
    global signal
    signalplot.clear()
    MOBILE_NUMBER = mobileNumber
    listMobile = listMobileGenerator(MOBILE_NUMBER)
    sendAscii(listMobile, ui.SpinInterferencesAmplitude.value(), ui.SliderInterferencesRate.value())
    ui.LabelSignal.setText("")
    printErrorRateStr()
    ui.plotLabel.clear()
    comboBoxGenerate()
    comboboxListener()
    codeSize = (len(str(bin(listMobile[0].ovsfCode))) - 2)
    ui.codeLengthLabel.setText(str(codeSize))
    ui.LabelThroughput.setText(str(3840 / codeSize) + "kbps")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = loadUi('gui.ui')
    simulation(MOBILE_NUMBER)

    ui.mobileNumber.setValue(MOBILE_NUMBER)
    ui.mobileNumber.valueChanged.connect(spinnerListener)
    ui.buttonBitSimulation.clicked.connect(buttonListener)
    ui.buttonStringSimulation.clicked.connect(buttonStrListener)
    ui.SliderInterferencesRate.valueChanged.connect(sliderListener)
    ui.show()

    sys.exit(app.exec_())
