# 使い方

## ライブラリインストール
```
pip install -r requirements.txt
```

## 検索ページの設定
同じディレクトリに.envファイルを作成して以下の情報を記入

ex) 検索結果の1ページ目から1ページ取得
```
PAGE_START = 1
PAGE_LIMIT = 1
SEARCH_URL = 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&ek=000525620&rn=0005'
```

ex) 検索結果の1ページ目から2ページ取得
```
PAGE_START = 1
PAGE_LIMIT = 2
SEARCH_URL = 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&ek=000525620&rn=0005'
```

ex) 検索結果の2ページ目から3ページ取得
```
PAGE_START = 2
PAGE_LIMIT = 3
SEARCH_URL = 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&ek=000525620&rn=0005'
```