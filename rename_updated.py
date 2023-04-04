'''Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки'''

import os

dir_name_list = ['video', 'music', 'images', 'docs']
foto_expansion = ['jpg', 'jpeg', 'png']
music_expansion = ['mp3', 'wav']
docs_expansion = ['doc', 'txt', 'odt']
video_expansion = ['mp4', 'mov']


def dir_sort(name_list: list[str], images: list[str], music: list[str], video: list[str], docs: list[str]) -> None:
    file_list = [obj for obj in os.listdir() if os.path.isfile(obj)]
    dir_list = [obj for obj in os.listdir() if os.path.isdir(obj)]
    for i in name_list:
        if i not in dir_list:
            os.mkdir(i)

    for file_ in file_list:
        if file_.split('.')[1] in images:
            os.replace(file_, os.path.join(os.getcwd(), 'images', file_))
        elif file_.split('.')[1] in music:
            os.replace(file_, os.path.join(os.getcwd(), 'music', file_))
        elif file_.split('.')[1] in video:
            os.replace(file_, os.path.join(os.getcwd(), 'video', file_))
        elif file_.split('.')[1] in docs:
            os.replace(file_, os.path.join(os.getcwd(), 'docs', file_))


if __name__ == '__main__':
    dir_sort(dir_name_list, foto_expansion, music_expansion, video_expansion, docs_expansion)
