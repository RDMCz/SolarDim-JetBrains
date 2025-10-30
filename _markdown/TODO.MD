# SolarDim color theme for JetBrains IDEs

[← Back to root](https://github.com/RDMCz/SolarDim-JetBrains)

## TODO

My most-used JetBrains IDE these days is probably PyCharm, and I'm happy with how Python currently looks with this color theme. I would like to review the colors for other languages and I would also like them to be the same as in SolarDim for VS Code. This plugin inherits from _solarized_ by _espositocode_, while the VS Code extension inherits from _vscode-better-solarized_ by _edheltzel_. I prefer some color decisions from one theme and some from the other (whether these were intentional or implied), so deciding how SolarDim should approach colors for other languages isn't straightforward.

* [ ] Colors of things other than programming language keywords
  * [ ] Make version control colors in file list same as in VS Code (green==new, yellow==changed)
  * [ ] Highlighted item in context menus – change it from gray to orange (like in VS Code)
  * [ ] Text selection – I think VS Code looks better to me
  * [ ] Add border around error explaination pop-ups
  * [ ] Full width infos/warnings (eg Python interpreter not set) are maybe too bright?
  * [ ] Make side panel different color like in VS Code?
* [x] Python
* [x] Rust
* [ ] Go
* [ ] JavaScript
* [ ] ...
* [ ] Markdown
* [ ] JSON
* [ ] XML, HTML
* [ ] CSS
* [ ] C++ & C# (I usually use Visual Studio 2022 for these)

## Known issues

* Some changes in `scheme.xml` do nothing. The IDE sees the color I have set, but _"Inherit values from:"_ checkbox is checked inside _Color Scheme_ settings. Example: it doesn't matter what I set `MARKDOWN.HEADER_LEVEL_1` to, because in settings it says _"Inherit values from: Identifiers→Constants (Language Defaults)"_ and Markdown header is always purple. I do not know how to make it unchecked from `scheme.xml`.

* There are some keywords, which seem to be explicitly set to some color value (not inherited), but they don't appear anywhere in `scheme.xml`... where do they come from? (eg `"org.rust.CRATE"` = `#835DDA`)

* Boolean values cannot be styled independently in JetBrains IDEs :(
