1. Acesse o Console de Desenvolvedor do Google.
2. Clique em "Selecione um projeto" ou crie um novo projeto.
3. No painel de navegação à esquerda, clique em "APIs e Serviços" > "Credenciais".
4. Clique em "Criar credenciais" e selecione "Chave da API".
5. Sua chave da API será gerada. Copie essa chave e armazene-a em um local seguro.

6. Certifique-se de que você tenha Python instalado em seu computador. Você pode baixá-lo em python.org.
7. Instale as bibliotecas necessárias executando os seguintes comandos:

- pip install google-api-python-client
- pip install python-dotenv
- pip install textblob
- python -m textblob.download_corpora

8. Crie uma pasta para o seu projeto e navegue até ela em seu terminal ou prompt de comando.
9. Crie um arquivo Python (por exemplo, analyze_comments.py) e cole o código fornecido na pergunta no arquivo.

10. Crie um arquivo chamado .env na pasta do seu projeto.
11. Dentro do arquivo .env, insira sua chave da API do YouTube da seguinte maneira:
- API_KEY=YOUR_YOUTUBE_API_KEY
- Substitua YOUR_YOUTUBE_API_KEY pela chave da API do YouTube que você gerou no Passo 1.

12. Abra um terminal ou prompt de comando e navegue até a pasta do seu projeto onde o arquivo Python está localizado.
13. Execute o código Python usando o seguinte comando:
- python SEU_ARQUIVO.py

O script irá buscar os comentários do vídeo especificado, realizar análise de sentimentos e exibir os resultados no console.

Certifique-se de substituir video_id pelo ID do vídeo do YouTube que você deseja analisar os comentários.

Isso é tudo! Você agora deve ter um projeto que busca os comentários do YouTube, analisa seus sentimentos e exibe os resultados no console. Certifique-se de seguir as etapas acima e substituir video_id pela ID do vídeo desejado.