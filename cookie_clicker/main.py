from run_game import RunGame
import time

run_game = RunGame()
last_check_time = 0
OG_TIME = -1

while True:
    run_game.click_cookie()
    if OG_TIME == -1:
        OG_TIME = time.time()
    if time.time() - last_check_time >= 5:
        last_check_time = time.time()
        if run_game.check_upgrade_availability():
            run_game.buy_upgrade()
    if time.time() - OG_TIME >= 15:
        print(f"Cookies/Second:{run_game.get_score()}")
        run_game.stop()
        break