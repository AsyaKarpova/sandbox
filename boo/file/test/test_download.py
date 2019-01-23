from pathlib import Path

from boo.file.download import curl
from boo.settings import url


def test_url():
    assert url(2012) == 'http://www.gks.ru/opendata/storage/7708234640-bdboo2012/data-20181029t000000-structure-20121231t000000.csv'


def test_url_on_string():
    assert url("sample")


def test_curl():
    curl(url(2012), 'dat.dat', 200)
    p = Path('dat.dat')
    assert p.stat().st_size == 200 * 1024
    p.unlink()
