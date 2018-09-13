import unittest
import pypriority


class TestPyPriorityFunc(unittest.TestCase):

    def test_1(self):
        sample = {
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

        self.assertEqual(55, pypriority.py_priority_func(sample))

    def test_2(self):
        sample = {
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

        self.assertEqual(125, pypriority.py_priority_func(sample))


if __name__ == '__main__':
    unittest.main()
