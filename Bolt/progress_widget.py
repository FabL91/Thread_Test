from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QProgressBar, QPushButton, QLabel, QSpinBox, QListView
)
from PyQt6.QtCore import QTimer

# Constant to control delay widgets visibility
SHOW_DELAY_CONTROLS = True

class ProgressWidget(QWidget):
    def __init__(self, delay):
        super().__init__()
        self.init_ui()
        self.delay = delay
        self.is_running = True  # New variable to track the progress status

    def init_ui(self):
        # Create main layout
        layout = QVBoxLayout(self)

        # Create progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        layout.addWidget(self.progress_bar)

        # Create a list view
        self.list_view = QListView()
        layout.addWidget(self.list_view)  # Add the list view to the main layout

        
        # Create delay control layout
        delay_layout = QHBoxLayout()
        self.delay_label = QLabel("Total Duration (ms):")
        self.delay_spinbox = QSpinBox()
        self.delay_spinbox.setRange(1, 10000)
        self.delay_spinbox.setValue(1000)
        layout.addWidget(self.delay_label)
        delay_layout.addWidget(self.delay_spinbox)
        layout.addLayout(delay_layout)

        # Set visibility based on constant
        self.delay_label.setVisible(SHOW_DELAY_CONTROLS)
        self.delay_spinbox.setVisible(SHOW_DELAY_CONTROLS)

        # Create start and stop buttons
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_progress)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_progress)
        layout.addWidget(self.stop_button)

        # Initialize variables
        self.current_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

    # Fonction pour calculer la moyenne d'une liste de nombres
    

    
    def additionner(self, a, b):
        """
        Adds two numbers and returns their sum.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b


    def start_progress(self):
        """
        Start the progress bar and disable the start button.

        This function sets the is_running attribute to True, disables the start button,
        enables the stop button, and disables the delay spin box. It also resets the current_value
        and progress bar value to 0. Additionally, it calculates the timer interval based on
        the desired total duration and ensures a minimum interval of 1ms. Finally, it starts the timer.

        Args:
            self (ProgressWidget): The instance of the ProgressWidget class.

        Returns:
            None
        """
        self.is_running = True
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.delay_spinbox.setEnabled(False)
        self.current_value = 0
        self.progress_bar.setValue(0)

        # Calculate timer interval for 100 steps
        total_duration = int(self.delay)  # Convert delay to integer
        interval = int(total_duration / 100)

        # Ensure minimum interval of 1ms
        interval = max(1, interval)

        self.timer.start(interval)

    def stop_progress(self):
        self.is_running = False
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.timer.stop()

    def update_progress(self):
        if self.is_running:
            self.current_value += 1
            self.progress_bar.setValue(self.current_value)

            if self.current_value >= 100:
                self.timer.stop()
                self.start_button.setEnabled(True)
                self.delay_spinbox.setEnabled(True)
                self.current_value = 0