import random

from utils import _


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError('modular inverse does not exist')
    else:
        return x % m


def primes(n):
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))


big_primes = list(set(primes(5000)) - set(primes(1000)))


def generate_p_q():
    return {
        'p': random.choice(big_primes),
        'q': random.choice(big_primes)
    }


def compute_n():
    return {
        'n': _('p') * _('q')
    }


def calculate_d():
    e = _('e')
    p = _('p')
    q = _('q')
    phi_n = (p - 1) * (q - 1)
    try:
        return {
            'd': modinv(e, phi_n)
        }
    except ValueError as e:
        return {
            'error': str(e)
        }


def encrypt_rsa():
    return {
        'c': pow(_('m'), _('e'), _('n'))
    }


def decrypt_rsa():
    return {
        'decrypt': pow(_('c'), _('d'), _('n'))
    }
