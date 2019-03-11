from rsa import modinv
from utils import _

p = 65537
g = 3


def compute_y():
    return {'y': pow(g, _('x'), p)}


def compute_c1():
    return {'c1': pow(g, _('r'), p)}


def compute_c2():
    return {'c2': _('m') * pow(_('y'), _('r'), p)}


def decrypt():
    return {
        'dec': _('c2') * modinv(pow(_('c1'), _('x'), p), p) % p
    }


def compute_z1():
    return {
        'z1': _('c1') * pow(g, _('c'), p) % p
    }


def compute_z2():
    return {
        'z2': _('c2') * pow(_('y'), _('c'), p) % p
    }


def re_decrypt():
    return {
        're_dec': int(_('z2') * modinv(pow(_('z1'), _('x'), p), p) % p)
    }
