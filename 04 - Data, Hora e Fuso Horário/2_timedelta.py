from datetime import timedelta, datetime, date

tipo_carro = 'G'  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"Veículo de tamanho: Pequeno / Entrada: {data_atual} / Saída: {data_estimada}")

elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"Véiculo de tamanho: Médio / Entrada: {data_atual} / Saída: {data_estimada}")

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"Veículo de tamanho: Grande / Entrada: {data_atual} / Saída: {data_estimada}")


print(date.today() - timedelta(days=1))

resultado = datetime(2024, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().date())