# -*- coding: utf-8 -*-
from url_regex import find_urls


class TestUrl:
    def test_empty(self):
        assert len(tuple(find_urls(""))) == 0

    def test_known_scheme(self):
        u1 = "https://localhost/123"
        s1 = f"some {u1}"
        assert find_urls(s1) == [u1]
        u2 = "HTTP://Problem"
        s2 = f"GET {u2} ="
        assert find_urls(s2) == [u2]
        s3 = "https:/nsu.qqqqq"
        assert find_urls(s3) == []
        s4 = "htps://good.qqqqq"
        assert find_urls(s4) == []

    def test_www(self):
        u1 = "www.nsu.qqqqq/123"
        s1 = f"some {u1}"
        assert find_urls(s1) == [u1]
        u2 = "wWw.nsu.qqqqq"
        s2 = f"GET {u2} ="
        assert find_urls(s2) == [u2]
        u3 = "www.bad..ru"
        s3 = f"{u3}"
        assert find_urls(s3) == [u3]

    def test_multiple(self):
        u1_1 = "https://google.com"
        u1_2 = "http://yandex.com"
        s1 = f"print {u1_1},{u1_2}"
        assert find_urls(s1) == [u1_1, u1_2]

    def test_big_text(self):
        u1 = "https://5kas.sudrf.ru/modules.php"
        s1 = f"""Обжалование
01.10.2020 прокурор подал кассационную жалобу.
{u1}
    • Указывает, что суд, ссылаясь в приговоре на показания """
        assert find_urls(s1) == [u1]
        u2 = "https://www.oracle.com/corporate/conflict-in-ukraine/russia/"
        s2 = f"""Соответствующая информация была размещена на официальном сайте ORACLE в сети Интернет ({u2}). 
12 апреля 2022 г. Истец обратился к Ответчику с предложением"""
        assert find_urls(s2) == [u2]
        u3 = "https://oracle.com/contracts/documentation."
        s3 = (f"окументацию по использованию Продуктов пользователь получает с сайта {u3}"
              f" При попытке входа на указанную страницу российским пользователем выдается результат "
              f"«Page Not found» (страница не найдена). ")
        assert find_urls(s3) == [u3]
