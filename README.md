# (Monty) Python Dojo - Killer-Rabbit training program
A repository for the killer-rabbit training problem. In it, there is a python-based solution with unit tests and a random input generator.

## Description (PT-BR)
Sir Lancelot, após recuperar o Calice Sagrado dos vis franceses com Rei Arthur e os demais cavaleiros da Tavola Redonda, resolveu tirar férias. Por ser um nobre e honrado cavaleiro (e por isso, não tem direito a férias), combinou com o Rei Arthur que poderia receber cavaleiros para treinar durante seu afastamento em sua casa de campo.

Na primeira leva de cavaleiros, Sir Lancelot se tocou que eram todos uns imbecis e que jamais conseguiria treina-los. Propos então que o Rei capturasse os coelhos assassinos de Carbannog e usasse-os como armas mortais. Mas para isso precisariam do treinamento de Sir Lancelot!

O combinado foi:
- A cada dia, um coelho chegaria para ser treinado;
- Ao começar o treinamento de um coelho, este não poderá ser interrompido até terminado;
- Coelhos demoram T dias para serem treinados;
- Caso não estejam sendo treinados, os coelhos entrarão em um estado de matança descontrolada;
- Sir Lancelot deve pagar multas diárias para cada coelho que esteja matando a população;
- A multa é um valor F que varia dependendo do coelho.

Sir Lancelot deve ser capaz de prever qual o menor valor de multa possível que ele terá que pagar à população, dado uma fila de coelhos que chegarão em um período de N dias e suas caracteristicas.

## Input
A i-ésima linha da entrada diz respeito ao i-ésimo coelho enviado pelo Rei Arthur para Sir Lancelot e consiste de dois inteiros: Ti e Fi, representando respectivamente o número de dias necessários para treinar o i-ésimo coelho e a multa cobrada por dia que o coelho passa matando a população. Para quaisquer i e j distintos, Ti / Fi ≠ Tj / Fj.

## Output
Imprima uma linha contendo unicamente o valor mínimo total da multa que Lancelot pagará a Távola Redonda.

## Source
- Problema original: https://www.urionlinejudge.com.br/judge/pt/problems/view/1851
- Testador de input/output: https://www.urionlinejudge.com.br/judge/pt/problems/toolkit/1851
