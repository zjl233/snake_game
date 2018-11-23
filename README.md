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
cd snake_game
pipenv install
pipenv shell
pyinstaller src/main.py -n snake -F
cp dist/snake /usr/bin/
```

# run

```bash
snake
```

# uninstall

```bash
rm /usr/bin/snake
```

