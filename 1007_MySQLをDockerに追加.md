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
docker exec -it my-python-app_devcontainer-db-1 
```
できた

```sh
docker compose exec db mysql demo
```
↑ これでもできるはずなのにできない、  
docker composeで立ち上げていないから、、、？  
docker ps でサービスが上がっていることは確認したのに