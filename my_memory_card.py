from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, 
QRadioButton, QPushButton, QLabel, QButtonGroup, QMessageBox)
from random import shuffle, randint

class Question:
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Что такое "Вопрос"', 'это вопрос', 'это андатра', 'это это', 'это окно'))
question_list.append(Question('Как правильно прогуливать уроки', 'Сказать что заболел', '2', 'молча', 'придти на урок'))

app = QApplication([])
mw = QWidget()
mw.setWindowTitle('Memory Card')

rbtn_1 = QRadioButton('Это вопрос')
rbtn_2 = QRadioButton('это андатра')
rbtn_3 = QRadioButton('это это')
rbtn_4 = QRadioButton('это окно')



RadioGroupBox = QButtonGroup()
RadioGroupBox.addButton(rbtn_1)
RadioGroupBox.addButton(rbtn_2)
RadioGroupBox.addButton(rbtn_3)
RadioGroupBox.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
self.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат текста')
lb_Result = QLabel('Правильно или неправильно')
lb_Corect = QLabel('Правильный ответ')

layout_res = QHBoxLayout()
layout_res.addWidget(lb_Result, aligment = (Qt.AligmenLeft | Qt.AligmenTop))
layout_res.addWidget(lb_Corect, aligment = Qt.AligmenHCenter)
layout_res = addLayout(lb_Result)
layout_res = addLayout(lb_Corect)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayot()
layout_line2 = QHBoxLayot()
layout_line3 = QHBoxLayot()

layout_line1 = addWidget(quest, aligment = (QT,AligmenHCenter | Qt.AligmenVCenter))
layout_line2 = addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QHBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_quest():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroupBox.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroupBox.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    quest.setText(question)
    show_quest()


def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        mw.score += 1
        print(f'Рейтинг: {mw.score/mw.total*100}%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print(f'Рейтинг: {mw.score/mw.total*100}%')

def next_question():
    mw.total += 1
    print(f'Статистика/n-Всего вопросов {mw.total}/n-Правильных ответов {mw.score}')
    if len(question_list) > 0:
        cur_question = randint(0, len(question_list)-1)
        q = question_list(cur_question)
        ask(q)
        question_list.pop(cur_question)
    else:
        victory_win = QMessageBox()
        victory_win.setText('Вы ответили на все вопросы правильно')
        victory_win.exec_()

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

mw.setLayout(layout_card)
btn_OK.clicked.connect(click_OK)
mw.total = 0
mw.score = 0
mw.resize(300, 0)
next_question()
mw.show()
app.exec_()