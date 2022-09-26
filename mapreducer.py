""" from functools import reduce
from mrjob.job import MRJob
from mrjob.step import MRStep
import scrapy
from scrapy.selector import Selector
import pandas as pd
import os
import csv

class ContadorDePokemons(MRJob):

  file = open('saida.txt')
  linha = file.readlines()

  def steps(self):
    return [
        MRStep(mapper=self.mapper,
                reducer=self.reducer),
        MRStep(reducer=self.mapper_pokemon)
    ]

  def mapper(self, _, linha):
    palavras = linha.lower().split()
    for palavra in palavras:    
      yield palavra, 1

  def reducer(self, chave, valores):
      yield chave, sum(valores)

  def mapper_pokemon(self, chave, valor):
    if chave == "Green":
      yield chave, valor 


if __name__ == '__main__':
  ContadorDePokemons.run() """