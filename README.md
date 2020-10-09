# Snake game 🐍

![image](https://user-images.githubusercontent.com/22743709/95580358-1d861800-0a2f-11eb-963e-9b1804537b04.png)

My journey of learning python by creating a [snake game](https://en.wikipedia.org/wiki/Snake_(video_game_genre)).

## Contents 📗
- [Dependencies](#dependencies🕸️)
- [Setup and tests](#setup🔧)

### [Dependencies](https://github.com/C-gyorfi/snake_game/blob/master/Pipfile)🕸️
- Test are run by [Pytest](https://pypi.org/project/pytest/) 🧪 
- Using the assertion library [Assertpy](https://github.com/assertpy/assertpy) 🗣️ 
- Test coverage: [Pytest-cov](https://pypi.org/project/pytest-cov/) 💯 
- Linting: [Pylint](https://pypi.org/project/pylint/) 👌
- [Autopep8](https://pypi.org/project/autopep8/) for automatically fix styling errors 🦾

### [Setup](https://github.com/C-gyorfi/snake_game/blob/master/Makefile)🔧

To run the tests you will need to install python3 and pipenv:
```bash
brew install python3 pipenv
```
Install dev dependency's
```bash
make setup
```
Run tests
```bash
make tests
```
Run linting
```bash
make lint
```
Auto fix linting errors
```bash
make auto-lint
```
