class Logger:
    ERROR = 0
    WARNING = 1
    INFO = 2
    DEBUG = 3
    TRACE = 4
    COLORS = {
        ERROR: "\033[31m",
        WARNING: "\033[33m",
        INFO: "\033[32m",
        DEBUG: "\033[37m",
        TRACE: "\033[35m"
    }
    ENDCOLOR = '\033[0m'

    def __init__(self, log_level, stdout=True, file=None):
        self.log_level = log_level
        self.stdout = stdout
        self.file = file

    def log(self, log_level, *args, **kwargs):
        if log_level <= self.log_level:
            message = ' '.join(map(str, args))
            formatted_message = f"[{self.get_level_name(log_level)}]  {message}"
            if self.stdout:
                color = self.COLORS.get(log_level, '')
                end_color = self.ENDCOLOR if color else ''
                print(f"{color}{formatted_message}{end_color}", **kwargs)
            if self.file:
                with open(self.file, 'a') as f:
                    f.write(formatted_message + '\n')

    def get_level_name(self, log_level):
        level_names = ["[E]", "[W]", "[I]", "[D]", "[T]"]
        return level_names[log_level]

    def set_log_level(self, log_level):
        if log_level in range(len(self.get_level_name(log_level))):
            self.log_level = log_level

    def e(self, *args, **kwargs):
        self.log(self.ERROR, *args, **kwargs)

    def w(self, *args, **kwargs):
        self.log(self.WARNING, *args, **kwargs)

    def i(self, *args, **kwargs):
        self.log(self.INFO, *args, **kwargs)

    def d(self, *args, **kwargs):
        self.log(self.DEBUG, *args, **kwargs)

    def t(self, *args, **kwargs):
        self.log(self.TRACE, *args, **kwargs)


if __name__ == "__main__":
    log = Logger(Logger.DEBUG, file='myapp.log')

    log.e("Это error сообщение:", 7, 8, 9, end='\n\n')
    log.w("Это warning сообщение:", 1, 2, 3)
    log.t("Это trace сообщение:", 4, 5, 6)
    log.set_log_level(Logger.DEBUG)

    log.d("Это debug сообщение:", 10, 11, 12)
    log.i("Это info сообщение:", 13, 14, 15)
    log.t("Это trace сообщение:", 16, 17, 18)
