import sys
import os
import re
import shutil
import pathlib
from typing import List
from pathlib import Path
from tkinter import filedialog
from PySide6 import QtWidgets, QtGui
from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox, QApplication, QMainWindow, QDialog

from des import Ui_MainWindow       # Подключаем интерфейс
from dialog_form import Ui_Dialog   # Подключаем интерфейс диалога


class Dialog(QDialog):
    # Класс запуска GUI Кастомного диалога
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Attention")


class MainWindow(QMainWindow):
    # Класс запуска основного GUI
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Sort Files by Folders (Beta 0.4)")

        self.ui_dialog = Dialog()       # Экземпляр окна кастомного диалога
        self.ui_dialog.setModal(True)   # Делаем окно модальным

        # Код выполняемый при запуске:
        self.path = None
        self.path_selection = None
        self.path_start_house = None
        self.folder_list = []
        self.file_list = []
        self.start_directory()      # Вызов домашней директории
        self.edit_folder_on_off()   # Функция настроек edit_folder_* (on/off)

        # Cигналы от GUI
        self.ui.action.triggered.connect(self.open_folder_dialog)   # Сигнал диалога выбора папки
        self.ui.action_2.triggered.connect(self.message_box_about)  # Сигнал всплывающего сообщения "About"
        self.ui.pushButton_2.clicked.connect(self.view_files)       # Сигнал обновить список файлов
        self.ui.pushButton.clicked.connect(self.files_sorting)      # Сигнал сортировки

        # Проверяем настройки checkbox_*
        self.ui.checkBox_image_2.clicked.connect(self.edit_folder_on_off)
        self.ui.checkBox_audio_2.clicked.connect(self.edit_folder_on_off)
        self.ui.checkBox_video_2.clicked.connect(self.edit_folder_on_off)
        self.ui.checkBox_document_2.clicked.connect(self.edit_folder_on_off)
        self.ui.checkBox_archive_2.clicked.connect(self.edit_folder_on_off)
        self.ui.checkBox_program_2.clicked.connect(self.edit_folder_on_off)
        self.ui.checkBox_torrent_2.clicked.connect(self.edit_folder_on_off)
        self.ui.checkBox_other_2.clicked.connect(self.edit_folder_on_off)

    def statusbar(self, status, show_time):
        # Вывод сообщений в статус бар:
        self.ui.statusBar.showMessage(f"  {str(status)}", int(show_time))

    @Slot()
    def edit_folder_on_off(self):
        # Функция настроек edit_folder_* (on/off)
        self.ui.edit_folder_image.setEnabled(self.ui.checkBox_image_2.isChecked())
        self.ui.edit_folder_audio.setEnabled(self.ui.checkBox_audio_2.isChecked())
        self.ui.edit_folder_video.setEnabled(self.ui.checkBox_video_2.isChecked())
        self.ui.edit_folder_document.setEnabled(self.ui.checkBox_document_2.isChecked())
        self.ui.edit_folder_archive.setEnabled(self.ui.checkBox_archive_2.isChecked())
        self.ui.edit_folder_program.setEnabled(self.ui.checkBox_program_2.isChecked())
        self.ui.edit_folder_torrent.setEnabled(self.ui.checkBox_torrent_2.isChecked())
        self.ui.edit_folder_other.setEnabled(self.ui.checkBox_other_2.isChecked())

    @Slot()
    def message_box_about(self):
        # Создание всплывающего сообщения
        msg = QMessageBox()

        # Установка иконки окна сообщения
        icon_path = str(Path('icon', 'about-128.ico'))
        msg.setWindowIcon(QIcon(icon_path))

        # Установка заголовка окна сообщения
        title = "About the Program"
        msg.setWindowTitle(title)

        # Установка текста сообщения
        program_name = "Sort Files by Folders"
        developer = "ParadigmX"
        idea_author = "C@med0z"
        version = "0.4"

        message_text = f"{program_name}\nVersion: {version}\n\nProgram developed by: {developer}\nIdea: {idea_author}"
        msg.setText(message_text)

        # Отображение сообщения в модальном режиме
        msg.exec()

    @Slot()
    def message_box_no_files(self, folder_name):
        # Создание всплывающего сообщения
        msg = QMessageBox()

        # Получение имени папки
        folder_path = Path(folder_name)
        folder_name = folder_path.name

        # Установка заголовка окна сообщения
        title = "Внимание!"
        msg.setWindowTitle(title)

        # Установка текста сообщения
        message_text = f"В корне папки {folder_name} нет файлов для сортировки!"
        msg.setText(message_text)

        # Отображение сообщения в модальном режиме
        msg.exec()

    def message_dialog_files_already(self, not_moved_list, folder_moved_list, text):
        # Вызов диалога 'файлы уже есть в папках!'
        self.ui_dialog.show()   # Открываем окно

        self.ui_dialog.ui.label.setText(f'{text[0]}')       # Текст №1
        self.ui_dialog.ui.label_2.setText(f'{text[1]}')     # Текст №2

        # Добавляем папки и файлы в список
        for folder_m_l, not_m_l in zip(folder_moved_list, not_moved_list):
            self.ui_dialog.ui.listWidget.addItem(f'[{folder_m_l}] - {not_m_l}')

    def start_directory(self):
        # Функция возвращает домашнюю директорию
        path_start_house = Path(pathlib.Path.home(), 'Downloads')
        if path_start_house:
            self.path_start_house = path_start_house
            self.view_files()
        else:
            self.statusbar('Что-то не так с домашней директорией!', 10000)

        return path_start_house  # Домашняя директория

    @Slot()
    def open_folder_dialog(self):
        # Функция вызывает диалог, возвращает выбранную директорию
        path_selection = filedialog.askdirectory()    # Диалог выбора папки
        if path_selection:
            self.path_selection = Path(path_selection)
            self.view_files()
        else:
            self.statusbar('Путь не выбран!', 5000)

        return path_selection                         # Выбранная директория

    @Slot()
    def view_files(self):
        # Функция создает список файлов и папок директории
        path_start_house = self.path_start_house
        path_selection = self.path_selection

        # Проверяем настройки radioButton_*
        radio_button_checked_1 = self.ui.radioButton_1.isChecked()
        radio_button_checked_2 = self.ui.radioButton_2.isChecked()

        path_start = path_start_house
        path_selection = path_selection
        if path_selection:
            path = path_selection
        else:
            path = path_start

        self.ui.lineEdit.setText(str(f' {path} '))

        folder_list = []
        file_list = []

        if radio_button_checked_1:
            # Поиск только в корне каталога:
            # Список папок и фалов:
            # Полный путь к каждому файлу и папке:
            full_path_to_files = map(lambda name_name: os.path.join(path, name_name), os.listdir(path))

            # Перебор имен папок и фалов, запись их в списки:
            for name_file in full_path_to_files:
                if os.path.isdir(name_file):
                    # Имена папок:
                    name_file = os.path.basename(name_file)
                    folder_list.append(name_file)

                if os.path.isfile(name_file):
                    # Имена файлов:
                    # name_file = os.path.basename(name_file)
                    file_list.append(name_file)

        elif radio_button_checked_2:
            # Поиск в папках и подпапках каталога:
            # Список папок и фалов только корня:
            root_files = map(lambda name_name: os.path.join(path, name_name), os.listdir(path))

            # Перебор папок корня:
            for root_name_file in root_files:
                if os.path.isdir(root_name_file):
                    folder_list.append(os.path.basename(root_name_file))  # Список имен папок

            # Перебор фалов в папках и подпапках, запись их путей и имен в список:
            for path_pa, dirs, files in os.walk(path):
                for name in files:
                    if os.path.isfile(os.path.join(path_pa, name)):
                        file_list.append(os.path.join(path_pa, name))  # Список файлов с полными путями

        # Вывод статистики:
        self.ui.label_item_full_num.setText(str(int(len(folder_list)) + int(len(file_list))))  # Элементов
        self.ui.label_item_folders_num.setText(str(len(folder_list)))
        self.ui.label_item_files_num.setText(str(len(file_list)))

        # Вывод полученных данных:
        self.path = path  # Путь текущего каталога
        self.folder_list = folder_list  # Имена папок
        self.file_list = file_list  # Имена файлов

        # Вызов наполнения listWidget:
        self.list_add_items()

    @Slot()
    def list_add_items(self):
        # Функция выводит список папок и файлов в listWidget
        folder_list = self.folder_list
        file_list = self.file_list
        path = self.path
        self.ui.listWidget.clear()

        def convert_bytes_to_unit(file_name):
            # Функция принимает путь к файлу.
            # Затем функция возвращает размер файла в соответствующих единицах (ГБ, МБ, КБ или Б)
            bytes_size = os.stat(file_name).st_size
            for unity in ['B', 'KB', 'MB', 'GB']:
                if bytes_size < 1024.0:
                    return f"{bytes_size:.2f} {unity}"
                bytes_size /= 1024.0
            return "0 B"  # По умолчанию, если размер файла равен 0

        # Вывод папок в лист:
        for items in folder_list:
            item = QtWidgets.QListWidgetItem()
            item.setIcon(QIcon(str(Path('icon', 'folder.png'))))
            item.setText(items)
            self.ui.listWidget.addItem(item)  # Папки

        # Вывод файлов в лист:
        for items in file_list:
            # Узнаем величину файлов:
            converted, unit = convert_bytes_to_unit(Path(path, items)).split()
            # Выводим все в лист:
            item = QtWidgets.QListWidgetItem()
            item.setIcon(QIcon(str(Path('icon', 'file.png'))))
            item.setText(items)
            item.setToolTip(str(f'{round(float(converted), 2)} {unit}'))
            self.ui.listWidget.addItem(item)  # Файлы

    @Slot()
    def files_sorting(self):
        # Функция сортирует файлы
        self.ui.listWidget.clear()  # Очистить текущий список в listWidget
        selected_file_list = self.file_list  # Имена файлов
        path = self.path

        # Проверяем настройки checkbox_*:
        checkbox_image = self.ui.checkBox_image_2.isChecked()
        checkbox_audio = self.ui.checkBox_audio_2.isChecked()
        checkbox_video = self.ui.checkBox_video_2.isChecked()
        checkbox_document = self.ui.checkBox_document_2.isChecked()
        checkbox_archive = self.ui.checkBox_archive_2.isChecked()
        checkbox_program = self.ui.checkBox_program_2.isChecked()
        checkbox_torrent = self.ui.checkBox_torrent_2.isChecked()
        checkbox_other = self.ui.checkBox_other_2.isChecked()

        # Проверяем настройки edit_folder_*:
        edit_folder_image = self.ui.edit_folder_image.text()
        edit_folder_audio = self.ui.edit_folder_audio.text()
        edit_folder_video = self.ui.edit_folder_video.text()
        edit_folder_document = self.ui.edit_folder_document.text()
        edit_folder_archive = self.ui.edit_folder_archive.text()
        edit_folder_program = self.ui.edit_folder_program.text()
        edit_folder_torrent = self.ui.edit_folder_torrent.text()
        edit_folder_other = self.ui.edit_folder_other.text()

        # Регулярные выражения форматов:
        image_reg = r'\.(?:jp(?:e?g|e|2)|gif|png|tiff?|bmp|ICO|heic|heif|webp|jxr|wdp|dng|cr2|arw)$'
        image_reg = re.compile(image_reg, re.IGNORECASE)

        audio_reg = r'\.(?:mp3|wav|og(?:g|a)|flac|midi?|rm|aac|wma|mka|ape|opus)$'
        audio_reg = re.compile(audio_reg, re.IGNORECASE)

        video_reg = r'\.(?:mpeg|ra?m|avi|mp(?:g|e|4)|mov|divx|asf|qt|wmv|m\dv|rv|vob|asx|ogm|ogv|webm|flv|mkv|f4v|m4v' \
                    r'|swf)$'
        video_reg = re.compile(video_reg, re.IGNORECASE)

        document_reg = r'\.(?:pdf|ppt|pptx|xlsx?|docx?|odf|odt|rtf|txt|nfo)$'
        document_reg = re.compile(document_reg, re.IGNORECASE)

        archive_reg = r'\.(?:z(?:ip|[0-9]{2,})|r(?:ar|[0-9]{2,})|jar|bz2|tgz|gz|tar|rpm|7z(?:ip)?|lzma|xz)$'
        archive_reg = re.compile(archive_reg, re.IGNORECASE)

        program_reg = r'\.(?:exe|msi|dmg|bin|xpi|iso)$'
        program_reg = re.compile(program_reg, re.IGNORECASE)

        torrent_reg = r'\.torrent$'
        torrent_reg = re.compile(torrent_reg, re.IGNORECASE)

        list_fil_item = []
        image_list, audio_list, video_list, document_list = [], [], [], []
        archive_list, program_list, torrent_list = [], [], []

        # Создаем чистый список файлов:
        for item_file in selected_file_list:  # Перебор списка всех файлов
            item_file = os.path.splitext(item_file)  # Разбиваем на имя и формат
            item_file = str(f'{item_file[0]}{item_file[1].lower()}')  # Приводим формат в нижний регистр
            list_fil_item.append(item_file)  # Записываем нормализованные имя и формат в лист

        # Сортируем файлы:
        for fil_item in list_fil_item:  # Перебор списка всех файлов
            fil_item = os.path.splitext(fil_item)  # Разбиваем на имя и формат ['name', 'format']

            # Фото:
            if re.match(image_reg, fil_item[1]) is not None:  # Сравниваем с регулярным выражением
                fil_item = str("".join(fil_item))  # Соединяем имя и формат 'name.format'
                image_list.append(fil_item)  # Наполняем список фото

            # Аудио:
            if re.match(audio_reg, fil_item[1]) is not None:  # Сравниваем с регулярным выражением
                fil_item = str("".join(fil_item))  # Соединяем имя и формат 'name.format'
                audio_list.append(fil_item)  # Наполняем список аудио

            # Видео:
            if re.match(video_reg, fil_item[1]) is not None:  # Сравниваем с регулярным выражением
                fil_item = str("".join(fil_item))  # Соединяем имя и формат 'name.format'
                video_list.append(fil_item)  # Наполняем список видео

            # Документы:
            if re.match(document_reg, fil_item[1]) is not None:  # Сравниваем с регулярным выражением
                fil_item = str("".join(fil_item))  # Соединяем имя и формат 'name.format'
                document_list.append(fil_item)  # Наполняем список документов

            # Архивы:
            if re.match(archive_reg, fil_item[1]) is not None:  # Сравниваем с регулярным выражением
                fil_item = str("".join(fil_item))  # Соединяем имя и формат 'name.format'
                archive_list.append(fil_item)  # Наполняем список архивов

            # Программы:
            if re.match(program_reg, fil_item[1]) is not None:  # Сравниваем с регулярным выражением
                fil_item = str("".join(fil_item))  # Соединяем имя и формат 'name.format'
                program_list.append(fil_item)  # Наполняем список программ

            # Торрент:
            if re.match(torrent_reg, fil_item[1]) is not None:  # Сравниваем с регулярным выражением
                fil_item = str("".join(fil_item))  # Соединяем имя и формат 'name.format'
                torrent_list.append(fil_item)  # Наполняем список торрентов

        def number_of_sorted_files():
            # Собираем все отсортированные списки в один список:
            full_list_sort = []
            for category_list in [image_list, audio_list, video_list, document_list, archive_list, program_list,
                                  torrent_list]:
                full_list_sort.extend(category_list)

            # Устанавливаем текст меток в пользовательском интерфейсе:
            sorted_count = len(full_list_sort)
            unsorted_count = len(list_fil_item) - sorted_count
            self.ui.label_item_sorted_num.setText(f"{sorted_count}")
            self.ui.label_item_other_num.setText(f"{unsorted_count}")

            # Обрабатываем случай, когда отсутствуют файлы в каждой из категорий:
            if sorted_count == 0:
                self.message_box_no_files(str(path))

        number_of_sorted_files()

        def get_other_files() -> List[str]:
            # Собираем все отсортированные списки в один список:
            sorted_file_lists = [
                image_list,
                audio_list,
                video_list,
                document_list,
                archive_list,
                program_list,
                torrent_list,
            ]
            all_sorted_files = set(sum(sorted_file_lists, []))

            # Получаем список всех файлов и вычитаем из него отсортированные файлы:
            all_files = get_all_files()
            other_files = [file for file in all_files if file not in all_sorted_files]

            return other_files

        def get_all_files() -> List[str]:
            all_files = []
            for file_item in list_fil_item:  # Перебор списка всех файлов
                all_files.append(file_item)  # Наполняем список файлов
            return all_files

        def save_files(selected_files_list, folder, name_new_folder):
            # Функция создает папку и копирует в нее файлы.

            not_moved_list = []
            folder_moved_list = []

            # Проверка наличия выбранных файлов и пути к папке
            if not selected_files_list:
                return not_moved_list, folder_moved_list
            if not folder:
                return not_moved_list, folder_moved_list

            # Проверка наличия папки назначения
            if not os.path.exists(os.path.join(folder, name_new_folder)):
                try:
                    os.mkdir(os.path.join(folder, name_new_folder))
                except OSError:
                    print(f"Не удалось создать папку {name_new_folder} в {folder}.")
                    return not_moved_list, folder_moved_list

            # Перемещение файлов в папку
            for file in selected_files_list:
                if not os.path.isfile(file):
                    not_moved_list.append(os.path.basename(file))
                    folder_moved_list.append(name_new_folder)
                    continue

                dest_path = os.path.join(folder, name_new_folder, os.path.basename(file))

                if os.path.isfile(dest_path):
                    not_moved_list.append(os.path.basename(file))
                    folder_moved_list.append(name_new_folder)
                    continue

                try:
                    shutil.move(file, dest_path)
                except (shutil.Error, OSError):
                    not_moved_list.append(os.path.basename(file))
                    folder_moved_list.append(name_new_folder)

            if not_moved_list:
                # Вызов функции
                text = [f'Файлы с таким именем уже есть в папках: ',
                        'Они не будут перемещены! ']
                self.message_dialog_files_already(not_moved_list, folder_moved_list, text)

        def function_launch_save_files():
            self.ui_dialog.ui.listWidget.clear()    # Стирает предыдущий список не перемещенных файлов

            # Проверяем checkbox и edit_folder_*, запускаем функцию save_files:
            if checkbox_image and not edit_folder_image:
                save_files(image_list, path, 'Images')
            elif checkbox_image and edit_folder_image:
                save_files(image_list, path, edit_folder_image)

            if checkbox_audio and not edit_folder_audio:
                save_files(audio_list, path, 'Audio')
            elif checkbox_audio and edit_folder_audio:
                save_files(audio_list, path, edit_folder_audio)

            if checkbox_video and not edit_folder_video:
                save_files(video_list, path, 'Video')
            elif checkbox_video and edit_folder_video:
                save_files(video_list, path, edit_folder_video)

            if checkbox_document and not edit_folder_document:
                save_files(document_list, path, 'Document')
            elif checkbox_document and edit_folder_document:
                save_files(document_list, path, edit_folder_document)

            if checkbox_archive and not edit_folder_archive:
                save_files(archive_list, path, 'Archive')
            elif checkbox_archive and edit_folder_archive:
                save_files(archive_list, path, edit_folder_archive)

            if checkbox_program and not edit_folder_program:
                save_files(program_list, path, 'Program')
            elif checkbox_program and edit_folder_program:
                save_files(program_list, path, edit_folder_program)

            if checkbox_torrent and not edit_folder_torrent:
                save_files(torrent_list, path, 'Torrent')
            elif checkbox_torrent and edit_folder_torrent:
                save_files(torrent_list, path, edit_folder_torrent)

            if checkbox_other and not edit_folder_other:
                other_list = get_other_files()
                save_files(other_list, path, 'Other')
            elif checkbox_other and edit_folder_other:
                other_list = get_other_files()
                save_files(other_list, path, edit_folder_other)

            self.statusbar('Done!', 3000)
            self.view_files()

        function_launch_save_files()    # Запуск функции проверки настроек и старта сортировки


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(str(Path('icon', 'sort.png'))))
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
