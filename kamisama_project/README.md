# kamisama_project

※宗教文化士という資格があり、中でも上級宗教文化士という資格をお持ちの元神主の方から

依頼を受けて作成したプロジェクトになっております。予めご了承ください。※

日本の神々の分類に関するプロジェクトです。

書籍の分類方法に適用できます。

例えば、
```
種類1 ┬ 1群 ┬ 神々

    　┝ 2群 ┬　グループ1 ━ 神々

        　  ┝ グループ2 ━ 神々

        　  └ グループ3 ━ 神々

    　└ 3群 ━ 神々

種類2 ┬ 1群 ━ 神々

    　┝ 2群 ━ 神々

    　└ 3群 ┬　グループ1 ━ 神々

        　  ┝ グループ2 ━ 神々

        　  └ グループ3 ━ 神々

種類3 ━ 神々
```
このような構成で神々がカテゴリー分けされていた場合、

通常のForeignKeyではモデルを定義できません。

そこで登場するのが、TaggedItemというモデルです。（test2_models.py）

GenericForeignKey,ContentTypeを使います。

Djangoドキュメント（https://docs.djangoproject.com/ja/4.0/ref/contrib/contenttypes/）
```
from django.contrib.contenttypes.fields import GenericForeignKey

from django.contrib.contenttypes.models import ContentType
```
TaggedItemというテーブル（モデル）を介して、神々を各カテゴリーに紐づける考え方です。

db.sqlite3に既に仮登録してありますので、

python manage.py runserver

をしてローカルホストを立ち上げて、127.0.0.1:8000にアクセスすると、

登録状況が見れます。

127.0.0.1:8000/admin/

とし、username:admin, password:password26

でDjangoの管理画面にログインすると、TaggedItemというテーブル名があるので、

そこを見てみると分かりやすいかと・・・
