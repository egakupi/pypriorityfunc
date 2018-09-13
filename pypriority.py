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


sample1 = {
            "info": {
                "as": 19574,
                "as_org": "Corporation Service Company",
                "city": "Wilmington",
                "country": "United States",
                "iso": "US",
                "isp": "Corporation Service Company",
                "org": "Corporation Service Company"
            },
            "url": "http://degeuzen.nl/jeygtgv.exe",
        }

sample2 = {
            "info": {
                "as": 197068,
                "as_org": "HLL LLC",
                "city": "",
                "country": "Russia",
                "iso": "RU",
                "isp": "HLL LLC",
                "org": "HLL LLC"
            },
            "url": "https://download.geo.drweb.com/pub/drweb/windows/katana/1.0/drweb-1.0-katana.exe?download=MSXML3.DLL",
        }


def py_priority_func(src):
    priority = 50
    url = src.get("url").lower()
    if ".exe" or ".dll" or ".pdf" in url:
        if url.endswith(".exe") or url.endswith(".dll") or url.endswith(".pdf"):
            priority += 15
        else:
            priority += 5

    # TODO Хост содержит домен второго уровня "drweb" +50 к приоритету
    # TODO Поле "as" сожержит "666" +50 к приоритету
    # TODO Поле "iso" содержит "US" -10 к приоритету
    # TODO Поле "iso" содержит "RU" +10 к приоритету
    # TODO Поле "iso" содержит "CN", "TW" -30 к приоритету

    print(src.get("info"))
    print(src.get("url"))
    print("Priority: ", priority)
    return priority


py_priority_func(sample1)
py_priority_func(sample2)
