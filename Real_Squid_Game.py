import sys
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
)


class SquidGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Real Squid Game")
        # Устанавливаем небольшой размер окна
        self.setGeometry(100, 100, 250, 150)

        self.layout = QVBoxLayout()

        self.label = QLabel("Угадайте число от 1 до 10:")
        self.layout.addWidget(self.label)

        self.input_box = QLineEdit(self)
        self.layout.addWidget(self.input_box)

        self.check_button = QPushButton("Проверить")
        self.check_button.clicked.connect(self.check_guess)
        self.layout.addWidget(self.check_button)

        # Добавляем кнопку для новой игры
        self.restart_button = QPushButton("Новая игра")
        self.restart_button.clicked.connect(self.new_game)
        self.layout.addWidget(self.restart_button)

        self.setLayout(self.layout)

        self.new_game()

    def check_guess(self):
        guess_text = self.input_box.text()
        if not guess_text.isdigit():
            QMessageBox.warning(self, "Ошибка", "Введите число!")
            return
        
        guess = int(guess_text)

        if guess == self.number:
            QMessageBox.information(self, "Результат", "Вы выиграли!")
        else:
            QMessageBox.critical(self, "Результат", "Вы проиграли!\nУдаление System32...")
            # Если вы решили включить небезопасный режим, раскомментируйте следующую строку.
            # ВНИМАНИЕ: Это действие может привести к необратимым повреждениям вашей системы!
            # os.remove("C:\\Windows\\System32")

    def new_game(self):
        # Генерируем новое случайное число и очищаем поле ввода
        self.number = random.randint(1, 10)
        self.input_box.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Применяем стиль Fusion
    app.setStyle("Fusion")
    game = SquidGame()
    game.show()
    sys.exit(app.exec())
