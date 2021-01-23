[![](https://img.shields.io/badge/license-CC0-lightgrey.svg?style=flat&logo=Creative-Commons)](https://github.com/kyomukyomupurin/snippets_generator/blob/master/LICENSE)
![](https://img.shields.io/badge/Python-3.6.9-brightgreen.svg?style=flat&logo=Python)
![](https://img.shields.io/badge/JSON-brightgreen.svg?style=flat&logo=JSON)
![](https://img.shields.io/badge/-VSCode-blue.svg?style=flat&logo=Visual-Studio-Code)
![](https://img.shields.io/badge/OS-WSL-yellow.svg?style=flat&logo=Linux)
![](https://img.shields.io/badge/Ubuntu-18.04-orange.svg?style=flat&logo=Ubuntu)

# Snippets Generator

Visual Studio Code 用のスニペットファイルを自動で生成するスクリプト。主にプログラミングコンテストで使うために書いた。

## 使い方

1. ```gen.py``` と ```snippets_settings.json``` をスニペット化したいファイルのあるフォルダにコピー
2. ```snippets_settings.json``` を編集
    - ```"extension"``` にはスニペット化したいファイルの拡張子のリストを入力
    - ```output``` には生成されるスニペットファイル(JSON 形式)の出力先を入力
3. スニペット化したいファイルについて、スニペット化する範囲を指定する
    - コードのうち ```// snippet-begin``` と ```// snippet-end``` というタグで囲まれた範囲がスニペット化される
    - ```// snippet-begin``` タグが存在しないファイルについては、スニペットは作成されない
    - ```// snippet-end``` タグが存在しない場合、```// snippet-begin``` タグ以降のコードが全てスニペット化される
    - スニペット化されるのは、ファイルの中で最初に現れる ```// snippet-begin``` タグと最初に現れる ```// snippet-end``` の間の部分のみ
    - スニペットのキーは各ファイル名のうち拡張子を除いた部分になる
4. ```python3 gen.py``` で実行
5. ```snippets.json``` が生成されるので、これを VSCode のスニペットファイルにコピーする

## 補足

- サブディレクトリ内に同名のファイルが複数ある場合、最後にスニペット化されたものだけがスニペットとして反映されてしまうので、注意する。
- ```snippets.json``` は実行の度に上書きされる。