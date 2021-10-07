# Pythonを利用しての音声感情認識及びデータベース格納実装
## 1.操作方法、実装内容
### 課題説明
・pythonにて音声感情認識apiを取得しmysqlへの格納を実装しました。
・指定の音声データを読み込むと喜怒哀楽の感情を分析し結果をデータベースへ保存します。

### 環境構築
・pythonをインストール後、mysql-connector-python、requestsをpipにてインストールしライブラリの仕様を可能にします。
・my sqlにvoice_dbのデータベースを作製し、voice_an_dbのテーブルを作製します。
・error、calm、anger、joy、sprrow、energy、idのカラムをint型で合わせて作成します。
・MAMPのlocalhostでアクセスできるようにvoiceAna.pyファイルを配置します。

### 操作方法
#### 音声データ準備
下記形式音声ファイルの準備
1.PCM WAVE形式 16bit
2.データサイズが1.9MB以下
3.PCM_FLOAT、PCM_SIGNED、PCM_UNSIGNEDのいずれかのフォーマット
3.録音時間が5.0秒未満
4.サンプリング周波数が11025Hz
5.チャンネル数が1（モノラル）

#### 音声データ読み込み
・voiceAna.pyの20行目「wav = '音声データ'」のファイルパスを記載します。

#### 分析実行及びデータ格納
・ターミナル上で実行をします。
・ターミナルに分析データがjson型で表示されると同時に、データベースにパーセンテージで表示されます。

## 2.実装の工夫
・サンプル用に音声データを加工しました。
・辞書型データの格納するmy sql insert構文のサーベイに時間がかかりました。
・my sqlに格納するために、分析データをjson型から辞書型へ変換し、値のみ格納の実装に時間がかかりました。
・格納可能な型へ変換することへの理解が深まりました。
・音声感情分析参照ページ
https://webempath.net/lp-jpn/
https://qiita.com/keki/items/c0bea07274fe41a14978
・json型データの辞書型参考ページ
https://paloma69.hatenablog.com/entry/2020/01/18/190820
c54a057a014b1977c538
https://hibiki-press.tech/python/dict/1136
・python my sql insert参考ページ
https://python.softmoco.com/basics/python-mysql-insert.php
https://stackoverflow.com/questions/9336270/using-a-python-dict-for-a-sql-insert-statement

## 3.感想、疑問点
pythonでのsql構文は応用が効く参考コードが日本語ではあまりありませんでした。pythonでのmy sql利用は少ないのか調べてみようと思いました。

