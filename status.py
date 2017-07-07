import enum


class Status(enum.Enum):
    end = "終了"
    open = "予約可"
    close = "予約済"
