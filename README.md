# Green Charge — Monitoramento Inteligente de Eletropostos (GoodWe)

A ideia desse projeto é resolver o gargalo dos eletropostos urbanos: a sobrecarga da rede elétrica nos horários de pico e o desperdício de energia gerada. Integrando a lógica dos inversores da GoodWe com bancos de baterias, o sistema gerencia as fontes de energia de forma autônoma.

---

## Como funciona a lógica do protótipo

O script em Python simula o comportamento do eletroposto rodando em tempo real. Ele analisa três frentes:
1. **Geração Solar:** Quanto os painéis (via inversores GoodWe) estão gerando de energia limpa.
2. **Banco de Baterias:** Armazenamento local para guardar o excedente e dar resiliência ao sistema.
3. **Demanda do Eletroposto:** O consumo dinâmico dos carros conectados.

Com base nisso, o algoritmo decide de onde puxar a energia em milissegundos, priorizando sempre a sustentabilidade e a eficiência da rede.

---

## Eficiência Energética e Sustentabilidade na Prática

O código foi estruturado em cima de dois conceitos chave:

* **Desvio de Pico:** Entre 18h e 21h (pico da rede urbana), o sistema corta o consumo da rede da concessionária e passa a alimentar os veículos usando a energia armazenada nas baterias durante o dia. Isso evita sobrecarga na malha pública e reduz custos tarifários.
* **Aproveitamento Total:** Se há geração solar mas nenhum carro está conectado, o excedente vai 100% para carregar as baterias locais, zerando o desperdício.

Gustavo de Souza Abreu — RM 574080

Enzo Coppa Selingarde — RM 573393

Gabriel Carlos Barbosa — RM 574074
