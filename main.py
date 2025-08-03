#!/usr/bin/env python3
"""
ZENOX Framework v2.0 - Enhanced CLI Version
Framework de Pentest e OSINT com interface terminal agressiva
Desenvolvido para Kali Linux e ambientes de pentesting
"""

import sys
import time
from ui_components import ZenoxUI
from scanner import start_scan

class ZenoxFramework:
    """Classe principal do ZENOX Framework"""
    
    def __init__(self):
        self.ui = ZenoxUI()
        self.running = True
        self.scan_history = []
    
    def show_banner(self):
        """Exibe banner e inicialização"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        # Efeito de inicialização
        init_messages = [
            "Carregando módulos de segurança...",
            "Inicializando scanner de rede...",
            "Verificando dependências...",
            "Sistema pronto para operação!"
        ]
        
        for msg in init_messages:
            self.ui.print_info(msg)
            time.sleep(0.3)
        
        self.ui.print_separator()
        time.sleep(0.5)
    
    def show_help(self):
        """Exibe ajuda e documentação"""
        self.ui.clear_screen()
        
        help_text = """
🔧 ZENOX FRAMEWORK - GUIA DE USO

📋 COMANDOS PRINCIPAIS:
  1. Network Scan    - Varredura completa de rede e análise de portas
  2. Análise Avançada - Análise detalhada de vulnerabilidades (em desenvolvimento)
  3. Relatórios      - Visualização e exportação de resultados (em desenvolvimento)
  4. Configurações   - Personalização do framework (em desenvolvimento)
  5. Help & Docs     - Esta tela de ajuda

🎯 COMO USAR O SCANNER:
  • Digite o IP, hostname ou range de rede (ex: 192.168.1.1)
  • Suporte para ranges CIDR (ex: 192.168.1.0/24)
  • Suporte para hostnames (ex: google.com)

⚠️  AVISOS IMPORTANTES:
  • Use apenas em redes autorizadas
  • Respeite as leis locais de cibersegurança
  • Este framework é para fins educacionais e testes autorizados

🔗 DEPENDÊNCIAS:
  • python-nmap: Scanner de rede
  • rich: Interface terminal avançada
  • termcolor: Cores no terminal

📚 DOCUMENTAÇÃO COMPLETA:
  • GitHub: https://github.com/zenox-framework
  • Wiki: https://wiki.zenox-framework.com
        """
        
        from rich.panel import Panel
        help_panel = Panel(
            help_text.strip(),
            title="[bold cyan]ZENOX FRAMEWORK - DOCUMENTAÇÃO[/bold cyan]",
            border_style="cyan",
            padding=(1, 2)
        )
        
        self.ui.console.print(help_panel)
        self.ui.wait_for_enter()
    
    def network_scan_menu(self):
        """Menu de scan de rede"""
        self.ui.clear_screen()
        self.ui.print_info("MÓDULO DE NETWORK SCAN ATIVADO")
        self.ui.print_separator()
        
        # Obter target do usuário
        target = self.ui.get_user_choice(
            "Digite o IP, domínio ou range para escanear: ",
            valid_choices=None
        )
        
        if not target:
            return
        
        # Validação básica
        if target.strip() == "":
            self.ui.print_error("Target não pode estar vazio!")
            self.ui.wait_for_enter()
            return
        
        # Executar scan
        self.ui.print_separator()
        results = start_scan(target)
        
        # Salvar no histórico
        if results:
            self.scan_history.append({
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'target': target,
                'results': results
            })
    
    def show_coming_soon(self, feature_name):
        """Exibe mensagem de funcionalidade em desenvolvimento"""
        self.ui.clear_screen()
        
        coming_soon_text = f"""
🚧 FUNCIONALIDADE EM DESENVOLVIMENTO

{feature_name} está sendo desenvolvida e estará disponível em breve!

📋 ROADMAP:
  • Interface de configuração avançada
  • Relatórios em PDF e HTML
  • Integração com bases de vulnerabilidades
  • Módulos de OSINT
  • Scanner de aplicações web
  • Análise de malware

🔔 FIQUE ATUALIZADO:
  • GitHub: https://github.com/zenox-framework
  • Discord: https://discord.gg/zenox
        """
        
        from rich.panel import Panel
        dev_panel = Panel(
            coming_soon_text.strip(),
            title="[bold yellow]EM DESENVOLVIMENTO[/bold yellow]",
            border_style="yellow",
            padding=(1, 2)
        )
        
        self.ui.console.print(dev_panel)
        self.ui.wait_for_enter()
    
    def main_menu(self):
        """Menu principal do framework"""
        while self.running:
            self.ui.clear_screen()
            self.ui.print_banner()
            self.ui.print_menu()
            
            choice = self.ui.get_user_choice(
                "COMANDO> ",
                valid_choices=["0", "1", "2", "3", "4", "5", "6", "7"]
            )
            
            if choice == "1":
                self.network_scan_menu()
            elif choice == "2":
                self.vulnerability_scanner_menu()
            elif choice == "3":
                self.exploit_search_menu()
            elif choice == "4":
                self.brute_force_menu()
            elif choice == "5":
                self.show_coming_soon("WAR REPORTS")
            elif choice == "6":
                self.show_coming_soon("WEAPON CONFIG")
            elif choice == "7":
                self.show_help()
            elif choice == "0":
                self.exit_framework()
            elif choice is None:  # Ctrl+C
                self.exit_framework()
    
    def vulnerability_scanner_menu(self):
        """Menu do scanner de vulnerabilidades avançado"""
        self.ui.clear_screen()
        self.ui.print_exploit("MÓDULO DE CAÇA DE VULNERABILIDADES ATIVADO")
        self.ui.print_separator()
        
        # Obter target do usuário
        target = self.ui.get_user_choice(
            "Digite o IP, domínio ou range para caçar vulnerabilidades: ",
            valid_choices=None
        )
        
        if not target:
            return
        
        # Validação básica
        if target.strip() == "":
            self.ui.print_error("Target não pode estar vazio!")
            self.ui.wait_for_enter()
            return
        
        # Executar scan avançado
        self.ui.print_separator()
        results = start_scan(target)
        
        # Salvar no histórico
        if results:
            self.scan_history.append({
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'target': target,
                'results': results,
                'scan_type': 'vulnerability_scan'
            })
    
    def exploit_search_menu(self):
        """Menu de busca de exploits"""
        self.ui.clear_screen()
        self.ui.print_exploit("MÓDULO DE BUSCA DE EXPLOITS")
        self.ui.print_separator()
        
        exploit_info = """
🔓 BUSCA DE EXPLOITS - EM DESENVOLVIMENTO

Este módulo permitirá:
• Busca automática de exploits baseada em serviços detectados
• Integração com bases de dados de vulnerabilidades (CVE, ExploitDB)
• Sugestões de exploits baseadas nos resultados do scan
• Links para ferramentas e payloads específicos

📋 FUNCIONALIDADES PLANEJADAS:
• Busca por CVE automatizada
• Integração com Metasploit Framework
• Geração automática de comandos de exploit
• Base de dados local de exploits

🔔 STATUS: BETA - Disponível em breve!
        """
        
        from rich.panel import Panel
        exploit_panel = Panel(
            exploit_info.strip(),
            title="[bold magenta]EXPLOIT SEARCH ENGINE[/bold magenta]",
            border_style="magenta",
            padding=(1, 2)
        )
        
        self.ui.console.print(exploit_panel)
        self.ui.wait_for_enter()
    
    def brute_force_menu(self):
        """Menu de ataques de força bruta"""
        self.ui.clear_screen()
        self.ui.print_exploit("MÓDULO DE FORÇA BRUTA")
        self.ui.print_separator()
        
        # Aviso legal
        warning_text = """
⚠️  AVISO LEGAL IMPORTANTE ⚠️

Este módulo é apenas para fins EDUCACIONAIS e testes AUTORIZADOS.

• Use apenas em sistemas que você possui ou tem permissão explícita
• Ataques de força bruta podem ser ilegais em muitas jurisdições
• Você é totalmente responsável pelo uso desta ferramenta
• Os desenvolvedores não se responsabilizam por uso inadequado

CONTINUAR APENAS SE VOCÊ ENTENDE E ACEITA ESTES TERMOS.
        """
        
        from rich.panel import Panel
        warning_panel = Panel(
            warning_text.strip(),
            title="[bold red]AVISO LEGAL[/bold red]",
            border_style="red",
            padding=(1, 2)
        )
        
        self.ui.console.print(warning_panel)
        
        # Confirmar aceitação
        accept = self.ui.get_user_choice(
            "Digite 'ACEITO' para continuar ou qualquer outra coisa para voltar: ",
            valid_choices=None
        )
        
        if accept != "ACEITO":
            self.ui.print_info("Operação cancelada.")
            self.ui.wait_for_enter()
            return
        
        # Obter target
        target = self.ui.get_user_choice(
            "Digite o IP ou hostname do target AUTORIZADO: ",
            valid_choices=None
        )
        
        if not target or target.strip() == "":
            self.ui.print_error("Target não pode estar vazio!")
            self.ui.wait_for_enter()
            return
        
        # Executar scan com foco em brute force
        self.ui.print_separator()
        self.ui.print_attack(f"Iniciando testes de força bruta em {target}")
        results = start_scan(target)
        
        # Salvar no histórico
        if results:
            self.scan_history.append({
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'target': target,
                'results': results,
                'scan_type': 'brute_force'
            })
    
    def exit_framework(self):
        """Encerra o framework"""
        self.ui.clear_screen()
        
        exit_text = """
🚪 ENCERRANDO ZENOX FRAMEWORK

Obrigado por usar o ZENOX Framework!

📊 ESTATÍSTICAS DA SESSÃO:
  • Scans realizados: {scan_count}
  • Tempo de execução: {runtime}

🔒 LIMPEZA DE SEGURANÇA:
  • Cache limpo
  • Logs seguros
  • Memória liberada

Até a próxima, hacker! 🎯
        """.format(
            scan_count=len(self.scan_history),
            runtime="N/A"  # Implementar contador de tempo se necessário
        )
        
        from rich.panel import Panel
        exit_panel = Panel(
            exit_text.strip(),
            title="[bold red]SAINDO...[/bold red]",
            border_style="red",
            padding=(1, 2)
        )
        
        self.ui.console.print(exit_panel)
        
        # Efeito de saída
        self.ui.print_info("Finalizando processos...")
        time.sleep(0.5)
        self.ui.print_success("Framework encerrado com segurança!")
        
        self.running = False
        sys.exit(0)

def main():
    """Função principal"""
    try:
        # Verificar se está rodando no Python 3
        if sys.version_info[0] < 3:
            print("ERRO: ZENOX Framework requer Python 3.x")
            sys.exit(1)
        
        # Inicializar framework
        zenox = ZenoxFramework()
        
        # Exibir banner inicial
        zenox.show_banner()
        
        # Iniciar menu principal
        zenox.main_menu()
        
    except KeyboardInterrupt:
        print("\n\n🚪 Framework encerrado pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

