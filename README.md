### はじめに
高柳の学習記録です

基本的には「(日付)_~~~~.md」を書きつつ、「my-python-app」プロジェクトも記述していく想定です

### 動かし方
1. 「my-python-app/.devcontainer」に移動  
    ```sh
    cd my-python-app/.devcontainer
    ```
1. イメージ作成する  
    ```sh
    docker compose build
    ```
1. ~~pyproject.toml を作る~~  →  gitにあげてるので不要、次の手順へ  
    pyproject.toml: package.json的なやつ
    ```sh
    docker compose run --entrypoint "poetry init --name my-python-app --dependency fastapi --dependency uvicorn[standard]" my-python-app
    ```
1. pyproject.tomlをもとにパッケージインストール
    ```sh
    docker compose run --entrypoint "poetry install --no-root" my-python-app
    ```
1. devcontainerでコンテナビルド
1. SwaggerUIにアクセス  
  http://localhost:8000/docs
