
class Config:
    BASE_URL = 'https://b2c.passport.rt.ru/' #страница авторизации
    BASE_REG_URL = 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'

    VALID_EMAIL = "nastyaabashkina8@gmail.com"
    VALID_PHONE = "+79153780179"
    VALID_LOGIN = "nastas_666"
    VALID_PASSWORD = "123Anastas"
    CONFIRM_VALID_PASSWORD = "123Anastas"
    VALID_NAME = "Анастасия"
    VALID_SURNAME = "Абашкина"

    DEFAULT_REGION = "Москва г"
    VALID_REGION = "Московская обл"
    REQ_ELEMENTS_REG = "ИмяФамилияРегионE-mail или мобильный телефонПарольПодтверждение пароля"
    REQ_ELEMENTS_AUTH = ["Авторизация", "Телефон", "Почта", "Логин", "Лицевой счёт"]
    REQ_ELEMENTS_RESET = ["Телефон", "Почта", "Логин", "Лицевой счёт"]
    DEFAULT_LOGIN_TEXT = "Мобильный телефон"
    TAGLINE_TEXT = "Персональный помощник в цифровом мире Ростелекома"
    PLACEHOLDER_NAME = ["Мобильный телефон", "Электронная почта", "Логин", "Лицевой счёт", "Пароль"]
    ERROR_VALIDATION_PASSWORD = ["Длина пароля должна быть не менее 8 символов",
                                 "Пароль должен содержать хотя бы одну заглавную букву",
                                 "Пароль должен содержать хотя бы одну прописную букву",
                                 "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру",
                                 "Длина пароля должна быть не более 20 символов"]
    ERROR_VALIDATION_NAME = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    ERRORS_OF_FIELDS_TEXT = "Необходимо заполнить поле кириллицей. От 2 до 30 символов.Необходимо заполнить поле кириллицей. От 2 до 30 символов.Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ruДлина пароля должна быть не менее 8 символовДлина пароля должна быть не менее 8 символов"
    POP_UP_WINDOW_TEXT = ["Учётная запись уже существует", "Попробуйте войти в неё. Если вы забыли пароль — восстановите его.",
                          "Войти", " Восстановить пароль "]
    POP_UP_WINDOW_TITLE = "Учётная запись уже существует"