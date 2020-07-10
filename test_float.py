# -*- coding: utf-8 -*-
# Ce code teste si la variable désignée peut être convertie en float

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False