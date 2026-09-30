---
title: "Lab 08: Acesso Remoto SSH & CLI Cisco \\- Quiz de Avaliação`\\\\ \\textsc{solutions}`{=latex}`<br><span style=\"font-variant: small-caps;\">solutions</span>`{=html}"
header-includes: |
    ```{=latex}
    %%%% Begin text2qti custom preamble
    % Page layout
    \usepackage[margin=1in]{geometry}
    % Graphics
    \usepackage{graphicx}
    % Math/science
    \usepackage{amsmath, amssymb}
    \usepackage{siunitx}
    % Symbols for solutions
    \usepackage{fontawesome}
    % Answers and solutions use itemize with custom item symbols
    \def\texttoqtimctfchoicesymb{%
        \resizebox{2ex}{!}{\faCircleO}}
    \def\texttoqtimctfcorrectchoicesymb{%
        \resizebox{2ex}{!}{\faDotCircleO}}
    \def\texttoqtimultanschoicesymb{%
        \resizebox{2ex}{!}{\faSquareO}}
    \def\texttoqtimultanscorrectchoicesymb{%
        \resizebox{2ex}{!}{\faCheckSquare}}
    \def\texttoqtigeneralcorrectanssymb{%
        \resizebox{2ex}{!}{\faArrowRight}}
    \def\texttoqtisolutionsymb{%
        \resizebox{2ex}{!}{\faFileTextO}}
    \def\texttoqtishortansbox{%
        \framebox[0.25\linewidth]{\strut}}
    \def\texttoqtiessayansbox{%
        \framebox{\begin{minipage}\vspace{4\baselineskip}\end{minipage}}}
    %%%% End text2qti custom preamble

    ```

    ```{=html}
    <style type="text/css">
    html {
        line-height: 1.2;
    }
    div.text2qti-randomized > ul {
        list-style-position: outside;
        margin-left: -0.5em;
    }
    div.text2qti-randomized > ul > li {
        list-style-type: "[?]";
        padding-left: 0.5em;
    }
    ul.text2qti {
        list-style-position: outside;
        /* margin-left: -0.5em; */
    }
    ul > li.text2qti-mctf-choice::marker, ul > li.text2qti-mctf-correct-choice::marker {
        font-size: 1.5em;
    }
    ul > li.text2qti-mctf-choice, ul > li.text2qti-mctf-correct-choice {
        margin-top: -0.5em;
    }
    li.text2qti-mctf-choice {
        list-style-type: "○";
        padding-left: 0.5em;
    }
    li.text2qti-mctf-correct-choice {
        list-style-type: "●";
        padding-left: 0.5em;
    }
    li.text2qti-multans-choice {
        list-style-type: "☐";
        padding-left: 0.5em;
    }
    li.text2qti-multans-correct-choice {
        list-style-type: "☑";
        padding-left: 0.5em;
    }
    li.text2qti-generic-correct {
        list-style-type: "🡆";
        padding-left: 0.5em;
    }
    ul > li.text2qti-solution::marker {
        font-size: 1.75em;
    }
    ul > li.text2qti-solution {
        margin-top: -0.25em;
    }
    li.text2qti-solution {
        list-style-type: "🗈";
        padding-left: 0.5em;
    }
    </style>

    ```


...

Quiz avaliativo baseado exclusivamente no Roteiro 08 (Modos do Cisco IOS, Topologia, Endereçamento IP, Servidor DHCP, Chaves RSA, SSHv2 e Gerenciamento Seguro de Switch L2).

------------------------------------------------------------------------------

@.  No Cisco IOS, um administrador está configurando a interface GigabitEthernet0/0/0 no modo de configuração de interface (`R-LAB(config-if)#`). Qual comando ele deve digitar para retornar diretamente ao modo Privileged EXEC (`R-LAB#`) em um único passo?

    ```{=latex}
    \begin{itemize}
    ```

    ```{=html}
    <ul class="text2qti">
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    exit

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfcorrectchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-correct-choice">
    ```

    end

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    disable

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    quit

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \end{itemize}
    ```

    ```{=html}
    </ul>
    ```

@.  Durante o Experimento 1 do laboratório, o primeiro acesso ao roteador Cisco ISR 4331 recém-instalado deve ser realizado obrigatoriamente através da porta Console (`line con 0`) e não via SSH. Qual é a justificativa técnica apresentada no roteiro?

    ```{=latex}
    \begin{itemize}
    ```

    ```{=html}
    <ul class="text2qti">
    ```

    ```{=latex}
    \item[\texttoqtimctfcorrectchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-correct-choice">
    ```

    O roteador sai de fábrica sem endereços IP configurados, e a conexão por Console é out-of-band, não dependendo de rede ou interfaces ativas.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    A porta Console possui criptografia nativa superior ao SSHv2 de 1024 bits.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    O protocolo SSH só pode ser habilitado por comandos disponíveis no modo User EXEC da porta auxiliar (AUX).

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    A porta Console aceita até 5 sessões simultâneas de gerenciamento, permitindo acesso concorrente.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \end{itemize}
    ```

    ```{=html}
    </ul>
    ```

@.  Ao tentar executar o comando `crypto key generate rsa`, o Cisco IOS exibe a mensagem de erro `"% Please define a domain-name first"`. Qual comando deve ser configurado no modo de configuração global para sanar essa pendência?

    ```{=latex}
    \begin{itemize}
    ```

    ```{=html}
    <ul class="text2qti">
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    ip domain-lookup labredes.local

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    ip host R-LAB labredes.local

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfcorrectchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-correct-choice">
    ```

    ip domain-name labredes.local

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    domain-name rsa 1024

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \end{itemize}
    ```

    ```{=html}
    </ul>
    ```

@.  Por que a definição prévia de um hostname personalizado (ex: `hostname R-LAB`) e de um nome de domínio é obrigatória antes da geração das chaves RSA no Cisco IOS?

    ```{=latex}
    \begin{itemize}
    ```

    ```{=html}
    <ul class="text2qti">
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    Porque o IOS exige esses valores para criar o pool DHCP de clientes.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfcorrectchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-correct-choice">
    ```

    Porque o IOS utiliza a junção do hostname e do domínio para compor o FQDN e batizar o par de chaves RSA (ex: R-LAB.labredes.local).

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    Porque sem um hostname a interface GigabitEthernet0/0/0 não aceita o comando "no shutdown".

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    Porque o protocolo TCP porta 22 bloqueia pacotes cujo cabeçalho não contenha o hostname do roteador.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \end{itemize}
    ```

    ```{=html}
    </ul>
    ```

@.  No Experimento 2, antes de criar o pool DHCP para os clientes, foi inserido o comando `ip dhcp excluded-address 192.168.1.1 192.168.1.10`. Qual é a finalidade desta configuração?

    ```{=latex}
    \begin{itemize}
    ```

    ```{=html}
    <ul class="text2qti">
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    Bloquear o acesso dos primeiros 10 clientes à internet e ao servidor DNS.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    Desativar as interfaces GigabitEthernet associadas a essas portas.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfcorrectchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-correct-choice">
    ```

    Reservar essa faixa estática, impedindo que o roteador distribua para os clientes IPs já usados por gateways ou servidores.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    Forçar os clientes da rede a se autenticarem via SSH antes de receberem o endereço IP.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \end{itemize}
    ```

    ```{=html}
    </ul>
    ```

@.  Qual é a principal diferença estrutural e operacional entre a linha de Console (`line con 0`) e as linhas de Terminal Virtual (`line vty 0 4`) abordada no roteiro?

    ```{=latex}
    \begin{itemize}
    ```

    ```{=html}
    <ul class="text2qti">
    ```

    ```{=latex}
    \item[\texttoqtimctfcorrectchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-correct-choice">
    ```

    A Console é uma porta física RJ-45 para acesso out-of-band com 1 conexão simultânea; as VTYs são portas lógicas em memória para acesso remoto via rede e suportam múltiplas sessões.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    A Console utiliza a porta 22 TCP e exige IP configurado; as VTYs utilizam apenas sinalização serial assíncrona.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    A Console suporta 16 sessões simultâneas com criptografia RSA; as VTYs suportam apenas 1 conexão serial por cabo azul.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    O comando "login local" só funciona na porta Console, sendo proibido nas linhas VTY.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \end{itemize}
    ```

    ```{=html}
    </ul>
    ```

@.  No endurecimento das linhas VTY (`line vty 0 4`), quais comandos garantem, respectivamente, o bloqueio do protocolo Telnet (texto claro) em favor exclusivo do SSH, e a obrigatoriedade do uso do banco de credenciais configurado no próprio dispositivo (`username ... secret ...`)?

    ```{=latex}
    \begin{itemize}
    ```

    ```{=html}
    <ul class="text2qti">
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    service password-encryption e enable secret class

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    ip ssh version 2 e crypto key generate rsa

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfcorrectchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-correct-choice">
    ```

    transport input ssh e login local

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    default-router 10.0.0.1 e login synchronous

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \end{itemize}
    ```

    ```{=html}
    </ul>
    ```

@.  No Cisco Packet Tracer, ao tentar conectar via SSH a partir do Command Prompt do PC-Admin (10.0.0.11) para o roteador R-LAB (10.0.0.1), qual é a sintaxe correta de comando especificada no roteiro?

    ```{=latex}
    \begin{itemize}
    ```

    ```{=html}
    <ul class="text2qti">
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    ssh admin@10.0.0.1

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfcorrectchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-correct-choice">
    ```

    ssh -l admin 10.0.0.1

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    connect ssh 10.0.0.1 -u admin

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    telnet 10.0.0.1 -ssh -user admin

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \end{itemize}
    ```

    ```{=html}
    </ul>
    ```

@.  No Experimento 5 (Switch L2), se o switch opera na Camada 2 (Enlace) comutando quadros Ethernet por hardware (ASIC) sem precisar de IP para o tráfego dos clientes, por que configuramos um IP na interface virtual `vlan 1` (SVI)?

    ```{=latex}
    \begin{itemize}
    ```

    ```{=html}
    <ul class="text2qti">
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    Para que o switch possa rotear pacotes entre as portas FastEthernet e a rede externa.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfcorrectchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-correct-choice">
    ```

    Para o Plano de Gerenciamento (Management Plane), permitindo que a CPU do switch tenha uma pilha TCP/IP para escutar na porta 22 (SSH).

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    Porque sem IP na SVI as portas físicas FastEthernet entram em estado de shutdown automático.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    Para habilitar a tabela CAM e permitir o aprendizado de endereços MAC.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \end{itemize}
    ```

    ```{=html}
    </ul>
    ```

@.  No teste de validação do Switch SW-Admin, um administrador conectou com sucesso via SSH a partir do PC-Admin (10.0.0.11). Porém, ao testar a partir do PC-A (192.168.1.11), a conexão falharia com timeout caso o comando `ip default-gateway 10.0.0.1` não estivesse configurado no switch. Qual é a causa técnica dessa falha?

    ```{=latex}
    \begin{itemize}
    ```

    ```{=html}
    <ul class="text2qti">
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    O switch L2 bloqueia nativamente qualquer pacote originado de interfaces GigabitEthernet.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    Sem o gateway padrão, a chave RSA do switch reduz seu tamanho de 1024 bits para 512 bits.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfcorrectchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-correct-choice">
    ```

    O switch L2 não possui tabela de roteamento e, sem o gateway padrão, não sabe para onde encaminhar os pacotes TCP de resposta de volta à rede externa 192.168.1.0/24.

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \item[\texttoqtimctfchoicesymb]
    ```

    ```{=html}
    <li class="text2qti-mctf-choice">
    ```

    O PC-A só consegue acessar switches se o comando "line vty 0 4" for utilizado em vez de "line vty 0 15".

    ```{=latex}

    ```

    ```{=html}
    </li>
    ```

    ```{=latex}
    \end{itemize}
    ```

    ```{=html}
    </ul>
    ```

