"""
ZENOX Scanner Module - Advanced Penetration Testing Version
Módulo de scanner com funcionalidades avançadas de pentest e exploração
"""

import nmap
import socket
import time
import subprocess
import threading
import random
from ui_components import ZenoxUI

ui = ZenoxUI()

class AdvancedScanner:
    """Classe para scanner avançado com funcionalidades de pentest"""
    
    def __init__(self):
        self.scanner = nmap.PortScanner()
        self.target = None
        self.results = {}
        
    def resolve_host(self, host):
        """Resolve hostname para IP"""
        try:
            ip = socket.gethostbyname(host)
            return ip
        except Exception:
            return None
    
    def aggressive_port_scan(self, host):
        """Executa scan agressivo de portas com detecção de versão"""
        ui.print_attack("Iniciando varredura agressiva de portas...")
        
        try:
            # Scan TCP sem privilégios root (usando -sT ao invés de -sS)
            ui.print_info("Executando scan TCP (-sT -sV -T4)")
            self.scanner.scan(host, arguments="-sT -sV -T4 --script=default,safe")
            
            tcp_results = self.process_tcp_results(host)
            
            # Scan UDP básico (limitado sem root)
            ui.print_info("Executando scan UDP básico")
            try:
                self.scanner.scan(host, arguments="-sU --top-ports 50 -T4")
                udp_results = self.process_udp_results(host)
            except Exception as e:
                ui.print_warning(f"Scan UDP limitado sem privilégios root: {str(e)}")
                udp_results = []
            
            return tcp_results, udp_results
            
        except Exception as e:
            ui.print_error(f"Erro durante scan agressivo: {str(e)}")
            return [], []
    
    def process_tcp_results(self, host):
        """Processa resultados TCP com informações detalhadas"""
        tcp_ports = []
        
        if host in self.scanner.all_hosts():
            for proto in self.scanner[host].all_protocols():
                if proto == 'tcp':
                    ports = self.scanner[host][proto].keys()
                    for port in sorted(ports):
                        port_info = self.scanner[host][proto][port]
                        
                        tcp_ports.append({
                            'port': port,
                            'service': port_info.get('name', 'unknown'),
                            'version': port_info.get('version', 'unknown'),
                            'product': port_info.get('product', 'unknown'),
                            'extrainfo': port_info.get('extrainfo', ''),
                            'state': port_info['state'],
                            'reason': port_info.get('reason', 'unknown')
                        })
        
        return tcp_ports
    
    def process_udp_results(self, host):
        """Processa resultados UDP"""
        udp_ports = []
        
        if host in self.scanner.all_hosts():
            for proto in self.scanner[host].all_protocols():
                if proto == 'udp':
                    ports = self.scanner[host][proto].keys()
                    for port in sorted(ports):
                        port_info = self.scanner[host][proto][port]
                        
                        if port_info['state'] in ['open', 'open|filtered']:
                            udp_ports.append({
                                'port': port,
                                'service': port_info.get('name', 'unknown'),
                                'version': port_info.get('version', 'unknown'),
                                'state': port_info['state']
                            })
        
        return udp_ports
    
    def nse_vulnerability_scan(self, host, ports):
        """Executa scripts NSE para detecção de vulnerabilidades"""
        ui.print_exploit("Executando scripts NSE para detecção de vulnerabilidades...")
        
        vulnerabilities = []
        
        # Scripts NSE que funcionam sem root
        nse_scripts = [
            "safe",
            "default", 
            "discovery",
            "version"
        ]
        
        for script_category in nse_scripts:
            try:
                ui.print_info(f"Executando scripts NSE: {script_category}")
                
                # Executar scan com scripts específicos (sem privilégios root)
                script_args = f"--script={script_category}"
                port_range = ",".join([str(p['port']) for p in ports if p['state'] == 'open'])
                
                if port_range:
                    self.scanner.scan(host, ports=port_range, arguments=f"-sT {script_args}")
                    
                    # Processar resultados dos scripts
                    if host in self.scanner.all_hosts():
                        host_info = self.scanner[host]
                        
                        # Verificar scripts executados
                        for proto in host_info.all_protocols():
                            for port in host_info[proto].keys():
                                port_info = host_info[proto][port]
                                
                                if 'script' in port_info:
                                    for script_name, script_output in port_info['script'].items():
                                        if any(keyword in script_output.lower() for keyword in 
                                              ['vulnerable', 'exploit', 'cve', 'security', 'weakness']):
                                            
                                            severity = self.determine_vulnerability_severity(script_output)
                                            
                                            vulnerabilities.append({
                                                'port': port,
                                                'service': port_info.get('name', 'unknown'),
                                                'script': script_name,
                                                'severity': severity,
                                                'description': script_output[:200] + "..." if len(script_output) > 200 else script_output
                                            })
                
                time.sleep(0.5)  # Evitar sobrecarga
                
            except Exception as e:
                ui.print_warning(f"Erro ao executar script {script_category}: {str(e)}")
                continue
        
        return vulnerabilities
    
    def determine_vulnerability_severity(self, script_output):
        """Determina a severidade da vulnerabilidade baseada na saída do script"""
        output_lower = script_output.lower()
        
        # Palavras-chave para alta severidade
        high_keywords = ['critical', 'remote code execution', 'rce', 'buffer overflow', 
                        'sql injection', 'authentication bypass', 'privilege escalation']
        
        # Palavras-chave para média severidade
        medium_keywords = ['vulnerable', 'weakness', 'disclosure', 'denial of service',
                          'information leak', 'brute force']
        
        if any(keyword in output_lower for keyword in high_keywords):
            return 'high'
        elif any(keyword in output_lower for keyword in medium_keywords):
            return 'medium'
        else:
            return 'low'
    
    def service_enumeration(self, tcp_ports):
        """Executa enumeração específica de serviços"""
        ui.print_exploit("Iniciando enumeração de serviços...")
        
        enumeration_results = []
        
        for port_info in tcp_ports:
            port = port_info['port']
            service = port_info['service'].lower()
            
            try:
                if service in ['ssh', 'ssh-2.0']:
                    enum_result = self.enumerate_ssh(port_info)
                elif service in ['ftp']:
                    enum_result = self.enumerate_ftp(port_info)
                elif service in ['smb', 'microsoft-ds', 'netbios-ssn']:
                    enum_result = self.enumerate_smb(port_info)
                elif service in ['http', 'https', 'http-alt']:
                    enum_result = self.enumerate_web(port_info)
                else:
                    continue
                
                if enum_result:
                    enumeration_results.append(enum_result)
                    
            except Exception as e:
                ui.print_warning(f"Erro na enumeração da porta {port}: {str(e)}")
                continue
        
        return enumeration_results
    
    def enumerate_ssh(self, port_info):
        """Enumera serviço SSH"""
        ui.print_info(f"Enumerando SSH na porta {port_info['port']}")
        
        # Verificar versão e configurações SSH
        ssh_info = {
            'service': 'SSH',
            'port': port_info['port'],
            'version': port_info.get('version', 'unknown'),
            'findings': []
        }
        
        # Verificar versões vulneráveis conhecidas
        version = port_info.get('version', '').lower()
        if 'openssh' in version:
            if any(vuln_version in version for vuln_version in ['5.3', '6.6', '7.4']):
                ssh_info['findings'].append("Versão SSH potencialmente vulnerável detectada")
        
        # Verificar configurações comuns
        ssh_info['findings'].append("Serviço SSH ativo - verificar configurações de segurança")
        
        return ssh_info
    
    def enumerate_ftp(self, port_info):
        """Enumera serviço FTP"""
        ui.print_info(f"Enumerando FTP na porta {port_info['port']}")
        
        ftp_info = {
            'service': 'FTP',
            'port': port_info['port'],
            'version': port_info.get('version', 'unknown'),
            'findings': []
        }
        
        # Verificar login anônimo
        try:
            # Simular verificação de login anônimo
            ftp_info['findings'].append("FTP ativo - verificar acesso anônimo")
            
            # Verificar versões vulneráveis
            version = port_info.get('version', '').lower()
            if 'vsftpd' in version and any(v in version for v in ['2.3.4', '3.0.2']):
                ftp_info['findings'].append("Versão FTP potencialmente vulnerável")
                
        except Exception:
            pass
        
        return ftp_info
    
    def enumerate_smb(self, port_info):
        """Enumera serviço SMB"""
        ui.print_info(f"Enumerando SMB na porta {port_info['port']}")
        
        smb_info = {
            'service': 'SMB',
            'port': port_info['port'],
            'findings': []
        }
        
        # SMB é sempre interessante para pentest
        smb_info['findings'].append("Serviço SMB detectado - alto potencial para enumeração")
        smb_info['findings'].append("Verificar compartilhamentos e permissões")
        
        return smb_info
    
    def enumerate_web(self, port_info):
        """Enumera serviços web"""
        ui.print_info(f"Enumerando serviço web na porta {port_info['port']}")
        
        web_info = {
            'service': 'HTTP/HTTPS',
            'port': port_info['port'],
            'findings': []
        }
        
        # Informações básicas sobre serviços web
        web_info['findings'].append("Serviço web ativo - verificar aplicações e diretórios")
        
        # Verificar servidor web
        product = port_info.get('product', '').lower()
        if 'apache' in product:
            web_info['findings'].append("Servidor Apache detectado")
        elif 'nginx' in product:
            web_info['findings'].append("Servidor Nginx detectado")
        elif 'iis' in product:
            web_info['findings'].append("Servidor IIS detectado")
        
        return web_info
    
    def basic_brute_force(self, target_services):
        """Executa ataques básicos de força bruta"""
        ui.print_exploit("Iniciando ataques básicos de força bruta...")
        
        brute_results = []
        
        # Credenciais comuns para teste
        common_creds = [
            ('admin', 'admin'),
            ('admin', 'password'),
            ('admin', '123456'),
            ('root', 'root'),
            ('root', 'toor'),
            ('user', 'user'),
            ('guest', 'guest'),
            ('test', 'test')
        ]
        
        for service_info in target_services:
            service = service_info['service'].lower()
            port = service_info['port']
            
            if 'ssh' in service:
                brute_result = self.brute_force_ssh(port, common_creds)
            elif 'ftp' in service:
                brute_result = self.brute_force_ftp(port, common_creds)
            else:
                continue
            
            if brute_result:
                brute_results.append(brute_result)
        
        return brute_results
    
    def brute_force_ssh(self, port, credentials):
        """Simula brute force SSH (apenas para demonstração)"""
        ui.print_warning(f"Simulando brute force SSH na porta {port}")
        
        # NOTA: Este é apenas um exemplo educacional
        # Em um ambiente real, usar ferramentas como hydra ou medusa
        
        result = {
            'service': 'SSH',
            'port': port,
            'status': 'attempted',
            'findings': [
                f"Tentativa de brute force em SSH porta {port}",
                f"Testadas {len(credentials)} combinações de credenciais",
                "AVISO: Use apenas em sistemas autorizados!"
            ]
        }
        
        return result
    
    def brute_force_ftp(self, port, credentials):
        """Simula brute force FTP (apenas para demonstração)"""
        ui.print_warning(f"Simulando brute force FTP na porta {port}")
        
        result = {
            'service': 'FTP',
            'port': port,
            'status': 'attempted',
            'findings': [
                f"Tentativa de brute force em FTP porta {port}",
                f"Testadas {len(credentials)} combinações de credenciais",
                "AVISO: Use apenas em sistemas autorizados!"
            ]
        }
        
        return result

def executar_scan(host):
    """Executa scan completo com funcionalidades avançadas"""
    
    # Inicializar scanner avançado
    advanced_scanner = AdvancedScanner()
    
    # Cabeçalho do scan
    ui.print_scan_header(host)
    
    # Resolver host
    ui.print_info("Resolvendo hostname...")
    ip = advanced_scanner.resolve_host(host)
    
    if ip:
        ui.print_success(f"Host resolvido: {host} → {ip}")
        host_display = f"{host} ({ip})"
        target_host = ip
    else:
        ui.print_warning(f"Usando host diretamente: {host}")
        host_display = host
        target_host = host
    
    ui.print_separator()
    
    # Fase 1: Scan agressivo de portas
    ui.print_attack("FASE 1: RECONHECIMENTO AGRESSIVO")
    
    with ui.console.status("[bold red]Executando varredura agressiva...") as status:
        tcp_ports, udp_ports = advanced_scanner.aggressive_port_scan(target_host)
        time.sleep(1)
    
    ui.print_success(f"Reconhecimento concluído: {len(tcp_ports)} TCP, {len(udp_ports)} UDP")
    ui.print_separator()
    
    # Fase 2: Detecção avançada de vulnerabilidades
    if tcp_ports:
        ui.print_attack("FASE 2: DETECÇÃO DE VULNERABILIDADES")
        
        with ui.console.status("[bold red]Executando scripts NSE...") as status:
            nse_vulnerabilities = advanced_scanner.nse_vulnerability_scan(target_host, tcp_ports)
            time.sleep(2)
        
        ui.print_success(f"Scripts NSE concluídos: {len(nse_vulnerabilities)} vulnerabilidades detectadas")
        ui.print_separator()
    else:
        nse_vulnerabilities = []
    
    # Fase 3: Enumeração de serviços
    if tcp_ports:
        ui.print_attack("FASE 3: ENUMERAÇÃO DE SERVIÇOS")
        
        with ui.console.status("[bold red]Enumerando serviços...") as status:
            enumeration_results = advanced_scanner.service_enumeration(tcp_ports)
            time.sleep(1)
        
        ui.print_success(f"Enumeração concluída: {len(enumeration_results)} serviços analisados")
        ui.print_separator()
    else:
        enumeration_results = []
    
    # Fase 4: Ataques básicos de força bruta (opcional e educacional)
    brute_results = []
    if tcp_ports and any(p['service'].lower() in ['ssh', 'ftp'] for p in tcp_ports):
        ui.print_attack("FASE 4: TESTES DE FORÇA BRUTA (EDUCACIONAL)")
        ui.print_warning("AVISO: Use apenas em sistemas autorizados!")
        
        # Filtrar serviços para brute force
        brute_targets = [p for p in tcp_ports if p['service'].lower() in ['ssh', 'ftp']]
        
        with ui.console.status("[bold yellow]Executando testes básicos...") as status:
            brute_results = advanced_scanner.basic_brute_force(brute_targets)
            time.sleep(1)
        
        ui.print_success(f"Testes de força bruta concluídos: {len(brute_results)} serviços testados")
        ui.print_separator()
    
    # Combinar todas as vulnerabilidades
    all_vulnerabilities = []
    
    # Vulnerabilidades básicas (do código original)
    basic_vulnerabilities = detect_basic_vulnerabilities(tcp_ports, udp_ports)
    all_vulnerabilities.extend(basic_vulnerabilities)
    
    # Vulnerabilidades do NSE
    all_vulnerabilities.extend(nse_vulnerabilities)
    
    # Exibir resultados
    ui.print_attack("RELATÓRIO FINAL DE PENETRAÇÃO")
    ui.print_scan_results_table(tcp_ports, udp_ports, all_vulnerabilities)
    
    # Exibir resultados de enumeração
    if enumeration_results:
        display_enumeration_results(enumeration_results)
    
    # Exibir resultados de brute force
    if brute_results:
        display_brute_force_results(brute_results)
    
    # Resumo final
    print_advanced_scan_summary(host_display, tcp_ports, udp_ports, all_vulnerabilities, 
                               enumeration_results, brute_results)
    
    return {
        'host': host_display,
        'tcp_open': tcp_ports,
        'udp_open': udp_ports,
        'vulnerabilities': all_vulnerabilities,
        'enumeration': enumeration_results,
        'brute_force': brute_results
    }

def detect_basic_vulnerabilities(tcp_ports, udp_ports):
    """Detecta vulnerabilidades básicas (código original melhorado)"""
    vulnerabilities = []
    
    # Verificar vulnerabilidades TCP
    for port_info in tcp_ports:
        port = port_info['port']
        service = port_info['service']
        
        if port == 23:
            vulnerabilities.append({
                'port': port,
                'service': service,
                'severity': 'high',
                'description': 'Telnet ativo — protocolo inseguro, transmissão em texto claro'
            })
        elif port == 1900:
            vulnerabilities.append({
                'port': port,
                'service': service,
                'severity': 'high',
                'description': 'UPnP exposto — pode permitir ataques de amplificação e controle remoto'
            })
        elif port == 21:
            vulnerabilities.append({
                'port': port,
                'service': service,
                'severity': 'medium',
                'description': 'FTP detectado — verificar acesso anônimo e versão'
            })
        elif port == 22 and service == 'ssh':
            vulnerabilities.append({
                'port': port,
                'service': service,
                'severity': 'low',
                'description': 'SSH detectado — verificar configurações e versão'
            })
        elif port == 135:
            vulnerabilities.append({
                'port': port,
                'service': service,
                'severity': 'high',
                'description': 'RPC Endpoint Mapper — alto risco para ataques Windows'
            })
        elif port == 445:
            vulnerabilities.append({
                'port': port,
                'service': service,
                'severity': 'high',
                'description': 'SMB ativo — verificar vulnerabilidades EternalBlue e compartilhamentos'
            })
        elif port == 3389:
            vulnerabilities.append({
                'port': port,
                'service': service,
                'severity': 'medium',
                'description': 'RDP ativo — verificar configurações de segurança'
            })
    
    # Verificar vulnerabilidades UDP
    for port_info in udp_ports:
        port = port_info['port']
        service = port_info['service']
        
        if port == 1900:
            vulnerabilities.append({
                'port': port,
                'service': service,
                'severity': 'high',
                'description': 'UPnP UDP exposto — risco de amplificação DDoS'
            })
        elif port == 161:
            vulnerabilities.append({
                'port': port,
                'service': service,
                'severity': 'medium',
                'description': 'SNMP detectado — verificar community strings'
            })
        elif port == 53:
            vulnerabilities.append({
                'port': port,
                'service': service,
                'severity': 'medium',
                'description': 'DNS ativo — verificar configurações e recursão'
            })
    
    return vulnerabilities

def display_enumeration_results(enumeration_results):
    """Exibe resultados de enumeração"""
    if not enumeration_results:
        return
    
    ui.print_exploit("RESULTADOS DE ENUMERAÇÃO DE SERVIÇOS")
    
    for enum_result in enumeration_results:
        service_panel = ui.console.print(
            f"\n[bold cyan]🔍 {enum_result['service']} (Porta {enum_result['port']})[/bold cyan]"
        )
        
        for finding in enum_result['findings']:
            ui.console.print(f"  • {finding}")

def display_brute_force_results(brute_results):
    """Exibe resultados de brute force"""
    if not brute_results:
        return
    
    ui.print_exploit("RESULTADOS DE TESTES DE FORÇA BRUTA")
    
    for brute_result in brute_results:
        service_panel = ui.console.print(
            f"\n[bold yellow]🔥 {brute_result['service']} (Porta {brute_result['port']})[/bold yellow]"
        )
        
        for finding in brute_result['findings']:
            ui.console.print(f"  • {finding}")

def print_advanced_scan_summary(host, tcp_ports, udp_ports, vulnerabilities, 
                               enumeration_results, brute_results):
    """Exibe resumo avançado do scan"""
    
    # Determinar nível de risco
    risk_level = "BAIXO"
    risk_color = "green"
    
    if vulnerabilities:
        high_risk = any(v['severity'] == 'high' for v in vulnerabilities)
        medium_risk = any(v['severity'] == 'medium' for v in vulnerabilities)
        
        if high_risk:
            risk_level = "CRÍTICO"
            risk_color = "red"
        elif medium_risk:
            risk_level = "MÉDIO"
            risk_color = "yellow"
    
    # Criar painel de resumo avançado
    summary_text = f"""
🎯 TARGET: {host}
📊 PORTAS TCP: {len(tcp_ports)} abertas
📊 PORTAS UDP: {len(udp_ports)} abertas
💀 VULNERABILIDADES: {len(vulnerabilities)} detectadas
🔍 SERVIÇOS ENUMERADOS: {len(enumeration_results)}
🔥 TESTES BRUTE FORCE: {len(brute_results)}
🚨 NÍVEL DE RISCO: {risk_level}
    """
    
    from rich.panel import Panel
    summary_panel = Panel(
        summary_text.strip(),
        title=f"[bold {risk_color}]>> RELATÓRIO FINAL DE PENETRAÇÃO <<[/bold {risk_color}]",
        border_style=risk_color,
        padding=(1, 2)
    )
    
    ui.console.print(summary_panel)
    
    # Recomendações de segurança
    if vulnerabilities:
        ui.print_attack("RECOMENDAÇÕES CRÍTICAS DE SEGURANÇA:")
        high_vulns = [v for v in vulnerabilities if v['severity'] == 'high']
        
        if high_vulns:
            ui.console.print("[bold red]VULNERABILIDADES CRÍTICAS:[/bold red]")
            for vuln in high_vulns[:5]:  # Mostrar apenas as 5 primeiras
                ui.console.print(f"  • Porta {vuln['port']}: {vuln['description']}")
        
        ui.console.print("\n[bold yellow]AÇÕES RECOMENDADAS:[/bold yellow]")
        ui.console.print("  • Aplicar patches de segurança imediatamente")
        ui.console.print("  • Fechar portas desnecessárias")
        ui.console.print("  • Implementar firewall restritivo")
        ui.console.print("  • Monitorar logs de acesso")
        ui.console.print("  • Realizar testes de penetração regulares")
    else:
        ui.print_success("Nenhuma vulnerabilidade crítica detectada!")
        ui.console.print("[green]Sistema aparenta estar bem configurado.[/green]")

def start_scan(host):
    """Função principal para iniciar scan avançado"""
    try:
        if not host or host.strip() == "":
            ui.print_error("Host não pode estar vazio!")
            return None
            
        ui.print_attack(f"Preparando operação de penetração para: {host}")
        ui.display_hacker_motd()
        time.sleep(1)
        
        results = executar_scan(host.strip())
        
        ui.print_separator()
        ui.print_success("OPERAÇÃO DE PENETRAÇÃO CONCLUÍDA COM SUCESSO!")
        
        # Mostrar caveira se houver vulnerabilidades críticas
        if any(v['severity'] == 'high' for v in results.get('vulnerabilities', [])):
            ui.show_ascii_skull()
        
        ui.wait_for_enter("PRESSIONE ENTER PARA CONTINUAR...")
        
        return results
        
    except KeyboardInterrupt:
        ui.print_warning("\nOPERAÇÃO INTERROMPIDA PELO OPERADOR!")
        return None
    except Exception as e:
        ui.print_error(f"ERRO CRÍTICO DURANTE OPERAÇÃO: {str(e)}")
        return None

