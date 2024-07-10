class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    users_list = []
    def log_in(self):
        if self.nickname in User:
            return self

    def register(self, nickname, password, age):
        for user in self.users_list:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        self.users_list.append(User(nickname, hash(password), age))
        self.log_in(nickname, password)

    def log_out(self, ):
        pass

    def get_videos(self):
        pass

    def watch_video(self):
        pass


class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = hash(password)


class User:

    def __init__(self, nickname, password, age):
        self.age = age
        self.password = hash(password)
        self.nickname = nickname
    

    def __add__(self, other):
        self.videos += ur
        return self


if __name__ == "__main__":
    database = Database()
    while True:
        choiсe = int(input("Приветствуем! выберете действие: \n1 - регистрация \n2 - вход\n"))
        if choiсe == 1:
            user = User(input('Введите логин:'), password := input('Введите пароль:'),
                        password2 := input('Введите пароль еще раз:'), age = int(input('лет')))
            if password != password2:
                print('пароли не совпадают')
            database.add_user(user.nickname, hash(user.password))
            UrTube().register()

        if choiсe == 2:
            login = input("Введите логин: ")
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                    break
                else:
                    print('Неверный пароль!')
            else:
                print('Пользователь не найден!')


class Video:
    def __init__(self, title, duration, time_now, adult_mode=False):
        self.adult_mode = adult_mode
        self.time_now = time_now
        self.title = title
        self.duration = duration


ur = UrTube('users', 'videos', 'current_user')
v1 = Video('Лучший язык программирования 2024 года', 200, 0)
v2 = Video('Для чего девушкам парень программист?', 10, 44, adult_mode=True)
ur.add(v1, v2)
ur.register()