# snippets_generator

競プロ用のスニペット作成スクリプト(for VSCode)。ライブラリを更新するたびに手動でスニペットも書き換えるのはつらいので。

## 使い方

```snippets_settings.json``` に次の 3 つの設定を書いておく。  
-  ```"root"``` : スニペット作成の対象とする一番上のディレクトリへのパス  
-  ```"output"``` : 作成される json ファイルへのパス(もともと ```output.json``` が無かったら新規作成される)  
-  ```extension``` : スニペット作成の対象とするファイルの拡張子のリスト

VSCode の json ファイルは次のような構造からなる。  

```json
    "snippets_name": {
        "prefix": "prefix_name",
        "body": [
            "body_content"
        ]
    }
```

```"snippets_name"``` は各スニペットの名前。```"prefix_name"``` と入力すると予測候補に ```"prefix"``` が現れるようになり、これを選択するとコードに ```"body_content"``` が挿入される。  
スニペット化したい C++ ファイルのそれぞれについて、ファイル中のスニペット化したい部分を ```"// snippet-begin"``` と ```"// snippet-end"``` で囲んでおく。  
適当な場所で ```main.py``` を実行するとファイル名を ```"prefix_name"``` 、そのファイル中で```"// snippet-begin"``` と ```"// snippet-end"``` で囲まれた部分を ```"body_content"``` としたスニペットが作成される。囲まれた部分が無い場合、そのファイルのスニペットは作成されない。```"// snippet-end"``` のあとに改行を入れること(そのうち改行とか空白の指定を緩くするかも)。  
```output.json``` の中身は VSCode の ```cpp.json``` (なんか変な場所にあったやつ)にコピペするなりなんなりする。  
```main.py``` の実行のたびに ```output.json``` は新規作成される(上書きされない)