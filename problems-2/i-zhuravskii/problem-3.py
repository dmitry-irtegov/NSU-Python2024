import os
import sys
import unittest
import tempfile


def list_files_sorted_by_size(directory):
    try:
        # Проверяем, существует ли директория
        if not os.path.exists(directory):
            print(f"The directory '{directory}' does not exist.")
            return

        # Проверяем, является ли путь директорией
        if not os.path.isdir(directory):
            print(f"The path '{directory}' is not a directory.")
            return

        # Проверяем права доступа к директории
        if not os.access(directory, os.R_OK):
            print(f"Cannot read the directory '{directory}' due to insufficient permissions.")
            return

        # Получаем список всех файлов в директории
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        # Создаем список кортежей (имя файла, размер файла)
        files_with_sizes = [(f, os.stat(os.path.join(directory, f)).st_size) for f in files]

        # Сортируем список сначала по размеру (в обратном порядке), а затем по имени файла
        files_with_sizes.sort(key=lambda x: (-x[1], x[0]))

        # Выводим отсортированный список файлов с их размерами
        for file, size in files_with_sizes:
            print(f"{file}: {size} bytes")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


class TestListFilesSortedBySize(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.test_dir.cleanup()

    def test_directory_not_exists(self):
        result = self._capture_output(lambda: list_files_sorted_by_size('non_existing_directory'))
        self.assertIn("The directory 'non_existing_directory' does not exist.", result)

    def test_not_a_directory(self):
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.close()
        try:
            result = self._capture_output(lambda: list_files_sorted_by_size(temp_file.name))
            self.assertIn(f"The path '{temp_file.name}' is not a directory.", result)
        finally:
            os.remove(temp_file.name)

    def test_permission_error(self):
        if os.name == 'nt':  # Windows
            print("Permission error test is skipped on Windows due to limitations in setting directory permissions.")
            return

        os.chmod(self.test_dir.name, 0o000)
        result = self._capture_output(lambda: list_files_sorted_by_size(self.test_dir.name))
        self.assertIn(f"Cannot read the directory '{self.test_dir.name}' due to insufficient permissions.", result)
        os.chmod(self.test_dir.name, 0o700)

    def test_list_files(self):
        file1_path = os.path.join(self.test_dir.name, 'file1.txt')
        file2_path = os.path.join(self.test_dir.name, 'file2.txt')
        with open(file1_path, 'w') as file1:
            file1.write('A' * 100)
        with open(file2_path, 'w') as file2:
            file2.write('B' * 50)

        result = self._capture_output(lambda: list_files_sorted_by_size(self.test_dir.name))
        self.assertIn("file1.txt: 100 bytes", result)
        self.assertIn("file2.txt: 50 bytes", result)

    def test_list_files_names(self):
        # Создаем несколько временных файлов
        file1_path = os.path.join(self.test_dir.name, 'file1.txt')
        file2_path = os.path.join(self.test_dir.name, 'file2.txt')
        with open(file1_path, 'w') as file1:
            file1.write('A' * 40)
        with open(file2_path, 'w') as file2:
            file2.write('B' * 50)

        result = self._capture_output(lambda: list_files_sorted_by_size(self.test_dir.name))
        self.assertIn("file2.txt: 50 bytes", result)
        self.assertIn("file1.txt: 40 bytes", result)

    def _capture_output(self, func):
        from io import StringIO
        import sys
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            func()
            return sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout


if __name__ == "__main__":
    if len(sys.argv) == 2:
        directory_path = sys.argv[1]
        list_files_sorted_by_size(directory_path)
    else:
        unittest.main(argv=[sys.argv[0]])
