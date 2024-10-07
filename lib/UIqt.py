from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from time import sleep
import os, debug, sys
from exec import pseudo_class

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
# Snip...
_mlist={
        'nav bar' : "_UI_NAV_BAR_",
        'ListView': "_CTRL_LV_AD_",
        'TreeView': "_CTRL_TV_AD_",
        'Button'  : "_OBJ_BUTTON_",
        'Stat bar': "_UI_STA_BAR_",
    }
_clist={
    '_UI_NAV_BAR_': '_UI_NAV_BAR_',
    '_CTRL_LV_AD_': '_CTRL_LV_AD_',
    '_CTRL_TV_AD_': '_CTRL_TV_AD_',
    '_OBJ_BUTTON_': '_OBJ_BUTTON_',
    '_UI_STA_BAR_': '_UI_STA_BAR_',
}



# Step 1: Create a worker class
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        """Long-running task."""
        for i in range(5):
            sleep(1)
            self.progress.emit(i + 1)
        self.finished.emit()


module_list=[
    '_SYS_FILE_CTRL_',   #:_SYS_FILE_CTRL_,
    '_SYS_FOLDER_'   ,   #:_SYS_FOLDER_   ,
    '_SYS_ROOT_DIR_' ,   #:_SYS_ROOT_DIR_ ,
    '_LNK_FAV_DIR_'  ,   #:_LNK_FAV_DIR_  ,
    '_SYS_RECYCLE_'  ,   #:_SYS_RECYCLE_  ,
    '_SYS_W_DRIVE_'      #:_SYS_W_DRIVE_
    ]


class Window(QMainWindow):
    frames=[]
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicksCount = 0
        self.frames=[]
    def setupUi(self):
        self.setWindowTitle("Freezing GUI")
        self.resize(300, 150)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        # Create and connect widgets
        self.clicksLabel = QLabel("Counting: 0 clicks", self)
        self.clicksLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.stepLabel = QLabel("Long-Running Step: 0")
        self.stepLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.countBtn = QPushButton("Click me!", self)
        self.countBtn.clicked.connect(self.countClicks)
        self.longRunningBtn = QPushButton("Long-Running Task!", self)
        self.longRunningBtn.clicked.connect(self.runLongTask)
        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.clicksLabel)
        layout.addWidget(self.countBtn)
        layout.addStretch()
        layout.addWidget(self.stepLabel)
        layout.addWidget(self.longRunningBtn)
        self.centralWidget.setLayout(layout)
    def countClicks(self):
        self.clicksCount += 1
        self.clicksLabel.setText(f"Counting: {self.clicksCount} clicks")
    def reportProgress(self, n):
        self.stepLabel.setText(f"Long-Running Step: {n}")
    def runLongTask(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.longRunningBtn.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.longRunningBtn.setEnabled(True)
        )
        self.thread.finished.connect(
            lambda: self.stepLabel.setText("Long-Running Step: 0")
        )
    def add_frame(self,name,frame):
        if not name or not frame:
            print("can't add in list")
            return
        self.frames[name] =frame
        return frame
    def show(self):
        self.window.mainloop()
        #self.tr.start()
    def GUI_Thread(self):
        self.window.mainloop()

class _UI_NAV_BAR_: pass
class _CTRL_LV_AD_: pass
class _CTRL_TV_AD_: pass
class _OBJ_BUTTON_: pass
class _UI_STA_BAR_: pass
class Window_2:
    def __init__(self) -> None:
        self.frame=pseudo_class()

if __name__ == "__main__":
    gui=Window()
    gui.add_frame('nav bar' , _UI_NAV_BAR_())
    gui.add_frame('ListView', _CTRL_LV_AD_())
    gui.add_frame('TreeView', _CTRL_TV_AD_())
    gui.add_frame('Button'  , _OBJ_BUTTON_())
    gui.add_frame('Stat bar', _UI_STA_BAR_())


app = QApplication(sys.argv)
win1 = Window()
win2 = Window()
win1.show()
win2.show()
sys.exit(app.exec())
