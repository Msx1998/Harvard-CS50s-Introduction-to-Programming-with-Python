from um import count

def test():
    assert count("yummy") == 0
    assert count("Hi um David") == 1
    assert count("um, thanks.") == 1
    assert count("um?") == 1
    assert count("Um, no thanks, um...") == 2



