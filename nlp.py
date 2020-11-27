import MeCab
import re
import pandas as pd
import numpy as np

def pos_mecab(sentence) :
    """

    :param sentence:
    :return:
    """
    m = MeCab.Tagger()

    # 저	NP,*,F,저,Inflect,NP,NP,제/NP/*
    out = m.parse(sentence)

    sentences = out.split('\n')
    p = re.compile('(.*)\t(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)')
    sentences = [p.findall(s) for s in sentences]

    tags = []
    for s in sentences :
        if len(s) > 0 and len(s[0]) > 0 :
            s = s[0]
            tags.append((s[0], s[1]))
    return tags