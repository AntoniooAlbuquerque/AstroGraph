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