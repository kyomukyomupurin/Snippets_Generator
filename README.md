[![](https://img.shields.io/badge/license-CC0-lightgrey.svg?style=flat&logo=Creative-Commons)](https://github.com/kyomukyomupurin/snippets_generator/blob/master/LICENSE)
![](https://img.shields.io/badge/Python-3.6.9-brightgreen.svg?style=flat&logo=Python)
![](https://img.shields.io/badge/JSON-brightgreen.svg?style=flat&logo=JSON)
![](https://img.shields.io/badge/-VSCode-blue.svg?style=flat&logo=Visual-Studio-Code)
![](https://img.shields.io/badge/OS-WSL-yellow.svg?style=flat&logo=Linux)
![](https://img.shields.io/badge/Ubuntu-18.04-orange.svg?style=flat&logo=Ubuntu)

# Snippets Generator

Snippets generator for Visual Studio Code. I developed this for competitive programming. 

![](code.gif)

## How to use

Edit ```snippets_settings.json```.  
-  ```"root"``` : Path to the top directory where the snippets will be generated.  
-  ```"output"``` : Path to the json file to be generated.  
-  ```"extension"``` : List of file extensions to generate snippets.  

The overall structure of the snippets json file in VSCode is like the following.

```json
    "snippets_name": {
        "prefix": "prefix_name",
        "body": [
            "body_content"
        ]
    }
```

```"snippets_name"``` is the name of snippets. When you type ```"prefix_name"```, then  ```"prefix"```appears in input candidate and if you select it, ```"body_content"``` will be inserted.  
If you want to generate snippet from a file, only you have to do is to enclose the specific parts with ```"// snippet-begin"``` and ```"// snippet-end"```.  
When you run ```gen.py```, a snippet whose ```"prefix_name"``` is each file name without extension will be generated. If there is no enclosed parts in a file, no snippets for the file will be created. You have to insert a new line after ```"// snippet-end"```(I'll fix it in time).  
To enable snippets, copy and paste the contents of ```output.json``` into the ```cpp.json``` or an other json file for snippets.  
Every time you run ```gen.py```, ```output.json``` will be newly generated(not overwritten).  
Don't create multiple files with the same name!
