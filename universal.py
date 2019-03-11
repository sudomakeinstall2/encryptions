from rsa import modinv
from utils import _

p = 65537
g = 3


def compute_A():
    return {'A': pow(g, _('a'), p)}


def compute_xywz():
    return {
        'X': pow(_('A'), _('r'), p) * _('m') % p,
        'Y': pow(g, _('r'), p),
        'W': pow(_('A'), _('s'), p),
        'Z': pow(g, _('s'), p),
    }


def decrypt():
    return {
        'dec': _('X') * modinv(pow(_('Y'), _('a'), p), p) % p,
        'check': _('W') * modinv(pow(_('Z'), _('a'), p), p) % p,
    }


def re_encrypt():
    return {
        'XX': _('X') * pow(_('W'), _('rr'), p) % p,
        'YY': _('Y') * pow(_('Z'), _('rr'), p) % p,
        'WW':  pow(_('W'), _('ss'), p),
        'ZZ': pow(_('Z'), _('ss'), p)
    }


def re_decrypt():
    return {
        're_dec': _('XX') * modinv(pow(_('YY'), _('a'), p), p) % p,
        're_check': _('WW') * modinv(pow(_('ZZ'), _('a'), p), p) % p,
    }
