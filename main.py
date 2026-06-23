import networkx as nx
from pyvis.network import Network

# 1. INICIALIZAÇÃO DO GRAFO DIRECONADO
# Instanciamos um DiGraph (Grafo Direcionado) porque as órbitas possuem um sentido 
G = nx.DiGraph()

# 2. BASE DE DADOS
astros = {
    # Estrela Central
    "Sol": {"tipo": "Estrela", "classificacao": "Ana Amarela"},
    
    # Planetas Principais
    "Mercurio": {"tipo": "Planeta", "classificacao": "Rochoso"},
    "Venus": {"tipo": "Planeta", "classificacao": "Rochoso"},
    "Terra": {"tipo": "Planeta", "classificacao": "Rochoso"},
    "Marte": {"tipo": "Planeta", "classificacao": "Rochoso"},
    "Jupiter": {"tipo": "Planeta", "classificacao": "Gigante Gasoso"},
    "Saturno": {"tipo": "Planeta", "classificacao": "Gigante Gasoso"},
    "Urano": {"tipo": "Planeta", "classificacao": "Gigante Gelado"},
    "Netuno": {"tipo": "Planeta", "classificacao": "Gigante Gelado"},
    
    # Planetas Anões
    "Plutao": {"tipo": "Planeta Anao", "classificacao": "Plutoide"},
    "Ceres": {"tipo": "Planeta Anao", "classificacao": "Asteroide Grande"},
    "Eris": {"tipo": "Planeta Anao", "classificacao": "Plutoide"},
    "Haumea": {"tipo": "Planeta Anao", "classificacao": "Plutoide"},
    "Makemake": {"tipo": "Planeta Anao", "classificacao": "Plutoide"},

    # Satélites Naturais (Luas da Terra e de Marte)
    "Lua": {"tipo": "Satelite", "classificacao": "Rochoso"},
    "Fobos": {"tipo": "Satelite", "classificacao": "Asteroide Capturado"},
    "Deimos": {"tipo": "Satelite", "classificacao": "Asteroide Capturado"},
    
    # Satélites Naturais (Luas de Júpiter)
    "Io": {"tipo": "Satelite", "classificacao": "Galileana"},
    "Europa": {"tipo": "Satelite", "classificacao": "Galileana"},
    "Ganimedes": {"tipo": "Satelite", "classificacao": "Galileana"},
    "Calisto": {"tipo": "Satelite", "classificacao": "Galileana"},
    "Amalteia": {"tipo": "Satelite", "classificacao": "Interna Irregular"},
    "Himalia": {"tipo": "Satelite", "classificacao": "Externa Irregular"},
    "Tebe": {"tipo": "Satelite", "classificacao": "Interna Irregular"},
    "Elara": {"tipo": "Satelite", "classificacao": "Externa Irregular"},
    "Pasife": {"tipo": "Satelite", "classificacao": "Externa Irregular"},
    "Carme": {"tipo": "Satelite", "classificacao": "Externa Irregular"},
    
    # Satélites Naturais (Luas de Saturno)
    "Tita": {"tipo": "Satelite", "classificacao": "Atmosfera Densa"},
    "Encelado": {"tipo": "Satelite", "classificacao": "Criovulcanica"},
    "Mimas": {"tipo": "Satelite", "classificacao": "Corpo Gelado"},
    "Reia": {"tipo": "Satelite", "classificacao": "Corpo Gelado"},
    "Japeto": {"tipo": "Satelite", "classificacao": "Bicolor"},
    "Dione": {"tipo": "Satelite", "classificacao": "Corpo Gelado"},
    "Tetis": {"tipo": "Satelite", "classificacao": "Corpo Gelado"},
    "Hiperion": {"tipo": "Satelite", "classificacao": "Esponjoso"},
    
    # Satélites Naturais (Luas de Urano)
    "Titania": {"tipo": "Satelite", "classificacao": "Corpo Gelado"},
    "Oberon": {"tipo": "Satelite", "classificacao": "Corpo Gelado"},
    "Umbriel": {"tipo": "Satelite", "classificacao": "Corpo Gelado"},
    "Ariel": {"tipo": "Satelite", "classificacao": "Corpo Gelado"},
    
    # Satélites Naturais (Lua de Netuno)
    "Tritao": {"tipo": "Satelite", "classificacao": "Orbita Retrograda"}
}

# 3. INJEÇÃO DOS NÓS NO NETWORKX
for nome, propiedades in astros.items():
    G.add_node(nome, **propiedades)

print(f"Grafo inicializado com {G.number_of_nodes()} nos do Sistema Solar.")

# 4. MAPEAMENTO DE RELACIONAMENTOS
# (Astro_Orbital, Centro_Gravitacional, Distancia_km)
conexoes = [
    # Planetas Principais e Planetas Anões que orbitam diretamente o Sol
    ("Mercurio", "Sol", 57900000), ("Venus", "Sol", 108200000), 
    ("Terra", "Sol", 149600000), ("Marte", "Sol", 227900000),
    ("Jupiter", "Sol", 778500000), ("Saturno", "Sol", 1434000000), 
    ("Urano", "Sol", 2871000000), ("Netuno", "Sol", 4495000000),
    ("Plutao", "Sol", 5906000000), ("Ceres", "Sol", 413700000),
    ("Eris", "Sol", 10120000000), ("Haumea", "Sol", 6450000000), 
    ("Makemake", "Sol", 6850000000),
    
    # Satélites orbitando seus respectivos planetas hospedeiros
    ("Lua", "Terra", 384400), ("Fobos", "Marte", 9377), ("Deimos", "Marte", 23460),
    ("Io", "Jupiter", 421700), ("Europa", "Jupiter", 670900), 
    ("Ganimedes", "Jupiter", 1070400), ("Calisto", "Jupiter", 1882700),
    ("Amalteia", "Jupiter", 181400), ("Himalia", "Jupiter", 11461000),
    ("Tebe", "Jupiter", 221900), ("Elara", "Jupiter", 11741000),
    ("Pasife", "Jupiter", 23624000), ("Carme", "Jupiter", 23404000),
    ("Tita", "Saturno", 1221800), ("Encelado", "Saturno", 238000), 
    ("Mimas", "Saturno", 185400), ("Reia", "Saturno", 527100),
    ("Japeto", "Saturno", 3560800), ("Dione", "Saturno", 377400),
    ("Tetis", "Saturno", 294600), ("Hiperion", "Saturno", 1481100),
    ("Titania", "Urano", 435900), ("Oberon", "Urano", 583500),
    ("Umbriel", "Urano", 266000), ("Ariel", "Urano", 191000),
    ("Tritao", "Netuno", 354800)
]

for origem, destino, dist in conexoes:
    G.add_edge(origem, destino, relacao="ORBITA", distancia_km=dist)

print(f"Vinculos orbitais estabelecidos com {G.number_of_edges()} arestas.")