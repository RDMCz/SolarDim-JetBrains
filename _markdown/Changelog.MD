# SolarDim color theme for JetBrains IDEs

[← Back to root](https://github.com/RDMCz/SolarDim-JetBrains)

## Changelog

### 0.1.1

* C++ struct field foreground color changed from blue to dark cyan
* _ParameterInfo currentOverloadBackground_: fixed dark foreground on dark background

### 0.1.0

* __C++__, __Go__, __JavaScript__ review

* Changed some language defaults (class_name→yellow, doc_comment→gray, keyword→violet, string→green, string_escape→magenta)

  * (This may bring languages I haven't reviewed yet more closer to SolarDim colors, or on the other hand, it may reduce the variability of the colors used in these languages. Because, for example, they can inherit the keyword color, which is now violet, but also have the violet color set explicitly for a different token type.) ¯\\\_(ツ)\_/¯

### 0.0.2

* __Rust__ review

### 0.0.1

* Initial release
* Changes compared to _solarized_ v1.5:
  * Base colors: _"Solarized Light colors"_ were swapped for _"SolarDim Colors"_
  * __Python__ review
  * Altered project structure and replaced all _"magic colors"_ with _"variables"_
