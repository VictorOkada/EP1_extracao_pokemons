from functools import reduce
from mrjob.job import MRJob
from mrjob.step import MRStep
import scrapy
from scrapy.selector import Selector
import pandas as pd
import os
import csv

urls = []
url_pokedex = []
cor = ""

 
def corrigir_ordem(index, nome):

  if nome=="Bulbasaur": index = 1
  elif nome=="Ivysaur": index = 2
  elif nome=="Venusaur": index = 3
  elif nome=="Venusaur": index = 3
  elif nome=="Charmander": index = 4
  elif nome=="Charmeleon": index = 5
  elif nome=="Charizard": index = 6
  elif nome=="Charizard": index = 6
  elif nome=="Charizard": index = 6
  elif nome=="Squirtle": index = 7
  elif nome=="Wartortle": index = 8
  elif nome=="Blastoise": index = 9
  elif nome=="Blastoise": index = 9
  elif nome=="Caterpie": index = 10
  elif nome=="Metapod": index = 11
  elif nome=="Butterfree": index = 12
  elif nome=="Weedle": index = 13
  elif nome=="Kakuna": index = 14
  elif nome=="Beedrill": index = 15
  elif nome=="Beedrill": index = 15
  elif nome=="Pidgey": index = 16
  elif nome=="Pidgeotto": index = 17
  elif nome=="Pidgeot": index = 18
  elif nome=="Pidgeot": index = 18
  elif nome=="Rattata": index = 19
  elif nome=="Rattata": index = 19
  elif nome=="Raticate": index = 20
  elif nome=="Raticate": index = 20
  elif nome=="Spearow": index = 21
  elif nome=="Fearow": index = 22
  elif nome=="Ekans": index = 23
  elif nome=="Arbok": index = 24
  elif nome=="Pikachu": index = 25
  elif nome=="Pikachu": index = 25
  elif nome=="Raichu": index = 26
  elif nome=="Raichu": index = 26
  elif nome=="Sandshrew": index = 27
  elif nome=="Sandshrew": index = 27
  elif nome=="Sandslash": index = 28
  elif nome=="Sandslash": index = 28
  elif nome=="Nidoranâ™€": index = 29
  elif nome=="Nidorina": index = 30
  elif nome=="Nidoqueen": index = 31
  elif nome=="Nidoranâ™‚": index = 32
  elif nome=="Nidorino": index = 33
  elif nome=="Nidoking": index = 34
  elif nome=="Clefairy": index = 35
  elif nome=="Clefable": index = 36
  elif nome=="Vulpix": index = 37
  elif nome=="Vulpix": index = 37
  elif nome=="Ninetales": index = 38
  elif nome=="Ninetales": index = 38
  elif nome=="Jigglypuff": index = 39
  elif nome=="Wigglytuff": index = 40
  elif nome=="Zubat": index = 41
  elif nome=="Golbat": index = 42
  elif nome=="Oddish": index = 43
  elif nome=="Gloom": index = 44
  elif nome=="Vileplume": index = 45
  elif nome=="Paras": index = 46
  elif nome=="Parasect": index = 47
  elif nome=="Venonat": index = 48
  elif nome=="Venomoth": index = 49
  elif nome=="Diglett": index = 50
  elif nome=="Diglett": index = 50
  elif nome=="Dugtrio": index = 51
  elif nome=="Dugtrio": index = 51
  elif nome=="Meowth": index = 52
  elif nome=="Meowth": index = 52
  elif nome=="Meowth": index = 52
  elif nome=="Persian": index = 53
  elif nome=="Persian": index = 53
  elif nome=="Psyduck": index = 54
  elif nome=="Golduck": index = 55
  elif nome=="Mankey": index = 56
  elif nome=="Primeape": index = 57
  elif nome=="Growlithe": index = 58
  elif nome=="Growlithe": index = 58
  elif nome=="Arcanine": index = 59
  elif nome=="Arcanine": index = 59
  elif nome=="Poliwag": index = 60
  elif nome=="Poliwhirl": index = 61
  elif nome=="Poliwrath": index = 62
  elif nome=="Abra": index = 63
  elif nome=="Kadabra": index = 64
  elif nome=="Alakazam": index = 65
  elif nome=="Alakazam": index = 65
  elif nome=="Machop": index = 66
  elif nome=="Machoke": index = 67
  elif nome=="Machamp": index = 68
  elif nome=="Bellsprout": index = 69
  elif nome=="Weepinbell": index = 70
  elif nome=="Victreebel": index = 71
  elif nome=="Tentacool": index = 72
  elif nome=="Tentacruel": index = 73
  elif nome=="Geodude": index = 74
  elif nome=="Geodude": index = 74
  elif nome=="Graveler": index = 75
  elif nome=="Graveler": index = 75
  elif nome=="Golem": index = 76
  elif nome=="Golem": index = 76
  elif nome=="Ponyta": index = 77
  elif nome=="Ponyta": index = 77
  elif nome=="Rapidash": index = 78
  elif nome=="Rapidash": index = 78
  elif nome=="Slowpoke": index = 79
  elif nome=="Slowpoke": index = 79
  elif nome=="Slowbro": index = 80
  elif nome=="Slowbro": index = 80
  elif nome=="Slowbro": index = 80
  elif nome=="Magnemite": index = 81
  elif nome=="Magneton": index = 82
  elif nome=="Farfetch'd": index = 83
  elif nome=="Farfetch'd": index = 83
  elif nome=="Doduo": index = 84
  elif nome=="Dodrio": index = 85
  elif nome=="Seel": index = 86
  elif nome=="Dewgong": index = 87
  elif nome=="Grimer": index = 88
  elif nome=="Grimer": index = 88
  elif nome=="Muk": index = 89
  elif nome=="Muk": index = 89
  elif nome=="Shellder": index = 90
  elif nome=="Cloyster": index = 91
  elif nome=="Gastly": index = 92
  elif nome=="Haunter": index = 93
  elif nome=="Gengar": index = 94
  elif nome=="Gengar": index = 94
  elif nome=="Onix": index = 95
  elif nome=="Drowzee": index = 96
  elif nome=="Hypno": index = 97
  elif nome=="Krabby": index = 98
  elif nome=="Kingler": index = 99
  elif nome=="Voltorb": index = 100
  elif nome=="Voltorb": index = 100
  elif nome=="Electrode": index = 101
  elif nome=="Electrode": index = 101
  elif nome=="Exeggcute": index = 102
  elif nome=="Exeggutor": index = 103
  elif nome=="Exeggutor": index = 103
  elif nome=="Cubone": index = 104
  elif nome=="Marowak": index = 105
  elif nome=="Marowak": index = 105
  elif nome=="Hitmonlee": index = 106
  elif nome=="Hitmonchan": index = 107
  elif nome=="Lickitung": index = 108
  elif nome=="Koffing": index = 109
  elif nome=="Weezing": index = 110
  elif nome=="Weezing": index = 110
  elif nome=="Rhyhorn": index = 111
  elif nome=="Rhydon": index = 112
  elif nome=="Chansey": index = 113
  elif nome=="Tangela": index = 114
  elif nome=="Kangaskhan": index = 115
  elif nome=="Kangaskhan": index = 115
  elif nome=="Horsea": index = 116
  elif nome=="Seadra": index = 117
  elif nome=="Goldeen": index = 118
  elif nome=="Seaking": index = 119
  elif nome=="Staryu": index = 120
  elif nome=="Starmie": index = 121
  elif nome=="Mr. Mime": index = 122
  elif nome=="Mr. Mime": index = 122
  elif nome=="Scyther": index = 123
  elif nome=="Jynx": index = 124
  elif nome=="Electabuzz": index = 125
  elif nome=="Magmar": index = 126
  elif nome=="Pinsir": index = 127
  elif nome=="Pinsir": index = 127
  elif nome=="Tauros": index = 128
  elif nome=="Magikarp": index = 129
  elif nome=="Gyarados": index = 130
  elif nome=="Gyarados": index = 130
  elif nome=="Lapras": index = 131
  elif nome=="Ditto": index = 132
  elif nome=="Eevee": index = 133
  elif nome=="Eevee": index = 133
  elif nome=="Vaporeon": index = 134
  elif nome=="Jolteon": index = 135
  elif nome=="Flareon": index = 136
  elif nome=="Porygon": index = 137
  elif nome=="Omanyte": index = 138
  elif nome=="Omastar": index = 139
  elif nome=="Kabuto": index = 140
  elif nome=="Kabutops": index = 141
  elif nome=="Aerodactyl": index = 142
  elif nome=="Aerodactyl": index = 142
  elif nome=="Snorlax": index = 143
  elif nome=="Articuno": index = 144
  elif nome=="Articuno": index = 144
  elif nome=="Zapdos": index = 145
  elif nome=="Zapdos": index = 145
  elif nome=="Moltres": index = 146
  elif nome=="Moltres": index = 146
  elif nome=="Dratini": index = 147
  elif nome=="Dragonair": index = 148
  elif nome=="Dragonite": index = 149
  elif nome=="Mewtwo": index = 150
  elif nome=="Mewtwo": index = 150
  elif nome=="Mewtwo": index = 150
  elif nome=="Mew": index = 151

  return index

def corrigir_pokedex(id_pokemon):

  if id_pokemon == '001': cor = 'Green'
  elif id_pokemon == '002': cor = 'Green'
  elif id_pokemon == '003': cor = 'Green'
  elif id_pokemon == '004': cor = 'Red'
  elif id_pokemon == '005': cor = 'Red'
  elif id_pokemon == '006': cor = 'Red'
  elif id_pokemon == '007': cor = 'Blue'
  elif id_pokemon == '008': cor = 'Blue'
  elif id_pokemon == '009': cor = 'Blue'
  elif id_pokemon == '010': cor = 'Green'
  elif id_pokemon == '011': cor = 'Green'
  elif id_pokemon == '012': cor = 'White'
  elif id_pokemon == '013': cor = 'Brown'
  elif id_pokemon == '014': cor = 'Yellow'
  elif id_pokemon == '015': cor = 'Yellow'
  elif id_pokemon == '016': cor = 'Brown'
  elif id_pokemon == '017': cor = 'Brown'
  elif id_pokemon == '018': cor = 'Brown'
  elif id_pokemon == '019': cor = 'Purple'
  elif id_pokemon == '020': cor = 'Brown'
  elif id_pokemon == '021': cor = 'Brown'
  elif id_pokemon == '022': cor = 'Brown'
  elif id_pokemon == '023': cor = 'Purple'
  elif id_pokemon == '024': cor = 'Purple'
  elif id_pokemon == '025': cor = 'Yellow'
  elif id_pokemon == '026': cor = 'Yellow'
  elif id_pokemon == '027': cor = 'Yellow'
  elif id_pokemon == '028': cor = 'Yellow'
  elif id_pokemon == '030': cor = 'Blue'
  elif id_pokemon == '031': cor = 'Blue'
  elif id_pokemon == '033': cor = 'Purple'
  elif id_pokemon == '034': cor = 'Purple'
  elif id_pokemon == '035': cor = 'Pink'
  elif id_pokemon == '036': cor = 'Pink'
  elif id_pokemon == '037': cor = 'Brown'
  elif id_pokemon == '038': cor = 'Yellow'
  elif id_pokemon == '039': cor = 'Pink'
  elif id_pokemon == '040': cor = 'Pink'
  elif id_pokemon == '041': cor = 'Purple'
  elif id_pokemon == '042': cor = 'Purple'
  elif id_pokemon == '043': cor = 'Blue'
  elif id_pokemon == '044': cor = 'Blue'
  elif id_pokemon == '045': cor = 'Red'
  elif id_pokemon == '046': cor = 'Red'
  elif id_pokemon == '047': cor = 'Red'
  elif id_pokemon == '048': cor = 'Purple'
  elif id_pokemon == '049': cor = 'Purple'
  elif id_pokemon == '050': cor = 'Brown'
  elif id_pokemon == '051': cor = 'Brown'
  elif id_pokemon == '052': cor = 'Yellow'
  elif id_pokemon == '053': cor = 'Yellow'
  elif id_pokemon == '054': cor = 'Yellow'
  elif id_pokemon == '055': cor = 'Blue'
  elif id_pokemon == '056': cor = 'Brown'
  elif id_pokemon == '057': cor = 'Brown'
  elif id_pokemon == '058': cor = 'Brown'
  elif id_pokemon == '059': cor = 'Brown'
  elif id_pokemon == '060': cor = 'Blue'
  elif id_pokemon == '061': cor = 'Blue'
  elif id_pokemon == '062': cor = 'Blue'
  elif id_pokemon == '063': cor = 'Brown'
  elif id_pokemon == '064': cor = 'Brown'
  elif id_pokemon == '065': cor = 'Brown'
  elif id_pokemon == '066': cor = 'Gray'
  elif id_pokemon == '067': cor = 'Gray'
  elif id_pokemon == '068': cor = 'Gray'
  elif id_pokemon == '069': cor = 'Green'
  elif id_pokemon == '070': cor = 'Green'
  elif id_pokemon == '071': cor = 'Green'
  elif id_pokemon == '072': cor = 'Blue'
  elif id_pokemon == '073': cor = 'Blue'
  elif id_pokemon == '074': cor = 'Brown'
  elif id_pokemon == '075': cor = 'Brown'
  elif id_pokemon == '076': cor = 'Brown'
  elif id_pokemon == '077': cor = 'Yellow'
  elif id_pokemon == '078': cor = 'Yellow'
  elif id_pokemon == '079': cor = 'Pink'
  elif id_pokemon == '080': cor = 'Pink'
  elif id_pokemon == '081': cor = 'Gray'
  elif id_pokemon == '082': cor = 'Gray'
  elif id_pokemon == '084': cor = 'Brown'
  elif id_pokemon == '085': cor = 'Brown'
  elif id_pokemon == '086': cor = 'White'
  elif id_pokemon == '087': cor = 'White'
  elif id_pokemon == '088': cor = 'Purple'
  elif id_pokemon == '089': cor = 'Purple'
  elif id_pokemon == '090': cor = 'Purple'
  elif id_pokemon == '091': cor = 'Purple'
  elif id_pokemon == '092': cor = 'Purple'
  elif id_pokemon == '093': cor = 'Purple'
  elif id_pokemon == '094': cor = 'Purple'
  elif id_pokemon == '095': cor = 'Gray'
  elif id_pokemon == '096': cor = 'Yellow'
  elif id_pokemon == '097': cor = 'Yellow'
  elif id_pokemon == '098': cor = 'Red'
  elif id_pokemon == '099': cor = 'Red'
  elif id_pokemon == '100': cor = 'Red'
  elif id_pokemon == '101': cor = 'Red'
  elif id_pokemon == '102': cor = 'Pink'
  elif id_pokemon == '103': cor = 'Yellow'
  elif id_pokemon == '104': cor = 'Brown'
  elif id_pokemon == '105': cor = 'Brown'
  elif id_pokemon == '106': cor = 'Brown'
  elif id_pokemon == '107': cor = 'Brown'
  elif id_pokemon == '108': cor = 'Pink'
  elif id_pokemon == '109': cor = 'Purple'
  elif id_pokemon == '110': cor = 'Purple'
  elif id_pokemon == '111': cor = 'Gray'
  elif id_pokemon == '112': cor = 'Gray'
  elif id_pokemon == '113': cor = 'Pink'
  elif id_pokemon == '114': cor = 'Blue'
  elif id_pokemon == '115': cor = 'Brown'
  elif id_pokemon == '116': cor = 'Blue'
  elif id_pokemon == '117': cor = 'Blue'
  elif id_pokemon == '118': cor = 'Red'
  elif id_pokemon == '119': cor = 'Red'
  elif id_pokemon == '120': cor = 'Brown'
  elif id_pokemon == '121': cor = 'Purple'
  elif id_pokemon == '123': cor = 'Green'
  elif id_pokemon == '124': cor = 'Red'
  elif id_pokemon == '125': cor = 'Yellow'
  elif id_pokemon == '126': cor = 'Red'
  elif id_pokemon == '127': cor = 'Brown'
  elif id_pokemon == '128': cor = 'Brown'
  elif id_pokemon == '129': cor = 'Red'
  elif id_pokemon == '130': cor = 'Blue'
  elif id_pokemon == '131': cor = 'Blue'
  elif id_pokemon == '132': cor = 'Purple'
  elif id_pokemon == '133': cor = 'Brown'
  elif id_pokemon == '134': cor = 'Blue'
  elif id_pokemon == '135': cor = 'Yellow'
  elif id_pokemon == '136': cor = 'Red'
  elif id_pokemon == '137': cor = 'Pink'
  elif id_pokemon == '138': cor = 'Blue'
  elif id_pokemon == '139': cor = 'Blue'
  elif id_pokemon == '140': cor = 'Brown'
  elif id_pokemon == '141': cor = 'Brown'
  elif id_pokemon == '142': cor = 'Purple'
  elif id_pokemon == '143': cor = 'Black'
  elif id_pokemon == '144': cor = 'Blue'
  elif id_pokemon == '145': cor = 'Yellow'
  elif id_pokemon == '146': cor = 'Yellow'
  elif id_pokemon == '147': cor = 'Blue'
  elif id_pokemon == '148': cor = 'Blue'
  elif id_pokemon == '149': cor = 'Brown'
  elif id_pokemon == '150': cor = 'Purple'
  elif id_pokemon == '151': cor = 'Pink'


  return cor


class BlogSpider(scrapy.Spider):
  name = 'blogspider'


  def start_requests(self):

      lista = ['bulbasaur','ivysaur','venusaur','venusaur','charmander','charmeleon','charizard','charizard','charizard','squirtle','wartortle','blastoise','blastoise',
      'caterpie','metapod','butterfree','weedle','kakuna','beedrill','beedrill','pidgey','pidgeotto','pidgeot','pidgeot','rattata','rattata','raticate','raticate',
      'spearow','fearow','ekans','arbok','pikachu','pikachu','raichu','raichu','sandshrew','sandshrew','sandslash','sandslash','nidoranâ™€','nidorina','nidoqueen',
      'nidoranâ™‚','nidorino','nidoking','clefairy','clefable','vulpix','vulpix','ninetales','ninetales','jigglypuff','wigglytuff','zubat','golbat','oddish','gloom',
      'vileplume','paras','parasect','venonat','venomoth','diglett','diglett','dugtrio','dugtrio','meowth','meowth','meowth','persian','persian','psyduck','golduck',
      'mankey','primeape','growlithe','growlithe','arcanine','arcanine','poliwag','poliwhirl','poliwrath','abra','kadabra','alakazam','alakazam','machop','machoke',
      'machamp','bellsprout','weepinbell','victreebel','tentacool','tentacruel','geodude','geodude','graveler','graveler','golem','golem','ponyta','ponyta','rapidash',
      'rapidash','slowpoke','slowpoke','slowbro','slowbro','slowbro','magnemite','magneton','farfetchd','farfetchd','doduo','dodrio','seel','dewgong','grimer','grimer',
      'muk','muk','shellder','cloyster','gastly','haunter','gengar','gengar','onix','drowzee','hypno','krabby','kingler','voltorb','voltorb','electrode','electrode',
      'exeggcute','exeggutor','exeggutor','cubone','marowak','marowak','hitmonlee','hitmonchan','lickitung','koffing','weezing','weezing','rhyhorn','rhydon','chansey',
      'tangela','kangaskhan','kangaskhan','horsea','seadra','goldeen','seaking','staryu','starmie','mr. mime','mr. mime','scyther','jynx','electabuzz','magmar','pinsir',
      'pinsir','tauros','magikarp','gyarados','gyarados','lapras','ditto','eevee','eevee','vaporeon','jolteon','flareon','porygon','omanyte','omastar','kabuto','kabutops',
      'aerodactyl','aerodactyl','snorlax','articuno','articuno','zapdos','zapdos','moltres','moltres','dratini','dragonair','dragonite','mewtwo','mewtwo','mewtwo','mew']

      for item in lista:
        urls.append("https://pokemondb.net/pokedex/"+ item)
      
      for index, item2 in enumerate(urls):
        yield scrapy.Request(url=item2, callback=self.parse, cb_kwargs={'index': index})

  def parse(self, response, index):

    nome = response.css('#main > h1::text').get()
    pos = corrigir_ordem(index, nome)
    id_pokemon = response.css('#tab-basic-'+str(pos)+'> div:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > strong:nth-child(1)::text').get()
    tipo1 = response.css('#tab-basic-'+str(pos)+'> div:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1)::text').get()
    tipo2 = response.css('#tab-basic-'+str(pos)+'> div:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(2)::text').get()
    tamanho = response.css('#tab-basic-'+str(pos)+' > div:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)::text').get()
    peso = response.css('#tab-basic-'+str(pos)+'> div:nth-child(1) > div:nth-child(2) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)::text').get()
    evolucao = response.css('div.infocard:nth-child(3) > span:nth-child(2) > small:nth-child(1)::text').get()
    dano = response.css('div.grid-row:nth-child(2) > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)::text').get()
    cor_pokedex = corrigir_pokedex(id_pokemon)

    yield {'nome': nome, 'id_pokemon': id_pokemon, 'tipo1': tipo1, 'tipo2': tipo2, 'tamanho': tamanho, 'peso': peso, 'evolucao': evolucao, 'dano': dano, 'cor_pokedex': cor_pokedex }


if __name__ == '__main__':
  BlogSpider.run()  

