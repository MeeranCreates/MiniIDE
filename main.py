from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
)


app = QApplication([])

# =========================
# Main Window
# =========================

window = QMainWindow()
window.setWindowTitle("MiniIDE")
window.setFixedSize(1280, 720)


# =========================
# Central Container
# =========================

container = QWidget()
root_layout = QVBoxLayout(container)


# =========================
# Main Area
# =========================

main_layout = QHBoxLayout()

# Project Explorer
explorer = QTextEdit()
explorer.setPlaceholderText("Project Explorer")

# Code Editor
editor = QTextEdit()
editor.setPlaceholderText("Code Editor")

main_layout.addWidget(explorer)
main_layout.addWidget(editor)


# =========================
# Output
# =========================

output = QTextEdit()
output.setPlaceholderText("Output")


# =========================
# Build Layout
# =========================

root_layout.addLayout(main_layout)
root_layout.addWidget(output)

window.setCentralWidget(container)


# =========================
# Show
# =========================

window.show()

app.exec()