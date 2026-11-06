# 🚀 Dashboard Operacional NOC CAB/PI: Monitoramento em Tempo Real da Rede (Prefeitura de Cabeceiras do Piauí)

Sistema de monitoramento centralizado desenvolvido com auxílio do **Antigravity**, projetado para monitorar a topologia e a telemetria em tempo real das **94 unidades escolares e administrativas** interligadas ao Core do **NOC CAB/PI** através de túneis IPsec Fortinet sobre a malha metropolitana, além dos links redundantes de alta capacidade da sede.

---

## 📦 Arquivos Disponibilizados

| Arquivo | Descrição |
| :--- | :--- |
| **`index.html`** | Aplicação web interativa autônoma com topologia radial em Canvas/WebGL, zoom, pan, gaveta lateral de inspeção e simulador de falhas. |
| **`noc_dashboard_grafana.json`** | Modelo pronto para importação direta no **Grafana 9.x / 10.x / 11.x**. |
| **`zabbix_sync_daemon.py`** | Script Python de integração com a API JSON-RPC do Zabbix (6.x e 7.x). |

---

## 🌟 O Que o Sistema Entrega na Prática

1. **Topologia em Tempo Real (Radial Tree Responsiva):**
   - Agrupamento das 94 escolas nos **4 Concentradores Regionais**:
     - **UPA NORTE** (14 unidades)
     - **SMTT** (11 unidades)
     - **SEPLOG** (19 unidades)
     - **UPA SUL** (50 unidades)
   - Visualização do nó central **CORE SEMED (SEDE BDR)** com os ativos de borda: `SW-L3-COR-SEMED`, `RTR-PE-SEMED-01`, `Rede GPON (569 Mbps)` e redundâncias `BK Rota 1/2`.
   - Animação de fluxo de dados nas linhas e pulso de saturação nos anéis de cada concentrador.

2. **Telemetria dos Links de Borda:**
   - **LINK 1: WAN02-RIMA (10 Gbps)**: Download, Upload, Latência RTT (1.8 ms), Jitter (0.2 ms) e taxa de perda (0.0%).
   - **LINK 2: WAN01-BKT (Port1)**: Backup redundante com failover automático.
   - **Tráfego Agregado WAN Core**: Monitoramento instantâneo em Mbps/Gbps com % de carga da malha óptica.

3. **Saúde dos Túneis IPsec (FortiGate CPE):**
   - Status individual de Phase 1 e Phase 2 (AES256-SHA256) de cada unidade.
   - Detecção instantânea de quedas (flapping ou timeout de rekeying).

4. **Filtro Inteligente de Incidentes:**
   - Painel inferior focado em **alarmes operacionais de alto impacto** (Disaster / High), eliminando ruídos de alertas transitórios.

5. **Interatividade & Inspeção Instantânea:**
   - **Zoom & Pan**: Navegação fluida via scroll do mouse ou botões de atalho (Core, UPA Norte, SEPLOG, SMTT, UPA Sul).
   - **Clique para Inspecionar**: Ao clicar em qualquer nó ou escola, uma gaveta lateral (*Slide Drawer*) exibe:
     - Modelo do Firewall CPE (`FortiGate 40F`) e versão do FortiOS.
     - Subrede LAN e IP virtual do túnel IPsec.
     - Gráfico dinâmico de throughput In/Out.
     - Switch Core local (`FortiSwitch 124E-POE`) e status dos APs (`FortiAP 231F`).
     - Botão de simulação de queda para testes de contingência do NOC.
   - **Visão em Grade Compacta**: Alternância com um clique para visualizar o mosaico das 94 unidades simultaneamente.

---

## 🛠️ Como Executar o Dashboard Web Imediatamente

Você pode abrir o arquivo `index.html` diretamente em qualquer navegador moderno (Chrome, Edge, Firefox):

```bash
# Opção 1: Abrir diretamente no navegador
start index.html

# Opção 2: Servir via servidor HTTP local (Python)
python -m http.server 8080
# Acesse no navegador: http://localhost:8080
```

---

## 📊 Como Importar no Grafana

### Pré-requisitos
1. Plugin do Zabbix instalado:
   ```bash
   grafana-cli plugins install alexanderzobnin-zabbix-app
   ```
2. Plugin Apache ECharts (para renderização radial):
   ```bash
   grafana-cli plugins install volkovlabs-echarts-panel
   ```
3. Reinicie o serviço do Grafana.

### Passo a Passo de Importação
1. No menu lateral do Grafana, clique em **Dashboards** > **New** > **Import**.
2. Faça o upload do arquivo `noc_dashboard_grafana.json` ou cole o seu conteúdo.
3. Selecione o seu Datasource do Zabbix configurado.
4. Clique em **Import**. O painel já virá configurado com os thresholds de cores e queries de tráfego.

---

## 🔌 Chaves de Coleta Zabbix Recomendadas

| Métrica | Chave Zabbix / SNMP | Unidade |
| :--- | :--- | :--- |
| **Ping / Latência** | `icmppingsec` | Segundos (renderizado em ms) |
| **Perda de Pacotes** | `icmppingloss` | % |
| **Túnel IPsec Fortinet** | `fortinet.ipsec.tunnel.status["{#TUNNEL_NAME}"]` | 1 = Up, 2 = Down |
| **Tráfego WAN In** | `net.if.in[ifHCInOctets.{#IFNAME}]` | bps |
| **Tráfego WAN Out** | `net.if.out[ifHCOutOctets.{#IFNAME}]` | bps |
| **Carga de CPU CPE** | `system.cpu.util` | % |

