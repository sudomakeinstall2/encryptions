from utils import _

p = 65537
g = 3


def compute_X():
    return {
        'X': pow(g, _('x'), p)
    }


def compute_Y():
    return {
        'Y': pow(g, _('y'), p)
    }


def compute_k1():
    return {
        'K1': pow(_('Y'), _('x'), p)
    }


def compute_k2():
    return {
        'K2': pow(_('X'), _('y'), p)
    }
