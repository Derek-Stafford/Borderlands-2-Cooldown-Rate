base = float(input("Base Cooldown (in seconds): "))
skills = float(input("Additional Cooldown Increase Percentage from skills (not including skills involving enemies): "))
class_mod = float(input("Cooldown Increase from your class mod = "))
relic = float(input("Cooldown Increase from your relic = "))
total = (skills + class_mod + relic)/100
effective = base/(1+total)
print(f"Your effective cooldown is {effective:.2f} seconds")