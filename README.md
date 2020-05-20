# snippets_generator

競プロ用のスニペット作成スクリプト(for VSCode)。ライブラリを更新するたびに手動でスニペットも書き換えるのはつらいので。

## 使い方

```main.py``` の import のあとの ```root_dir```, ```output_file```, ```extension_list``` を必要に応じて弄る。  
-  ```root_dir``` 以下のディレクトリがスニペット作成の対象になる。
-  ```output_file``` は作成される json ファイルへのパス  
-  ```extension_list``` はスニペット作成の対象とするファイルの拡張子のリスト

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