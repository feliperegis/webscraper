# Web Scraper

início: 22/04/24

REQUISITOS:
https://ocacesso.com/#/
https://ocacesso.com/#/diagnostico
https://ocacesso.com/#/diagnostico/medicina-nuclear

YOUTUBE:
1. SELENIUM - https://www.youtube.com/watch?v=Y2d2g4Hlqb4&list=PLFeyfVYazTkIYEFvAKB6SB-uJ-CWW4BrZ&index=9
2. SELENIUM - https://www.youtube.com/watch?v=XLkxOBY965w

"Algumas coisas como quimio e imunoterapia, alem de infusao de medicamentos pecisava de receita"

GITHUB COPILOT:

https://github.com/account/enterprises/new

GPT INITIAL SETUP:

Claro! Vou criar um guia passo a passo para você com todas as etapas necessárias para criar um projeto Python no Visual Studio Code (VSCode), configurar um ambiente virtual, iniciar o controle de versão com Git, criar os arquivos README.md, requirements.txt e .gitignore, e, por fim, publicar o seu projeto no GitHub. Vamos lá:

## Guia Passo a Passo: Criando um Projeto Python no VSCode e Publicando no GitHub

1. *Instale o Visual Studio Code (VSCode)*:
   - Se você ainda não tem o VSCode instalado, faça o download e instale-o a partir do [site oficial](https://code.visualstudio.com/).

2. *Crie um Diretório para o Seu Projeto*:
   - Abra o terminal ou prompt de comando.
   - Navegue até o diretório onde deseja criar o seu projeto:
     
     cd caminho/do/seu/diretorio
     

3. *Crie um Ambiente Virtual (Virtual Environment)*:
   - Execute o seguinte comando para criar um ambiente virtual (substitua myenv pelo nome que você desejar):
     
     python -m venv myenv
     

4. *Ative o Ambiente Virtual*:
   - No Windows:
     
     myenv\Scripts\activate
     
   - No macOS e Linux:
     
     source myenv/bin/activate
     

5. *Instale as Dependências do Seu Projeto*:
   - Com o ambiente virtual ativado, instale as bibliotecas Python necessárias para o seu projeto usando o pip. Por exemplo:
     
     pip install requests pandas
     

6. *Crie um Projeto no VSCode*:
   - Abra o VSCode:
     
     code .
     
   - Crie um novo arquivo Python (por exemplo, main.py) e comece a escrever o código do seu projeto.

7. *Inicie o Controle de Versão com Git*:
   - No terminal, execute os seguintes comandos:
     
     git init
     git add .
     git commit -m "Primeiro commit"
     

8. *Crie os Arquivos Necessários*:
   - Crie os arquivos README.md, requirements.txt e .gitignore na raiz do seu projeto.
   - Preencha o README.md com informações sobre o seu projeto.
   - O requirements.txt deve conter as dependências do seu projeto (geralmente gerado com pip freeze > requirements.txt).
   - O .gitignore deve listar os arquivos e pastas que você deseja ignorar no controle de versão (por exemplo, venv/, .vscode/, etc.).

9. *Crie um Repositório no GitHub*:
   - Acesse o [GitHub](https://github.com/) e faça login na sua conta.
   - Clique no botão "+" no canto superior direito e escolha "New repository".
   - Siga as instruções para criar o repositório.

10. *Conecte o Repositório Local ao GitHub*:
    - No terminal, execute os seguintes comandos (substitua seu-usuario e seu-repositorio pelos valores corretos):
      
      git remote add origin https://github.com/seu-usuario/seu-repositorio.git
      git branch -M main
      git push -u origin main
      

11. *Publique o Seu Projeto no GitHub*:
    - Agora o seu projeto está no GitHub! Você pode continuar fazendo commits e push para manter o repositório atualizado.

Lembre-se de adaptar os comandos e arquivos conforme as necessidades específicas do seu projeto. Espero que este guia seja útil! Se precisar de mais assistência, estou à disposição. 😊

Referências:
- [Documentação oficial do Python sobre ambientes virtuais](https://docs.python.org/3/tutorial/venv.html)
- [Documentação oficial do Git](https://git-scm.com/doc)
- [Documentação oficial do GitHub](https://docs.github.com/)
- [Guia do VSCode para Python](https://code.visualstudio.com/docs/python/python-tutorial)
- [Exemplo de arquivo .gitignore para projetos Python](https://github.com/github/gitignore/blob/master/Python.gitignore)
- [Exemplo de arquivo README.md](https://github.com/github/gitignore/blob/master/Python.gitignore)
- [Exemplo de arquivo requirements.txt](https://pip.pypa.io/en/st