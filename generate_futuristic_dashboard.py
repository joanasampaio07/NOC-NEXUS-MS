import os

html_content = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NOC NEXUS-M&S // CENTRO INTEGRADO DE OPERAÇÕES DE REDE & SOC</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700;800&family=Orbitron:wght@500;700;900&family=Inter:wght@400;500;600;700&display=swap');

    :root {
      --bg-dark: #030712;
      --panel-bg: rgba(6, 13, 26, 0.88);
      --panel-border: rgba(0, 240, 255, 0.22);
      --cyan-neon: #00f0ff;
      --emerald-neon: #00ff9d;
      --amber-warn: #ffb800;
      --crimson-alert: #ff003c;
    }

    body {
      background-color: var(--bg-dark);
      color: #e2e8f0;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      overflow-x: hidden;
    }

    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }

    .font-cyber {
      font-family: 'Orbitron', sans-serif;
      letter-spacing: 0.05em;
    }

    /* Cyber Glassmorphism */
    .cyber-glass {
      background: var(--panel-bg);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid var(--panel-border);
      box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5), inset 0 0 12px 0 rgba(0, 240, 255, 0.05);
    }

    .cyber-glass-alert {
      background: rgba(30, 6, 12, 0.92);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 0, 60, 0.4);
      box-shadow: 0 0 35px rgba(255, 0, 60, 0.25), inset 0 0 15px rgba(255, 0, 60, 0.1);
    }

    /* Glows */
    .glow-cyan {
      box-shadow: 0 0 20px rgba(0, 240, 255, 0.35);
    }
    .glow-emerald {
      box-shadow: 0 0 20px rgba(0, 255, 157, 0.35);
    }
    .glow-crimson {
      box-shadow: 0 0 25px rgba(255, 0, 60, 0.45);
    }
    .text-glow-cyan {
      text-shadow: 0 0 10px rgba(0, 240, 255, 0.65);
    }
    .text-glow-emerald {
      text-shadow: 0 0 10px rgba(0, 255, 157, 0.65);
    }
    .text-glow-crimson {
      text-shadow: 0 0 12px rgba(255, 0, 60, 0.8);
    }

    /* Futuristic Scanline Effect on Canvas */
    .scanline-overlay {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 240, 255, 0.02) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.01), rgba(0, 255, 0, 0.005), rgba(0, 0, 255, 0.01));
      background-size: 100% 3px, 6px 100%;
      pointer-events: none;
      z-index: 10;
    }

    /* Radar sweep animation */
    @keyframes radar-sweep {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    .radar-sweep-beam {
      position: absolute;
      top: 50%; left: 50%;
      width: 500px; height: 500px;
      margin-left: -250px; margin-top: -250px;
      border-radius: 50%;
      background: conic-gradient(from 0deg at 50% 50%, rgba(0, 240, 255, 0.12) 0deg, rgba(0, 240, 255, 0.04) 45deg, transparent 90deg);
      animation: radar-sweep 12s linear infinite;
      pointer-events: none;
      z-index: 2;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 5px;
      height: 5px;
    }
    ::-webkit-scrollbar-track {
      background: #020611;
    }
    ::-webkit-scrollbar-thumb {
      background: #0d2238;
      border-radius: 2px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: var(--cyan-neon);
    }

    /* Print styles for Executive Report */
    @media print {
      body * {
        visibility: hidden;
      }
      #executiveReportModal, #executiveReportModal * {
        visibility: visible;
      }
      #executiveReportModal {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        background: #ffffff !important;
        color: #0f172a !important;
        padding: 0 !important;
        box-shadow: none !important;
        border: none !important;
      }
      .no-print {
        display: none !important;
      }
    }
  </style>
</head>
<body class="bg-[#030712] text-slate-100 min-h-screen flex flex-col antialiased select-none font-sans">

  <!-- TOP MILITARY-GRADE COMMAND BAR -->
  <header class="bg-[#050b18]/95 border-b border-cyan-900/40 px-4 py-2 flex flex-wrap items-center justify-between gap-3 shadow-2xl relative z-40">
    <div class="flex items-center space-x-3">
      <!-- High-tech insignia -->
      <div class="relative flex items-center justify-center px-2.5 h-8 rounded bg-cyan-950/80 border border-cyan-400 text-cyan-300 font-cyber font-bold text-xs tracking-widest glow-cyan">
        NOC NEXUS-M&S
        <span class="absolute -top-1 -right-1 w-2.5 h-2.5 bg-emerald-400 rounded-full animate-ping"></span>
        <span class="absolute -top-1 -right-1 w-2.5 h-2.5 bg-emerald-500 rounded-full"></span>
      </div>

      <div class="border-l border-slate-700/60 pl-3">
        <div class="text-[11px] font-cyber font-bold tracking-wider text-cyan-400 flex items-center gap-2">
          <span>NEXUS-M&S // ENTERPRISE OPERATIONS</span>
          <span class="text-slate-600">//</span>
          <span class="text-slate-300">CENTRO INTEGRADO DE OPERAÇÕES DE REDE & SOC</span>
        </div>
        <div class="text-[10px] text-slate-400 flex items-center gap-2 font-mono">
          <span class="inline-block w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
          <span id="headerLinkStatusText" class="text-emerald-400 font-semibold">Links Core Nominais (WAN02 10G + WAN01 BK) • 94/94 Unidades Online</span>
          <span class="text-slate-600">|</span>
          <span class="text-cyan-500/80">ASN 263952</span>
          <span class="text-slate-600">|</span>
          <span class="text-slate-400">NEXUS CORE</span>
        </div>
      </div>
    </div>

    <!-- DEFCON & Status Center -->
    <div class="flex items-center gap-3">
      <!-- DEFCON Indicator -->
      <div id="defconIndicator" class="flex items-center gap-2 px-2.5 py-1 rounded bg-slate-900/80 border border-emerald-500/40 text-[10px] font-mono tracking-wider transition-all duration-300">
        <span class="text-slate-400">ESTADO DEFENSIVO:</span>
        <span id="defconValue" class="font-bold text-emerald-400 font-cyber flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          DEFCON 5 • COND. VERDE
        </span>
      </div>

      <!-- Quick Action Controls -->
      <button id="btnOpenCyberHud" class="cursor-pointer active:scale-95 bg-gradient-to-r from-red-600 via-rose-600 to-amber-600 hover:from-red-500 hover:to-rose-500 text-white font-cyber font-bold px-3 py-1.5 rounded text-[11px] transition shadow-lg shadow-rose-950/70 border border-rose-400 flex items-center gap-1.5 animate-pulse">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
        WAR ROOM • CSIRT
      </button>

      <button id="btnViewRadial" class="cursor-pointer active:scale-95 bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold px-3 py-1.5 rounded text-xs transition shadow-sm font-mono">
        Topologia Radial
      </button>

      <button id="btnViewGrid" class="cursor-pointer active:scale-95 bg-[#091524] hover:bg-[#122842] border border-[#1b3d63] text-cyan-300 px-3 py-1.5 rounded text-xs transition font-mono">
        Grade Matriz (94)
      </button>

      <button id="btnZabbixModal" class="cursor-pointer active:scale-95 bg-[#091524] hover:bg-[#122842] border border-[#1b3d63] text-slate-300 px-3 py-1.5 rounded text-xs flex items-center gap-1.5 transition font-mono">
        <span class="w-2 h-2 rounded-full bg-cyan-400"></span>
        Zabbix 7.0
      </button>

      <button id="btnSimulateIssue" class="cursor-pointer active:scale-95 bg-rose-950/60 hover:bg-rose-900 border border-rose-500/50 text-rose-300 px-2.5 py-1.5 rounded text-xs transition flex items-center gap-1 font-mono">
        ⚡ Simular Falha
      </button>
    </div>
  </header>

  <!-- HIGH-DENSITY TELEMETRY STRIP (KPIs) -->
  <section class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-2 px-4 py-2 bg-[#02050c] border-b border-cyan-950/40 relative z-30">
    <!-- KPI 1 -->
    <div class="cyber-glass rounded p-2 flex items-center justify-between border-l-2 border-l-emerald-500">
      <div>
        <span class="text-[10px] font-mono text-slate-400 block tracking-wider uppercase">Unidades Escolares</span>
        <div class="flex items-baseline space-x-1.5 mt-0.5">
          <span id="kpiOnlineCount" class="text-xl font-bold font-cyber text-emerald-400 text-glow-emerald">94</span>
          <span class="text-xs font-mono text-slate-500">/ 94 UP</span>
        </div>
        <div class="w-24 bg-slate-900 h-1 rounded-full mt-1 overflow-hidden">
          <div id="kpiSchoolBar" class="bg-emerald-400 h-full w-full transition-all duration-500"></div>
        </div>
      </div>
      <div class="text-right text-[10px] font-mono text-slate-400">
        <span class="text-emerald-400 font-bold">100% ONLINE</span>
        <span class="block text-slate-500 text-[9px]">SLA 99.98%</span>
      </div>
    </div>

    <!-- KPI 2 -->
    <div class="cyber-glass rounded p-2 flex items-center justify-between border-l-2 border-l-cyan-500">
      <div>
        <span class="text-[10px] font-mono text-slate-400 block tracking-wider uppercase">Túneis VPN IPsec</span>
        <div class="flex items-baseline space-x-1.5 mt-0.5">
          <span id="kpiVpnCount" class="text-xl font-bold font-cyber text-cyan-400 text-glow-cyan">94</span>
          <span class="text-xs font-mono text-slate-500">/ 94 UP</span>
        </div>
        <div class="w-24 bg-slate-900 h-1 rounded-full mt-1 overflow-hidden">
          <div id="kpiVpnBar" class="bg-cyan-400 h-full w-full transition-all duration-500"></div>
        </div>
      </div>
      <div class="text-right text-[10px] font-mono text-slate-400">
        <span class="text-cyan-300 font-semibold">IKEv2 / AES-256</span>
        <span class="block text-emerald-400 text-[9px]">0 Flapping</span>
      </div>
    </div>

    <!-- KPI 3 -->
    <div class="cyber-glass rounded p-2 flex items-center justify-between border-l-2 border-l-cyan-400">
      <div>
        <div class="flex items-center gap-1.5">
          <span class="text-[10px] font-mono text-slate-400 tracking-wider uppercase">Link 1: WAN02-RIMA</span>
          <span class="text-[9px] bg-cyan-950/80 text-cyan-300 px-1 rounded border border-cyan-500/40 font-mono">10G</span>
        </div>
        <div class="flex items-baseline space-x-2 mt-0.5 text-xs font-mono font-bold">
          <span class="text-emerald-400">↓ <span id="link1Rx">881.5</span>M</span>
          <span class="text-cyan-400">↑ <span id="link1Tx">376.0</span>M</span>
        </div>
        <div class="text-[10px] text-slate-400 font-mono flex items-center space-x-2 mt-0.5">
          <span>RTT: <strong id="link1Latency" class="text-cyan-300">1.8 ms</strong></span>
          <span>Perda: <strong id="link1Loss" class="text-emerald-400">0.0%</strong></span>
        </div>
      </div>
      <span class="w-2 h-2 rounded-full bg-emerald-400 shadow-[0_0_8px_#00ff9d]"></span>
    </div>

    <!-- KPI 4 -->
    <div class="cyber-glass rounded p-2 flex items-center justify-between border-l-2 border-l-indigo-500">
      <div>
        <div class="flex items-center gap-1.5">
          <span class="text-[10px] font-mono text-slate-400 tracking-wider uppercase">Link 2: WAN01-BKT</span>
          <span class="text-[9px] bg-indigo-950/80 text-indigo-300 px-1 rounded border border-indigo-500/40 font-mono">BK REDUNDANTE</span>
        </div>
        <div class="flex items-baseline space-x-2 mt-0.5 text-xs font-mono font-bold">
          <span class="text-indigo-300">↓ <span id="link2Rx">67.3</span>M</span>
          <span class="text-indigo-400">↑ <span id="link2Tx">40.5</span>M</span>
        </div>
        <div class="text-[10px] text-slate-400 font-mono flex items-center space-x-2 mt-0.5">
          <span>RTT: <strong id="link2Latency" class="text-indigo-300">3.4 ms</strong></span>
          <span>Perda: <strong id="link2Loss" class="text-emerald-400">0.0%</strong></span>
        </div>
      </div>
      <span class="w-2 h-2 rounded-full bg-emerald-400 shadow-[0_0_8px_#00ff9d]"></span>
    </div>

    <!-- KPI 5 -->
    <div class="cyber-glass rounded p-2 flex items-center justify-between border-l-2 border-l-teal-500">
      <div>
        <span class="text-[10px] font-mono text-slate-400 block tracking-wider uppercase">Vazão Total Core BDR</span>
        <div class="flex items-baseline space-x-1.5 mt-0.5">
          <span id="kpiCoreTraffic" class="text-xl font-bold font-cyber text-cyan-300 text-glow-cyan">1048.8</span>
          <span class="text-xs font-mono text-slate-400">Mbps</span>
        </div>
        <span class="text-[10px] text-slate-400 font-mono">Malha Óptica: <strong class="text-cyan-400">569 Mbps</strong></span>
      </div>
      <div class="text-right text-[10px] font-mono">
        <span class="text-slate-400">Carga Core</span>
        <span id="kpiCoreLoad" class="block font-bold text-emerald-400">10.4%</span>
      </div>
    </div>
  </section>

  <!-- MAIN VIEWPORT: RADIAL TOPOLOGY CANVAS + HUD -->
  <main class="relative flex-1 bg-[#02050c] overflow-hidden min-h-[550px]">
    <!-- Scanline and radar sweep visual flair -->
    <div class="scanline-overlay"></div>
    <div class="radar-sweep-beam"></div>

    <!-- Canvas for high performance radial node-link render -->
    <canvas id="topologyCanvas" class="w-full h-full block relative z-10"></canvas>

    <!-- FLOATING COMPACT WAR ROOM / SOAR HUD (FUTURISTIC CSIRT INTERFACE) -->
    <div id="cyberAttackHud" class="absolute top-3 right-3 w-[345px] cyber-glass rounded-xl p-3 z-30 transition-all duration-300 border border-cyan-500/40 shadow-[0_0_35px_rgba(0,240,255,0.15)]">
      <!-- HUD Header -->
      <div class="flex items-center justify-between border-b border-cyan-900/60 pb-2 mb-2">
        <div class="flex items-center gap-2">
          <div class="relative flex items-center justify-center w-7 h-7 rounded bg-rose-950/80 border border-rose-500 text-rose-400 font-cyber font-bold text-[10px] glow-crimson">
            <span class="animate-ping absolute inline-flex h-full w-full rounded bg-rose-400 opacity-40"></span>
            SOC
          </div>
          <div>
            <h2 class="text-xs font-cyber font-bold text-white flex items-center gap-1.5">
              <span>CSIRT CONSOLE • NEXUS-M&S</span>
            </h2>
            <div class="flex items-center gap-1">
              <span id="hudBadgeStatus" class="inline-block text-[9px] font-mono font-bold px-1.5 py-0.2 rounded bg-emerald-950 text-emerald-400 border border-emerald-500/50">OPERACIONAL NOMINAL</span>
            </div>
          </div>
        </div>

        <!-- Position & Window Controls -->
        <div class="flex items-center gap-1 font-mono">
          <button id="btnDockLeft" class="px-1.5 py-0.5 rounded bg-[#091524] hover:bg-[#122842] border border-cyan-900/50 text-slate-300 text-[10px] cursor-pointer" title="Acoplar à Esquerda">◧ Esq</button>
          <button id="btnDockRight" class="px-1.5 py-0.5 rounded bg-[#091524] hover:bg-[#122842] border border-cyan-900/50 text-slate-300 text-[10px] cursor-pointer" title="Acoplar à Direita">◨ Dir</button>
          <button id="btnToggleMinimize" class="px-1.5 py-0.5 rounded bg-[#091524] hover:bg-[#122842] border border-cyan-900/50 text-slate-300 text-[10px] cursor-pointer" title="Minimizar / Expandir">_ Min</button>
          <button id="btnCloseHud" class="text-slate-400 hover:text-white px-1.5 py-0.5 rounded hover:bg-slate-800 text-xs font-bold cursor-pointer" title="Ocultar Painel">✕</button>
        </div>
      </div>

      <!-- Collapsible Body -->
      <div id="hudBodyContent" class="space-y-2">
        <!-- Attack Vector Selector -->
        <div class="bg-[#02050c]/90 p-2 rounded border border-cyan-900/50">
          <label class="block text-[10px] font-mono text-cyan-400 mb-1 font-bold flex items-center justify-between uppercase tracking-wider">
            <span>Matriz de Ameaça Cibernética:</span>
            <span class="text-[9px] text-slate-400 font-cyber">4 VETORES</span>
          </label>
          <select id="selectAttackVector" class="w-full bg-[#07111f] border border-cyan-800/80 text-rose-300 font-mono text-[10px] rounded px-2 py-1.5 focus:outline-none focus:border-cyan-400 cursor-pointer">
            <option value="ddos_syn">⚡ [VETOR 01] DDoS SYN Flood (9.8G na WAN02 & UPA Norte)</option>
            <option value="ransomware">☣️ [VETOR 02] Ransomware & Propagação Lateral (SMTT & SEPLOG)</option>
            <option value="bgp_hijack">🌐 [VETOR 03] Sequestro BGP / Rota Maliciosa (Core RTR-PE)</option>
            <option value="blackout">💥 [VETOR 04] Blackout Massivo Multi-Vetor (Core + 4 Polos)</option>
          </select>
        </div>

        <!-- Action Control Buttons -->
        <div class="grid grid-cols-2 gap-1.5">
          <button id="btnTriggerAttack" class="col-span-2 cursor-pointer active:scale-95 select-none bg-gradient-to-r from-rose-700 via-red-600 to-rose-700 hover:from-rose-600 hover:to-red-500 hover:brightness-110 text-white font-cyber font-bold py-2 px-2.5 rounded text-[11px] shadow-lg transition-all flex items-center justify-center gap-1.5 border border-rose-400/50">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
            1. INJETAR AMEAÇA SELECIONADA
          </button>

          <button id="btnTriggerMitigation" class="col-span-2 cursor-pointer active:scale-95 select-none bg-gradient-to-r from-cyan-500 via-emerald-500 to-cyan-500 hover:brightness-110 text-slate-950 font-cyber font-black py-2 px-2.5 rounded text-[11px] shadow-lg transition-all flex items-center justify-center gap-1.5 border border-cyan-300 glow-cyan">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
            2. EXECUTAR SOAR & GERAR RELATÓRIO
          </button>

          <button id="btnOpenReportModal" class="col-span-2 cursor-pointer active:scale-95 select-none bg-gradient-to-r from-amber-600 to-yellow-500 hover:brightness-110 text-slate-950 font-mono font-bold py-1.5 px-2 rounded text-[10px] shadow-md transition-all flex items-center justify-center gap-1 border border-amber-300">
            📋 Relatório Executivo Pós-Incidente (RCA)
          </button>

          <button id="btnAutoDemoMode" class="cursor-pointer active:scale-95 select-none bg-gradient-to-r from-indigo-700 to-purple-700 hover:brightness-110 text-white font-mono font-bold py-1.5 px-2 rounded text-[10px] shadow-md transition-all flex items-center justify-center gap-1 border border-indigo-400/50">
            🎬 Execução Automática
          </button>

          <button id="btnResetSimulation" class="cursor-pointer active:scale-95 select-none bg-[#0a1626] hover:bg-[#142c4c] hover:brightness-110 border border-cyan-900/60 text-slate-200 font-mono font-bold py-1.5 px-2 rounded text-[10px] shadow-md transition-all flex items-center justify-center gap-1">
            🔄 Resetar Matriz
          </button>
        </div>

        <!-- Telemetry Summary -->
        <div class="bg-[#02050c]/90 p-2 rounded border border-cyan-950 text-[11px] font-mono flex items-center justify-between">
          <div>
            <span class="text-slate-500 block text-[9px] uppercase tracking-wider">Vetor Ativo / Alvo</span>
            <span id="incidentTargetInfo" class="text-slate-200 font-bold">Nenhum Incidente</span>
          </div>
          <div class="text-right">
            <span class="text-slate-500 block text-[9px] uppercase tracking-wider">Tempo SOAR (MTTR)</span>
            <span id="soarResponseTime" class="text-emerald-400 font-bold">0.0s</span>
          </div>
        </div>

        <!-- Live Terminal Log -->
        <div class="bg-[#020409] border border-cyan-950 rounded p-2 h-24 overflow-y-auto font-mono text-[10px]" id="socTerminalConsole">
          <div id="socTerminalLogs" class="space-y-1 text-slate-300 leading-tight">
            <div class="text-slate-500">[CSIRT] Motor SOAR em prontidão. Telemetria Core BDR operacional.</div>
          </div>
        </div>

        <!-- Sound & HUD Footer -->
        <div class="flex items-center justify-between pt-1 border-t border-slate-800 text-[10px] font-mono">
          <button id="btnSoundToggle" class="text-slate-400 hover:text-white flex items-center gap-1 cursor-pointer">
            🔊 Áudio Tático: <strong id="soundStateText" class="text-emerald-400">ON</strong>
          </button>
          <span class="text-slate-500 text-[9px]">ISO 27035 / NIST SP 800-61</span>
        </div>
      </div>
    </div>

    <!-- SIDE DRAWER: NODE TELEMETRY INSPECTION -->
    <div id="nodeDrawer" class="absolute top-0 right-0 h-full w-80 cyber-glass border-l border-cyan-500/40 p-4 transform translate-x-full transition-transform duration-300 z-20 overflow-y-auto">
      <div class="flex items-center justify-between border-b border-cyan-900/60 pb-3 mb-3">
        <div>
          <span id="drawerBadge" class="text-[10px] font-mono font-bold px-2 py-0.5 rounded bg-cyan-950 text-cyan-300 border border-cyan-500/40">UNIDADE ESCOLAR</span>
          <h3 id="drawerTitle" class="text-base font-cyber font-bold text-white mt-1">EMEF Orlando Santos</h3>
        </div>
        <button id="btnCloseDrawer" class="text-slate-400 hover:text-white text-lg font-bold p-1">✕</button>
      </div>

      <div class="space-y-3 font-sans text-xs">
        <div class="cyber-glass p-2.5 rounded border border-cyan-900/50">
          <span class="text-slate-400 text-[11px] font-mono uppercase block mb-1">Status Operacional</span>
          <div id="drawerStatusText" class="text-emerald-400 font-bold font-mono text-sm flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
            100% ONLINE (IKEv2 Ativo)
          </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div class="cyber-glass p-2.5 rounded border border-cyan-900/50">
            <span class="text-slate-400 text-[10px] font-mono uppercase block">Endereço IP</span>
            <span id="drawerIp" class="text-xs font-bold text-slate-200 font-mono">10.94.10.15</span>
          </div>
          <div class="cyber-glass p-2.5 rounded border border-cyan-900/50">
            <span class="text-slate-400 text-[10px] font-mono uppercase block">Concentrador</span>
            <span id="drawerConc" class="text-xs font-bold text-cyan-400 font-mono">UPA NORTE</span>
          </div>
        </div>

        <div class="cyber-glass p-2.5 rounded border border-cyan-900/50">
          <span class="text-slate-400 text-[10px] font-mono uppercase block">Latência / RTT</span>
          <div id="drawerLatency" class="text-sm font-bold text-cyan-300 font-mono mt-0.5">3.2 ms</div>
          <span class="text-[10px] text-slate-400 font-mono">Perda: 0.0% (Jitter: 0.2ms)</span>
        </div>

        <div class="cyber-glass p-2.5 rounded border border-cyan-900/50">
          <span class="text-slate-400 text-[10px] font-mono uppercase block mb-1">Equipamentos no Local</span>
          <div class="flex items-center justify-between text-[11px] mb-1">
            <span class="text-slate-400">Firewall CPE:</span>
            <span class="font-mono text-cyan-300 font-semibold">FortiGate 40F</span>
          </div>
          <div class="flex items-center justify-between text-[11px] mb-1">
            <span class="text-slate-400">Switch PoE:</span>
            <span class="font-mono text-slate-200">FortiSwitch 108F-PoE</span>
          </div>
          <div class="flex items-center justify-between text-[11px]">
            <span class="text-slate-400">Access Points:</span>
            <span class="font-mono text-emerald-400">4x FortiAP 231F</span>
          </div>
        </div>

        <div class="cyber-glass p-3 rounded border border-cyan-900/50">
          <span class="font-mono font-semibold text-slate-300 uppercase text-[10px] block mb-2">Triggers Zabbix 7.0 Ativos</span>
          <div class="space-y-1.5 font-mono text-[10px]">
            <div class="flex items-center justify-between text-slate-300">
              <span>VPN Tunnel Status</span>
              <span class="text-emerald-400 font-bold">UP (1)</span>
            </div>
            <div class="flex items-center justify-between text-slate-300">
              <span>ICMP Ping Latency</span>
              <span class="text-cyan-400 font-bold">3.2ms (OK)</span>
            </div>
            <div class="flex items-center justify-between text-slate-300">
              <span>BGP Route Prefix</span>
              <span class="text-emerald-400 font-bold">ESTABLISHED</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- FULL MATRIX / GRID VIEW (OVERLAY) -->
    <div id="fullGridView" class="absolute inset-0 bg-[#02050c]/98 backdrop-blur-xl z-20 hidden p-6 overflow-y-auto">
      <div class="flex items-center justify-between border-b border-cyan-900/60 pb-3 mb-4">
        <div>
          <h2 class="text-lg font-cyber font-bold text-white flex items-center gap-2">
            <span>GRADE MATRIZ DE CONECTIVIDADE • 94 UNIDADES ESCOLARES</span>
          </h2>
          <p class="text-xs text-slate-400 font-mono mt-0.5">Visão consolidada por concentrador regional (UPA Norte, SMTT, SEPLOG, UPA Sul)</p>
        </div>
        <button id="btnCloseGrid" class="bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-mono font-bold px-3 py-1.5 rounded text-xs transition cursor-pointer">
          Voltar à Topologia Radial
        </button>
      </div>
      <div id="gridRegionsContainer" class="space-y-6"></div>
    </div>
  </main>

  <!-- BOTTOM OPERATIONAL STATUS & CONCENTRATOR FOOTER -->
  <footer class="bg-[#050b18] border-t border-cyan-900/40 px-4 py-2.5 flex flex-wrap items-center justify-between gap-4 text-xs relative z-30 font-mono">
    <div class="flex items-center space-x-6">
      <div>
        <span class="text-slate-400 block text-[10px] uppercase">Concentrador Ativo</span>
        <span class="text-cyan-400 font-bold">CORE CENTRAL • 4 CONCENTRADORES</span>
      </div>
      <div class="border-l border-slate-800 pl-4">
        <span class="text-slate-400 block text-[10px] uppercase">Download Agregado</span>
        <span id="footerDlAggr" class="text-emerald-400 font-bold">948.8 Mbps</span>
      </div>
      <div class="border-l border-slate-800 pl-4">
        <span class="text-slate-400 block text-[10px] uppercase">Upload Agregado</span>
        <span id="footerUlAggr" class="text-cyan-400 font-bold">416.5 Mbps</span>
      </div>
      <div class="border-l border-slate-800 pl-4">
        <span class="text-slate-400 block text-[10px] uppercase">Latência Média</span>
        <span class="text-emerald-400 font-bold">5.6 ms</span>
      </div>
    </div>

    <!-- Active Alarms Bar -->
    <div class="flex-1 max-w-xl mx-4 cyber-glass px-3 py-1.5 rounded border border-cyan-900/50 flex items-center justify-between">
      <div class="flex items-center space-x-2">
        <span id="alertStatusDot" class="w-2 h-2 rounded-full bg-emerald-400 shadow-[0_0_8px_#00ff9d]"></span>
        <span class="font-bold text-amber-400 uppercase tracking-wide text-[10px]">ALERTAS FORTINET / ZABBIX</span>
      </div>
      <div id="alertMessageText" class="text-[11px] text-slate-300 truncate max-w-sm">
        Nenhum alarme crítico pendente. 94/94 túneis VPN operando normalmente.
      </div>
    </div>

    <div class="flex items-center space-x-3 text-[11px] text-slate-400">
      <span>Zabbix 7.0 LTS</span>
      <span class="text-slate-600">|</span>
      <span>Grafana 11.2</span>
      <span class="text-slate-600">|</span>
      <span class="text-emerald-400">SOAR Ativo</span>
    </div>
  </footer>

  <!-- ZABBIX CONFIG MODAL -->
  <div id="zabbixModal" class="fixed inset-0 bg-black/80 backdrop-blur-md flex items-center justify-center z-50 hidden p-4">
    <div class="cyber-glass rounded-xl max-w-2xl w-full p-5 border border-cyan-500/50 shadow-2xl">
      <div class="flex items-center justify-between border-b border-cyan-900/60 pb-3 mb-4">
        <div class="flex items-center space-x-2">
          <span class="w-3 h-3 rounded-full bg-cyan-400"></span>
          <h2 class="text-base font-cyber font-bold text-white">INTEGRAÇÃO ZABBIX 7.0 & GRAFANA</h2>
        </div>
        <button id="btnCloseZabbixModal" class="text-slate-400 hover:text-white font-bold p-1">✕</button>
      </div>

      <div class="space-y-3 text-xs font-sans">
        <p class="text-slate-300">
          Este dashboard consome dados em tempo real da API JSON-RPC do Zabbix Server 7.0 e do Grafana através dos seguintes itens de telemetria:
        </p>
        <div class="bg-[#02050c] p-3 rounded border border-cyan-950 font-mono text-[11px] space-y-1 text-slate-300">
          <div>• Status VPN IPsec: <code class="text-cyan-400 font-bold">fortinet.ipsec.tunnel.status["{#TUNNEL_NAME}"]</code></div>
          <div>• Latência ICMP: <code class="text-cyan-400 font-bold">icmppingsec</code> (RTT em ms)</div>
          <div>• Perda de Pacote: <code class="text-cyan-400 font-bold">icmppingloss</code> (%)</div>
          <div>• Tráfego de Interface: <code class="text-cyan-400 font-bold">net.if.in[ifHCInOctets.*]</code> e <code class="text-cyan-400 font-bold">net.if.out[ifHCOutOctets.*]</code></div>
        </div>
      </div>

      <div class="mt-5 pt-3 border-t border-cyan-900/60 flex justify-end">
        <button id="btnDismissZabbix" class="bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-mono font-bold px-4 py-1.5 rounded text-xs transition">
          Fechar
        </button>
      </div>
    </div>
  </div>

  <!-- EXECUTIVE POST-INCIDENT REPORT MODAL (OFFICIAL MUNICIPAL RCA FOR ALTA GESTÃO) -->
  <div id="executiveReportModal" class="fixed inset-0 bg-black/85 backdrop-blur-md flex items-center justify-center z-50 hidden p-3 overflow-y-auto">
    <div class="bg-white text-slate-900 rounded-xl max-w-4xl w-full p-6 shadow-2xl border border-slate-300 my-auto text-sm font-sans relative">

      <!-- Action buttons at modal header (no-print) -->
      <div class="flex items-center justify-between border-b border-slate-200 pb-3 mb-4 no-print">
        <div class="flex items-center gap-2">
          <span class="inline-block px-2.5 py-0.5 rounded bg-emerald-100 text-emerald-800 font-mono font-bold text-xs border border-emerald-300">
            INCIDENTE MITIGADO COM SUCESSO
          </span>
          <span class="text-xs text-slate-500 font-mono">CONFORME NIST SP 800-61 Rev. 2</span>
        </div>
        <div class="flex items-center gap-2">
          <button id="btnPrintExecutiveReport" class="cursor-pointer active:scale-95 bg-blue-600 hover:bg-blue-700 text-white font-bold px-3 py-1.5 rounded text-xs transition flex items-center gap-1.5 shadow-sm">
            🖨️ Imprimir / Salvar PDF
          </button>
          <button id="btnCloseExecutiveReport" class="cursor-pointer text-slate-400 hover:text-slate-700 px-2 py-1 rounded text-base font-bold">
            ✕
          </button>
        </div>
      </div>

      <!-- OFFICIAL MUNICIPAL HEADER -->
      <div class="border-b-2 border-slate-800 pb-4 mb-4 flex items-center justify-between">
        <div class="flex items-center gap-4">
          <div class="w-14 h-14 rounded-full bg-slate-900 text-cyan-400 flex items-center justify-center font-cyber font-black text-xs border-2 border-amber-500 shadow-md">
            NEXUS-M&S
          </div>
          <div>
            <div class="text-[11px] font-bold text-slate-600 uppercase tracking-widest">REPÚBLICA FEDERATIVA DO BRASIL • ESTADO DO PIAUÍ</div>
            <h1 class="text-lg font-black text-slate-900 tracking-tight">NEXUS-M&S // CENTRO DE OPERAÇÕES DE REDE & SOC</h1>
            <div class="text-xs font-semibold text-slate-700">SECRETARIA MUNICIPAL DE EDUCAÇÃO (NEXUS) • DIVISÃO DE TECNOLOGIA DA INFORMAÇÃO</div>
          </div>
        </div>

        <div class="text-right font-mono text-xs">
          <div class="font-bold text-slate-800">PROTOCOLO CSIRT / NOC</div>
          <div id="repTicketId" class="text-blue-600 font-black text-sm">INC-2026-NEXUS-8821</div>
          <div id="repTimestamp" class="text-slate-500 text-[11px]">06/11/2026 12:00:00</div>
        </div>
      </div>

      <!-- REPORT TITLE BAR -->
      <div class="bg-slate-100 p-2.5 rounded border border-slate-300 mb-4 flex items-center justify-between">
        <div>
          <span class="text-[10px] font-bold font-mono text-slate-500 uppercase tracking-wider block">Documento Oficial de Auditoria</span>
          <h2 class="text-sm font-bold text-slate-900">RELATÓRIO PÓS-INCIDENTE DE SEGURANÇA DA INFORMAÇÃO & ANÁLISE DE CAUSA RAIZ (RCA)</h2>
        </div>
        <div class="text-right">
          <span class="text-[10px] font-mono font-bold text-slate-500 block">CLASSIFICAÇÃO</span>
          <span class="text-xs font-mono font-bold text-amber-700 bg-amber-100 px-2 py-0.5 rounded border border-amber-300">USO INSTITUCIONAL RESTRITO</span>
        </div>
      </div>

      <!-- EXECUTIVE SUMMARY METRICS CARDS -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3 mb-4">
        <div class="bg-slate-50 border border-slate-200 p-2.5 rounded">
          <span class="text-[10px] font-mono text-slate-500 uppercase block">Tempo de Resposta (MTTR)</span>
          <div id="repMttrTime" class="text-base font-black text-emerald-600 font-mono">14.2 segundos</div>
          <span class="text-[10px] text-slate-500">Playbook SOAR Automatizado</span>
        </div>
        <div class="bg-slate-50 border border-slate-200 p-2.5 rounded">
          <span class="text-[10px] font-mono text-slate-500 uppercase block">Impacto na Operação</span>
          <div class="text-base font-black text-blue-600 font-mono">ZERO DOWNTIME</div>
          <span class="text-[10px] text-slate-500">94 Escolas 100% Preservadas</span>
        </div>
        <div class="bg-slate-50 border border-slate-200 p-2.5 rounded">
          <span class="text-[10px] font-mono text-slate-500 uppercase block">Vazamento de Dados</span>
          <div class="text-base font-black text-emerald-600 font-mono">0 REGISTROS</div>
          <span class="text-[10px] text-slate-500">LGPD / Sigilo Integral</span>
        </div>
        <div class="bg-slate-50 border border-slate-200 p-2.5 rounded">
          <span class="text-[10px] font-mono text-slate-500 uppercase block">Prejuízo Evitado (Est.)</span>
          <div class="text-base font-black text-emerald-700 font-mono">R$ 185.000,00</div>
          <span class="text-[10px] text-slate-500">Horas-aula e sistemas salvos</span>
        </div>
      </div>

      <!-- EXECUTIVE INCIDENT SYNOPSIS -->
      <div class="mb-4">
        <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-1 flex items-center gap-1.5">
          <span>1. Resumo Executivo para a Alta Gestão (Prefeito e Secretários)</span>
        </h3>
        <p id="repExecutiveSummary" class="text-xs text-slate-700 leading-relaxed bg-slate-50 p-3 rounded border border-slate-200 text-justify">
          Durante a rotina de monitoramento operacional do NOC/SOC da NEXUS-M&S Operations, os sistemas automáticos de detecção identificaram uma anomalia severa de tráfego volumétrico. O motor de automação SOAR acionou os playbooks de resposta imediata, isolando a ameaça nos firewalls de borda e restabelecendo o fluxo legítimo das 94 escolas municipais sem interrupção dos serviços públicos.
        </p>
      </div>

      <!-- FORENSIC TIMELINE TABLE -->
      <div class="mb-5">
        <h3 class="text-xs font-bold text-slate-800 uppercase tracking-wider mb-1 flex items-center gap-1.5">
          <span>2. Cronologia Forense da Ação Técnica (Linha do Tempo)</span>
        </h3>
        <table class="w-full text-left text-xs border border-slate-200 rounded overflow-hidden">
          <thead class="bg-slate-100 text-[10px] font-bold text-slate-600 uppercase border-b border-slate-200 font-mono">
            <tr>
              <th class="p-2 w-20">Fase</th>
              <th class="p-2 w-24">Tempo</th>
              <th class="p-2">Ação Técnica Executada (Playbook SOAR)</th>
              <th class="p-2 w-28">Status</th>
            </tr>
          </thead>
          <tbody id="repTimelineBody" class="divide-y divide-slate-200 font-mono text-[11px]"></tbody>
        </table>
      </div>

      <!-- CONCLUSION & SIGNATURES -->
      <div class="pt-3 border-t border-slate-200 flex flex-col md:flex-row items-center justify-between gap-4 text-xs">
        <div class="text-[10px] text-slate-500 leading-normal max-w-md">
          <strong>PARECER TÉCNICO CONCLUSIVO:</strong> A arquitetura de defesa cibernética e monitoramento da NEXUS / NEXUS operou em perfeita aderência aos padrões de resiliência e resposta a incidentes (NIST / CIS Controls).
        </div>
        <div class="text-center min-w-[240px]">
          <div class="border-b border-slate-400 pb-1 text-[11px] font-bold text-slate-800">
            COORDENADORIA DE TECNOLOGIA DA INFORMAÇÃO & NOC
          </div>
          <div class="text-[9px] text-slate-500 uppercase mt-0.5">
            NEXUS-M&S // CENTRO DE OPERAÇÕES DE REDE & SOC
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    // -------------------------------------------------------------
    // DATA MODEL: Topology Nodes & Concentrators
    // -------------------------------------------------------------
    const CONCENTRATORS = [
      { id: 'norte', name: 'UPA NORTE', count: 14, ip: '10.94.10.1', angle: 145, distance: 310, color: '#00f0ff' },
      { id: 'smtt', name: 'SMTT', count: 11, ip: '10.94.20.1', angle: 215, distance: 290, color: '#00f0ff' },
      { id: 'seplog', name: 'SEPLOG', count: 19, ip: '10.94.30.1', angle: 35, distance: 340, color: '#00f0ff' },
      { id: 'sul', name: 'UPA SUL', count: 50, ip: '10.94.40.1', angle: 325, distance: 360, color: '#00f0ff' }
    ];

    const CORE_DEVICES = [
      { id: 'sw_cor', name: 'SW-L3-COR-NEXUS', role: 'Switch Core L3', ip: '10.0.0.1', xOffset: -90, yOffset: -180 },
      { id: 'rtr_pe', name: 'RTR-PE-NEXUS-01', role: 'Roteador BGP / PE', ip: '10.0.0.254', xOffset: 30, yOffset: -180 },
      { id: 'gpon', name: 'Rede GPON', role: 'Malha Óptica Dedicada (569 Mbps)', ip: '10.254.0.1', xOffset: -160, yOffset: -80 },
      { id: 'link_bkt', name: 'LINK 2 - WAN01-BKT', role: 'Port1 Redundante BKT', ip: '187.19.20.1', xOffset: 120, yOffset: -150 }
    ];

    const SCHOOL_NAMES = {
      norte: [
        'EMEF Orlando Santos', 'EMEF Horácio Fontes', 'EMEF Vicente Olívio Brivio', 'EMEF Elaine Avelino',
        'EMEF CAIC', 'EMEF Maria da Glória', 'EMEF Dom Tarcísio', 'EMEF Sta Rita',
        'EMEF José Conrado', 'EMEF Augusto Severino', 'EMEF Mirocles S. Ramos', 'EMEF Monseñor Aniceto',
        'EMEF Prof. Zuleida', 'EMEF Maria Silveira'
      ],
      smtt: [
        'EMEF Nunes Mendonça', 'EMEF Aloísio Marques', 'EMEF Pres. Juscelino Kubitschek', 'EMEF Benjamim Alves',
        'EMEF CCFT/ICA', 'EMEF José Airton', 'EMEF José Resende', 'EMEF Min. Mário',
        'EMEF Almirante Tamandaré', 'EMEF Prof. João Oliveira', 'EMEF Almerinda Neri'
      ],
      seplog: [
        'EMEF Manoel Bonfim', 'EMEF Tancredo Neves', 'EMEF Quintina Diniz', 'EMEF Letícia Loli',
        'EMEF Thétis Nunes', 'EMEF Ágape', 'EMEF Santa Rita', 'EMEF Dr. Fernando Bua',
        'EMEF Costa Melo', 'EMEF João Teles', 'EMEF Carvalho Neto', 'EMEF Ana Luiza Mesquita',
        'EMEF Rachel Cortes', 'EMEF Dom Luciano', 'EMEF Papa João Paulo', 'EMEF Florentino Menezes',
        'EMEF Gov. Valadares', 'EMEF Arthur Bispo', 'EMEF Michele de Jesus'
      ],
      sul: [
        'EMEF Rachel Cortes Sul', 'EMEF Carvalho Neto II', 'EMEF João Teles II', 'EMEF Ana Luiza Mesquita II',
        'EMEF Papa João Paulo II', 'EMEF Dom José Brandão', 'EMEF Valter Cardoso', 'EMEF Laonte Gama',
        'EMEF Arício Fortes', 'EMEF José Carlos', 'EMEF Alceu Amoroso', 'EMEF Maria da Glória II',
        'EMEF Amadeu Amorim', 'EMEF Florentino Menezes II', 'EMEF José de Souza', 'EMEF Jessé Trindade',
        'EMEF Arthur Bispo II', 'EMEF Almirante Tamandaré II', 'EMEF Ângelo Mota', 'EMEF Antônio Vieira',
        'EMEF Minervina Marçal', 'EMEF João Prado', 'EMEF Almerinda Neri II', 'EMEF Janira Ferraz',
        'EMEF Elias Alves', 'EMEF Tarcísio Freire', 'EMEF Olavo Bilac', 'EMEF Santos Dumont',
        'EMEF Rui Barbosa', 'EMEF Tiradentes', 'EMEF Castro Alves', 'EMEF Gonçalves Dias',
        'EMEF Anísio Teixeira', 'EMEF Darcy Ribeiro', 'EMEF Paulo Freire', 'EMEF Cecília Meireles',
        'EMEF Monteiro Lobato', 'EMEF Carlos Drummond', 'EMEF Clarice Lispector', 'EMEF Graciliano Ramos',
        'EMEF Guimarães Rosa', 'EMEF Machado de Assis', 'EMEF Lima Barreto', 'EMEF Manuel Bandeira',
        'EMEF Mário de Andrade', 'EMEF Oswald de Andrade', 'EMEF Raul Pompéia', 'EMEF Cruz e Sousa',
        'EMEF Olavo Bilac II', 'EMEF Álvares de Azevedo'
      ]
    };

    let schools = [];
    let schoolIdCounter = 1;

    Object.keys(SCHOOL_NAMES).forEach(concId => {
      const conc = CONCENTRATORS.find(c => c.id === concId);
      SCHOOL_NAMES[concId].forEach((name, idx) => {
        schools.push({
          id: `sch_${schoolIdCounter++}`,
          name: name,
          concId: concId,
          concName: conc.name,
          ip: `10.94.${concId === 'norte' ? 10 : concId === 'smtt' ? 20 : concId === 'seplog' ? 30 : 40}.${idx + 10}`,
          status: 'online',
          latency: (2.5 + Math.random() * 3).toFixed(1),
          jitter: (0.1 + Math.random() * 0.4).toFixed(1),
          loss: '0.0',
          bandwidthDown: (10 + Math.random() * 20).toFixed(1),
          bandwidthUp: (3 + Math.random() * 8).toFixed(1),
          apCount: 4,
          cpe: 'FortiGate 40F',
          switch: 'FortiSwitch 108F-PoE'
        });
      });
    });

    // -------------------------------------------------------------
    // AUDIO SYNTHESIZER (Tactical Sound FX via Web Audio API)
    // -------------------------------------------------------------
    let soundEnabled = true;
    let audioCtx = null;

    function getAudioContext() {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
      return audioCtx;
    }

    const SoundFX = {
      playClick() {
        if (!soundEnabled) return;
        try {
          const ctx = getAudioContext();
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(800, ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(1400, ctx.currentTime + 0.04);
          gain.gain.setValueAtTime(0.08, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.04);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.05);
        } catch(e) {}
      },
      playAlert() {
        if (!soundEnabled) return;
        try {
          const ctx = getAudioContext();
          const now = ctx.currentTime;
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(440, now);
          osc.frequency.linearRampToValueAtTime(880, now + 0.15);
          osc.frequency.linearRampToValueAtTime(440, now + 0.3);
          gain.gain.setValueAtTime(0.12, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(now + 0.35);
        } catch(e) {}
      },
      playSuccess() {
        if (!soundEnabled) return;
        try {
          const ctx = getAudioContext();
          const now = ctx.currentTime;
          [523.25, 659.25, 783.99, 1046.50].forEach((freq, i) => {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, now + i * 0.08);
            gain.gain.setValueAtTime(0.09, now + i * 0.08);
            gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.25);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(now + i * 0.08);
            osc.stop(now + i * 0.08 + 0.25);
          });
        } catch(e) {}
      }
    };

    // -------------------------------------------------------------
    // CYBER ATTACK SCENARIOS & SOAR PLAYBOOKS MATRIX
    // -------------------------------------------------------------
    let currentScenarioKey = 'ddos_syn';

    const ATTACK_SCENARIOS = {
      ddos_syn: {
        id: 'ddos_syn',
        name: 'Ataque DDoS Volumétrico SYN Flood (9.8 Gbps)',
        targetInfo: 'WAN02-RIMA & UPA NORTE',
        targetSub: 'Vetor: TCP SYN Flood massivo originado de 14.800 IPs botnet',
        focusRegion: 'norte',
        targetSchools: ['EMEF Orlando Santos', 'EMEF Horácio Fontes', 'EMEF Vicente Olívio Brivio', 'EMEF Elaine Avelino', 'EMEF CAIC', 'EMEF Dom Tarcísio'],
        link1Rx: '9840.4',
        link1Tx: '4920.0',
        coreTraffic: '10480.0',
        link2Rx: '67.3',
        link2Tx: '40.5',
        mttr: '14.2 segundos',
        attackLogs: [
          { text: 'DETECÇÃO: Alerta Volumétrico Crítico no Link 1 (WAN02-RIMA: 9.8 Gbps)', type: 'danger' },
          { text: 'Zabbix Trigger: DISASTER - TCP SYN Flood contra Gateway UPA Norte', type: 'danger' },
          { text: 'Saturação de tabela de estados: 6 Unidades com perda de pacotes e flapping', type: 'danger' }
        ],
        soarSteps: [
          { text: '[1/4] Ativação BGP Flowspec no RTR-PE-NEXUS-01 para descarte de SYN malicioso', delay: 800 },
          { text: '[2/4] Desvio do tráfego limpo para o Scrubbing Center perimetral FortiGate', delay: 1600 },
          { text: '[3/4] Redirecionamento dinâmico via SD-WAN do tráfego escolar para LINK 2: WAN01-BKT', delay: 2400 },
          { text: '[4/4] Forçando re-keying acelerado IKEv2 Phase 2 em todos os firewalls CPE', delay: 3200 }
        ],
        reportSummary: 'Foi detectado um ataque de negação de serviço volumétrico (DDoS SYN Flood) de 9.8 Gbps direcionado ao link principal WAN02-RIMA e ao Concentrador UPA Norte. O playbook de resposta automatizada SOAR foi ativado instantaneamente, injetando regras BGP Flowspec e ativando mitigação perimetral no FortiGate. O tráfego das escolas foi mantido 100% íntegro com zero interrupção dos serviços pedagógicos e administrativos.',
        timelineRows: [
          { phase: 'Detecção', time: 'T+0.2s', action: 'Gatilho de anomalia volumétrica ativado pelo Zabbix e NetFlow v9', res: 'Alerta Crítico' },
          { phase: 'Contenção', time: 'T+1.8s', action: 'Injeção de rota BGP Flowspec /24 para descarte de pacotes SYN maliciosos', res: '9.8G Bloqueado' },
          { phase: 'Desvio SD-WAN', time: 'T+4.5s', action: 'Roteamento dinâmico do tráfego legítimo para o link redundante WAN01-BKT', res: 'Tráfego Isolado' },
          { phase: 'Restauração', time: 'T+14.2s', action: 'Re-keying dos túneis IPsec e normalização total da UPA Norte', res: '100% Normalizado' }
        ]
      },
      ransomware: {
        id: 'ransomware',
        name: 'Tentativa de Infiltração Ransomware & Propagação Lateral',
        targetInfo: 'CONCENTRADOR SMTT & SEPLOG',
        targetSub: 'Vetor: Exploração de SMBv1/v2 e varredura lateral RPC portas 445/135',
        focusRegion: 'smtt',
        targetSchools: ['EMEF Benjamim Alves', 'EMEF CCFT/ICA', 'EMEF José Airton', 'EMEF Nunes Mendonça', 'EMEF Aloísio Marques'],
        link1Rx: '1240.0',
        link1Tx: '890.5',
        coreTraffic: '2130.0',
        link2Rx: '180.2',
        link2Tx: '95.0',
        mttr: '11.8 segundos',
        attackLogs: [
          { text: 'DETECÇÃO: Tempestade de conexões SMB/RPC anômalas no concentrador SMTT', type: 'danger' },
          { text: 'FortiGate IPS: Assinatura Ransomware.WannaCry/Lockbit.Lateral.Movement', type: 'danger' },
          { text: 'Tentativa de sequestro de sessão em 5 escolas do polo SMTT/SEPLOG', type: 'danger' }
        ],
        soarSteps: [
          { text: '[1/4] Microsegmentação de emergência: Isolamento da VLAN de gerência e SMB (445)', delay: 700 },
          { text: '[2/4] Revogação de tokens de autenticação Kerberos/LDAP nos hosts suspeitos', delay: 1500 },
          { text: '[3/4] Quarentena automatizada dos IPs de origem no FortiSwitch Core via 802.1X', delay: 2300 },
          { text: '[4/4] Verificação de integridade dos backups e liberação de túneis limpos', delay: 3000 }
        ],
        reportSummary: 'O sistema de prevenção contra intrusão (IPS) e os agentes de segurança identificaram varreduras anômalas compatíveis com tentativa de movimentação lateral de ransomware via protocolo SMB/RPC. A automação SOAR executou a microsegmentação instantânea das VLANs afetadas, isolando os endpoints comprometidos em quarentena sem afetar os bancos de dados ou servidores centrais da Prefeitura.',
        timelineRows: [
          { phase: 'Detecção', time: 'T+0.3s', action: 'Assinatura comportamental de movimentação lateral bloqueada pelo IPS', res: 'Assinatura Ativa' },
          { phase: 'Isolamento', time: 'T+1.5s', action: 'Microsegmentação de VLAN e bloqueio de portas SMB/RPC (135, 445)', res: 'VLAN Isolada' },
          { phase: 'Quarentena', time: 'T+3.2s', action: 'Bloqueio MAC/IP via 802.1X nos switches gerenciados FortiSwitch', res: 'Hosts em Quarentena' },
          { phase: 'Validação', time: 'T+11.8s', action: 'Auditoria de integridade dos dados e restabelecimento dos túneis', res: 'Zero Dados Afetados' }
        ]
      },
      bgp_hijack: {
        id: 'bgp_hijack',
        name: 'Sequestro de Rota BGP / DNS Cache Poisoning',
        targetInfo: 'RTR-PE-NEXUS-01 & MALHA GPON',
        targetSub: 'Vetor: Rota ilegítima forjada por AS externo tentando desviar tráfego Core',
        focusRegion: 'core',
        targetSchools: ['EMEF Benjamim Alves', 'EMEF CCFT/ICA', 'EMEF Quintina Diniz', 'EMEF Letícia Loli', 'EMEF Thétis Nunes'],
        link1Rx: '320.0',
        link1Tx: '120.0',
        coreTraffic: '440.0',
        link2Rx: '410.0',
        link2Tx: '210.0',
        mttr: '14.5 segundos',
        attackLogs: [
          { text: 'Desvio de rota externa detectado: RTT disparou de 1.8ms para 310ms (Man-in-the-Middle)', type: 'danger' },
          { text: 'Instabilidade de túneis VPN por perda de convergência na malha metropolitana', type: 'danger' },
          { text: 'Zabbix Trigger: DISASTER - BGP Peer State Changed & Route Flapping', type: 'danger' }
        ],
        soarSteps: [
          { text: '[1/4] Validação RPKI (ROA) ativada: Rejeição imediata de anúncios de rota sem assinatura criptográfica', delay: 700 },
          { text: '[2/4] Purga das tabelas FIB/RIB do RTR-PE-NEXUS-01: Expurgo da rota maliciosa', delay: 1500 },
          { text: '[3/4] Reancoragem BGP via peering seguro no PTT/IX.br com aplicação de BGP Community protegida', delay: 2300 },
          { text: '[4/4] Convergência de rota legítima restabelecida e latência normalizada para 1.8 ms', delay: 3100 }
        ],
        reportSummary: 'Identificou-se um anúncio de prefixo de rede não autorizado (BGP Hijacking) na internet pública com intenção de desviar tráfego metropolitano do Core da Prefeitura. A governança do SOAR ativou validação criptográfica RPKI e descartou as rotas não autenticadas no roteador RTR-PE-NEXUS-01. O tráfego foi reancorado via rota de alta confiabilidade em 14.5 segundos, frustrando integralmente a tentativa de interceptação.',
        timelineRows: [
          { phase: 'Detecção', time: 'T+0.4s', action: 'Telemetria de latência Zabbix aponta salto anômalo de 1.8ms para 310ms', res: 'Alerta Rota BGP' },
          { phase: 'Filtragem', time: 'T+2.0s', action: 'Validação RPKI (Route Origin Authorization) descartando rota fraudulenta', res: 'Prefixo Rejeitado' },
          { phase: 'Reancoragem', time: 'T+5.5s', action: 'Reinjeção de rota legítima com BGP community protegida via link seguro', res: 'Rota Convergida' },
          { phase: 'Finalização', time: 'T+14.5s', action: 'Convergência metropolitana concluída com RTT estável em 1.8ms', res: 'Tráfego Seguro' }
        ]
      },
      blackout: {
        id: 'blackout',
        name: 'Blackout Massivo Multi-Vetor em Cascata',
        targetInfo: 'CORE SEDE BDR & TODOS OS 4 POLOS',
        targetSub: 'Vetor: Tempestade combinada de DDoS, saturação e falha forçada de túneis',
        focusRegion: 'all',
        targetSchools: ['EMEF Orlando Santos', 'EMEF CAIC', 'EMEF Benjamim Alves', 'EMEF Quintina Diniz', 'EMEF Rachel Cortes Sul', 'EMEF Darcy Ribeiro', 'EMEF Paulo Freire'],
        link1Rx: '9980.0',
        link1Tx: '5120.0',
        coreTraffic: '15100.0',
        link2Rx: '950.0',
        link2Tx: '620.0',
        mttr: '15.1 segundos',
        attackLogs: [
          { text: 'CRITICAL MULTI-VECTOR ATTACK: Ataque coordenado em larga escala contra toda a malha', type: 'danger' },
          { text: 'Ambos os links de borda (WAN02-RIMA e WAN01-BKT) com volumetria crítica superior a 95%', type: 'danger' },
          { text: '11 Unidades Escolares com queda simultânea de túnel IPsec em 4 regiões', type: 'danger' },
          { text: 'Zabbix Trigger: MULTIPLE DISASTERS - Ataque cibernético simultâneo em larga escala', type: 'danger' }
        ],
        soarSteps: [
          { text: '[1/4] ATIVAÇÃO DO PLANO DE DEFESA GLOBAL: Isolamento de perímetros críticos', delay: 700 },
          { text: '[2/4] Descarte perimetral coordenado de tráfego sujo por listas de reputação IP FortiGuard', delay: 1500 },
          { text: '[3/4] Rebalanceamento inteligente via SD-WAN com priorização absoluta de tráfego escolar', delay: 2300 },
          { text: '[4/4] Restauração paralela em lote de todas as 94 escolas municipais com túneis redundantes', delay: 3100 }
        ],
        reportSummary: 'A infraestrutura municipal foi alvo de um ataque massivo e coordenado em múltiplos vetores, combinando saturação volumétrica de borda com tempestades de pacotes direcionadas aos 4 concentradores regionais. O playbook de emergência do SOAR assumiu o gerenciamento integrado de toda a malha metropolitana, aplicando contenção simultânea nos firewalls e restabelecendo 100% dos serviços em 15.1 segundos com resiliência máxima.',
        timelineRows: [
          { phase: 'Alerta Global', time: 'T+0.2s', action: 'Disparo de alarmes de saturação e queda em múltiplos concentradores', res: 'Estado de Defesa' },
          { phase: 'Contenção Global', time: 'T+2.5s', action: 'Ativação do Fortinet Security Fabric e filtragem perimetral coordenada', res: 'Tráfego retido' },
          { phase: 'SD-WAN', time: 'T+6.0s', action: 'Orquestração de contingência com priorização de tráfego pedagógico e administrativo', res: 'Canais seguros' },
          { phase: 'Restabelecimento', time: 'T+15.1s', action: 'Conexão plena de 94 escolas restabelecida sem perda de dados ou registros', res: '100% Normalizado' }
        ]
      }
    };

    // -------------------------------------------------------------
    // CANVAS RENDERING ENGINE: RADIAL TOPOLOGY
    // -------------------------------------------------------------
    const canvas = document.getElementById('topologyCanvas');
    const ctx = canvas.getContext('2d');

    let canvasWidth = 0;
    let canvasHeight = 0;
    let cameraX = 0;
    let cameraY = 0;
    let zoomLevel = 1.0;
    let isDragging = false;
    let startDragX = 0;
    let startDragY = 0;
    let hoveredNode = null;
    let selectedNode = null;
    let animationFrameId = null;

    function resizeCanvas() {
      const rect = canvas.parentElement.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      canvasWidth = rect.width;
      canvasHeight = rect.height;
      canvas.width = canvasWidth * dpr;
      canvas.height = canvasHeight * dpr;
      ctx.scale(dpr, dpr);
    }

    window.addEventListener('resize', () => {
      resizeCanvas();
    });

    // Generate Layout Nodes
    function buildTopologyGraph() {
      const nodes = [];

      // Core Center Node
      const coreNode = {
        type: 'core',
        id: 'core_nexus',
        name: 'CORE NEXUS-M&S',
        sub: 'SEDE BDR',
        x: 0,
        y: 0,
        radius: 48,
        color: '#00f0ff',
        status: 'online'
      };
      nodes.push(coreNode);

      // Peripheral devices
      CORE_DEVICES.forEach(dev => {
        nodes.push({
          type: 'core_device',
          id: dev.id,
          name: dev.name,
          role: dev.role,
          x: dev.xOffset * 1.5,
          y: dev.yOffset * 1.5,
          radius: 20,
          color: dev.id.includes('link') ? '#818cf8' : dev.id.includes('sw') ? '#38bdf8' : '#2dd4bf',
          status: 'online'
        });
      });

      // 4 Regional Concentrators
      CONCENTRATORS.forEach(c => {
        const rad = (c.angle * Math.PI) / 180;
        const cx = Math.cos(rad) * c.distance;
        const cy = Math.sin(rad) * c.distance;

        const concNode = {
          type: 'concentrator',
          id: c.id,
          name: c.name,
          sub: `${c.count}/${c.count} ON`,
          count: c.count,
          x: cx,
          y: cy,
          radius: 34,
          color: c.color,
          status: 'online'
        };
        nodes.push(concNode);

        // Child schools attached to this concentrator
        const concSchools = schools.filter(s => s.concId === c.id);
        const total = concSchools.length;
        const arcSpread = total > 20 ? 1.6 : 1.2;
        const startAngle = rad - arcSpread / 2;
        const angleStep = arcSpread / (total > 1 ? total - 1 : 1);

        concSchools.forEach((sch, i) => {
          const sAngle = startAngle + i * angleStep;
          const sDist = c.distance + 110 + (i % 3) * 45;
          const sx = Math.cos(sAngle) * sDist;
          const sy = Math.sin(sAngle) * sDist;

          nodes.push({
            type: 'school',
            id: sch.id,
            name: sch.name,
            concId: c.id,
            schoolData: sch,
            x: sx,
            y: sy,
            radius: 8,
            color: '#00ff9d',
            status: sch.status
          });
        });
      });

      return nodes;
    }

    let graphNodes = buildTopologyGraph();

    // Render Loop
    let packetOffset = 0;

    function renderTopology() {
      ctx.clearRect(0, 0, canvasWidth, canvasHeight);

      ctx.save();
      ctx.translate(canvasWidth / 2 + cameraX, canvasHeight / 2 + cameraY);
      ctx.scale(zoomLevel, zoomLevel);

      // Concentric Range Rings (Radar / Military flight deck look)
      ctx.strokeStyle = 'rgba(0, 240, 255, 0.05)';
      ctx.lineWidth = 1;
      [150, 310, 480].forEach((dist, idx) => {
        ctx.beginPath();
        ctx.arc(0, 0, dist, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = 'rgba(0, 240, 255, 0.2)';
        ctx.font = '8px JetBrains Mono';
        ctx.fillText(`RAIO ESTRATÉGICO: ${(idx + 1) * 10} KM`, dist + 5, 0);
      });

      // 1. Draw Links
      const core = graphNodes.find(n => n.id === 'core_nexus');

      // Core to Core Devices
      graphNodes.filter(n => n.type === 'core_device').forEach(dev => {
        ctx.beginPath();
        ctx.moveTo(core.x, core.y);
        ctx.lineTo(dev.x, dev.y);
        ctx.strokeStyle = 'rgba(0, 240, 255, 0.25)';
        ctx.lineWidth = 1.5;
        ctx.setLineDash([4, 4]);
        ctx.stroke();
        ctx.setLineDash([]);
      });

      // Core to Concentrators
      graphNodes.filter(n => n.type === 'concentrator').forEach(conc => {
        const isAlert = conc.status === 'alert';
        const isOffline = conc.status === 'offline';

        ctx.beginPath();
        ctx.moveTo(core.x, core.y);
        ctx.lineTo(conc.x, conc.y);
        ctx.strokeStyle = isOffline ? 'rgba(255, 0, 60, 0.6)' : isAlert ? 'rgba(255, 184, 0, 0.6)' : 'rgba(0, 240, 255, 0.45)';
        ctx.lineWidth = 3;
        ctx.stroke();

        // Animated telemetry packet along trunk
        const trunkProg = ((packetOffset * 0.005) % 1);
        const px = core.x + (conc.x - core.x) * trunkProg;
        const py = core.y + (conc.y - core.y) * trunkProg;
        ctx.fillStyle = isOffline ? '#ff003c' : '#00f0ff';
        ctx.beginPath();
        ctx.arc(px, py, 3.5, 0, Math.PI * 2);
        ctx.fill();
      });

      // Concentrators to Schools
      graphNodes.filter(n => n.type === 'school').forEach(sch => {
        const conc = graphNodes.find(n => n.id === sch.concId);
        if (conc) {
          const isOff = sch.status === 'offline';
          const isWarn = sch.status === 'alert';

          ctx.beginPath();
          ctx.moveTo(conc.x, conc.y);
          ctx.lineTo(sch.x, sch.y);
          ctx.strokeStyle = isOff ? 'rgba(255, 0, 60, 0.5)' : isWarn ? 'rgba(255, 184, 0, 0.5)' : 'rgba(0, 255, 157, 0.2)';
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      });

      // 2. Draw Nodes
      graphNodes.forEach(node => {
        const isHovered = hoveredNode && hoveredNode.id === node.id;
        const isSelected = selectedNode && selectedNode.id === node.id;

        if (node.type === 'core') {
          // Core pulsing aura
          ctx.fillStyle = 'rgba(0, 240, 255, 0.08)';
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.radius + 18, 0, Math.PI * 2);
          ctx.fill();

          ctx.strokeStyle = 'rgba(0, 240, 255, 0.6)';
          ctx.lineWidth = 2;
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
          ctx.stroke();

          ctx.fillStyle = '#06162a';
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.radius - 2, 0, Math.PI * 2);
          ctx.fill();

          // Text
          ctx.fillStyle = '#00f0ff';
          ctx.font = 'bold 11px Orbitron, sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText('CORE NEXUS-M&S', node.x, node.y - 7);

          ctx.fillStyle = '#94a3b8';
          ctx.font = '8px JetBrains Mono';
          ctx.fillText('SEDE BDR', node.x, node.y + 8);
        }
        else if (node.type === 'concentrator') {
          const isOff = node.status === 'offline';
          const isWarn = node.status === 'alert';
          const mainColor = isOff ? '#ff003c' : isWarn ? '#ffb800' : '#00f0ff';

          ctx.fillStyle = isOff ? 'rgba(255, 0, 60, 0.15)' : 'rgba(0, 240, 255, 0.1)';
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.radius + 8, 0, Math.PI * 2);
          ctx.fill();

          ctx.strokeStyle = mainColor;
          ctx.lineWidth = 2.5;
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
          ctx.stroke();

          ctx.fillStyle = '#061324';
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.radius - 2, 0, Math.PI * 2);
          ctx.fill();

          ctx.fillStyle = mainColor;
          ctx.font = 'bold 10px Orbitron, sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(node.name, node.x, node.y - 5);

          ctx.fillStyle = '#94a3b8';
          ctx.font = '8px JetBrains Mono';
          ctx.fillText(node.sub, node.x, node.y + 7);
        }
        else if (node.type === 'school') {
          const isOff = node.status === 'offline';
          const isWarn = node.status === 'alert';
          const dotColor = isOff ? '#ff003c' : isWarn ? '#ffb800' : '#00ff9d';

          ctx.fillStyle = dotColor;
          ctx.beginPath();
          ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
          ctx.fill();

          if (isHovered || isSelected) {
            ctx.strokeStyle = '#ffffff';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Label on hover/select
            ctx.fillStyle = '#ffffff';
            ctx.font = '9px JetBrains Mono';
            ctx.textAlign = 'left';
            ctx.fillText(node.name, node.x + 12, node.y + 3);
          }
        }
        else if (node.type === 'core_device') {
          ctx.fillStyle = '#0c1a2e';
          ctx.strokeStyle = node.color;
          ctx.lineWidth = 1.5;
          ctx.beginPath();
          ctx.roundRect(node.x - 45, node.y - 12, 90, 24, 4);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = node.color;
          ctx.font = 'bold 8px JetBrains Mono';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(node.name, node.x, node.y);
        }
      });

      ctx.restore();

      packetOffset++;
      animationFrameId = requestAnimationFrame(renderTopology);
    }

    // -------------------------------------------------------------
    // INTERACTION HANDLERS: Pan, Zoom, Click, Inspect
    // -------------------------------------------------------------
    function getCanvasCoords(evt) {
      const rect = canvas.getBoundingClientRect();
      const cx = (evt.clientX - rect.left - (canvasWidth / 2 + cameraX)) / zoomLevel;
      const cy = (evt.clientY - rect.top - (canvasHeight / 2 + cameraY)) / zoomLevel;
      return { x: cx, y: cy };
    }

    canvas.addEventListener('mousedown', (e) => {
      isDragging = true;
      startDragX = e.clientX - cameraX;
      startDragY = e.clientY - cameraY;
    });

    window.addEventListener('mousemove', (e) => {
      if (isDragging) {
        cameraX = e.clientX - startDragX;
        cameraY = e.clientY - startDragY;
        return;
      }

      const coords = getCanvasCoords(e);
      let found = null;
      for (let n of graphNodes) {
        const dx = n.x - coords.x;
        const dy = n.y - coords.y;
        if (Math.sqrt(dx * dx + dy * dy) <= (n.radius + 4)) {
          found = n;
          break;
        }
      }
      hoveredNode = found;
      canvas.style.cursor = found ? 'pointer' : isDragging ? 'grabbing' : 'grab';
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
    });

    canvas.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.1 : 0.9;
      zoomLevel = Math.max(0.4, Math.min(2.5, zoomLevel * zoomFactor));
    }, { passive: false });

    canvas.addEventListener('click', (e) => {
      SoundFX.playClick();
      const coords = getCanvasCoords(e);
      let clicked = null;
      for (let n of graphNodes) {
        const dx = n.x - coords.x;
        const dy = n.y - coords.y;
        if (Math.sqrt(dx * dx + dy * dy) <= (n.radius + 6)) {
          clicked = n;
          break;
        }
      }

      if (clicked) {
        selectedNode = clicked;
        if (clicked.type === 'school') {
          openSchoolDrawer(clicked.schoolData);
        } else if (clicked.type === 'concentrator') {
          openConcentratorView(clicked);
        }
      }
    });

    function openSchoolDrawer(sch) {
      document.getElementById('drawerTitle').textContent = sch.name;
      document.getElementById('drawerIp').textContent = sch.ip;
      document.getElementById('drawerConc').textContent = sch.concName;
      document.getElementById('drawerLatency').textContent = `${sch.latency} ms`;

      const statusEl = document.getElementById('drawerStatusText');
      if (sch.status === 'offline') {
        statusEl.className = 'text-rose-400 font-bold font-mono text-sm flex items-center gap-2';
        statusEl.innerHTML = '<span class="w-2.5 h-2.5 rounded-full bg-rose-500 animate-ping"></span> OFFLINE (Túnel Inativo)';
      } else {
        statusEl.className = 'text-emerald-400 font-bold font-mono text-sm flex items-center gap-2';
        statusEl.innerHTML = '<span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span> 100% ONLINE (IKEv2 Ativo)';
      }

      document.getElementById('nodeDrawer').classList.remove('translate-x-full');
    }

    document.getElementById('btnCloseDrawer').addEventListener('click', () => {
      document.getElementById('nodeDrawer').classList.add('translate-x-full');
    });

    // -------------------------------------------------------------
    // SIMULATION ENGINE: Attack Ingestion & Autonomous SOAR
    // -------------------------------------------------------------
    let isAttackActive = false;
    let isMitigating = false;
    let activeSimulationTimers = [];

    function clearAllSimulationTimers() {
      activeSimulationTimers.forEach(id => clearTimeout(id));
      activeSimulationTimers = [];
    }

    function appendSocLog(msg, type = 'info') {
      const logs = document.getElementById('socTerminalLogs');
      const time = new Date().toLocaleTimeString('pt-BR');
      const row = document.createElement('div');
      if (type === 'danger') row.className = 'text-rose-400 font-bold';
      else if (type === 'action') row.className = 'text-cyan-300 font-semibold';
      else if (type === 'success') row.className = 'text-emerald-400 font-bold';
      else row.className = 'text-slate-300';
      row.innerHTML = `<span class="text-slate-500">[${time}]</span> ${msg}`;
      logs.appendChild(row);
      document.getElementById('socTerminalConsole').scrollTop = document.getElementById('socTerminalConsole').scrollHeight;
    }

    function setDefcon(level, label, alertMode = false) {
      const defconValue = document.getElementById('defconValue');
      const defconBox = document.getElementById('defconIndicator');
      if (alertMode) {
        defconBox.className = 'flex items-center gap-2 px-2.5 py-1 rounded bg-rose-950/80 border border-rose-500 text-[10px] font-mono tracking-wider transition-all duration-300 glow-crimson';
        defconValue.className = 'font-bold text-rose-400 font-cyber flex items-center gap-1.5 text-glow-crimson';
        defconValue.innerHTML = `<span class="w-2 h-2 rounded-full bg-rose-500 animate-ping"></span> ${label}`;
      } else {
        defconBox.className = 'flex items-center gap-2 px-2.5 py-1 rounded bg-slate-900/80 border border-emerald-500/40 text-[10px] font-mono tracking-wider transition-all duration-300';
        defconValue.className = 'font-bold text-emerald-400 font-cyber flex items-center gap-1.5';
        defconValue.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> ${label}`;
      }
    }

    function triggerAttack(scenarioKey) {
      clearAllSimulationTimers();
      isAttackActive = true;
      isMitigating = false;

      const scKey = scenarioKey || document.getElementById('selectAttackVector').value;
      const scenario = ATTACK_SCENARIOS[scKey] || ATTACK_SCENARIOS.ddos_syn;

      SoundFX.playAlert();
      setDefcon(2, 'DEFCON 2 • INTRUSÃO HOSTIL EM ANDAMENTO', true);

      // Telemetry update
      document.getElementById('link1Rx').textContent = scenario.link1Rx;
      document.getElementById('link1Tx').textContent = scenario.link1Tx;
      document.getElementById('kpiCoreTraffic').textContent = scenario.coreTraffic;
      document.getElementById('link2Rx').textContent = scenario.link2Rx;
      document.getElementById('link2Tx').textContent = scenario.link2Tx;

      document.getElementById('link1Latency').textContent = '248.5 ms';
      document.getElementById('link1Loss').textContent = '38.2%';
      document.getElementById('link1Loss').className = 'text-rose-400 font-bold';

      const hudBadge = document.getElementById('hudBadgeStatus');
      hudBadge.className = 'text-[9px] font-mono font-bold px-1.5 py-0.2 rounded bg-rose-950 text-rose-300 border border-rose-500 animate-pulse';
      hudBadge.textContent = 'DEFESA ATIVA: HOSTIL';

      document.getElementById('incidentTargetInfo').textContent = scenario.targetInfo;
      document.getElementById('headerLinkStatusText').textContent = `INCIDENTE CRÍTICO: ${scenario.name}`;
      document.getElementById('headerLinkStatusText').className = 'text-rose-400 font-bold';

      // Degrade target schools
      let affectedCount = 0;
      graphNodes.forEach(n => {
        if (n.type === 'school' && scenario.targetSchools.includes(n.name)) {
          n.status = 'offline';
          affectedCount++;
        }
        if (n.type === 'concentrator' && (scenario.focusRegion === n.id || scenario.focusRegion === 'all')) {
          n.status = 'alert';
        }
      });

      const onlineCount = 94 - affectedCount;
      document.getElementById('kpiOnlineCount').textContent = onlineCount;
      document.getElementById('kpiOnlineCount').className = 'text-xl font-bold font-cyber text-rose-400 text-glow-crimson';
      document.getElementById('kpiSchoolBar').style.width = `${(onlineCount / 94) * 100}%`;
      document.getElementById('kpiSchoolBar').className = 'bg-rose-500 h-full transition-all duration-500';

      document.getElementById('kpiVpnCount').textContent = onlineCount;
      document.getElementById('kpiVpnCount').className = 'text-xl font-bold font-cyber text-rose-400 text-glow-crimson';
      document.getElementById('kpiVpnBar').style.width = `${(onlineCount / 94) * 100}%`;
      document.getElementById('kpiVpnBar').className = 'bg-rose-500 h-full transition-all duration-500';

      appendSocLog(`AMEAÇA DETECTADA: ${scenario.name}`, 'danger');
      scenario.attackLogs.forEach((log, i) => {
        const tid = setTimeout(() => {
          appendSocLog(log.text, log.type);
        }, (i + 1) * 600);
        activeSimulationTimers.push(tid);
      });
    }

    function triggerMitigation(scenarioKey) {
      clearAllSimulationTimers();
      isMitigating = true;

      const scKey = scenarioKey || document.getElementById('selectAttackVector').value;
      const scenario = ATTACK_SCENARIOS[scKey] || ATTACK_SCENARIOS.ddos_syn;

      const hudBadge = document.getElementById('hudBadgeStatus');
      hudBadge.className = 'text-[9px] font-mono font-bold px-1.5 py-0.2 rounded bg-amber-950 text-amber-300 border border-amber-500 animate-pulse';
      hudBadge.textContent = 'SOAR: PLAYBOOK EM EXECUÇÃO';

      appendSocLog(`PLAYBOOK SOAR ENGILHADO: ${scenario.name}`, 'action');

      scenario.soarSteps.forEach(step => {
        const tid = setTimeout(() => {
          appendSocLog(step.text, 'action');
          SoundFX.playClick();
        }, step.delay);
        activeSimulationTimers.push(tid);
      });

      // Complete Resolution
      const finalTimer = setTimeout(() => {
        isAttackActive = false;
        isMitigating = false;

        SoundFX.playSuccess();
        setDefcon(5, 'DEFCON 5 • COND. VERDE (NOMINAL)');

        // Restore Telemetry
        document.getElementById('link1Rx').textContent = '881.5';
        document.getElementById('link1Tx').textContent = '376.0';
        document.getElementById('kpiCoreTraffic').textContent = '1048.8';
        document.getElementById('link2Rx').textContent = '67.3';
        document.getElementById('link2Tx').textContent = '40.5';

        document.getElementById('link1Latency').textContent = '1.8 ms';
        document.getElementById('link1Loss').textContent = '0.0%';
        document.getElementById('link1Loss').className = 'text-emerald-400 font-bold';

        // Restore Nodes
        graphNodes.forEach(n => {
          n.status = 'online';
        });

        document.getElementById('kpiOnlineCount').textContent = '94';
        document.getElementById('kpiOnlineCount').className = 'text-xl font-bold font-cyber text-emerald-400 text-glow-emerald';
        document.getElementById('kpiSchoolBar').style.width = '100%';
        document.getElementById('kpiSchoolBar').className = 'bg-emerald-400 h-full transition-all duration-500';

        document.getElementById('kpiVpnCount').textContent = '94';
        document.getElementById('kpiVpnCount').className = 'text-xl font-bold font-cyber text-cyan-400 text-glow-cyan';
        document.getElementById('kpiVpnBar').style.width = '100%';
        document.getElementById('kpiVpnBar').className = 'bg-cyan-400 h-full transition-all duration-500';

        hudBadge.className = 'text-[9px] font-mono font-bold px-1.5 py-0.2 rounded bg-emerald-950 text-emerald-400 border border-emerald-500/50';
        hudBadge.textContent = 'RESOLVIDO: 100% ONLINE';

        document.getElementById('incidentTargetInfo').textContent = 'Neutralizado com Sucesso';
        document.getElementById('soarResponseTime').textContent = scenario.mttr;
        document.getElementById('headerLinkStatusText').textContent = 'Links Core Nominais (WAN02 10G + WAN01 BK) • 94/94 Unidades Online';
        document.getElementById('headerLinkStatusText').className = 'text-emerald-400 font-semibold';

        appendSocLog(`INCIDENTE TOTALMENTE NEUTRALIZADO EM ${scenario.mttr}. Todas as 94 escolas operando com estabilidade.`, 'success');

        // Automatically open the Executive Report
        generateAndOpenExecutiveReport(scenario);

      }, 3800);
      activeSimulationTimers.push(finalTimer);
    }

    function resetSimulation() {
      clearAllSimulationTimers();
      isAttackActive = false;
      isMitigating = false;

      setDefcon(5, 'DEFCON 5 • COND. VERDE (NOMINAL)');

      document.getElementById('link1Rx').textContent = '881.5';
      document.getElementById('link1Tx').textContent = '376.0';
      document.getElementById('kpiCoreTraffic').textContent = '1048.8';
      document.getElementById('link2Rx').textContent = '67.3';
      document.getElementById('link2Tx').textContent = '40.5';

      document.getElementById('link1Latency').textContent = '1.8 ms';
      document.getElementById('link1Loss').textContent = '0.0%';
      document.getElementById('link1Loss').className = 'text-emerald-400 font-bold';

      graphNodes.forEach(n => {
        n.status = 'online';
      });

      document.getElementById('kpiOnlineCount').textContent = '94';
      document.getElementById('kpiOnlineCount').className = 'text-xl font-bold font-cyber text-emerald-400 text-glow-emerald';
      document.getElementById('kpiSchoolBar').style.width = '100%';
      document.getElementById('kpiSchoolBar').className = 'bg-emerald-400 h-full';

      document.getElementById('kpiVpnCount').textContent = '94';
      document.getElementById('kpiVpnCount').className = 'text-xl font-bold font-cyber text-cyan-400 text-glow-cyan';
      document.getElementById('kpiVpnBar').style.width = '100%';
      document.getElementById('kpiVpnBar').className = 'bg-cyan-400 h-full';

      const hudBadge = document.getElementById('hudBadgeStatus');
      hudBadge.className = 'text-[9px] font-mono font-bold px-1.5 py-0.2 rounded bg-emerald-950 text-emerald-400 border border-emerald-500/50';
      hudBadge.textContent = 'OPERACIONAL NOMINAL';

      document.getElementById('incidentTargetInfo').textContent = 'Nenhum Incidente';
      document.getElementById('soarResponseTime').textContent = '0.0s';
      document.getElementById('headerLinkStatusText').textContent = 'Links Core Nominais (WAN02 10G + WAN01 BK) • 94/94 Unidades Online';
      document.getElementById('headerLinkStatusText').className = 'text-emerald-400 font-semibold';

      appendSocLog('Sistema redefinido para linha de base operacional nominal.', 'info');
    }

    // -------------------------------------------------------------
    // EXECUTIVE REPORT GENERATOR (NIST SP 800-61 / ISO 27035)
    // -------------------------------------------------------------
    function generateAndOpenExecutiveReport(scenario) {
      if (!scenario) {
        const scKey = document.getElementById('selectAttackVector').value;
        scenario = ATTACK_SCENARIOS[scKey] || ATTACK_SCENARIOS.ddos_syn;
      }

      const randomTicket = `INC-2026-NEXUS-${Math.floor(1000 + Math.random() * 9000)}`;
      const nowStr = new Date().toLocaleString('pt-BR');

      document.getElementById('repTicketId').textContent = randomTicket;
      document.getElementById('repTimestamp').textContent = nowStr;
      document.getElementById('repMttrTime').textContent = scenario.mttr;
      document.getElementById('repExecutiveSummary').textContent = scenario.reportSummary;

      // Populate Timeline rows
      const tbody = document.getElementById('repTimelineBody');
      tbody.innerHTML = '';
      scenario.timelineRows.forEach(row => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50';
        tr.innerHTML = `
          <td class="p-2 font-bold text-slate-700">${row.phase}</td>
          <td class="p-2 text-slate-500">${row.time}</td>
          <td class="p-2 text-slate-800">${row.action}</td>
          <td class="p-2"><span class="px-2 py-0.5 rounded text-[10px] bg-emerald-100 text-emerald-800 font-bold">${row.res}</span></td>
        `;
        tbody.appendChild(tr);
      });

      document.getElementById('executiveReportModal').classList.remove('hidden');
    }

    // -------------------------------------------------------------
    // EVENT LISTENERS & WIDGET ATTACHMENTS
    // -------------------------------------------------------------
    document.getElementById('btnTriggerAttack').addEventListener('click', () => {
      triggerAttack();
    });

    document.getElementById('btnTriggerMitigation').addEventListener('click', () => {
      triggerMitigation();
    });

    document.getElementById('btnResetSimulation').addEventListener('click', () => {
      resetSimulation();
    });

    document.getElementById('btnOpenReportModal').addEventListener('click', () => {
      generateAndOpenExecutiveReport();
    });

    document.getElementById('btnCloseExecutiveReport').addEventListener('click', () => {
      document.getElementById('executiveReportModal').classList.add('hidden');
    });

    document.getElementById('btnPrintExecutiveReport').addEventListener('click', () => {
      window.print();
    });

    document.getElementById('selectAttackVector').addEventListener('change', (e) => {
      currentScenarioKey = e.target.value;
      const sc = ATTACK_SCENARIOS[currentScenarioKey];
      if (sc) {
        appendSocLog(`Vetor Selecionado: ${sc.name}`, 'info');
        document.getElementById('incidentTargetInfo').textContent = sc.targetInfo;
      }
    });

    document.getElementById('btnAutoDemoMode').addEventListener('click', () => {
      appendSocLog('Sequência Automatizada: Injetando ameaça em 2 segundos...', 'action');
      triggerAttack();
      const tid = setTimeout(() => {
        triggerMitigation();
      }, 5000);
      activeSimulationTimers.push(tid);
    });

    // Sound toggle
    document.getElementById('btnSoundToggle').addEventListener('click', () => {
      soundEnabled = !soundEnabled;
      document.getElementById('soundStateText').textContent = soundEnabled ? 'ON' : 'OFF';
      document.getElementById('soundStateText').className = soundEnabled ? 'text-emerald-400' : 'text-slate-500';
    });

    // HUD controls
    document.getElementById('btnOpenCyberHud').addEventListener('click', () => {
      document.getElementById('cyberAttackHud').classList.toggle('hidden');
    });

    document.getElementById('btnCloseHud').addEventListener('click', () => {
      document.getElementById('cyberAttackHud').classList.add('hidden');
    });

    document.getElementById('btnDockLeft').addEventListener('click', () => {
      const hud = document.getElementById('cyberAttackHud');
      hud.classList.remove('right-3');
      hud.classList.add('left-3');
    });

    document.getElementById('btnDockRight').addEventListener('click', () => {
      const hud = document.getElementById('cyberAttackHud');
      hud.classList.remove('left-3');
      hud.classList.add('right-3');
    });

    document.getElementById('btnToggleMinimize').addEventListener('click', () => {
      const body = document.getElementById('hudBodyContent');
      body.classList.toggle('hidden');
    });

    // Grid View Toggle
    document.getElementById('btnViewGrid').addEventListener('click', () => {
      const container = document.getElementById('gridRegionsContainer');
      container.innerHTML = '';

      CONCENTRATORS.forEach(conc => {
        const concSchools = schools.filter(s => s.concId === conc.id);
        const section = document.createElement('div');
        section.className = 'cyber-glass rounded-xl p-4 border border-cyan-900/50';
        section.innerHTML = `
          <div class="flex items-center justify-between border-b border-cyan-900/60 pb-2 mb-3">
            <h3 class="text-sm font-cyber font-bold text-cyan-400">${conc.name} (${concSchools.length} UNIDADES)</h3>
            <span class="text-xs font-mono text-emerald-400 font-bold">100% ONLINE</span>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-2">
            ${concSchools.map(s => `
              <div class="bg-[#040913] p-2 rounded border border-cyan-950 hover:border-cyan-500 text-[11px] font-mono cursor-pointer transition">
                <span class="block font-bold text-slate-200 truncate">${s.name}</span>
                <span class="text-[9px] text-slate-500">${s.ip}</span>
                <div class="flex items-center justify-between mt-1 text-[9px]">
                  <span class="text-emerald-400 font-bold">● UP</span>
                  <span class="text-cyan-400">${s.latency}ms</span>
                </div>
              </div>
            `).join('')}
          </div>
        `;
        container.appendChild(section);
      });

      document.getElementById('fullGridView').classList.remove('hidden');
    });

    document.getElementById('btnCloseGrid').addEventListener('click', () => {
      document.getElementById('fullGridView').classList.add('hidden');
    });

    document.getElementById('btnViewRadial').addEventListener('click', () => {
      document.getElementById('fullGridView').classList.add('hidden');
    });

    // Zabbix Modal
    document.getElementById('btnZabbixModal').addEventListener('click', () => {
      document.getElementById('zabbixModal').classList.remove('hidden');
    });

    document.getElementById('btnCloseZabbixModal').addEventListener('click', () => {
      document.getElementById('zabbixModal').classList.add('hidden');
    });

    document.getElementById('btnDismissZabbix').addEventListener('click', () => {
      document.getElementById('zabbixModal').classList.add('hidden');
    });

    document.getElementById('btnSimulateIssue').addEventListener('click', () => {
      triggerAttack('ddos_syn');
    });

    // Start Engine
    resizeCanvas();
    renderTopology();
  </script>
</body>
</html>
'''

target_path = r"C:\Users\Admin\.gemini\antigravity\scratch\noc-dashboard\index.html"
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated futuristic index.html successfully at:", target_path)
