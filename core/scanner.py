import nmap
import socket
from rich.console import Console
from rich.table import Table

console = Console()

def resolve_host(host):
    try:
        ip = socket.gethostbyname(host)
    except Exception:
        ip = None
    return ip

def executar_scan(host):
    scanner = nmap.PortScanner()

    ip = resolve_host(host)
    if ip:
        console.print(f"\nHost: {host} ({ip}) — ONLINE\n", style="bold cyan")
    else:
        console.print(f"\nHost: {host} — ONLINE\n", style="bold cyan")

    # Scan TCP SYN
    console.print("Iniciando scan TCP...")
    scanner.scan(host, arguments="-sS -Pn -T4")
    tcp_abertas = []
    tcp_filtradas = []
    tcp_servicos = {}

    if host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            if proto == 'tcp':
                ports = scanner[host][proto].keys()
                for port in sorted(ports):
                    estado = scanner[host][proto][port]['state']
                    servico = scanner[host][proto][port].get('name', 'desconhecido')
                    tcp_servicos[port] = servico
                    if estado == 'open':
                        tcp_abertas.append(port)
                    elif estado == 'filtered':
                        tcp_filtradas.append(port)

    # Scan UDP
    console.print("Iniciando scan UDP...")
    scanner.scan(host, arguments="-sU -Pn -T4 --top-ports 100")
    udp_abertas = []
    udp_servicos = {}

    if host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            if proto == 'udp':
                ports = scanner[host][proto].keys()
                for port in sorted(ports):
                    estado = scanner[host][proto][port]['state']
                    servico = scanner[host][proto][port].get('name', 'desconhecido')
                    udp_servicos[port] = servico
                    if estado == 'open':
                        udp_abertas.append(port)

    # Exibir resultados TCP
    if tcp_abertas:
        table_tcp = Table(title="Portas TCP Abertas")
        table_tcp.add_column("Porta", justify="right")
        table_tcp.add_column("Serviço")
        table_tcp.add_column("Observação")

        for port in tcp_abertas:
            servico = tcp_servicos.get(port, "desconhecido")
            obs = ""
            if port == 23:
                obs = "[red]Inseguro[/red]"
            elif port == 1900:
                obs = "[red]Vulnerável[/red]"
            elif port == 8080:
                obs = "(HTTP-Proxy)"
            table_tcp.add_row(str(port), servico, obs)
        console.print(table_tcp)

    # Exibir resultados UDP
    if udp_abertas:
        table_udp = Table(title="Portas UDP Abertas")
        table_udp.add_column("Porta", justify="right")
        table_udp.add_column("Serviço")
        table_udp.add_column("Observação")

        for port in udp_abertas:
            servico = udp_servicos.get(port, "desconhecido")
            obs = ""
            if port == 1900:
                obs = "[red]Vulnerável[/red]"
            table_udp.add_row(str(port), servico, obs)
        console.print(table_udp)

    # Exibir portas TCP filtradas
    if tcp_filtradas:
        lista = ", ".join(map(str, tcp_filtradas))
        console.print(f"Portas TCP Filtradas (provável firewall): {lista}", style="red")

    # Observações gerais
    observacoes = []
    if 23 in tcp_abertas:
        observacoes.append("Telnet está ativo — recomenda-se desligar ou proteger.")
    if 1900 in tcp_abertas or 1900 in udp_abertas:
        observacoes.append("UPnP exposto — pode permitir ataques remotos.")

    if observacoes:
        console.print("\nObservações:", style="magenta")
        for obs in observacoes:
            console.print(f"- {obs}")

def start_scan(host):
    executar_scan(host)
