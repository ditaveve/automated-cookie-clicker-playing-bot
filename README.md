# Cookie Clicker Bot

Uses Selenium to automatically play [Cookie Clicker](https://ozh.github.io/cookieclicker/): selects the English language, clicks the big cookie continuously, buys available upgrades every 5 seconds, and stops itself after a fixed run time, printing the final cookies-per-second score.

## Setup

Requires `selenium` and a Chrome browser (chromedriver is managed automatically by Selenium 4+):

```bash
pip install selenium
```

## Running

```bash
python3 main.py
```

## Changing how long it runs before stopping

By default, the bot clicks for **300 seconds** before stopping itself. This is controlled by the number in [main.py](main.py):

```python
if time.time() - OG_TIME >= 300:
    print(f"Cookies/Second:{run_game.get_score()}")
    run_game.stop()
    break
```

To change the run duration, replace `15` with the number of seconds you want it to run for before it prints the score and stops. For example, to run for 2 minutes instead:

```python
if time.time() - OG_TIME >= 120:
```
