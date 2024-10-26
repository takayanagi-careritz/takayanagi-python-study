### はじめに
高柳の学習記録です

進め方は「MMdd_~~~~.md」で学んだことを書きつつ、FastAPIプロジェクトも記述していきます

プロジェクトの実装は「0604_学習用アプリの概要.md」からとなっています

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

    ```sh
    docker compose up
    ```
</details>

