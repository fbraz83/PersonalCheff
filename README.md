# PersonalCheff
<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
<img src="exemplo.jfif" alt="exemplo imagem">
> Uma aplicação Web de receitas chamada PersonalCheff desenvolida durante curso de Python no Senac Americana. A aplicação listará receitas e clicando em cada nome de receita você poderá ver a receita completa.

### Lista de tarefas
Segue a lista de tarefas a serem desenvolvidas no projeto:
- [X] Pré-requisitos
    - [X] Instalar o Python
    - [X] Instalar Visual Studio Code
- [X] Criar e ativar ambiente visual
``` 
python -m venv .\venv\
venv\Scripts\activate
```
- [X] Instalar o Django
``` 
python -m pip install django==3.2
python -m pip freeze 
```
- [X] Criar o projeto personalCheff
```
django-admin.py startproject PersonalCheffProj
```
- [X] Subir o servidor e testar o projeto
``` 
Entrar na pasta do projeto 
cd PersonalCheffProj

Executar o projeto no servidor
python manage.py runserver
```

- [X] Alterar o idioma do projeto para `pt-br`
```
Linha 106 da settings.py LANGUAGE_CODE = 'pt-br'
```
- [X] Alterar o timezone do projeto para `America/São_Paulo`
```
Alterado a time zone no settings.py para America_Sao_Paulo.
Link para time zone 'list of pytz time zones · GitHub'
```
- [X] Criar o app receitas
```
*Preciso estar dentro da pasta do projeto (PeronalCheffProj) 
python manage.py startapp receitas
```
- [X] Registrar o app receitas
```
no arquivo setting.py adicionar o app receitas na lista de app INSTALED APP
```
- [ ] Configurar a rota inicial (index)
```
Criar uma pasta urls dentro de receitas 
```
- [ ] Registrar a rota inicial
- [ ] Criar o arquivo index.html 

## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
[⬆ Voltar ao topo](#nome-do-projeto)<br>
