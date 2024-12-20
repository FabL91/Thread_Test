import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QListView, QLabel, QSpinBox, QHBoxLayout, QPushButton, QGroupBox, QLineEdit, QSlider
from PyQt6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

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
        main_layout = QVBoxLayout(self)

        # Create progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        main_layout.addWidget(self.progress_bar)

        # Create a list view
        self.list_view = QListView()
        main_layout.addWidget(self.list_view)  # Add the list view to the main layout

        # Create delay control layout
        delay_layout = QHBoxLayout()
        self.delay_label = QLabel("Total Duration (ms):")
        self.delay_spinbox = QSpinBox()
        self.delay_spinbox.setRange(1, 10000)
        self.delay_spinbox.setValue(1000)
        main_layout.addWidget(self.delay_label)
        delay_layout.addWidget(self.delay_spinbox)
        main_layout.addLayout(delay_layout)

        # Set visibility based on constant
        self.delay_label.setVisible(SHOW_DELAY_CONTROLS)
        self.delay_spinbox.setVisible(SHOW_DELAY_CONTROLS)

        # Create group boxes
        left_groupbox = QGroupBox("Control")
        right_groupbox = QGroupBox("Trace")

        # Create layouts for group boxes
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        # Create start and stop buttons
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_progress)
        left_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_progress)
        left_layout.addWidget(self.stop_button)

        # Create start trace button and QLineEdit
        self.start_trace_button = QPushButton("Start Trace")
        self.start_trace_button.clicked.connect(self.start_trace)
        right_layout.addWidget(self.start_trace_button)

        self.trace_input = QLineEdit()
        right_layout.addWidget(self.trace_input)

        # Create frequency slider
        self.freq_slider = QSlider(Qt.Orientation.Horizontal)
        self.freq_slider.setRange(1, 1000)
        self.freq_slider.setValue(10)  # Default frequency
        self.freq_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.freq_slider.setTickInterval(100)
        self.freq_slider.valueChanged.connect(self.update_frequency_label)
        right_layout.addWidget(self.freq_slider)

        # Create frequency label
        self.freq_label = QLabel(f"Frequency: {self.freq_slider.value()} Hz")
        right_layout.addWidget(self.freq_label)

        # Set layouts for group boxes
        left_groupbox.setLayout(left_layout)
        right_groupbox.setLayout(right_layout)

        # Create horizontal layout for group boxes
        groupbox_layout = QHBoxLayout()
        groupbox_layout.addWidget(left_groupbox)
        groupbox_layout.addWidget(right_groupbox)
        main_layout.addLayout(groupbox_layout)

        # Create matplotlib figure with constrained layout
        self.figure = Figure(constrained_layout=True)
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        # Add matplotlib toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)
        main_layout.addWidget(self.toolbar)

        self.setLayout(main_layout)

    def start_progress(self):
        # Implementation for starting progress
        pass

    def stop_progress(self):
        # Implementation for stopping progress
        pass

    def start_trace(self):
        # Get the frequency from the slider
        frequency = self.freq_slider.value()

        # Generate a sine wave with the selected frequency
        t = np.linspace(0, 1, 1000)
        y = np.sin(2 * np.pi * frequency * t)

        # Compute the Fourier Transform of the sine wave
        yf = np.fft.fft(y)
        xf = np.fft.fftfreq(len(t), t[1] - t[0])

        # Clear the previous plot
        self.figure.clear()

        # Create subplots
        ax1, ax2 = self.figure.subplots(2, 1)

        # Plot the sine wave
        ax1.plot(t, y)
        ax1.set_title("Signal")
        ax1.set_xlabel("temps(s)")
        ax1.set_ylabel("intensité")

        # Plot the Fourier Transform
        ax2.plot(xf, np.abs(yf))
        ax2.set_title("Transformée de Fourier")
        ax2.set_xlabel("Fréquence (Hz)")
        ax2.set_ylabel("Amplitude")

        # Refresh the canvas
        self.canvas.draw()

    def update_frequency_label(self):
        # Update the frequency label with the current slider value
        self.freq_label.setText(f"Frequency: {self.freq_slider.value()} Hz")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ProgressWidget(1000)
    widget.show()
    sys.exit(app.exec())