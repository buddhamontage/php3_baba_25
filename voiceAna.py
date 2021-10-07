#requetsモジュールのインポート
import requests 

#jsonモジュールのインポート
import json 

#mysqlモジュールのインポート
import mysql.connector 

#empath apiの取得
url ='https://api.webempath.net/v2/analyzeWav' 


apikey = ''#api key入力

#payload リクエストメソッドの引数にparams=付与するパラメーターの hash で付与する.
payload = {'apikey': apikey} 

#「勉強疲れた」音声データ
wav = 'sound/joy_test.wav' 

#バイナリファイルの読み込み open関数の引数modeにrb指定
data = open(wav, 'rb') 

#辞書型グローバル変数dataからwav key指定でwavデータのみ取得
file = {'wav': data}

res = requests.post(url, params=payload, files=file) #HTTPライブラリのrequestsを利用しPOSTでリソース取得 urlにapiと音声データの引数を渡す
print(res.json()) #取得されたデータをJSON形式で取得

 # コネクション作成 sql接続

vdb = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='root',
        database='voice_db'
    )
# 接続状況確認
print(vdb.is_connected())

    #
    # cur = conn.cursor()
    
    # # 1件取得
    # cur.execute("select version()")
    # print(cur.fetchone())
    
    



# -----------------------------------------------------
 # カーソル作成 コネクションオブジェクトcursor() カーソルを設定することで問い合わせ結果を1行づつ取得
cursor=vdb.cursor(buffered=True) 

#
json_obj = res.json() 

#json型を辞書型変換
voiceData = dict(json_obj)

print(voiceData)
print(type(voiceData))

#辞書型から値取得しリスト型変換
voiceList = list(voiceData.values())
print(voiceList)
print(type(voiceList))

#executeメソッドでクエリを実行
#My SQL書き込み
cursor.execute("INSERT INTO voice_an_db (error, calm, anger, joy, sorrow, energy,id) VALUES (%s,%s,%s,%s,%s,%s,NULL)", (voiceList[0], voiceList[1],  voiceList[2], voiceList[3], voiceList[4], voiceList[5], ))

#close the connection to the database.
vdb.commit()
cursor.close()
# DB操作終了
vdb.close()