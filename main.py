import subprocess
import sys

from final.runner_function import lru_cache_demo, fib_with_cache
from final.ticTacToe.game_runner import start_game
from task_runner import Runner

from simple_term_menu import TerminalMenu


def main_menu():
    try:
        works = Runner().works
        options = [work.title for work in works]
        options.append("Выход")
        work_index = menu_run(options)
        if work_index == len(options) - 1:
            raise KeyboardInterrupt
        if work_index >= 0:
            options = [task.title for task in works[work_index].tasks]
            task_index = menu_run(options)
            if task_index >= 0:
                task = works[work_index].tasks[task_index]
                print(task.title)
                task.task_run()
                print("----------------------------------")
                main_menu()
    except (KeyboardInterrupt, TypeError):
        subprocess.call("clear", shell=True)
        print("\nВсего наилучшего!\n")
        sys.exit(0)


def menu_run(options):
    return TerminalMenu(options).show()


def main():
    # if __debug__:
    #     start_game()
    # else:
    main_menu()


if __name__ == '__main__':
    main()
