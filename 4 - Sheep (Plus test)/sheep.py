def sheep(number):
    found = [False] * 10
    if number == 0:
        return "INSOMNIA"
    i=1
    while True:
        for digit in str(number*i):
            found[int(digit)]=True
        if all(found):
            return number*i
        i+=1
    

if __name__ == "__main__":
    assert sheep(0) == "INSOMNIA"
    assert sheep(1) == 10
    assert sheep(2) == 90
    assert sheep(11) == 110
    assert sheep(1692) == 5076

    with open("c-input.in",'r') as infile:
        for line in infile.readlines()[1:]:
            print("Case #{}: {}".format(int(line),sheep(int(line))))


