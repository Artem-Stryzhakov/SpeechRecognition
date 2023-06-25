from PyQt5.QtWidgets import QApplication, QPushButton
from index import chatGptAnswer

import sys

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QPushButton("Push me")
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()