import tldextract

"""
Требуется написать функцию, которая принимает на вход определенную структуру данных,
содержащую URL, информацию об этом URL и вычисляет приоритет для этой структуры

Правила для вычисления приоритета:
 - Стандартный приоритет равен 50
 - Если параметры ссылки содержат ".exe", ".dll" или если ".pdf", то следует добавить 5 к приоритету или
   если URL-путь оканчивается на".exe", ".dll" или ".pdf" то добавить 15 к приоритету. Если выполняются оба условия,
   то добавлять только 15 к приоритету.
 - Хост содержит домен второго уровня "drweb" +50 к приоритету
 - Поле "as" сожержит "666" +50 к приоритету
 - Поле "iso" содержит "US" -10 к приоритету
 - Поле "iso" содержит "RU" +10 к приоритету
 - Поле "iso" содержит "CN", "TW" -30 к приоритету
"""


def py_priority_func(src):
    priority = 50

    info = src.get("info")
    if info.get("as") == 666:
        priority += 50
    if info.get("iso") == "US":
        priority -= 10
    if info.get("iso") == "RU":
        priority += 10
    if ("CN" or "TW") == info.get("iso"):
        priority -= 30

    url = src.get("url").lower()
    if (".exe" or ".dll" or ".pdf") in url:
        if url.endswith(".exe") or url.endswith(".dll") or url.endswith(".pdf"):
            priority += 15
        else:
            priority += 5
    if tldextract.extract(url).domain == 'drweb':
        priority += 50

    return priority
