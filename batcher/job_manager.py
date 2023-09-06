import sys
from PySide6.QtCore import Qt, QCoreApplication, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow
from job_manager_ui import Ui_MainWindow  # Import the generated UI class


class JobManager(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.jobs = []
        self.current_job_index = 0
        self.timer = QTimer()

        self.timer.timeout.connect(self.execute_next_job)
        self.pushButtonAddJob.clicked.connect(self.add_job)
        self.pushButtonStartExecution.clicked.connect(self.start_execution)

    def add_job(self):
        print("add job")
        code = self.textEditJobInput.toPlainText()
        self.jobs.append(code)
        self.textEditJobInput.clear()

    def start_execution(self):
        if not self.timer.isActive():
            self.execute_next_job()
            self.timer.start(0)

    def execute_next_job(self):
        if self.current_job_index < len(self.jobs):
            code = self.jobs[self.current_job_index]
            try:
                exec(code)
            except Exception as e:
                self.plainTextEditResults.appendPlainText(f"Error executing job: {e}")

            self.current_job_index += 1
        else:
            self.plainTextEditResults.appendPlainText("All jobs processed.")
            self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JobManager()
    window.show()
    sys.exit(app.exec_())
