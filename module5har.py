import time


class User:
    def __init__(self, nickname, password, age):
        self.password = password
        self.nickname = nickname
        self.age = age

    def __str__(self):
        return f"User(name={self.nickname}, Password={self.password}), age={self.age})"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.adult_mode = adult_mode
        self.title = title
        self.duration = duration
        self.time_now = 0


class UrTube:
    def __init__(self):
        self.user_list = []
        self.video_list = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.user_list:
            if nickname == user.nickname:
                print(f'Пользователь с {nickname} уже существует')
                return

        self.user_list.append(User(nickname, hash(password), age))

    def log_in(self, nickname, password):
        if self.current_user is None:
            for user in self.user_list:
                if user.nickname == nickname and user.password == hash(password):
                    print('Вы вошли в систему')
            print('Неверный логин или пароль')
        else:
            print('Вы уже вошли в систему')

    def log_out(self):
        if self.current_user is None:
            print('Вы вышли из системы')
            return
        self.current_user = None

    def add(self, *video_list):
        for video in video_list:
            if video.title not in [v.title for v in self.video_list]:
                self.video_list.append(video)
            else:
                print(f'Видео {video.title} уже существует')

    def get_video_list(self, search_word):
        result = []
        for video in self.video_list:
            if search_word.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт')
            return
        for video in self.video_list:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет восемьнадцати лет')
                    return
            print('Воспроизведение: ', end=' ')
            for second in range(video.duration):
                print(second, end=' ')
                time.sleep(1)
            print('Конец видео.')
            return
        print('Видео не найдено')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_video_list('лучший'))
print(ur.get_video_list('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
