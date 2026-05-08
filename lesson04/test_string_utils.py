import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# @pytest.mark.positive_capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),                # обычная строка
    ("hello Vika", "Hello Vika"),        # строка с пробелом, второе слово с заглавной буквы
    ("питон хороший", "Питон хороший"),  # строка с пробелом, второе слово с маленькой буквы
    ("Skypro", "Skypro"),                # строка уже начинается с заглавной буквы
    ("SKYPRO", "Skypro")                 # все буквы заглавные
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# @pytest.mark.negative_capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),   # строка с цифрами
    ("", ""),               # пустая строка
    ("   ", "   ")          # строка с пробелом
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# @pytest.mark.positive_trim
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),      # обычный случай с пробелами в начале
    ("skypro", "skypro"),         # без пробелов
    ("     ", ""),                # только пробелы
    ("  sky pro  ", "sky pro  "), # пробелы только в начале, остальные остаются
    ("", ""),                      # пустая строка
    ("\tskypro", "\tskypro"),      # табуляция в начале — не удаляется
    ("\nskypro", "\nskypro"),      # перенос строки в начале — не удаляется
    ("   привет", "привет")       # кириллица с пробелами
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

# @pytest.mark.negative_trim
@pytest.mark.parametrize("input_value", [
        None,                # метод startswith не существует у None
        123,                 # число, не строка
        ["list"],            # список
        True,                # булевое значение
        object()             # объект, не являющийся строкой
])

def test_trim_negative(input_value):
    with pytest.raises(AttributeError):
        string_utils.trim(input_value)

# @pytest.mark.positive_conttains
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),       # символ есть в начале
    ("SkyPro", "y", True),       # символ есть внутри
    ("SkyPro", "o", True),       # символ есть внутри, в конце
    ("SkyPro", "U", False),      # символа нет
    ("", "a", False),            # пустая строка
    ("привет", "и", True),       # кириллица
    ("hello", "", True)         # поиск пустого символа — Python считает True
])

def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# @pytest.mark.negative_contains
@pytest.mark.parametrize("string, symbol", [
    ("hello", None),    # symbol не строка
    ("hello", 1),       # symbol число
    ("hello", ["h"])   # symbol список
])

def test_contains_negative(string, symbol):
    with pytest.raises(TypeError):
        string_utils.contains(string, symbol)

#@pytest.mark.positive_delete
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),        # удалить одну букву
    ("SkyPro", "Pro", "Sky"),        # удалить подстроку
    ("aaaaa", "a", ""),               # удалить все буквы
    ("hello world", "l", "heo word"), # удалить несколько вхождений
    ("hello", "x", "hello"),          # символа нет — строка не меняется
    ("привет", "и", "првет"),         # кириллица
    ("", "a", ""),                     # пустая строка
    ("hello", "", "hello"),           # пустая подстрока — ничего не удаляется
])

def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

#@pytest.mark.negative_delete
@pytest.mark.parametrize("string, symbol", [
    (None, "a"),        # string не строка
    (123, "1"),         # string число
    ({"key": "val"}, "k") # string словарь
])

def test_delete_symbol_negative(string, symbol):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(string, symbol)
