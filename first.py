import re
from datetime import datetime


class Patient:
    def __init__(
        self,
        passport: str,
        name: str,
        birth_date: str,
        phone: str,
        temperature: float
    ):
        self.passport: str = passport
        self.name: str = name
        self.birth_date: str = birth_date
        self.phone: str = phone
        self.temperature: float = temperature


class Date:
    def __init__(
        self,
        dd: int,
        mm: int,
        yyyy: int
    ):
        self.dd: int = dd
        self.mm: int = mm
        self.yyyy: int = yyyy


def input_passport():
    while True:
        passport = input("Введите паспорт в формате XX XX-XXXXXX: ")

        if re.fullmatch(r"\d{2} \d{2}-\d{6}", passport):
            return passport

        print("Ошибка. Паспорт должен иметь формат XX XX-XXXXXX.")
        print("Пример: 12 34-567890")


def input_name():
    while True:
        name = input("Введите ФИО пациента: ").strip()

        if name:
            return name

        print("Ошибка. Имя не может быть пустым.")


def input_birth_date():
    while True:
        date_string = input("Введите дату рождения в формате YYYY-MM-DD: ")

        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_string):
            print("Ошибка. Дата должна иметь формат YYYY-MM-DD.")
            continue

        try:
            date = datetime.strptime(date_string, "%Y-%m-%d")

            if date.date() > datetime.now().date():
                print("Ошибка. Дата рождения не может быть в будущем.")
                continue

            return Date(
                date.day,
                date.month,
                date.year
            )

        except ValueError:
            print("Ошибка. Такой даты не существует.")


def input_phone():
    while True:
        phone = input(
            "Введите телефон "
            "(+X(XXX) XXX-XX-XX или X(XXX) XXX-XXXX): "
        )

        pattern = r"(\+\d|\d)\(\d{3}\) \d{3}-\d{2}-\d{2,4}"

        if re.fullmatch(pattern, phone):
            return phone

        print("Ошибка. Неверный формат телефона.")
        print("Пример: +7(999) 123-45-67")
        print("Или: 7(999) 123-4567")


def input_temperature():
    while True:
        temperature_string = input(
            "Введите температуру в формате XX.XX: "
        )

        if not re.fullmatch(r"\d{2}\.\d{2}", temperature_string):
            print("Ошибка. Температура должна иметь формат XX.XX.")
            continue

        temperature = float(temperature_string)

        return temperature


def print_patient(patient):
    print("\nДанные пациента:")
    print(f"Паспорт: {patient.passport}")
    print(f"ФИО: {patient.name}")

    print(
        f"Дата рождения: "
        f"{patient.birth_date.yyyy:04d}-"
        f"{patient.birth_date.mm:02d}-"
        f"{patient.birth_date.dd:02d}"
    )

    print(f"Телефон: {patient.phone}")
    print(f"Температура: {patient.temperature:.2f}")


def main():
    print("=== Ввод данных пациента ===\n")

    passport = input_passport()
    name = input_name()
    birth_date = input_birth_date()
    phone = input_phone()
    temperature = input_temperature()

    patient = Patient(
        passport,
        name,
        birth_date,
        phone,
        temperature
    )

    print_patient(patient)


if __name__ == "__main__":
    main()
