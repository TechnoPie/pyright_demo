#a.py
class A:
    _datetime_reference: ClassVar[datetime] = datetime.now()

    def __init__(self):
        return None

if __name__ == "__main__":
    print(A._datetime_reference)
    b = B()
    b.initialize(datetime_now_callable=lambda: A._datetime_reference)

    while True:
        if msvcrt.kbhit():
            if msvcrt.getch().decode('utf-8').lower() == 'x':
                break
        A._datetime_reference += timedelta(hours=1)
        print(f'A.datetime_now={A._datetime_reference} --- b.datetime_now= {b.get_datetime_now()}')
        sleep(1)

    A._datetime_reference = datetime.now()
    print(A._datetime_reference)
