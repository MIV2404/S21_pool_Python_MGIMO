# Используй модуль datetime для работы с датами и календарём
from datetime import date

def validation_year(inp_year) -> bool:
    valid = inp_year.isdigit() and 0 < int(inp_year) < 10000
    return valid

# простая для понимания версия
def how_unlucky(year:int) -> int:
  if validation_year(year):
    count, year = 0, int(year)
    for month in range(1, 13):
        day = date(year, month, 13)
        if day.weekday() == 4:
            count += 1
    return count
  return "Год введен некорректно. \nРабота программы завершена."

#сложная для понимания версия
# def how_unlucky(year):
#     if validation_year(year):
#         count = sum((1) for month in range(1, 13) if (date(int(year), month, 13)).weekday() == 4)
#         return count
#     return "Год введен некорректно. \nРабота программы завершена."

year = input()
print(how_unlucky(year))
