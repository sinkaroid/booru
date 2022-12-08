# Booru
Python bindings for Booru imageboards

<a href="http://sinkaroid.github.io/booru"><img align="right" src="https://cdn.discordapp.com/attachments/952117487166705747/961124440400351232/mataa.png" width="390"></a>

- [Booru](#booru)
  - [Features](#features)
  - [Features availability](#this-library-vs-the-competition)
  - [Usage](#usage)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Example](#example)
      - [search](#search)
      - [get_image](#get-image)
      - [find_tags](#find_tags)
  - [booru.resolve()](#booruresolve)
  - [Import specific booru client](#search)
  - [Testing cases](https://github.com/sinkaroid/booru/actions)
      - [The core](https://github.com/sinkaroid/booru/actions)
      - [Tags completion](https://github.com/sinkaroid/booru/actions/workflows/find_tags.yml)
  - [Documentation](#documentation)
  - [Legal](#legal)  

----

<div align="center">

<a href="https://sinkaroid.github.io/booru"><img src="https://github.com/sinkaroid/booru/actions/workflows/docs.yml/badge.svg"></a>
<a href="https://github.com/sinkaroid/booru/actions/workflows/find_tags.yml"><img src="https://github.com/sinkaroid/booru/workflows/Tags completion/badge.svg"></a>
<a href="https://codeclimate.com/github/sinkaroid/booru/maintainability"><img src="https://api.codeclimate.com/v1/badges/c334d91994d1d84b8d7d/maintainability" /></a>

Python bindings for the imageboards.
It is takes a much more functionalities to interacts with ease, and featureful. Making your interaction significantly tidier, less of pain, and hopefully will be reusable.

<b>
<a href="https://github.com/sinkaroid/booru/blob/master/CONTRIBUTING.md">Contributing</a> •
<a href="https://sinkaroid.github.io/booru">Documentation</a> •
<a href="https://github.com/sinkaroid/booru/issues/new/choose">Report Issues</a>
</b>
</div>

## Features
- Plenty of imageboards
- Search random & gacha object
- Tags block, resolved safety tags concerns
- Tags finder, tags & query completion
- Parses and returns the image only
- Documented and tested
- Easy to use, check your intelisense

## Usage
Async context, and it's recommended use [asyncio](https://docs.python.org/3/library/asyncio.html) / https://sinkaroid.github.io/booru

### Prerequisites
<table>
	<td><b>NOTE:</b> Python 3.7 or above</td>
</table>

### Installation
`pip install booru`


## This library vs. the Competition

**Features availability** for this library 

| Booru                                       | Status                                                                                                                                                   | Random | Tags block | Tags finder     | Get images     | Gacha     |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- | ----- | ----- | ----- | 
| [Gelbooru](https://gelbooru.com/)           | [![status](https://github.com/sinkaroid/booru/workflows/Gelbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/gel.yml)            | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Danbooru](https://danbooru.donmai.us/)     | [![status](https://github.com/sinkaroid/booru/workflows/Danbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/danbo.yml)  | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Rule34](https://rule34.xxx)                | [![status](https://github.com/sinkaroid/booru/workflows/Rule34/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/r34.yml)        | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Realbooru](https://realbooru.com/)         | [![status](https://github.com/sinkaroid/booru/workflows/Realbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/real.yml)       | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Tbib](https://tbib.org/)                   | [![status](https://github.com/sinkaroid/booru/workflows/Tbib/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/tbib.yml)   | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Xbooru](https://xbooru.com/)               | [![status](https://github.com/sinkaroid/booru/workflows/Xbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/xbo.yml)    | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Safebooru](https://safebooru.org/)         | [![status](https://github.com/sinkaroid/booru/workflows/Safebooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/safe.yml)   | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Yandere](https://yande.re/)                | [![status](https://github.com/sinkaroid/booru/workflows/Yandere/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/yande.yml)   | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Lolibooru](https://lolibooru.moe/)         | [![status](https://github.com/sinkaroid/booru/workflows/Lolibooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/loli.yml)    | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Konachan](https://konachan.com/)           | [![status](https://github.com/sinkaroid/booru/workflows/Konachan/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/kona.yml)    | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Konachan.net](https://konachan.net/)       | [![status](https://github.com/sinkaroid/booru/workflows/KonachanNet/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/konanet.yml) | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Hypnohub](https://hypnohub.net/)           | [![status](https://github.com/sinkaroid/booru/workflows/Hypnohub/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/hypno.yml)  | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [E621](https://e621.net/)                   | [![status](https://github.com/sinkaroid/booru/workflows/E621/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/e6.yml)     | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 
| [E926](https://e926.net/)                   | [![status](https://github.com/sinkaroid/booru/workflows/E926/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/e9.yml)     | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 
| [Derpibooru](https://derpibooru.org/)       | [![status](https://github.com/sinkaroid/booru/workflows/Derpibooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/derpi.yml)   | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 
| [Furbooru](https://furbooru.org/)           | [![status](https://github.com/sinkaroid/booru/workflows/Furbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/fur.yml)     | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 
| [ATFbooru](https://booru.allthefallen.moe/) | [![status](https://github.com/sinkaroid/booru/workflows/ATFbooru/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/atf.yml)    | `Yes`      | `Yes`      | `Yes` | `Yes` | `Yes` | 
| [Behoimi](http://behoimi.org/)              | [![status](https://github.com/sinkaroid/booru/workflows/Behoimi/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/behoi.yml)   | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 
| [Paheal](https://rule34.paheal.net/)        | [![status](https://github.com/sinkaroid/booru/workflows/Paheal/badge.svg)](https://github.com/sinkaroid/booru/actions/workflows/paheal.yml)     | `Yes`      | `No`      | `No` | `Yes` | `Yes` | 

## Example
### **search()**
Takes parameter `(query: str, block: str = "", limit: int = 100, page: int = 1, random: bool = True, gacha: bool = False)`
```py
import asyncio
import booru

async def main():
    dan = booru.Danbooru()
    res = await dan.search(query="cat_girl", block="futanari")
    print(res) ## this is <class 'str'>
    print(booru.resolve(res)) ## this is <class 'list'>

asyncio.run(main())
```  
- You will never gets content which contains futa tags.

You can also import specific booru client.
```py
from booru import Rule34
some_booru = Rule34()

## do with r34
```

### **search_image()**
Takes parameter `search_image(query: str, block: str = "", limit: int = 100, page: int = 1)`
```py
import asyncio
from booru import Rule34

async def main():
    r34 = Rule34()
    img = await r34.search(query="cat_girl", block="futanari")
    print(img)

asyncio.run(main())
```  
- This will parses image url only, instead object

### **find_tags()**
```py
import asyncio
from booru import Danbooru

async def main():
    dan = Danbooru()
    find_tags = await dan.find_tags("jeanne") ## arbitrary tags
    print(find_tags)

asyncio.run(main())
```
Returns
```js
[   
    "jeanne_d'arc_alter_(fate)",
    "jeanne_d'arc_(fate)",
    "jeanne_d'arc_(fate)+ai:jeanne_d'arc_(fate)%2C0%25",
    "jeanne_d'arc_alter_(avenger)_(fate)",
    "jeanne_d'arc_(ruler)_(fate)"
]
```
- No more sussy tags, use this for validating query in related imageboards. 
- Get the `get_proper_tags[0]` for the best predicts.

## booru.resolve()
You will need this for every object, this library designed to be neat and clean returns, although it must be reparsed to the string first, that's why `booru.resolve()` exist.

## Documentation
The documentation can be found https://sinkaroid.github.io/booru

## Legal
This tool can be freely copied, modified, altered, distributed without any attribution whatsoever. However, if you feel
like this tool deserves an attribution, mention it. It won't hurt anybody