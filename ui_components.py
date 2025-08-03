"""
ZENOX UI Components - Aggressive Hacker-Style Terminal Interface
Módulo responsável por elementos visuais agressivos e animações de hacker
"""

import time
import sys
import threading
import random
import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.text import Text
from rich.align import Align
from rich.layout import Layout
from rich.live import Live
from rich.rule import Rule

console = Console()

class Colors:
    """Códigos de cores ANSI para terminal - Paleta Hacker Agressiva"""
    NEON_GREEN = '\033[38;5;46m'
    BLOOD_RED = '\033[38;5;196m'
    ELECTRIC_BLUE = '\033[38;5;51m'
    TOXIC_YELLOW = '\033[38;5;226m'
    GHOST_WHITE = '\033[38;5;15m'
    SHADOW_GRAY = '\033[38;5;240m'
    MATRIX_GREEN = '\033[38;5;40m'
    DANGER_RED = '\033[38;5;160m'
    CYBER_PURPLE = '\033[38;5;129m'
    BOLD = '\033[1m'
    BLINK = '\033[5m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

class ZenoxUI:
    """Classe principal para interface do ZENOX - Estilo Hacker Agressivo"""
    
    def __init__(self):
        self.console = Console()
        self.is_loading = False
        self.banner_variants = [
            """
███████╗███████╗███╗   ██╗ ██████╗ ██╗  ██╗
╚══███╔╝██╔════╝████╗  ██║██╔═══██╗╚██╗██╔╝
  ███╔╝ █████╗  ██╔██╗ ██║██║   ██║ ╚███╔╝ 
 ███╔╝  ██╔══╝  ██║╚██╗██║██║   ██║ ██╔██╗ 
███████╗███████╗██║ ╚████║╚██████╔╝██╔╝ ██╗
╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
            """,
            """
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
██▀▀▀▀▀ ██▀▀▀▀▀ ██▀▀▀▀██ ██▀▀▀▀██ ██▀▀▀▀██
▀▀▀██   ██▀▀▀▀▀ ██▀▀▀▀██ ██    ██  ▀▀██▀▀ 
   ██   ██▀▀▀▀▀ ██▀▀▀▀██ ██    ██   ██   
   ██   ██▀▀▀▀▀ ██    ██ ██▀▀▀▀██   ██   
▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀▀    ▀▀ ▀▀    ▀▀  ▀▀▀▀  
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """,
            """
▒███████▒▓█████  ███▄    █  ▒█████  ▒██   ██▒
▒ ▒ ▒ ▄▀░▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▒▒ █ █ ▒░
░ ▒ ▄▀▒░ ▒███   ▓██  ▀█ ██▒▒██░  ██▒░░  █   ░
  ▄▀▒   ░▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░ ░ █ █ ▒ 
▒███████▒░▒████▒▒██░   ▓██░░ ████▓▒░▒██▒ ▒██▒
░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
░░▒ ▒ ░ ▒ ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░
░ ░ ░ ░ ░   ░      ░   ░ ░ ░ ░ ░ ▒   ░    ░  
  ░ ░       ░  ░         ░     ░ ░   ░    ░  
            """,
            """
╔══════════════════════════════════════════════╗
║ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ║
║   ███     ███     ███     ███     ███   ║
║ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ║
║   ███     ███     ███     ███     ███   ║
║ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀ ║
╚══════════════════════════════════════════════╝
            """
        ]
    def clear_screen(self):
        """Limpa a tela do terminal"""
        import os
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def animated_banner(self, duration=3.0):
        """Exibe banner animado estilo Metasploit Framework"""
        colors = ['red', 'green', 'cyan', 'yellow', 'magenta', 'blue']
        
        # Limpar tela
        self.clear_screen()
        
        # Calcular número de frames
        frames = int(duration * 10)  # 10 FPS
        
        with Live(console=self.console, refresh_per_second=10) as live:
            for frame in range(frames):
                # Escolher banner e cor aleatórios
                banner_text = random.choice(self.banner_variants)
                color = random.choice(colors)
                
                # Criar texto com efeito glitch ocasional
                if frame % 7 == 0:  # Efeito glitch a cada 7 frames
                    # Adicionar caracteres aleatórios para efeito glitch
                    glitch_chars = ['▓', '▒', '░', '█', '▄', '▀', '■', '□']
                    lines = banner_text.strip().split('\n')
                    glitched_lines = []
                    
                    for line in lines:
                        if random.random() < 0.3:  # 30% chance de glitch por linha
                            # Inserir caracteres glitch aleatórios
                            pos = random.randint(0, max(0, len(line)-5))
                            glitch = random.choice(glitch_chars) * random.randint(1, 3)
                            line = line[:pos] + glitch + line[pos+len(glitch):]
                        glitched_lines.append(line)
                    
                    banner_text = '\n'.join(glitched_lines)
                
                # Criar painel com banner
                banner_panel = Panel(
                    Align.center(Text(banner_text, style=f"bold {color}")),
                    border_style=color,
                    padding=(1, 2),
                    title=f"[bold {color}]ZENOX FRAMEWORK v2.0[/bold {color}]"
                )
                
                # Adicionar informações do sistema
                subtitle = Text("PENETRATION TESTING & OSINT FRAMEWORK", style=f"bold {color}")
                description = Text(">> INITIALIZING OFFENSIVE SECURITY MODULES <<", style=f"dim {color}")
                
                # Layout completo
                layout_content = Align.center(banner_panel)
                
                live.update(layout_content)
                time.sleep(0.1)
        
        # Banner final estático
        final_banner = Panel(
            Align.center(Text(self.banner_variants[0], style="bold red")),
            border_style="red",
            padding=(1, 2),
            title="[bold red]ZENOX FRAMEWORK v2.0[/bold red]"
        )
        
        self.console.print(final_banner)
        self.console.print(Align.center(Text("PENETRATION TESTING & OSINT FRAMEWORK", style="bold cyan")))
        self.console.print(Align.center(Text(">> SISTEMA PRONTO PARA OPERAÇÕES OFENSIVAS <<", style="dim white")))
        self.console.print()
    
    def print_banner(self):
        """Exibe o banner principal do ZENOX com animação"""
        self.animated_banner()
        
        # Status do sistema
        self.print_system_status()
    
    def print_system_status(self):
        """Exibe status do sistema com estilo hacker agressivo"""
        status_table = Table(show_header=False, box=None, padding=(0, 2))
        status_table.add_column("Item", style="bold red")
        status_table.add_column("Status", style="bold green")
        
        status_table.add_row("🔥 SISTEMA", "[bold green]ONLINE[/bold green]")
        status_table.add_row("⚡ MÓDULOS", "[bold green]ARMADOS[/bold green]")
        status_table.add_row("🎯 SCANNER", "[bold green]READY TO KILL[/bold green]")
        status_table.add_row("💀 EXPLOITS", "[bold yellow]CARREGADOS[/bold yellow]")
        status_table.add_row("🔓 VULNS", "[bold red]HUNTING MODE[/bold red]")
        
        status_panel = Panel(
            status_table,
            title="[bold red]>> WEAPON SYSTEMS STATUS <<[/bold red]",
            border_style="red",
            padding=(0, 1)
        )
        
        self.console.print(status_panel)
        self.console.print()
    
    def print_menu(self):
        """Exibe menu principal estilizado com tema hacker agressivo"""
        menu_table = Table(
            title="[bold red]>> ARSENAL DE FERRAMENTAS <<[/bold red]",
            show_lines=True,
            border_style="red",
            title_style="bold red"
        )
        
        menu_table.add_column("CMD", justify="center", style="bold red", width=8)
        menu_table.add_column("WEAPON", style="bold white", width=25)
        menu_table.add_column("DESCRIPTION", style="white", width=40)
        menu_table.add_column("STATUS", justify="center", width=12)
        
        menu_table.add_row(
            "[1]", 
            "🎯 NETWORK RECON", 
            "Varredura agressiva de rede e portas",
            "[green]ARMED[/green]"
        )
        menu_table.add_row(
            "[2]", 
            "💀 VULN SCANNER", 
            "Caça de vulnerabilidades críticas",
            "[red]LOADED[/red]"
        )
        menu_table.add_row(
            "[3]", 
            "🔓 EXPLOIT SEARCH", 
            "Busca e execução de exploits",
            "[yellow]BETA[/yellow]"
        )
        menu_table.add_row(
            "[4]", 
            "🔥 BRUTE FORCE", 
            "Ataques de força bruta",
            "[red]DANGER[/red]"
        )
        menu_table.add_row(
            "[5]", 
            "📊 WAR REPORTS", 
            "Relatórios de batalha",
            "[yellow]DEV[/yellow]"
        )
        menu_table.add_row(
            "[6]", 
            "⚙️ WEAPON CONFIG", 
            "Configurações de armamento",
            "[yellow]DEV[/yellow]"
        )
        menu_table.add_row(
            "[7]", 
            "📚 HACKER DOCS", 
            "Documentação e manuais",
            "[green]READY[/green]"
        )
        menu_table.add_row(
            "[0]", 
            "🚪 SHUTDOWN", 
            "Desligar sistema de guerra",
            "[red]EXIT[/red]"
        )
        
        self.console.print(menu_table)
        self.console.print()
        
        # Adicionar mensagem de aviso
        warning_text = "⚠️  USE APENAS EM REDES AUTORIZADAS - VOCÊ É RESPONSÁVEL PELO USO ⚠️"
        warning_panel = Panel(
            Align.center(Text(warning_text, style="bold yellow")),
            border_style="yellow",
            padding=(0, 1)
        )
        self.console.print(warning_panel)
        self.console.print()
    
    def get_user_choice(self, prompt="[ZENOX]> ", valid_choices=None):
        """Obtém escolha do usuário com prompt estilizado e agressivo"""
        while True:
            try:
                # Prompt mais agressivo
                aggressive_prompt = f"[bold red]┌─[[/bold red][bold white]ZENOX[/bold white][bold red]]─[[/bold red][bold yellow]READY[/bold yellow][bold red]]"
                aggressive_prompt += f"\n└──╼ [/bold red][bold green]${prompt}[/bold green]"
                
                choice = self.console.input(aggressive_prompt).strip()
                
                if valid_choices and choice not in valid_choices:
                    self.print_error(f"COMANDO INVÁLIDO! Escolha entre: {', '.join(valid_choices)}")
                    continue
                    
                return choice
            except KeyboardInterrupt:
                self.print_warning("\n[CTRL+C] OPERAÇÃO CANCELADA PELO OPERADOR.")
                return None
    
    def print_success(self, message):
        """Exibe mensagem de sucesso com estilo hacker"""
        self.console.print(f"[bold green]✓ [SUCCESS][/bold green] {message}")
    
    def print_error(self, message):
        """Exibe mensagem de erro com estilo agressivo"""
        self.console.print(f"[bold red]✗ [ERROR][/bold red] {message}")
    
    def print_warning(self, message):
        """Exibe mensagem de aviso com estilo militar"""
        self.console.print(f"[bold yellow]⚠ [WARNING][/bold yellow] {message}")
    
    def print_info(self, message):
        """Exibe mensagem informativa com estilo cyber"""
        self.console.print(f"[bold cyan]ℹ [INFO][/bold cyan] {message}")
    
    def print_attack(self, message):
        """Exibe mensagem de ataque/operação"""
        self.console.print(f"[bold red]🎯 [ATTACK][/bold red] {message}")
    
    def print_exploit(self, message):
        """Exibe mensagem de exploit"""
        self.console.print(f"[bold magenta]💀 [EXPLOIT][/bold magenta] {message}")
    
    def hacker_typing_effect(self, text, delay=0.05):
        """Efeito de digitação estilo hacker com ruído"""
        noise_chars = ['█', '▓', '▒', '░']
        
        for i, char in enumerate(text):
            # Ocasionalmente adicionar ruído
            if random.random() < 0.1:  # 10% chance
                noise = random.choice(noise_chars)
                sys.stdout.write(noise)
                sys.stdout.flush()
                time.sleep(0.02)
                sys.stdout.write('\b')  # Backspace
                sys.stdout.flush()
            
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def show_loading(self, message="PROCESSANDO", duration=None):
        """Exibe animação de loading estilo hacker"""
        spinners = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        hacker_messages = [
            "INFILTRANDO SISTEMA...",
            "QUEBRANDO CRIPTOGRAFIA...",
            "BYPASSING FIREWALL...",
            "COLETANDO INTEL...",
            "EXECUTANDO PAYLOAD...",
            "ESCALANDO PRIVILÉGIOS..."
        ]
        
        with Progress(
            SpinnerColumn(spinner_style="red"),
            TextColumn("[bold red]{task.description}[/bold red]"),
            transient=True,
        ) as progress:
            # Alternar entre mensagens
            current_msg = message
            if message == "PROCESSANDO":
                current_msg = random.choice(hacker_messages)
                
            task = progress.add_task(description=current_msg, total=None)
            
            if duration:
                time.sleep(duration)
            else:
                # Loading infinito até ser parado externamente
                while self.is_loading:
                    time.sleep(0.1)
    
    def aggressive_progress_bar(self, total_steps, description="OPERAÇÃO EM ANDAMENTO"):
        """Exibe barra de progresso com estilo militar"""
        with Progress(
            TextColumn("[bold red]{task.description}[/bold red]"),
            BarColumn(bar_width=None, style="red", complete_style="green"),
            TaskProgressColumn(style="bold white"),
            TextColumn("[bold green]{task.completed}/{task.total}[/bold green]"),
        ) as progress:
            task = progress.add_task(description, total=total_steps)
            
            for i in range(total_steps):
                time.sleep(0.1)  # Simula trabalho
                progress.update(task, advance=1)
            
            return progress
    
    def print_scan_header(self, target):
        """Exibe cabeçalho do scan com estilo militar"""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        
        header_text = f"""
🎯 INICIANDO OPERAÇÃO DE RECONHECIMENTO
TARGET: {target}
TIMESTAMP: {timestamp}
OPERATOR: ZENOX-FRAMEWORK
MISSION: NETWORK PENETRATION TEST
        """
        
        header_panel = Panel(
            header_text.strip(),
            title="[bold red]>> OPERATION STARTED <<[/bold red]",
            border_style="red",
            padding=(1, 2)
        )
        
        self.console.print(header_panel)
        
        # Mensagem de início de ataque
        self.print_attack(f"Iniciando varredura agressiva em {target}")
        self.console.print(Rule(style="red"))
    
    def print_scan_results_table(self, tcp_ports, udp_ports, vulnerabilities):
        """Exibe resultados do scan em tabelas estilizadas com tema militar"""
        
        # Tabela de portas TCP
        if tcp_ports:
            tcp_table = Table(
                title="[bold red]🎯 PORTAS TCP COMPROMETIDAS[/bold red]",
                border_style="red"
            )
            tcp_table.add_column("PORTA", justify="center", style="bold red")
            tcp_table.add_column("SERVIÇO", style="white")
            tcp_table.add_column("STATUS", justify="center", style="bold green")
            tcp_table.add_column("THREAT LEVEL", justify="center", style="bold yellow")
            
            for port_info in tcp_ports:
                # Determinar nível de ameaça
                threat = "LOW"
                threat_color = "green"
                if port_info['port'] in [21, 23, 135, 139, 445, 1433, 3389]:
                    threat = "HIGH"
                    threat_color = "red"
                elif port_info['port'] in [22, 25, 53, 80, 443, 993, 995]:
                    threat = "MEDIUM"
                    threat_color = "yellow"
                
                tcp_table.add_row(
                    str(port_info['port']),
                    port_info['service'].upper(),
                    "[bold green]OPEN[/bold green]",
                    f"[bold {threat_color}]{threat}[/bold {threat_color}]"
                )
            
            self.console.print(tcp_table)
            self.console.print()
        
        # Tabela de portas UDP
        if udp_ports:
            udp_table = Table(
                title="[bold blue]📡 PORTAS UDP EXPOSTAS[/bold blue]",
                border_style="blue"
            )
            udp_table.add_column("PORTA", justify="center", style="bold blue")
            udp_table.add_column("SERVIÇO", style="white")
            udp_table.add_column("STATUS", justify="center", style="bold green")
            udp_table.add_column("EXPLOIT POTENTIAL", justify="center", style="bold magenta")
            
            for port_info in udp_ports:
                exploit_potential = "LOW"
                if port_info['port'] in [53, 161, 1900]:
                    exploit_potential = "HIGH"
                elif port_info['port'] in [67, 68, 123]:
                    exploit_potential = "MEDIUM"
                
                udp_table.add_row(
                    str(port_info['port']),
                    port_info['service'].upper(),
                    "[bold green]OPEN[/bold green]",
                    f"[bold magenta]{exploit_potential}[/bold magenta]"
                )
            
            self.console.print(udp_table)
            self.console.print()
        
        # Tabela de vulnerabilidades
        if vulnerabilities:
            vuln_table = Table(
                title="[bold red]💀 VULNERABILIDADES CRÍTICAS DETECTADAS[/bold red]",
                border_style="red"
            )
            vuln_table.add_column("PORTA", justify="center", style="bold red")
            vuln_table.add_column("SERVIÇO", style="white")
            vuln_table.add_column("SEVERIDADE", justify="center", style="bold red")
            vuln_table.add_column("EXPLOIT DESCRIPTION", style="white")
            
            for vuln in vulnerabilities:
                severity_color = {
                    'low': 'yellow',
                    'medium': 'orange',
                    'high': 'red'
                }.get(vuln['severity'], 'red')
                
                vuln_table.add_row(
                    str(vuln['port']),
                    vuln['service'].upper(),
                    f"[bold {severity_color}]{vuln['severity'].upper()}[/bold {severity_color}]",
                    vuln['description']
                )
            
            self.console.print(vuln_table)
            self.console.print()
            
            # Alerta de vulnerabilidades críticas
            if any(v['severity'] == 'high' for v in vulnerabilities):
                critical_alert = Panel(
                    "[bold red]⚠️  VULNERABILIDADES CRÍTICAS DETECTADAS! ⚠️[/bold red]\n"
                    "[white]Sistema altamente vulnerável a ataques remotos![/white]",
                    border_style="red",
                    padding=(1, 2)
                )
                self.console.print(critical_alert)
    
    def print_separator(self, char="═", length=80):
        """Exibe separador visual com estilo cyber"""
        separator_chars = ["═", "━", "▬", "▭", "▰"]
        char = random.choice(separator_chars)
        self.console.print(f"[dim red]{char * length}[/dim red]")
    
    def wait_for_enter(self, message="Pressione ENTER para continuar..."):
        """Aguarda o usuário pressionar ENTER com prompt militar"""
        military_message = f"[dim yellow]>> {message.upper()} <<[/dim yellow]"
        self.console.input(military_message)
    
    def start_loading(self, message="PROCESSANDO"):
        """Inicia loading em thread separada"""
        self.is_loading = True
        loading_thread = threading.Thread(target=self.show_loading, args=(message,))
        loading_thread.daemon = True
        loading_thread.start()
        return loading_thread
    
    def stop_loading(self):
        """Para o loading"""
        self.is_loading = False
    
    def display_hacker_motd(self):
        """Exibe mensagem do dia estilo hacker"""
        motd_messages = [
            "Remember: With great power comes great responsibility",
            "Only test on networks you own or have explicit permission",
            "Knowledge is power, use it wisely",
            "The best defense is understanding the offense",
            "Stay curious, stay ethical",
            "Security through obscurity is not security"
        ]
        
        motd = random.choice(motd_messages)
        motd_panel = Panel(
            f"[italic yellow]{motd}[/italic yellow]",
            title="[bold cyan]HACKER WISDOM[/bold cyan]",
            border_style="cyan",
            padding=(0, 1)
        )
        self.console.print(motd_panel)
        self.console.print()
    
    def show_ascii_skull(self):
        """Exibe caveira ASCII para vulnerabilidades críticas"""
        skull = """
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░
        ░░░░░░░░░▄▄█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▄▄░░░░░░
        ░░░░░░▄█▀▀░░░░░░░░░░░░░░░░░░░░░▀▀█▄░░░░
        ░░░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄░░
        ░░▄█▀░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▀█▄
        ░▄█▀░░░▄▄▄░░░░░░░░░░░░░░░░░░▄▄▄░░░░░▀█▄
        ▄█░░░░█▀▀▀█░░░░░░░░░░░░░░░░█▀▀▀█░░░░░░█▄
        █▀░░░░▀▀▀▀▀░░░░░░░░░░░░░░░░▀▀▀▀▀░░░░░░▀█
        █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
        █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
        █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
        █▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█
        ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
        ░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░
        ░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░
        ░░░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀░░░░
        ░░░░░░▀█▄▄░░░░░░░░░░░░░░░░░░░░░▄▄█▀░░░░░░
        ░░░░░░░░░▀▀█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▀▀░░░░░░░░░
        ░░░░░░░░░░░░░░▀▀▀▀▀▀▀▀▀▀▀▀▀▀░░░░░░░░░░░░
        """
        
        skull_panel = Panel(
            Align.center(Text(skull, style="bold red")),
            title="[bold red]CRITICAL VULNERABILITY DETECTED[/bold red]",
            border_style="red",
            padding=(1, 2)
        )
        
        self.console.print(skull_panel)

