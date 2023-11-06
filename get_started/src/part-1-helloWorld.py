import datetime


def helloWorld() -> None:
    """
    Hello World function that prints "Hello World" and displays the number of days until 2024
    """

    now = datetime.datetime.now()
    difference = datetime.datetime(2024, 1, 1) - now

    print(f"Hello world ! Number of days to 2024 : {difference}")
