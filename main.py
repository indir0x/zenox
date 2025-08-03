from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from core.scanner import start_scan

console = Console()

def banner():
    console.print("\nZENOX - Framework de Pentest e OSINT", style="bold cyan")
    console.print("Desenvolvido para automação e inteligência ofensiva\n", style="dim")

def menu():
    table = Table(title="Menu Principal", show_lines=True)
    table.add_column("Opção", justify="center")
    table.add_column("Descrição")

    table.add_row("1", "Iniciar varredura")
    table.add_row("2", "Visualizar relatórios")
    table.add_row("3", "Configurações")
    table.add_row("0", "Sair")

    console.print(table)
    escolha = Prompt.ask("Selecione uma opção", choices=["1", "2", "3", "0"], default="1")
    return escolha

def main():
    banner()
    while True:
        escolha = menu()

        if escolha == "1":
            host = Prompt.ask("\nDigite o IP, domínio ou range para escanear (ex: 192.168.0.0/24 ou exemplo.com)")
            start_scan(host)
        elif escolha == "2":
            console.print("\n[bold yellow]Funcionalidade de visualizar relatórios ainda está em desenvolvimento.[/bold yellow]\n")
        elif escolha == "3":
            console.print("\n[bold yellow]Funcionalidade de configurações ainda está em desenvolvimento.[/bold yellow]\n")
        elif escolha == "0":
            console.print("\nSaindo do Zenox. Até logo!", style="bold red")
            break

if __name__ == "__main__":
    main()
