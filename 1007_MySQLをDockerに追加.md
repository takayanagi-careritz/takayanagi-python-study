### 
サービスにDBを追加
```yaml
# 一言でいうなら、コンテナ管理を設定

version: "3"
services:

  ############## 省略 #############

  db:
    image: mysql:8.0 # 上とは違いDockerFileではなく用意されてるImageを使う
    platform: linux/x86_64 # いろんなMacのチップに対応できる
    environment:
      MYSQL_ALLOW_EMPTY_PASSWORD: "yes" # パスワードなしでOK設定
      MYSQL_DATABASE: "demo"
      TZ: "Asia/Tokyo"
    volumes:
      - mysql_data:/var/lib/mysql
    command: --default-authentication-plugin=mysql_native_password # 認証方法をちょっと古い方法に指定
    ports:
      - 33306:3306 # ホストの33306をDockerの3306に接続、今回のFastAPIからアクセスするなら3306を見る
      
volumes:
  mysql_data: # ボリュームの名前だけを定義

```

DBのコンテナ上げれた後に接続確認する
```sh
docker exec -it my-python-app_devcontainer-db-1 mysql demo
```
できた

```sh
docker compose exec db mysql demo
```
↑ これでもできるはずなのにできない、  
~~docker composeで立ち上げていないから、、、？  
docker ps でサービスが上がっていることは確認したのに~~  

（10/17）  

docker compose ~~ は docker compose up を使って起動したコンテナ内でコマンドを実行  
注意すべきはdocker-compose.yamlに記載したサービス名を指定するということ

一方 -it は、上がっているコンテナに対し一時的にコマンドを入れられるモード（インタラクティブオプションとターミナルオプション）  
こっちはコンテナ名を指定する

docker exec は docker-compose を使っていなくても機能するが、docker compose exec は docker-compose.yml で定義されたサービスを前提にしている！