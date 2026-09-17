# SolarDim color theme for JetBrains IDEs

[← Back to root](https://github.com/RDMCz/SolarDim-JetBrains)

## TODO

* [ ] Colors of things other than programming language keywords
  * [x] ~~Highlighted item in context menus – change it from gray to orange~~
  * [ ] Text selection – I think VS Code looks better to me
  * [ ] Add border around error explaination pop-ups
  * [ ] Full width infos/warnings (e.g. Python interpreter not set) are maybe too bright?
  * [ ] Make version control colors in file list same as in VS Code? (green==new, yellow==changed)
  * [ ] Make side panel different color like in VS Code?
* [ ] —————
* [x] C++&ensp;(CLion)
* [x] C#&ensp;(Rider)
* [x] Go&ensp;(Goland)
* [x] Java&ensp;(IntelliJ IDEA)
* [x] JavaScript&ensp;(WebStorm)
* [ ] Kotlin
* [ ] PHP&ensp;(PhpStorm)
* [x] Python&ensp;(PyCharm)
* [ ] Ruby&ensp;(RubyMine)
* [x] Rust&ensp;(RustRover)
* [ ] SQL&ensp;(DataGrip)
* [ ] —————
* [ ] Markdown
* [x] JSON
* [x] XML, HTML
* [x] CSS
* [ ] —————

## Known issues

* Some changes in `scheme.xml` do nothing. The IDE sees the color I have set, but _"Inherit values from:"_ checkbox is checked inside _Color Scheme_ settings. Example: it doesn't matter what I set `MARKDOWN.HEADER_LEVEL_1` to, because in settings it says _"Inherit values from: Identifiers→Constants (Language Defaults)"_ and Markdown header is always purple. I do not know how to make it unchecked from `scheme.xml`.

* There are some keywords, which seem to be explicitly set to some color value (not inherited), but they don't appear anywhere in `scheme.xml`... where do they come from? (e.g. `"org.rust.CRATE"` = `#835DDA`)

* Boolean values cannot be styled independently in JetBrains IDEs :(

* Gray text on gray background, e.g. when hitting Ctrl+F in _Editor → Color Scheme_ settings

* White icons on light background, e.g. run icon when the file is not runnable
