# zola-academic

A theme inspired by [Hugo Academic](https://github.com/gcushen/hugo-academic) for [Zola](https://www.getzola.org).

![A screenshot of the zola-academic theme](https://raw.githubusercontent.com/tforgione/zola-academic/master/screenshot-cropped.png)

# Getting started

You should first [install Zola](https://www.getzola.org/documentation/getting-started/installation/).

Once that's done, you can create your page by entering

``` bash
zola init my-page-name
```

Then, you need to add the zola-academic theme to your page

``` bash
cd my-page-name/themes
git clone https://github.com/tforgione/academic-zola
```

and add the following in your `config.toml` **before** the `[extra]`:
```
theme = "zola-academic"
```
