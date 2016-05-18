# Level 2
# fifth exercise

import os


def mk_dir_with_files(directory, subdirectory, filename):
    if not os.path.isdir(directory):
        for i in range(1, 7):
            os.makedirs(os.path.join(directory, subdirectory + str(i)))

            for j in range(1, 7):

                file = filename + str(j) + '.py'
                with open(os.path.join(directory, subdirectory + str(i), file), 'a') as task_file:
                    task_file.write(" ")


# mk_dir_with_files('python', 'lesson', 'task')
mk_dir_with_files('/home/oksana/python_homeworks/python-for-qa', 'lesson', 'task')
