from PySide2 import QtWidgets, QtCore
import os
import sys


class Ui(QtWidgets.QWidget):
    """for creating widget for the UI
    """
    def __init__(self):
        """for initializing
        """
        super().__init__()
        self.createUi()
        self.createLayout()
    
    def createUi(self):
        """Function for Creating widgets for Ui
        """
        self.LabelShotdetails = QtWidgets.QLabel("Shot Details")
        self.LabelShotdetails.setObjectName("ShotDetails")
        self.LabelProject = QtWidgets.QLabel("Project")
        self.LabelScope = QtWidgets.QLabel("Scope")
        self.LabelProject2= QtWidgets.QLabel("Project")
        self.LabelScope2 = QtWidgets.QLabel("Scope")
        self.TextBoxProject = QtWidgets.QLineEdit()
        self.TextBoxProject2 = QtWidgets.QLineEdit()
        self.TextBoxScope = QtWidgets.QLineEdit()
        self.TextBoxScope2 = QtWidgets.QLineEdit()
        # platblast details
        self.LabelPlayblastdetails = QtWidgets.QLabel("Playblast Details")
        self.LabelPlayblastdetails.setObjectName("PlayblastDetails")
        self.LabelWireframe = QtWidgets.QLabel("Wireframe")
        self.LabelShaded = QtWidgets.QLabel("Shaded")
        self.LabelCone= QtWidgets.QLabel("Cone")
        self.LabelPersp = QtWidgets.QLabel("Persp")
        self.LabelCustom = QtWidgets.QLabel("Custom")
        self.LabelCustomfiles = QtWidgets.QLabel("CustomFiles")
        self.wireframecb = QtWidgets.QCheckBox()
        self.shadedcb = QtWidgets.QCheckBox()
        self.conecb = QtWidgets.QCheckBox()
        self.perspcb = QtWidgets.QCheckBox()
        self.customcb = QtWidgets.QCheckBox()
        self.addButton = QtWidgets.QPushButton("+ADD")
        self.addButton.setObjectName("Add")
        self.TextBoxcustomfiles = QtWidgets.QLineEdit()
        # Publish section
        self.Labelpublishoption = QtWidgets.QLabel("Publish Option")
        self.Labelpublishoption.setObjectName("PublishOption")
        self.Labelpublishdetails = QtWidgets.QLabel("Publish Type")
        self.LabelDailies = QtWidgets.QLabel("Dailies")
        self.LabelReview = QtWidgets.QLabel("Review")
        self.LabelDelivery = QtWidgets.QLabel("Delivery")
        self.publishfrom = QtWidgets.QLabel("Publish From")
        self.LabelLocal = QtWidgets.QLabel("Local")
        self.LabelRemote = QtWidgets.QLabel("Remote")
        self.LabelVersion = QtWidgets.QLabel("Version:")
        self.LabelVersionNumber = QtWidgets.QLabel("V003")
        self.LabelCacheoption = QtWidgets.QLabel("Cache Export Option")
        self.LabelCacheoption.setObjectName("CacheExportOption")
        self.LabelDefalut = QtWidgets.QLabel("Default")
        self.LabelcustomCache = QtWidgets.QLabel("Custom")
        self.LabelFBX = QtWidgets.QLabel("FBX")
        self.LabelABC = QtWidgets.QLabel("ABC")
        self.LabelSTANDIN = QtWidgets.QLabel("STANDIN")
        self.LabelOBJ = QtWidgets.QLabel("OBJ")
        self.LabelUSD = QtWidgets.QLabel("USD")
        self.FBXcb = QtWidgets.QCheckBox()
        self.ABCcb = QtWidgets.QCheckBox()
        self.STANDINcb = QtWidgets.QCheckBox()
        self.OBJcb = QtWidgets.QCheckBox()
        self.USDcb = QtWidgets.QCheckBox()
        self.dailiesrd = QtWidgets.QRadioButton()
        self.Reviewrd = QtWidgets.QRadioButton()
        self.Deliveryrd = QtWidgets.QRadioButton()
        self.Localrd = QtWidgets.QRadioButton()
        self.remoterd = QtWidgets.QRadioButton()
        self.Defaultrd = QtWidgets.QRadioButton()
        self.Customrd = QtWidgets.QRadioButton()
        self.abccombobox = QtWidgets.QComboBox()
        self.fbxcombobox = QtWidgets.QComboBox()
        self.stadincombobox = QtWidgets.QComboBox()
        self.objcombobox = QtWidgets.QComboBox()
        self.usdcombobox = QtWidgets.QComboBox()
        # Notes section
        self.Labelpublishnotes = QtWidgets.QLabel("Publish Notes")
        self.LabelClinetnotes = QtWidgets.QLabel("Notes For Client")
        self.publishtextbox = QtWidgets.QLineEdit()
        self.clienttextbox = QtWidgets.QLineEdit()
        # Bottom Section
        self.LabelStatus = QtWidgets.QLabel("Status")
        self.statusBar = QtWidgets.QProgressBar()
        self.statusBar.setValue(24)
        self.cancelButton = QtWidgets.QPushButton("Cancel")
        self.cancelButton.setObjectName("Cancel")
        self.publishButton = QtWidgets.QPushButton("Publish")

    
    def createLayout(self):
        """Function for setup layout for the widgets
        """
        self.MainLayout = QtWidgets.QGridLayout()
        self.shotdetailgb = QtWidgets.QGroupBox()
        self.shotdetailsmainlayout = QtWidgets.QVBoxLayout()
        self.shotdetailgb.setLayout(self.shotdetailsmainlayout)
        self.shotdetailssublayout =  QtWidgets.QGridLayout()
        self.shotdetailssublayout.addWidget(self.LabelProject, 0, 0)
        self.shotdetailssublayout.addWidget(self.TextBoxProject, 1, 0)
        self.shotdetailssublayout.addWidget(self.LabelScope, 0, 1)
        self.shotdetailssublayout.addWidget(self.TextBoxScope, 1, 1)
        self.shotdetailssublayout.addWidget(self.LabelProject2, 0, 2)
        self.shotdetailssublayout.addWidget(self.TextBoxProject2, 1, 2)
        self.shotdetailssublayout.addWidget(self.LabelScope2, 0, 3)
        self.shotdetailssublayout.addWidget(self.TextBoxScope2, 1, 3)
        self.shotdetailsmainlayout.addWidget(self.LabelShotdetails)
        self.shotdetailsmainlayout.addLayout(self.shotdetailssublayout)
        #playblastdetails layout
        self.playblastgb = QtWidgets.QGroupBox()
        self.playblastgb.setFixedWidth(200)
        self.Playblastdetailsmainlayout = QtWidgets.QVBoxLayout()
        self.playblastgb.setLayout(self.Playblastdetailsmainlayout)
        self.palyblastsublayout =  QtWidgets.QFormLayout()
        self.palyblastsublayout.addRow(self.wireframecb, self.LabelWireframe)
        self.palyblastsublayout.addRow(self.shadedcb, self.LabelShaded)
        self.palyblastsublayout.addRow(self.conecb, self.LabelCone)
        self.palyblastsublayout.addRow(self.perspcb, self.LabelPersp)
        self.palyblastsublayout.addRow(self.customcb, self.LabelCustom)
        self.customfileFlayout =  QtWidgets.QHBoxLayout()
        self.customfileFlayout.addWidget(self.LabelCustomfiles)
        self.customfileFlayout.addWidget(self.addButton)
        self.Playblastdetailsmainlayout.addWidget(self.LabelPlayblastdetails)
        self.Playblastdetailsmainlayout.addLayout(self.palyblastsublayout)
        self.Playblastdetailsmainlayout.addLayout(self.customfileFlayout)
        self.Playblastdetailsmainlayout.addWidget(self.TextBoxcustomfiles)
        self.Playblastdetailsmainlayout.addStretch(1)
        # Publish option layout
        self.publishgb = QtWidgets.QGroupBox()
        self.publishMainLayout = QtWidgets.QGridLayout()
        self.publishgb.setLayout(self.publishMainLayout)
        self.publishTypeLayout = QtWidgets.QFormLayout()
        self.publishTypeLayout.addRow(self.dailiesrd, self.LabelDailies)
        self.publishTypeLayout.addRow(self.Reviewrd, self.LabelReview)
        self.publishTypeLayout.addRow(self.Deliveryrd, self.LabelDelivery)
        self.publishFromLayout = QtWidgets.QFormLayout()
        self.publishFromLayout.addRow(self.Localrd, self.LabelLocal)
        self.publishFromLayout.addRow(self.remoterd, self.LabelRemote)
        self.publishFromLayout.addRow(self.LabelVersion, self.LabelVersionNumber)
        self.cacheexportLayout = QtWidgets.QGridLayout()
        self.cacheexportLayout.addWidget(self.Defaultrd, 0, 0)
        self.cacheexportLayout.addWidget(self.LabelDefalut, 0, 1)
        self.cacheexportLayout.addWidget(self.Customrd, 1, 0)
        self.cacheexportLayout.addWidget(self.LabelcustomCache, 1, 1)
        self.cacheexportLayout.addWidget(self.ABCcb, 2, 0)
        self.cacheexportLayout.addWidget(self.LabelABC, 2, 1)
        self.cacheexportLayout.addWidget(self.abccombobox, 2, 2)
        self.cacheexportLayout.addWidget(self.FBXcb, 3, 0)
        self.cacheexportLayout.addWidget(self.LabelFBX, 3, 1)
        self.cacheexportLayout.addWidget(self.fbxcombobox, 3, 2)
        self.cacheexportLayout.addWidget(self.STANDINcb, 4, 0)
        self.cacheexportLayout.addWidget(self.LabelSTANDIN, 4, 1)
        self.cacheexportLayout.addWidget(self.stadincombobox, 4, 2)
        self.cacheexportLayout.addWidget(self.OBJcb, 5, 0)
        self.cacheexportLayout.addWidget(self.LabelOBJ, 5, 1)
        self.cacheexportLayout.addWidget(self.objcombobox, 5, 2)
        self.cacheexportLayout.addWidget(self.USDcb, 6, 0)
        self.cacheexportLayout.addWidget(self.LabelUSD, 6, 1)
        self.cacheexportLayout.addWidget(self.usdcombobox, 6, 2)
        
        self.publishMainLayout.addWidget(self.Labelpublishoption, 0, 0)
        self.publishMainLayout.addWidget(self.Labelpublishdetails, 1, 0)
        self.publishMainLayout.addLayout(self.publishTypeLayout, 2, 0)
        self.publishMainLayout.addWidget(self.publishfrom, 1, 1)
        self.publishMainLayout.addLayout(self.publishFromLayout, 2, 1)
        self.publishMainLayout.addWidget(self.LabelCacheoption, 3, 0)
        self.publishMainLayout.addLayout(self.cacheexportLayout, 4, 0)

        self.notegb = QtWidgets.QGroupBox()
        self.NotesLayout = QtWidgets.QGridLayout()
        self.notegb.setLayout(self.NotesLayout)
        self.NotesLayout.addWidget(self.Labelpublishnotes, 0, 0)
        self.NotesLayout.addWidget(self.LabelClinetnotes, 0, 1)
        self.NotesLayout.addWidget(self.publishtextbox, 1, 0)
        self.NotesLayout.addWidget(self.clienttextbox, 1, 1)

        self.bottomgb = QtWidgets.QGroupBox()
        self.bottomLayout = QtWidgets.QHBoxLayout()
        self.bottomgb.setLayout(self.bottomLayout)
        self.statusLayout = QtWidgets.QHBoxLayout()
        self.statusLayout.addWidget(self.LabelStatus)
        self.statusLayout.addWidget(self.statusBar)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.addWidget(self.cancelButton)
        self.buttonLayout.addWidget(self.publishButton)
        self.bottomLayout.addLayout(self.statusLayout)
        spacer = QtWidgets.QSpacerItem(100, 0, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        self.bottomLayout.addItem(spacer)
        self.bottomLayout.addLayout(self.buttonLayout)


        self.TextBoxcustomfiles.setStyleSheet("QLineEdit { height: 250px; }")
        self.publishtextbox.setStyleSheet("QLineEdit { height: 50px; }")
        self.clienttextbox.setStyleSheet("QLineEdit { height: 50px; }")

        # Main layout
        self.MainLayout.addWidget(self.shotdetailgb, 0, 0, 1, 2)
        self.MainLayout.addWidget(self.playblastgb, 1, 0, 2, 1)
        self.MainLayout.addWidget(self.publishgb, 1, 1)
        self.MainLayout.addWidget(self.notegb, 2, 1)
        self.MainLayout.addWidget(self.bottomgb, 3, 0, 1, 2)
        self.setLayout(self.MainLayout)


class MyMainWindow(QtWidgets.QMainWindow):
    """For creating Mainwindow for the ui
    """
    def __init__(self):
        """For initializing
        """
        super().__init__()
        my_widget = Ui()
        self.setCentralWidget(my_widget)
        self.setWindowTitle("Random UI")
        screen_geometry = QtWidgets.QDesktopWidget().availableGeometry()
        x = (screen_geometry.width() - my_widget.width()) // 2
        y = (screen_geometry.height() - my_widget.height()) // 2
        self.setGeometry(x, y, 500, 650)



app = QtWidgets.QApplication(sys.argv)
repo_dir = os.path.dirname(__file__).split("\\")
repo_dir.pop(-1)
repo_dir = "\\".join(repo_dir)
file_path = os.path.join(repo_dir, 'styles', 'stylesheet.qss')
print(file_path)
file = QtCore.QFile(file_path)  # Replace with the actual path to your stylesheet file pesent submission the folder
if file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
    stream = QtCore.QTextStream(file)
    stylesheet = stream.readAll()
    file.close()
    app.setStyleSheet(stylesheet)

# for direct use to avoid change the location  stylesheet is added in this file 
# app.setStyleSheet(stylesheet)

obj = MyMainWindow()
obj.show()
sys.exit(app.exec_())
