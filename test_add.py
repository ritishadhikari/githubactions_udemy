from add import add

def test_add():
    assert add(a=2,b=3)==5
    assert add(a=1,b=1)==2
    assert add(a=0,b=0)==0