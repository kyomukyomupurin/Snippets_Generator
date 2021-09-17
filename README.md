# Snippets Generator - Visual Studio Code 用のスニペット作成ツール

[![](https://img.shields.io/badge/license-CC0-lightgrey.svg?style=flat&logo=Creative-Commons)](https://github.com/kyomukyomupurin/snippets_generator/blob/master/LICENSE)
![](https://img.shields.io/badge/-VSCode-blue.svg?style=flat&logo=Visual-Studio-Code)

## About

Visual Studio Code（VSCode）用のスニペットを作成するためのスクリプトです。単一の Python スクリプトで、特定の拡張子のファイルからスニペットを作成します。

## Requirements

以下が必要です。

- Python(>= 3.8)

## Installation

`generator.py` をダウンロードしてください。

## Quick Start

1. スニペットを作成したいファイル（ここでは、`sample2.cc` とします）に、以下のようにコメントを追加してください。ファイル名の拡張子を除いた部分（ここでは `sample2`）をキー、コメントで挟まれた範囲を値とするスニペットが作成されます。

```cpp
#include <iostream>

// snippet-begin
int main() {
  std::cout << "Hello, World!" << std::endl;

  return 0;
}
// snippet-end
```

2. コマンドラインから `generator.py` を実行してください。スニペット化の対象となるのは、`generator.py` と同一ディレクトリまたはサブディレクトリに存在するファイルのうち、1. でコメントを追加されたファイルです。

3. `snippet.json` が生成されるので、これをスニペットの設定ファイルにコピーしてください。この設定ファイルは、多くの場合は `C:\Users\{USERNAME}\AppData\Roaming\Code\User\snippets\cpp.json` にあるはずです。存在しない場合は、エディタ上で「ファイル」→「ユーザー設定」→「ユーザースニペット」の順に選択し、「cpp」を選択することで作成できます。

4. VSCode の設定で `editor.tabCompletion` を `on` に設定してください。
