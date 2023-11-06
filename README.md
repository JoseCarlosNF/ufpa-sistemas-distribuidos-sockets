# SD-SOCKETS

```
                          UNIVERSIDADE FEDERAL DO PARÁ
                    INSTITUTO DE CIÊNCIAS EXATAS E NATURAIS
                            FACULDADE DE COMPUTAÇÃO
                        EN05227 - SISTEMAS DISTRIBUIDOS
```

## Requisitos

- Criar um programa para criar vários _sockets_;
- Para cada socket, o programa deve mostrar qual porta está sendo utilizada;

## Questionamentos

1. **Existe alguma relação entre os valores das portas obtidas?**

    O único ponto de coincidência encontrado foi a utilização de portas "altas",
    acima de 1024. 

2. **Os valores mudam a cada execução? Porquê?**

    Sim e não, se um valor de porta for definido, a tendência é que ele sempre seja
    usado pelo programa. A menos que já estava em uso no momento da execução.

    Por outro lado, se não for definido um valor fixo, sempre que houver uma nova
    execução, uma nova série de portas altas será usada.

3. **Após mudar a lógica para que, antes de uma nova criação de porta o programa
feche a anterior. Houve alguma mudança no comportamento de obtenção das
portas?**

    Não houve mudança. Sempre que acontece uma nova criação de porta, se não houver
    um valor fixo, uma nova porta alta será atribuída.

## :rocket: Como executar?

É possível executar localmente, sem necessidade de instalação de nenhuma
biblioteca:

```
python3 app/
```

Ou utilizando docker, através dos comandos a seguir:

```
docker build -t sd-sockets-app .
docker run --name sd-sockets-app --rm --network host sd-sockets-app
```

Ao utilizar a opção `--network host` todas as portas que forem expostas no
container serão exatamente as mesmas do host onde o comando foi executado. Dando
a impressão que o programa foi executado na máquina host, e não no container.
