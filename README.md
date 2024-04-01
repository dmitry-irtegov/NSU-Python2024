# NSU-Python2024
For NSU Python course year 2024.

This project is for "Python programming" course in Novosibirsk State University, spring semester 2023. Students should sumbit task solutions as pull requests to this repository

Имя файла должно формироваться по принципу: Группа задач/имя пользователя/problem[1-9].py например problems-1/v-nikiforov/problem1.py .  Если решение состоит из нескольких файлов, например файла решеия и тестов, 
или входных данных, или данных для тестов, или внешних модулей, следует создать папку с именем problemX и разместить в ней или ее подпапках все необходимые файлы.  

Есди решение требует установки дополнительных пакетов через pip, необходимо положить в папку файл requirements.txt стандартного формата.  Папку для создания venv в пулл реквест включать не следует.

Пулл реквест не должен содержать посторонних файлов, в том числе файлов с настройками среды разработки или файлов других задач.

Программы, использующие аннотации типов, не должны использовать кавычки в аннотациях типов, например:
```def __add__(self, other: 'Vector') -> 'Vector':```

Программы, использующие аннотации типов, должны проходить проверку mypy --python-version=3.12

Это относится в том числе к пулл реквестам, отправленным до внесения этого уточнения в правила

Собственно сдача задач будет проходить в виде публичного code review, сданные задания будут мержиться в мастер.
