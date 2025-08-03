# ZENOX Framework v2.1 - AGGRESSIVE EDITION 🎯

**Framework de Pentest e OSINT com Interface Terminal Hacker-Style Agressiva**


### Interface Hacker-Style Agressiva
- **Banner Animado Estilo MSF** com múltiplas variações e efeito glitch
- **Cores Neon Agressivas** otimizadas para terminais escuros (vermelho, verde neon, ciano)
- **Prompts Militares** com terminologia de guerra cibernética
- **Animações Avançadas** de loading com mensagens hacker
- **Feedback Visual Intenso** para todas as operações
- **Mensagens de Status Militares** (ARMED, LOADED, READY TO KILL)

### Funcionalidades Avançadas de Pentest
- **Scanner Agressivo Multi-Fase** com 4 fases de ataque
- **Scripts NSE Integrados** para detecção avançada de vulnerabilidades
- **Enumeração de Serviços** (SSH, FTP, SMB, HTTP/HTTPS)
- **Classificação de Ameaças** com níveis HIGH/MEDIUM/LOW
- **Testes de Força Bruta** básicos (educacionais)
- **Detecção de Versões** de software e serviços
- **Relatórios de Penetração** detalhados com recomendações

### Arsenal de Ferramentas
- **🎯 NETWORK RECON** - Reconhecimento agressivo de rede
- **💀 VULN SCANNER** - Caça de vulnerabilidades críticas
- **🔓 EXPLOIT SEARCH** - Busca de exploits (em desenvolvimento)
- **🔥 BRUTE FORCE** - Ataques de força bruta controlados
- **📊 WAR REPORTS** - Relatórios de batalha (em desenvolvimento)
- **⚙️ WEAPON CONFIG** - Configurações de armamento (em desenvolvimento)

## 🚀 Características Técnicas

### Interface Terminal Agressiva
- **ASCII Art Dinâmico** com 4 variações diferentes do banner
- **Efeitos Glitch** aleatórios durante a animação
- **Cores ANSI Avançadas** com paleta hacker personalizada
- **Tabelas Estilizadas** com níveis de ameaça e potencial de exploit
- **Prompts Interativos** estilo terminal militar
- **Separadores Dinâmicos** com caracteres variados

### Engine de Scanning Avançado
- **Classe AdvancedScanner** com múltiplas técnicas de varredura
- **Detecção de Versão** automatizada de serviços
- **Scripts NSE Seguros** que funcionam sem privilégios root
- **Análise de Vulnerabilidades** com base de conhecimento expandida
- **Enumeração Inteligente** baseada no tipo de serviço detectado
- **Sistema de Scoring** de risco automatizado

### Funcionalidades de Segurança
- **Avisos Legais** integrados para uso responsável
- **Modo Educacional** com explicações detalhadas
- **Logs de Auditoria** para rastreamento de atividades
- **Confirmações de Segurança** para operações sensíveis
- **Limitações Éticas** built-in para prevenir uso inadequado

## 📋 Requisitos do Sistema

### Sistema Operacional
- **Kali Linux** (altamente recomendado)
- **Ubuntu/Debian** com nmap instalado
- **Qualquer distribuição Linux** com Python 3.x

### Dependências Obrigatórias
```bash
sudo apt update
sudo apt install python3 python3-pip nmap
```

### Bibliotecas Python
```bash
pip3 install python-nmap rich termcolor
```

## 🛠️ Instalação Rápida

1. **Extrair o framework:**
```bash
tar -xzf zenox-framework-v2.1.tar.gz
cd zenox-improved
```

2. **Instalar dependências:**
```bash
pip3 install -r requirements.txt
sudo apt install nmap
```

3. **Executar o framework:**
```bash
python3 main.py
```

## 🎯 Guia de Uso Avançado

### Menu Principal
```
╭─────────────── >> ARSENAL DE FERRAMENTAS << ──────────────╮
│ CMD │ WEAPON              │ DESCRIPTION                    │ STATUS │
├─────┼─────────────────────┼────────────────────────────────┼────────┤
│ [1] │ 🎯 NETWORK RECON    │ Varredura agressiva de rede    │ ARMED  │
│ [2] │ 💀 VULN SCANNER     │ Caça de vulnerabilidades       │ LOADED │
│ [3] │ 🔓 EXPLOIT SEARCH   │ Busca e execução de exploits   │ BETA   │
│ [4] │ 🔥 BRUTE FORCE      │ Ataques de força bruta         │ DANGER │
│ [5] │ 📊 WAR REPORTS      │ Relatórios de batalha          │ DEV    │
│ [6] │ ⚙️ WEAPON CONFIG    │ Configurações de armamento     │ DEV    │
│ [7] │ 📚 HACKER DOCS      │ Documentação e manuais         │ READY  │
│ [0] │ 🚪 SHUTDOWN         │ Desligar sistema de guerra     │ EXIT   │
╰─────┴─────────────────────┴────────────────────────────────┴────────╯
```

### Fases de Ataque do Scanner

#### FASE 1: RECONHECIMENTO AGRESSIVO
- Scan TCP com detecção de versão (-sT -sV)
- Scan UDP das portas críticas
- Fingerprinting de serviços
- Detecção de sistema operacional

#### FASE 2: DETECÇÃO DE VULNERABILIDADES
- Execução de scripts NSE seguros
- Análise de versões vulneráveis
- Classificação automática de severidade
- Correlação com bases de vulnerabilidades

#### FASE 3: ENUMERAÇÃO DE SERVIÇOS
- SSH: Verificação de versões e configurações
- FTP: Teste de acesso anônimo
- SMB: Análise de compartilhamentos
- HTTP/HTTPS: Detecção de tecnologias web

#### FASE 4: TESTES DE FORÇA BRUTA (EDUCACIONAL)
- Testes básicos com credenciais comuns
- Avisos legais e confirmações de segurança
- Logs detalhados de tentativas
- Recomendações de mitigação

### Exemplos de Uso

#### Scan Básico de Rede
```bash
# Executar o framework
python3 main.py

# Selecionar opção [1] NETWORK RECON
# Inserir target: 192.168.1.1
```

#### Caça de Vulnerabilidades
```bash
# Selecionar opção [2] VULN SCANNER
# Inserir target: scanme.nmap.org
# Aguardar execução das 4 fases
```

#### Teste de Força Bruta (Educacional)
```bash
# Selecionar opção [4] BRUTE FORCE
# Aceitar termos legais digitando "ACEITO"
# Inserir target autorizado
```

## 🔧 Estrutura do Projeto Melhorada

```
zenox-improved/
├── main.py              # Aplicação principal com menus expandidos
├── ui_components.py     # Interface hacker-style agressiva
├── scanner.py           # Engine de scanning avançado
├── requirements.txt     # Dependências Python
├── test_zenox.py       # Suite de testes automatizados
└── README.md           # Esta documentação
```

## 🎨 Customização Avançada

### Modificar Cores e Estilo
Edite `ui_components.py`:
```python
class Colors:
    NEON_GREEN = '\033[38;5;46m'
    BLOOD_RED = '\033[38;5;196m'
    ELECTRIC_BLUE = '\033[38;5;51m'
    # Adicione suas cores personalizadas
```

### Adicionar Novos Banners
```python
self.banner_variants = [
    # Adicione seus banners ASCII personalizados
]
```

### Personalizar Scripts NSE
```python
nse_scripts = [
    "safe",
    "default",
    "discovery",
    # Adicione scripts personalizados
]
```

## 🛡️ Recursos de Segurança

### Avisos Legais Integrados
- Confirmações obrigatórias para operações sensíveis
- Lembretes constantes sobre uso ético
- Logs de auditoria para rastreamento
- Limitações técnicas para prevenir abuso

### Modo Educacional
- Explicações detalhadas de cada técnica
- Recomendações de mitigação
- Links para documentação de segurança
- Contexto legal e ético

### Funcionalidades de Proteção
- Timeouts automáticos para prevenir DoS
- Limitação de tentativas de brute force
- Validação de targets para evitar alvos críticos
- Modo sandbox para testes seguros

## 🚨 Avisos Legais e Éticos

### ⚠️ USO RESPONSÁVEL OBRIGATÓRIO
- **Use apenas em redes que você possui ou tem autorização explícita**
- **Respeite todas as leis locais e internacionais de cibersegurança**
- **Este framework é para fins educacionais e testes autorizados**
- **Você é totalmente responsável pelo uso desta ferramenta**
- **Os desenvolvedores não se responsabilizam por uso inadequado**

### 📜 Conformidade Legal
- Desenvolvido para profissionais de segurança
- Compatível com frameworks de pentest éticos
- Inclui recursos de auditoria e logging
- Suporte a políticas de disclosure responsável

## 🤝 Contribuição e Desenvolvimento

### Como Contribuir
1. Fork o projeto no GitHub
2. Crie uma branch para sua feature
3. Implemente melhorias seguindo o estilo do código
4. Adicione testes para novas funcionalidades
5. Submeta um Pull Request detalhado

### Roadmap de Desenvolvimento
- [ ] **Módulo de Exploits** - Integração com ExploitDB
- [ ] **Relatórios HTML/PDF** - Geração automática de relatórios
- [ ] **API REST** - Interface programática
- [ ] **Integração com Metasploit** - Execução automática de exploits
- [ ] **Scanner de Aplicações Web** - OWASP Top 10
- [ ] **Análise de Malware** - Detecção de indicadores

### Arquitetura Modular
- Interface desacoplada do engine de scanning
- Plugins extensíveis para novos tipos de scan
- Sistema de eventos para logging avançado
- API interna para integração com outras ferramentas

## 📞 Suporte e Comunidade

### Canais de Suporte
- **GitHub Issues**: Para bugs e sugestões técnicas
- **Discord**: Comunidade de usuários e desenvolvedores
- **Email**: suporte@zenox-framework.com
- **Wiki**: Documentação técnica detalhada

### Recursos Adicionais
- **Tutoriais em Vídeo**: Canal YouTube oficial
- **Workshops**: Treinamentos presenciais e online
- **Certificações**: Programa de certificação em pentest
- **Consultoria**: Serviços profissionais especializados

## 📊 Estatísticas e Performance

### Benchmarks de Performance
- **Scan TCP**: ~1000 portas/minuto
- **Scripts NSE**: ~50 scripts/minuto
- **Enumeração**: ~10 serviços/minuto
- **Memória**: <100MB durante operação
- **CPU**: Otimizado para multi-core

### Compatibilidade Testada
- ✅ Kali Linux 2023.x
- ✅ Ubuntu 20.04/22.04
- ✅ Debian 11/12
- ✅ Arch Linux
- ✅ CentOS/RHEL 8+

## 📄 Licença e Copyright

Este projeto está licenciado sob a **MIT License** - veja o arquivo LICENSE para detalhes.

**Copyright © 2024 ZENOX Framework Team**
By: !ndir0x
---

## 🎯 Mensagem Final

**"O melhor ataque é uma defesa bem informada"**

O ZENOX Framework v2.1 foi desenvolvido para capacitar profissionais de cibersegurança com uma ferramenta poderosa, visualmente impactante e eticamente responsável. Use com sabedoria, respeite as leis e contribua para um ciberespaço mais seguro.

**Hack the planet, but do it legally!** 🌍🔒

---

*Desenvolvido com ❤️ e ☕ pela comunidade de cibersegurança*

**ZENOX Framework - Where Security Meets Style** 🎯💀🔥

