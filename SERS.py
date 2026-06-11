import time
import random
from datetime import datetime


class GreenChargeSystem:
    def __init__(self):
        # Capacidade máxima da bateria em kWh e carga inicial (50%)
        self.bateria_capacidade_max = 100.0
        self.bateria_atual = 50.0

    def simular_ambiente(self, hora):
        """ Simula as condições climáticas e demanda com base no horário do dia """
        # Geração solar pico entre 10h e 16h
        if 6 <= hora <= 18:
            geracao_solar = round(random.uniform(20.0, 45.0), 2)
        else:
            geracao_solar = 0.0  # Sem sol à noite

        # Horário de pico urbano (18h às 21h) aumenta a demanda do eletroposto
        if 18 <= hora <= 21:
            demanda_eletroposto = round(random.uniform(35.0, 50.0), 2)
            horario_pico = True
        else:
            demanda_eletroposto = round(random.uniform(10.0, 25.0), 2)
            horario_pico = False

        return geracao_solar, demanda_eletroposto, horario_pico

    def processar_energia(self, geracao_solar, demanda, horario_pico):
        fonte_solar = 0.0
        fonte_bateria = 0.0
        fonte_rede = 0.0

        sobrou_solar = 0.0
        demanda_restante = demanda

        # 1. Prioridade Máxima: Usar energia Solar direta (Sustentabilidade)
        if geracao_solar >= demanda_restante:
            fonte_solar = demanda_restante
            sobrou_solar = geracao_solar - demanda_restante
            demanda_restante = 0.0
        else:
            fonte_solar = geracao_solar
            demanda_restante -= geracao_solar

        # 2. Se sobrou solar, armazena na bateria (Eficiência Energética)
        if sobrou_solar > 0:
            espaco_bateria = self.bateria_capacidade_max - self.bateria_atual
            if sobrou_solar <= espaco_bateria:
                self.bateria_atual += sobrou_solar
            else:
                self.bateria_atual = self.bateria_capacidade_max

        # 3. Segunda Prioridade: Se falta energia, usa a Bateria (especialmente no pico)
        if demanda_restante > 0 and self.bateria_atual > 5.0:  # Mantém margem de segurança de 5%
            energia_disponivel = self.bateria_atual - 5.0
            if energia_disponivel >= demanda_restante:
                fonte_bateria = demanda_restante
                self.bateria_atual -= demanda_restante
                demanda_restante = 0.0
            else:
                fonte_bateria = energia_disponivel
                self.bateria_atual = 5.0
                demanda_restante -= energia_disponivel

        # 4. Último caso: Usa a rede elétrica externa (Evita sobrecarga se for horário de pico)
        if demanda_restante > 0:
            fonte_rede = demanda_restante
            demanda_restante = 0.0

        return fonte_solar, fonte_bateria, fonte_rede

    def executar_monitoramento(self, ciclos=10):
        print("=" * 70)
        print("     GREEN CHARGE - SISTEMA DE MONITORAMENTO INTELIGENTE (GOODWE)     ")
        print("=" * 70)

        hora_simulada = 15  # Começa a simulação às 15h para pegar transição dia/noite

        for i in range(ciclos):
            hora_formatada = f"{hora_simulada:02d}:00"
            sol, demanda, pico = self.simular_ambiente(hora_simulada)

            f_solar, f_bateria, f_rede = self.processar_energia(sol, demanda, pico)

            print(f"\n[HORÁRIO: {hora_formatada}] | STATUS REDE: {'⚠️ PICO URBANO' if pico else '🟢 NORMAL'}")
            print(f" -> Geração Solar Atual: {sol} kWh")
            print(f" -> Demanda do Eletroposto: {demanda} kWh")
            print(f" -> Banco de Baterias: {round(self.bateria_atual, 2)} kWh ({round((self.bateria_atual / self.bateria_capacidade_max) * 100, 1)}%)")
            print(f" DISTRIBUIÇÃO DA ENERGIA UTILIZADA:")
            print(f"    ️ [Solar Direta]:  {round(f_solar, 2)} kWh")
            print(f"     [Banco Bateria]: {round(f_bateria, 2)} kWh")
            print(f"     [Rede Elétrica]: {round(f_rede, 2)} kWh")

            # Validação lógica de sustentabilidade no terminal
            if f_rede == 0 and f_bateria > 0:
                print("🍃 Impacto Zero na Rede Concessionária: Eletroposto sustentado por baterias/sol.")
            elif pico and f_rede > 0:
                print("⚠️ Alerta: Demanda crítica superou o armazenamento local no horário de pico.")

            print("-" * 70)

            # Avança o tempo na simulação
            hora_simulada = (hora_simulada + 1) % 24
            time.sleep(2)  # Pausa para leitura didática no terminal


if __name__ == "__main__":
    sistema = GreenChargeSystem()
    sistema.executar_monitoramento(ciclos=8)