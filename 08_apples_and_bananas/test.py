import re
import os
from subprocess import getstatusoutput, getoutput

prg = './apples.py'
fox = '../inputs/fox.txt'


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
def test_bad_vowel():
    
    rv, out = getstatusoutput(f'{prg} -v x foo')
    assert rv != 0
    assert re.match('usage', out, re.IGNORECASE)


# --------------------------------------------------
def test_command_line():
    
    rv, out = getstatusoutput(f'{prg} foo')
    assert rv == 0
    assert out.rstrip() == 'faa'


# --------------------------------------------------
def test_command_line_with_vowel():
    
    out = getoutput(f'{prg} -v i foo')
    assert out.rstrip() == 'fii'


# --------------------------------------------------
def test_command_line_with_vowel_preserve_case():
    
    out = getoutput(f'{prg} "APPLES AND BANANAS" --vowel i')
    assert out.rstrip() == 'IPPLIS IND BININIS'


# --------------------------------------------------
def test_file():
    
    out = getoutput(f'{prg} {fox}')
    assert out.rstrip() == 'Tha qaack brawn fax jamps avar tha lazy dag.'


# --------------------------------------------------
def test_file_with_vowel():
    
    out = getoutput(f'{prg} --vowel o {fox}')
    assert out.strip() == 'Tho qoock brown fox jomps ovor tho lozy dog.'


# --------------------------------------------------
def test_squeeze():
    
    out = getoutput(f'{prg} --squeeze {fox}')
    assert out.rstrip() == 'Tha qack brawn fax jamps avar tha lazy dag.'
