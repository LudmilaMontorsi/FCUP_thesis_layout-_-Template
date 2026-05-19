# Como Usar Abreviações Automáticas

## Sistema Configurado

O documento agora usa o pacote `glossaries` para gerenciar abreviações automaticamente.

## Como Adicionar Novas Abreviações

Edite o arquivo `preamble.tex` e adicione suas abreviações no final, usando:

```latex
\newacronym{sigla}{SIGLA}{Descrição Completa da Sigla}
```

**Exemplos já configurados:**
```latex
\newacronym{fcup}{FCUP}{Faculdade de Ciências da Universidade do Porto}
\newacronym{cnn}{CNN}{Convolutional Neural Network}
\newacronym{unet}{U-Net}{U-shaped Network}
\newacronym{ct}{CT}{Computed Tomography}
```

## Como Usar no Texto

### Comandos Disponíveis:

1. **`\gls{sigla}`** - Uso padrão
   - **Primeira vez:** Mostra "Descrição Completa da Sigla (SIGLA)"
   - **Próximas vezes:** Mostra apenas "SIGLA"
   
   Exemplo:
   ```latex
   A \gls{fcup} é uma faculdade...
   Resultado 1ª vez: A Faculdade de Ciências da Universidade do Porto (FCUP) é uma faculdade...
   Resultado 2ª vez: A FCUP é uma faculdade...
   ```

2. **`\Gls{sigla}`** - Igual ao anterior, mas com primeira letra maiúscula

3. **`\glspl{sigla}`** - Forma plural
   Exemplo: `\glspl{cnn}` → "Convolutional Neural Networks (CNNs)"

4. **`\acrshort{sigla}`** - Sempre mostra apenas a sigla
   Exemplo: `\acrshort{fcup}` → "FCUP"

5. **`\acrlong{sigla}`** - Sempre mostra apenas a descrição completa
   Exemplo: `\acrlong{fcup}` → "Faculdade de Ciências da Universidade do Porto"

6. **`\acrfull{sigla}`** - Sempre mostra a forma completa
   Exemplo: `\acrfull{fcup}` → "Faculdade de Ciências da Universidade do Porto (FCUP)"

## Exemplo de Uso no Texto

```latex
\chapter{Introdução}

Este trabalho foi desenvolvido na \gls{fcup}, que pertence à \gls{up}.
A pesquisa utilizou \glspl{cnn} para processar imagens de \gls{ct}.

A arquitetura \gls{unet} é amplamente utilizada em segmentação de imagens.
Neste estudo, a \gls{unet} foi modificada para incluir o módulo \gls{aspp}.
```

**Resultado:**
- 1ª menção de FCUP: "Faculdade de Ciências da Universidade do Porto (FCUP)"
- 2ª menção de U-Net: "U-Net" (apenas a sigla)
- Todas as siglas usadas aparecerão automaticamente na Lista de Abreviações

## Processo de Compilação

Para que as abreviações apareçam corretamente, você precisa compilar 3 vezes:

```bash
pdflatex main.tex
makeglossaries main
pdflatex main.tex
```

Ou no VS Code com a extensão LaTeX Workshop, ela fará isso automaticamente.

## Resetar Primeira Ocorrência

Se quiser que uma abreviação seja tratada como "primeira vez" novamente:

```latex
\glsreset{sigla}
```

## Lista de Abreviações

A lista é gerada automaticamente no arquivo `precontent.tex` com:

```latex
\printglossary[type=\acronymtype,title=Lista de Abreviaturas]
```

**Importante:** Apenas as abreviações que você **usar no texto** com `\gls{}` ou comandos similares aparecerão na lista!
