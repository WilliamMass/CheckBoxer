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