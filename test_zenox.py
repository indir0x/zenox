#!/usr/bin/env python3
"""
Teste básico do ZENOX Framework
"""

import sys
import time
from ui_components import ZenoxUI
from scanner import AdvancedScanner

def test_ui():
    """Testa a interface do usuário"""
    print("=== TESTANDO INTERFACE ===")
    ui = ZenoxUI()
    
    # Testar mensagens
    ui.print_success("Teste de mensagem de sucesso")
    ui.print_error("Teste de mensagem de erro")
    ui.print_warning("Teste de mensagem de aviso")
    ui.print_info("Teste de mensagem informativa")
    ui.print_attack("Teste de mensagem de ataque")
    ui.print_exploit("Teste de mensagem de exploit")
    
    print("\n=== TESTANDO SEPARADOR ===")
    ui.print_separator()
    
    print("\n=== TESTANDO MOTD ===")
    ui.display_hacker_motd()
    
    return True

def test_scanner():
    """Testa o scanner básico"""
    print("\n=== TESTANDO SCANNER ===")
    scanner = AdvancedScanner()
    
    # Testar resolução de host
    ip = scanner.resolve_host("google.com")
    if ip:
        print(f"✓ Resolução de host funcionando: google.com -> {ip}")
    else:
        print("✗ Erro na resolução de host")
        return False
    
    return True

def main():
    """Função principal de teste"""
    print("ZENOX Framework - Teste de Funcionalidades\n")
    
    try:
        # Testar UI
        if not test_ui():
            print("✗ Falha no teste de UI")
            return False
        
        # Testar Scanner
        if not test_scanner():
            print("✗ Falha no teste de Scanner")
            return False
        
        print("\n" + "="*50)
        print("✓ TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("✓ ZENOX Framework está funcionando corretamente")
        print("="*50)
        
        return True
        
    except Exception as e:
        print(f"\n✗ ERRO DURANTE OS TESTES: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
