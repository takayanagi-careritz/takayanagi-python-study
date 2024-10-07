### はじめに
高柳の学習記録です

基本的には「(日付)_~~~~.md」を書きつつ、「my-python-app」プロジェクトも記述していく想定です

### 動かし方

1. devcontainerでコンテナビルド
1. SwaggerUIにアクセス  
   http://localhost:8000/docs

<details>
<summary>devcontainer実装前手順</summary>

1. イメージ作成する
   
    ```sh
    docker compose build
    ```

2. ~~pyproject.toml を作る~~  →  gitにあげてるので不要、次の手順へ  
   pyproject.toml: package.json的なやつ

    ```sh
    docker compose run --entrypoint "poetry init --name my-python-app --dependency fastapi --dependency uvicorn[standard]" my-python-app
    ```

3. pyproject.tomlをもとにパッケージインストール

    ```sh
    docker compose run --entrypoint "poetry install --no-root" my-python-app
    ```

4. コンテナ作成
</details>

