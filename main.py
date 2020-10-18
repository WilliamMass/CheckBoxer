import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBoxer")
        self.setGeometry(50, 50, 500, 1000)  #  Probably this should be set to more reasonable params for height in px
        self.setWindowIcon(QIcon('box_favicon_blue.png'))  #  If you release this, replace this icon.

        '''
        Replicate the next four lines for each menu item (eg File -> Exit)
        '''
        file_menu_exit = QAction("&Exit", self)
        file_menu_exit.setShortcut("Ctrl+Q")
        file_menu_exit.setStatusTip("Leave The App")
        file_menu_exit.triggered.connect(self.exit_application)

        open_editor = QAction("&Text Editor", self)
        open_editor.setShortcut("Ctrl+E")
        open_editor.setStatusTip("Open Editor")
        open_editor.triggered.connect(self.editor)

        open_file = QAction("&Open File", self)
        open_file.setShortcut("Ctrl-O")
        open_file.setStatusTip("Open")
        open_file.triggered.connect(self.file_open)

        save_file = QAction("&Save File", self)
        save_file.setShortcut("Ctrl-S")
        save_file.setStatusTip("Save")
        save_file.triggered.connect(self.file_save)
        '''
        Placeholder items for menus
        '''
        edit_menu_placeholder = QAction("&Placeholder", self)
        edit_menu_placeholder.setShortcut("Ctrl+Alt+Del")
        edit_menu_placeholder.setStatusTip("Not Yet Implemented")
        edit_menu_placeholder.triggered.connect(self.placeholder)

        help_menu_placeholder = QAction("&Placeholder", self)
        help_menu_placeholder.setShortcut("Ctrl+Alt+Del")
        help_menu_placeholder.setStatusTip("Not Yet Implemented")
        help_menu_placeholder.triggered.connect(self.placeholder)

        self.statusBar()
        mainMenu = self.menuBar()

        '''
        Replicate the next two lines for each menu heading
        '''
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(open_file)
        fileMenu.addAction(save_file)
        fileMenu.addSeparator()
        fileMenu.addAction(file_menu_exit)

        editMenu = mainMenu.addMenu("&Edit")
        editMenu.addAction(open_editor)
        editMenu.addSeparator()  # Adds a separator line to an individual menu between line items
        editMenu.addAction(edit_menu_placeholder)

        helpMenu = mainMenu.addMenu("&Help")
        helpMenu.addAction(help_menu_placeholder)
        self.home()

    '''
    TODO - Need to make the buttons (and each of the list items) resize themselves to the width of the window,
    and 50px high. This might be something that we have to use CSS for?
    '''
    def home(self):  #  Specific to this page
        delete_btn = QPushButton("Delete all checked items", self)
        delete_btn.clicked.connect(self.delete_items)
        delete_btn.resize(500, 50)
        delete_btn.move(0, 950)
        delete_btn.setFont(QFont('Helvetica', 12)) #  Apply some styling, heh

        '''
        # This stuff is all to build a toolbar, but we don't really want that for this program -
        # unless we go all toolbar, no menubar?
        extractAction = QAction(QIcon('box_favicon_blue.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.exit_application)
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        # This is a demonstration of the FontChoice Widget - we can move it out of this toolbar and
        # into the menu bar
        fontChoice = QAction("Font", self)
        fontChoice.triggered.connect(self.font_choice)
        # self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

        # This is a demonstration of the ColorPicker Widget - we can move it out of the toolbar and
        # into the menu bar, or simply have it select from a few different options and load an appropriate
        # style sheet - that would constrain the options but we wouldn't need to include this.
        color = QColor(0, 0, 0)
        fontColor = QAction('Font Background Color', self)
        fontColor.triggered.connect(self.color_picker)

        self.toolBar.addAction(fontColor)
        '''

        # This is a demonstration of a single checkbox - we're going to create ours much in the same
        # fashion, but we're going to instantiate it as an item in a list.
        checkBox = QCheckBox('Checkbox Item Test', self)
        checkBox.resize(500, 30)
        checkBox.setFont(QFont('Helvetica', 12))
        checkBox.move(0, 30)
        checkBox.stateChanged.connect(self.state_checked)

        '''
        # This stuff is to build a progress bar, which we don't really want for this program - it can
        # be completely removed at the end of the tutorial.
        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        self.btn = QPushButton("Download", self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        
        # This stuff is to build a dropdown menu (and to introduce some basic styles) - which we don't
        # necessarily want for this program.
        self.styleChoice = QLabel("Windows", self)
        combo_box = QComboBox(self)
        combo_box.addItem("motif")
        combo_box.addItem("Windows")
        combo_box.addItem("cde")
        combo_box.addItem("Plastique")
        combo_box.addItem("Cleanlooks")
        combo_box.addItem("windowsvista")

        combo_box.move(0, 250)
        self.styleChoice.move(50, 150)
        combo_box.activated[str].connect(self.style_choice)
        '''
        '''
        # This is a calendar widget, which we do want to be able to instantiate, so that we can
        # use it to automatically reset things at a particular date or time, or pop up reminders.
        # Obviously we don't need it for the reminder pushes, we need it so people can schedule their
        # own stuff.
        calendar = QCalendarWidget(self)
        calendar.move(50, 500)
        calendar.resize(400, 400)
        '''

    '''
    TODO - Make the delete items method do something (like, say, iterate through all the items in the current
    tab and then remove them if they're checked.
    '''
    def delete_items(self):
        choice = QMessageBox.question(self, "Delete Items?",
                                      "Are you sure you want to delete all checked items? This action can't be undone.",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Deleting all checked items")
        else:
            pass

    # This is for the color picker - it can be removed or left in as we desire - this one only changes
    # the background color, we would have to do a different stylesheet for foreground color.
    def color_picker(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())

    # setCentralWidget takes over the entire application, which is really pretty much perfect for
    # what we're looking for? Although we should look at how the tabs were built when we built a web
    # browser
    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

    '''
    In PyQT5, we need to open the file as a tuple, so (file_name, _) is required; this does crash
    '''
    def file_open(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if file_name:
            file = open(file_name, 'r')

            self.editor()
            with file:
                text = file.read()
                self.textEdit.setText(text)
                file.close()
        else:
            print('No file loaded')

    def file_save(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File')
        if file_name:
            file = open(file_name, 'w')
            text = self.textEdit.toPlainText()  # this is just for our text editor -> converts anything from QT to plain text
            file.write(text)
            file.close()

        else:
            print('Operation cancelled without saving')

    # This is for the progress bar stuff above, it's totally extraneous to this project and can
    # be completely removed.
    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
    
    # This is to choose styles in a dropdown menu, it's totally extraneous to this project, and
    # can be completely removed.
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    # This is for font choice - we can leave this in - if we do, move it to the edit menu.
    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def exit_application(self):
        sys.exit(app.exec_())

    def state_checked(self, state):  # we might need to return state out of this, we'll see
        if state == Qt.Checked:
            pass
        else:
            pass
        print("We're using checkboxes to indicate if something is done - we don't actually do much "
              "with that information other than make sure that it stays in that state (until such a"
              "time as it is either reset, or else deleted")

    def reset_daily_items(self):
        print("Not yet implemented - this will reset all the items with the property 'daily'"
              "we can do it manually through the file menu, or we can set a timer to do it at"
              "a particular time each day")

    def reset_weekly_items(self):
        print("Not yet implemented - this will reset all the items with the property 'weekly'"
              "we can do it manually through the file menu, or we can set a timer to do it at"
              "a particular time each week")

    def placeholder(self):
        print("This is a placeholder function for all unimplemented menu functions")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
