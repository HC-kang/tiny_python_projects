import os
import random
import re
import string
from subprocess import getoutput, getstatusoutput


prg = './abuse.py'


# --------------------------------------------------
def random_string():
    
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_exist():
    
    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match('usage', out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_adjective_str():
    
    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -a {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_adjective_num():
    
    n = random.choice(range(-10, 0))
    rv, out = getstatusoutput(f'{prg} -a {n}')
    # print(out)
    assert rv != 0
    assert re.search(f'--adjectives "{n}" must be > 0', out)


# --------------------------------------------------
def test_bad_number_str():
    
    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -n {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_number_int():
    
    bad = random.randint(-10, 0)
    rv, out = getstatusoutput(f'{prg} -n {bad}')
    assert rv != 0
    assert re.search(f'--number "{bad}" must be > 0', out)


# --------------------------------------------------
def test_bad_seed():
    
    bad = random_string()
    rv, out = getstatusoutput(f'{prg} -s {bad}')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_01():
    
    out = getoutput(f'{prg} -s 1 -n 1')
    assert out.strip() == 'You filthsome, cullionly fiend!'


# --------------------------------------------------
