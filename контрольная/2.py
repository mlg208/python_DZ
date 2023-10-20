# Функция возвращает аббревиатуру от переданной строки
def get_abbr(phrase):
    abr = ''
    for word in phrase.split():
        abr += word[0].upper()
    return abr



def test_get_abbr():
    assert get_abbr('семь раз отмерь - один раз отрежь') == 'СРО-ОРО'
    assert get_abbr("don't repeat yourself") == 'DRY'
    assert get_abbr('') == ''

test_get_abbr()