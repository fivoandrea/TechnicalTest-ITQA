# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eRKGaT144j5SYVM7wmw0CA04u2oZVxCu
"""

text = 'Indonesia RAYA'

def vocal_search(text):
  vocal_voc = ['a','i','u','e','o']
  text = text.lower()
  for i in text:
    if i in vocal_voc:
      print(i,end='')

vocal_search(text)