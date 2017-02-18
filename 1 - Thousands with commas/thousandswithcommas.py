def thousands_with_commas(i):
    # puts commas between groups of 3 digits
    # return "{:,}".format(i)
    j = i if i >= 0 else -i
    result = ""
    while j >= 1000:
        result = "," + str(j % 1000).zfill(3) + result
        j = j // 1000

    return ("" if i >= 0 else "-") + str(j) + result


if __name__ == '__main__':
    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'
    assert thousands_with_commas(0) == '0'
    assert thousands_with_commas(1000) == '1,000'
    assert thousands_with_commas(10001) == '10,001'
