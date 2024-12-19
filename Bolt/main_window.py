from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from progress_widget import ProgressWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Bar Demo")
        self.setGeometry(100, 100, 400, 200)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create progress widget
        progress_widget = ProgressWidget(5000)
        layout.addWidget(progress_widget)