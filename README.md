# working with Openrazer

the way that I'm working with [Openrazer](https://openrazer.github.io/)

# config

add to `.zshrc`:

```zsh
function openrazer() {
  python3 Projects/openrazer/set.py $1;
}
```
