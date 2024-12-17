title = r"""
▗▖  ▗▖   ▐▌█  ▐▌▄▄▄▄  ▗▞▀▚▖ ▄▄▄  ▄▄▄▄
▐▛▚▞▜▌   ▐▌▀▄▄▞▘█   █ ▐▛▀▀▘█   █ █   █
▐▌  ▐▌▗▞▀▜▌     █   █ ▝▚▄▄▖▀▄▄▄▀ █   █
▐▌  ▐▌▝▚▄▟▌         ▗▄▖
                   ▐▌ ▐▌
                    ▝▀▜▌
                   ▐▙▄▞▘
"""
win_msg = r"""
.  .   .  .
 \  \ /  /
  \  \  /.  . .-...--..-.  .--. .-.
   \/ \/ |  |(   ||  (   ) |  |(   )
    ' '  `--| `-`|'   `-'`-'  `-`-'`-
            ; ._.'
         `-'
"""
lose_msg = r"""
  _____
 |  __ \
 | |__) | __ _______  __ _ _ __ __ _ _ __   __ _
 |  ___/ '__|_  / _ \/ _` | '__/ _` | '_ \ / _` |
 | |   | |   / /  __/ (_| | | | (_| | | | | (_| |
 |_|   |_|  /___\___|\__, |_|  \__,_|_| |_|\__,_|
                      __/ |
                     |___/
"""
print("Witajcie w")
print(title)
input("Naciśnij klawisz aby rozpocząć")

print("\033c")
print("Rozpoczyna się twoja przygoda")
name = input("Podaj swoje imię ")

input("Spotykasz wielkiego bossa. Każe ci zapamiętać następująca sekwencję: 🔴🔵🟡🟢")
print("\033c")
answer = int(input("Który numer miało kółko żółte? "))

if answer == 3:
    print(win_msg)
    print(f"Gratulacje {name}, wygrywasz grę")
else:
    print(lose_msg)
    print(f"Nie przejmuj się, {name}, spróbuj jeszcze raz.")
