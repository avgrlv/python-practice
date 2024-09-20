# python-practice

Для запуска необходимо установить пакет:

`` 
pip install simple-term-menu
``

После чего запускать из **терминала** скриптом:

``
python main.py
``

Для отладки в режиме DEBUG необходимо править main, так как simple-term-menu не работает в терминале PyCharm

````
def main():
    if __debug__:
        task_14()       <--- указывая и импортируя нужную задачу
    else:
        main_menu()
````
