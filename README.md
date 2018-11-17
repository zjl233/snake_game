# snake_game

## screenshot

![alt screenshot](images/snake_game.gif)

## install

prerequest

1. python 3.6
2. pip3
3. pipenv

```bash
git clone https://github.com/zjl233/snake_game.git
pipenv install
pipenv shell
pyinstaller src/main.py -n snake_game -F
cp dist/snake_game /usr/bin/
```

# run

```bash
snake_game
```

# uninstall

```bash
rm /usr/bin/snake_game
```

