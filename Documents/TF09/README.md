# TF 09: O Atalho na Árvore

Implementação da classe `Atalho(Item)` aplicando os pilares da Orientação a Objetos (Encapsulamento, Herança e Polimorfismo) em Python, sem o uso de `else` ou `isinstance`.

## Interface vs Implementação
- **Interface**: Define o *o quê* o objeto deve fazer (como os métodos `tamanho()` e `mostrar()` definidos na classe base `Item` e na classe mixin `Medivel`), estabelecendo um contrato sem se preocupar com os detalhes internos.
- **Implementação**: Define o *como* é feito (como o cálculo específico do tamanho do atalho baseado no seu destino na classe `Atalho`, utilizando atributos privados encapsulados via `__slots__` e propriedades).