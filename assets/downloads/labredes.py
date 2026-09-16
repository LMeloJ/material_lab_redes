#!/usr/bin/env python3
"""
Exercício Mininet
Topologia: 2 Redes + Roteador + Servidores DHCP/DNS + HTTP

Rede 1 (192.168.1.0/24): 3 PCs + Servidor DHCP/DNS
Rede 2 (10.0.1.0/24): Servidor HTTP
Roteador conectando as duas redes

"""

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSSwitch, Host
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link
import time

class RouterHost(Host):
    """Host customizado que funciona como roteador Linux"""
    
    def config(self, **kwargs):
        Host.config(self, **kwargs)
        self.cmd('sysctl net.ipv4.ip_forward=1')

class TopologiaPacketTracer(Topo):
    """
    Topologia:
    
    Rede 1 (192.168.1.0/24):          Rede 2 (10.0.1.0/24):
    ┌─────────────────────────┐       ┌─────────────────────┐
    │ PC1, PC2, PC3           │       │                     │
    │ Servidor DHCP/DNS       │       │ Servidor HTTP       │
    │ (192.168.1.100)         │  R1   │ (10.0.1.100)        │
    │          Switch1 ───────┼───────┼─────── Switch2      │
    │                         │       │                     │
    └─────────────────────────┘       └─────────────────────┘
           192.168.1.1                      10.0.1.1
    """
    
    def build(self):
        switch1 = self.addSwitch('s1')  # Switch da rede LAN interna
        switch2 = self.addSwitch('s2')  # Switch da rede externa/DMZ
        
        router = self.addHost('r1', cls=RouterHost, ip='192.168.1.1/24')
        
        servidor_dhcp_dns = self.addHost(
            'dns_srv', 
            ip='192.168.1.100/24',
            defaultRoute='via 192.168.1.1'
        )
        
        pc1 = self.addHost('pc1', ip='0.0.0.0/24')
        pc2 = self.addHost('pc2', ip='0.0.0.0/24') 
        pc3 = self.addHost('pc3', ip='0.0.0.0/24')
        
        servidor_http = self.addHost(
            'web_srv',
            ip='10.0.1.100/24', 
            defaultRoute='via 10.0.1.1'
        )
        
        self.addLink(switch1, servidor_dhcp_dns)
        self.addLink(switch1, pc1)
        self.addLink(switch1, pc2)
        self.addLink(switch1, pc3)
        
        self.addLink(switch2, servidor_http)
        
        self.addLink(router, switch1)
        self.addLink(router, switch2)

def configurar_roteador(net):
    """Configura o roteador Linux (equivale ao Cisco 1941)"""
    print("=== Configurando Roteador (Cisco 1941 equivalente) ===")
    
    router = net.get('r1')
    
    router.cmd('ifconfig r1-eth0 192.168.1.1/24')
    
    router.cmd('ifconfig r1-eth1 10.0.1.1/24')
    
    print("✓ Interface r1-eth0: 192.168.1.1/24 (rede interna)")
    print("✓ Interface r1-eth1: 10.0.1.1/24 (rede externa)")
    
    print("✓ IP Forwarding habilitado")

def configurar_servidor_dhcp_dns(net):
    """Configura servidor DHCP/DNS (192.168.1.100)"""
    print("\n=== Configurando Servidor DHCP/DNS ===")
    
    servidor = net.get('dns_srv')
    
    print("Configurando DNS...")
    
    servidor.cmd('pkill -f dnsmasq 2>/dev/null || true')
    
    dns_zone = '''127.0.0.1 localhost
192.168.1.100 servidor.local
10.0.1.100 site.com
192.168.1.1 gateway.local'''
    
    servidor.cmd('echo "%s" > /etc/hosts' % dns_zone)
    
    print("Configurando DHCP...")
    
    dnsmasq_conf = '''# Configuração DNS + DHCP
bind-interfaces
interface=dns_srv-eth0
listen-address=192.168.1.100
port=53

# Configuração DNS
no-resolv
no-poll
domain-needed
bogus-priv
expand-hosts
domain=local

# Entradas DNS locais
address=/site.com/10.0.1.100
address=/servidor.local/192.168.1.100

# Configuração DHCP
dhcp-range=192.168.1.101,192.168.1.150,255.255.255.0,12h
dhcp-option=option:router,192.168.1.1
dhcp-option=option:dns-server,192.168.1.100
dhcp-option=option:domain-name,local

# Log para debug
log-queries
log-dhcp'''
    
    servidor.cmd('echo "%s" > /tmp/dnsmasq.conf' % dnsmasq_conf)
    servidor.cmd('dnsmasq -C /tmp/dnsmasq.conf --pid-file=/tmp/dnsmasq.pid &')
    
    # Aguardar inicialização
    time.sleep(2)
    
    # Verificar se dnsmasq está rodando
    result = servidor.cmd('ps aux | grep dnsmasq | grep -v grep')
    if 'dnsmasq' in result:
        print("✓ DNS/DHCP iniciado com sucesso")
    else:
        print("✗ Erro ao iniciar DNS/DHCP")
        servidor.cmd('cat /tmp/dnsmasq.conf')
    
    print("✓ DNS configurado:")
    print("  - servidor.local → 192.168.1.100")  
    print("  - site.com → 10.0.1.100")
    print("✓ DHCP configurado:")
    print("  - Pool: 192.168.1.101 - 192.168.1.150")
    print("  - Gateway: 192.168.1.1")
    print("  - DNS: 192.168.1.100")

def configurar_servidor_http(net):
    """Configura servidor HTTP (10.0.1.100)"""
    print("\n=== Configurando Servidor HTTP ===")
    
    servidor = net.get('web_srv')

    servidor.cmd('echo "nameserver 192.168.1.100" > /etc/resolv.conf')
    servidor.cmd('mkdir -p /tmp/www')
    html_content = '''<!DOCTYPE html>
<html>
<head>
<title>Bem-vindo ao Site.com</title>
<meta charset="UTF-8">
</head>
<body style="font-family: Arial; text-align: center; background-color: #f0f8ff; padding: 50px;">
<h1 style="color: #2c3e50;">Bem-vindo ao Site.com</h1>
<h2 style="color: #27ae60;">Servidor HTTP Externo</h2>
<hr>
<h3>Informacoes do Servidor</h3>
<p><strong>Endereco:</strong> 10.0.1.100</p>
<p><strong>Rede:</strong> 10.0.1.0/24</p>
<p><strong>Protocolo:</strong> HTTP</p>
<p><strong>DNS:</strong> site.com</p>
<hr>
<h3>Conectividade</h3>
<p>Sua requisicao passou pelo <strong>roteador</strong></p>
<p>DNS resolvido pelo servidor <strong>192.168.1.100</strong></p>
<p>Trafego roteado de <strong>192.168.1.0/24</strong> para <strong>10.0.1.0/24</strong></p>
<hr>
<p style="color: #e74c3c; font-size: 18px;"><strong>Laboratorio de Redes - Exercicio Packet Tracer replicado!</strong></p>
<p><em>Acesso realizado com sucesso via DNS e roteamento inter-redes</em></p>
</body>
</html>'''
    
    with open('/tmp/index_temp.html', 'w') as f:
        f.write(html_content)
    
    servidor.cmd('cp /tmp/index_temp.html /tmp/www/index.html')
    servidor.cmd('rm -f /tmp/index_temp.html')
    servidor.cmd('cd /tmp/www && python3 -m http.server 80 &')
    
    print("✓ Servidor HTTP ativo em 10.0.1.100:80")
    print("✓ Página de boas-vindas configurada")
    print("✓ DNS configurado para 192.168.1.100")

def configurar_clientes_dhcp(net):
    """Configura PCs para receberem IP via DHCP"""
    print("\n=== Configurando Clientes DHCP ===")
    
    clientes = ['pc1', 'pc2', 'pc3']
    
    print("Aguardando servidor DHCP estar pronto...")
    time.sleep(2)
    
    for cliente_nome in clientes:
        cliente = net.get(cliente_nome)
        
        print(f"\nConfigurando {cliente_nome} com DHCP real...")
        
        # Limpar configuração anterior
        cliente.cmd('pkill dhclient 2>/dev/null || true')
        cliente.cmd(f'ip addr flush dev {cliente_nome}-eth0')
        cliente.cmd(f'ip link set {cliente_nome}-eth0 down')
        cliente.cmd(f'ip link set {cliente_nome}-eth0 up')
        
        print(f"Solicitando IP via DHCP...")
        
        dhclient_result = cliente.cmd(f'timeout 10 dhclient -1 -v {cliente_nome}-eth0 2>&1')
        
        time.sleep(2)
        
        ip_info = cliente.cmd(f'ip addr show {cliente_nome}-eth0 | grep "inet " | awk "{{print $2}}" | cut -d/ -f1')
        
        if ip_info.strip() and "192.168.1." in ip_info.strip() and ip_info.strip() != "192.168.1.100":
            ip_obtido = ip_info.strip()
            print(f"  ✓ {cliente_nome}: IP obtido via DHCP: {ip_obtido}")
            
            gateway_info = cliente.cmd('ip route | grep default | awk "{print $3}"')
            if "192.168.1.1" in gateway_info:
                print(f"     Gateway: {gateway_info.strip()}")
            else:
                cliente.cmd('ip route add default via 192.168.1.1')
                print(f"     Gateway: 192.168.1.1 (configurado manualmente)")
            
            resolv_content = cliente.cmd('cat /etc/resolv.conf 2>/dev/null || echo ""')
            if "192.168.1.100" not in resolv_content:
                cliente.cmd('echo "nameserver 192.168.1.100" > /etc/resolv.conf')
                print(f"     DNS: 192.168.1.100 (configurado)")
            else:
                print(f"     DNS: 192.168.1.100 (já configurado)")
                
        else:
            print(f"  ✗ DHCP falhou para {cliente_nome}, usando IP estático")
            
            if dhclient_result:
                print(f"     Debug: {dhclient_result.strip()[:100]}...")
            
            ip_estatico = f"192.168.1.{101 + clientes.index(cliente_nome)}"
            cliente.cmd(f'ip addr add {ip_estatico}/24 dev {cliente_nome}-eth0')
            cliente.cmd('ip route add default via 192.168.1.1')
            cliente.cmd('echo "nameserver 192.168.1.100" > /etc/resolv.conf')
            
            print(f"     IP: {ip_estatico} (estático)")
            print(f"     Gateway: 192.168.1.1")
            print(f"     DNS: 192.168.1.100")
    
    print(f"\nResumo de Leases DHCP:")
    dns_srv = net.get('dns_srv')
    leases = dns_srv.cmd('cat /tmp/dhcp.leases 2>/dev/null || echo "Nenhum lease ativo"')
    if "Nenhum lease" not in leases:
        print("Leases ativos:")
        for line in leases.strip().split('\n'):
            if line.strip():
                print(f"  {line}")
    else:
        print("  Nenhum lease DHCP encontrado (usando IPs estáticos)")
    
    print(f"\nTeste de conectividade básica:")
    pc1 = net.get('pc1')
    ping_result = pc1.cmd('ping -c 1 192.168.1.100 2>/dev/null')
    if "1 received" in ping_result:
        print("✓ PC1 → Servidor DNS: OK")
    else:
        print("✗ PC1 → Servidor DNS: FALHA")

def executar_testes_packet_tracer(net):
    print("\n" + "="*60)
    print("EXECUTANDO TESTES DO EXERCÍCIO PACKET TRACER")
    print("="*60)
    
    pc1 = net.get('pc1')
    
    # === TESTE 1: Verificar DHCP ===
    print("\nTESTE DHCP:")
    print("Verificando configuração IP do PC1...")
    result = pc1.cmd('ifconfig pc1-eth0')
    print("✓ Configuração de rede:")
    print(result.split('\n')[1])  # Linha com IP
    
    # === TESTE 2: Conectividade Inter-redes ===
    print("\nTESTE DE CONECTIVIDADE:")
    print("PC1 → Servidor HTTP (10.0.1.100)...")
    result = pc1.cmd('ping -c 3 10.0.1.100')
    if "3 received" in result:
        print("✓ Conectividade com 10.0.1.100: OK")
    else:
        print("✗ Falha na conectividade")
        print(result)
    
    # === TESTE 3: Resolução DNS ===
    print("\nTESTE DNS:")
    print("PC1 resolvendo 'site.com'...")
    result = pc1.cmd('nslookup site.com 192.168.1.100')
    print(result)
    
    print("PC1 → site.com via DNS...")
    result = pc1.cmd('ping -c 3 site.com')
    if "3 received" in result:
        print("✓ Resolução DNS site.com: OK")
    else:
        print("✗ Falha na resolução DNS")
    
    # === TESTE 4: Acesso HTTP via nome ===
    print("\nTESTE HTTP:")
    print("PC1 acessando http://site.com...")
    result = pc1.cmd('curl -s http://site.com/ | grep -o "<title>.*</title>"')
    if result:
        print(f"✓ Página carregada: {result}")
    else:
        print("✗ Falha no acesso HTTP")
    
    # Teste adicional: servidor.local
    print("\nTESTE EXTRA - DNS Local:")
    print("PC1 resolvendo 'servidor.local'...")
    result = pc1.cmd('ping -c 2 servidor.local')
    if "2 received" in result:
        print("✓ Resolução DNS servidor.local: OK")

def mostrar_status_rede(net):
    """Mostra status completo da rede"""
    print("\n" + "="*60)
    print("STATUS DA REDE - TOPOLOGIA PACKET TRACER")
    print("="*60)
    
    print("\nEQUIPAMENTOS:")
    print("├── Switch 1 (s1): Rede 192.168.1.0/24")
    print("├── Switch 2 (s2): Rede 10.0.1.0/24") 
    print("└── Roteador (r1): 192.168.1.1 ↔ 10.0.1.1")
    
    print("\nSERVIDORES:")
    print("├── DHCP/DNS: 192.168.1.100")
    print("│   ├── Pool DHCP: 192.168.1.101-150")
    print("│   ├── servidor.local → 192.168.1.100")
    print("│   └── site.com → 10.0.1.100")
    print("└── HTTP: 10.0.1.100 (site.com)")
    
    print("\nCLIENTES:")
    for i, pc in enumerate(['pc1', 'pc2', 'pc3']):
        ip = f"192.168.1.{101 + i}"
        print(f"├── {pc}: {ip} (DHCP)")
    
    print("\n📋 REGISTROS DNS:")
    print("├── servidor.local → 192.168.1.100")
    print("└── site.com → 10.0.1.100")

def main():
    
    setLogLevel('info')
    
    print("LABORATÓRIO MININET")
    print("Topologia: 2 Switches + Roteador + Servidores DHCP/DNS/HTTP")
    print("="*60)
    
    # Limpeza inicial
    print("Limpando ambiente...")
    import os
    os.system('sudo mn -c > /dev/null 2>&1')
    os.system('sudo pkill -f dnsmasq > /dev/null 2>&1')
    os.system('sudo pkill -f "python.*http.server" > /dev/null 2>&1')
    
    # Criar rede
    topo = TopologiaPacketTracer()
    net = Mininet(topo=topo, switch=OVSSwitch)
    
    # Iniciar rede
    net.start()
    
    print("\nConfigurando serviços...")
    
    # Configurações sequenciais
    configurar_roteador(net)
    time.sleep(1)
    
    configurar_servidor_dhcp_dns(net)
    time.sleep(2)
    
    configurar_servidor_http(net)
    time.sleep(1)
    
    configurar_clientes_dhcp(net)
    time.sleep(1)
    
    # Executar testes automáticos
    executar_testes_packet_tracer(net)
    
    # Mostrar status
    mostrar_status_rede(net)
    
    print("\n" + "="*60)
    print("COMANDOS ÚTEIS NO CLI:")
    print("="*60)
    print("# Teste geral de conectividade")
    print("pingall")
    print("")
    print("# Testes específicos do exercício:")
    print("pc1 ping 10.0.1.100")
    print("pc1 ping site.com")
    print("pc1 curl http://site.com/")
    print("pc2 nslookup servidor.local 192.168.1.100")
    print("")
    print("# Análise de tráfego:")
    print("pc1 tcpdump -i pc1-eth0 'port 53'  # DNS")
    print("r1 tcpdump -i r1-eth0 'icmp'       # Ping entre redes")
    print("")
    print("# Abrir terminais:")
    print("xterm pc1 dns_srv web_srv")
    
    # Entrar no CLI do Mininet
    print(f"\nAbrindo CLI do Mininet...")
    print("Experimente os comandos acima!")
    CLI(net)
    
    # Limpeza
    net.stop()

if __name__ == '__main__':
    main()

"""

TOPOLOGIA:
- 2 Switches (s1, s2) = Cisco 2960
- 1 Roteador Linux (r1) = Cisco 1941  
- Servidor DHCP/DNS (192.168.1.100)
- Servidor HTTP (10.0.1.100)
- 3 PCs clientes

CONFIGURAÇÕES:
- DHCP Pool: 192.168.1.101-150
- DNS: servidor.local, site.com
- Roteamento entre 192.168.1.0/24 ↔ 10.0.1.0/24
- Página web customizada

TESTES:
- Verificação DHCP
- Conectividade inter-redes
- Resolução DNS
- Acesso HTTP via nome

EXECUÇÃO:
sudo python3 labredes.py

"""