import pandas as pd
from deep_translator import GoogleTranslator
from tqdm import tqdm  # Barra de progresso (opcional, mas recomendada)

# Carregar dados
df = pd.read_csv('dados-imersao-final.csv')

# 1. Pegar apenas os cargos únicos (para não traduzir 30 mil linhas repetidas)
cargos_unicos = df['cargo'].unique()

# 2. Criar um tradutor
tradutor = GoogleTranslator(source='en', target='pt')

# 3. Criar um dicionário de tradução
# Dicionário com os termos mais comuns já traduzidos corretamente para o mercado BR
dicionario_cargos = {
    'Data Scientist': 'Cientista de Dados',
    'Software Engineer': 'Engenheiro de Software',
    'Data Engineer': 'Engenheiro de Dados',
    'Data Analyst': 'Analista de Dados',
    'Engineer': 'Engenheiro',
    'Machine Learning Engineer': 'Engenheiro de Machine Learning',
    'Manager': 'Gerente',
    'Analyst': 'Analista',
    'Research Scientist': 'Cientista Pesquisador',
    'Product Manager': 'Gerente de Produto',
    'Applied Scientist': 'Cientista Aplicado',
    'Data Architect': 'Arquiteto de Dados',
    'Analytics Engineer': 'Engenheiro de Analytics',
    'AI Engineer': 'Engenheiro de IA',
    'Business Intelligence Engineer': 'Engenheiro de BI',
    'Data Manager': 'Gerente de Dados',
    'Research Engineer': 'Engenheiro de Pesquisa',
    'Head of Data': 'Head de Dados',
    'Lead Data Scientist': 'Cientista de Dados Líder'
}

print("Iniciando tradução...")
# Loop para traduzir cada cargo único
for cargo in tqdm(cargos_unicos):
    try:
        # Traduz e guarda no dicionário
        mapa_traducao[cargo] = tradutor.translate(cargo)
    except:
        # Se der erro (timeout), mantém o original
        mapa_traducao[cargo] = cargo

# 4. Aplicar a tradução no DataFrame original
df['cargo_pt'] = df['cargo'].map(mapa_traducao)

# Ver o resultado
print(df[['cargo', 'cargo_pt']].head())

# Salvar
df.to_csv('dados-traduzidos.csv', index=False)