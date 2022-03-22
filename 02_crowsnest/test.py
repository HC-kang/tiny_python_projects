#!/usr/bin/env python3
""" test for crowsnest.py """

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'

def test_exist():
    """exist"""
    
    assert os.path.isfile(prg)
    
    
def test_usage():
    """usage"""
    
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')
        
def test_consonant():
    """brigantine -> a brigantine"""
    
    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)
        
def test_consonant_upper():
    """brigantine -> A Brigantine"""
    
    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('A', word.title())
        
def test_vowel():
    """octopus -> an octopus"""
    
    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)

def test_vowel_upper():
    """octopus -> An Octopus"""
    
    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('An', word.upper())
        
        
def test_consonant_article_title():
    """Brigantine -> A Brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('A', word.title())
    for word in consonant_words:
        out = getoutput(f'{prg} {word.lower()}')
        assert out.strip() == template.format('a', word.lower())


def test_vowel_article_title():
    """Octopus -> An Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('An', word.title())
    for word in vowel_words:
        out = getoutput(f'{prg} {word.lower()}')
        assert out.strip() == template.format('an', word.lower())


def test_which_side():
    """which side check """
    
    for flag in ['-s starboard', '--side frondside', '--side rearside']:
        out = getoutput(f'{prg} Octopus {flag}')
        assert out.strip() == template.format('An', 'Octopus').replace('larboard', flag.split()[1])


def test_startswith_check():
    """must start with char"""
    
    for flag in ['01ab', '*ad']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('cannot')        