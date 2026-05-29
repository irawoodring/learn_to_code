def process_player_input(command, player, world):
    command = command.lower().strip()

    if command == "":
        return "You must enter a command."

    words = command.split()

    if len(words) == 1:
        verb = words[0]
        target = None
    else:
        verb = words[0]
        target = " ".join(words[1:])

    # Movement commands
    if verb == "go" or verb == "move" or verb == "walk":
        if target is None:
            return "Go where?"

        if target == "north":
            if "north" in world[player["location"]]["exits"]:
                player["location"] = world[player["location"]]["exits"]["north"]

                if player["location"] == "dark_cave":
                    if "torch" not in player["inventory"]:
                        player["health"] -= 10
                        return "You stumble in the dark cave and lose 10 health."

                return f"You move north to {player['location']}."
            else:
                return "You cannot go north."

        elif target == "south":
            if "south" in world[player["location"]]["exits"]:
                player["location"] = world[player["location"]]["exits"]["south"]
                return f"You move south to {player['location']}."
            else:
                return "You cannot go south."

        elif target == "east":
            if "east" in world[player["location"]]["exits"]:
                if world[player["location"]].get("locked_east"):
                    if "rusty key" in player["inventory"]:
                        world[player["location"]]["locked_east"] = False
                        player["location"] = world[player["location"]]["exits"]["east"]
                        return "You unlock the eastern gate and proceed."
                    else:
                        return "The eastern gate is locked."
                else:
                    player["location"] = world[player["location"]]["exits"]["east"]
                    return f"You move east to {player['location']}."
            else:
                return "You cannot go east."

        elif target == "west":
            if "west" in world[player["location"]]["exits"]:
                player["location"] = world[player["location"]]["exits"]["west"]
                return f"You move west to {player['location']}."
            else:
                return "You cannot go west."

        else:
            return "Unknown direction."

    # Inventory commands
    elif verb == "take" or verb == "grab" or verb == "pick":
        if target is None:
            return "Take what?"

        room_items = world[player["location"]]["items"]

        if target in room_items:
            if len(player["inventory"]) >= player["max_inventory"]:
                return "Your inventory is full."

            if target == "cursed idol":
                player["cursed"] = True
                player["health"] -= 20

            player["inventory"].append(target)
            room_items.remove(target)

            if target == "gold coin":
                player["gold"] += 1

            return f"You take the {target}."
        else:
            return f"There is no {target} here."

    elif verb == "drop":
        if target is None:
            return "Drop what?"

        if target in player["inventory"]:
            player["inventory"].remove(target)
            world[player["location"]]["items"].append(target)

            if target == "torch":
                if player["location"] == "dark_cave":
                    player["health"] -= 5
                    return "You dropped the torch. Darkness surrounds you."

            return f"You dropped the {target}."
        else:
            return "You do not have that item."

    elif verb == "inventory" or verb == "inv":
        if len(player["inventory"]) == 0:
            return "Your inventory is empty."
        else:
            return "Inventory: " + ", ".join(player["inventory"])

    # Combat commands
    elif verb == "attack" or verb == "fight":
        if target is None:
            return "Attack what?"

        enemies = world[player["location"]].get("enemies", [])

        if target in enemies:
            if "sword" in player["inventory"]:
                damage = 25
            elif "dagger" in player["inventory"]:
                damage = 10
            else:
                damage = 2

            if target == "dragon":
                if "magic shield" not in player["inventory"]:
                    player["health"] -= 50

                    if player["health"] <= 0:
                        return "The dragon burns you alive."

                if "dragon" in enemies:
                    enemies.remove("dragon")
                    player["xp"] += 100
                    return "You slay the dragon!"

            elif target == "goblin":
                player["health"] -= 5

                if player["health"] <= 0:
                    return "The goblin defeats you."

                enemies.remove("goblin")
                player["xp"] += 10
                return "You defeat the goblin."

            elif target == "ghost":
                if "holy water" in player["inventory"]:
                    enemies.remove("ghost")
                    player["xp"] += 30
                    return "The ghost vanishes."
                else:
                    return "Your attacks pass through the ghost."

            else:
                enemies.remove(target)
                player["xp"] += 5
                return f"You defeat the {target}."

        else:
            return "There is nothing like that here."

    # Use item commands
    elif verb == "use":
        if target is None:
            return "Use what?"

        if target not in player["inventory"]:
            return "You do not have that item."

        if target == "health potion":
            if player["health"] >= 100:
                return "Your health is already full."

            player["health"] += 30

            if player["health"] > 100:
                player["health"] = 100

            player["inventory"].remove("health potion")
            return "You drink the health potion."

        elif target == "torch":
            if player["location"] == "dark_cave":
                return "The cave is illuminated."

            return "You wave the torch around."

        elif target == "magic scroll":
            if player["mana"] >= 50:
                return "Your mana is already full."

            player["mana"] += 50

            if player["mana"] > 50:
                player["mana"] = 50

            player["inventory"].remove("magic scroll")
            return "Arcane energy fills your body."

        elif target == "rusty key":
            if world[player["location"]].get("locked_chest"):
                world[player["location"]]["locked_chest"] = False
                return "You unlock the chest."
            else:
                return "Nothing happens."

        else:
            return "You cannot use that item."

    # Dialogue commands
    elif verb == "talk":
        if target is None:
            return "Talk to whom?"

        npcs = world[player["location"]].get("npcs", [])

        if target in npcs:
            if target == "merchant":
                if player["gold"] >= 10:
                    return "Merchant: Interested in rare goods?"
                else:
                    return "Merchant: Come back when you have more gold."

            elif target == "wizard":
                if player["xp"] >= 100:
                    player["spells"].append("fireball")
                    return "Wizard: I shall teach you fireball."
                else:
                    return "Wizard: You are not experienced enough."

            elif target == "guard":
                if player.get("criminal_record"):
                    return "Guard: You're under arrest!"
                else:
                    return "Guard: Stay out of trouble."

            else:
                return f"You speak with {target}."

        else:
            return "Nobody by that name is here."

    # Look command
    elif verb == "look":
        room = world[player["location"]]

        description = room["description"]

        if len(room["items"]) > 0:
            description += "\nItems: " + ", ".join(room["items"])

        if len(room.get("enemies", [])) > 0:
            description += "\nEnemies: " + ", ".join(room["enemies"])

        if len(room.get("npcs", [])) > 0:
            description += "\nPeople: " + ", ".join(room["npcs"])

        description += "\nExits: " + ", ".join(room["exits"].keys())

        return description

    # Status command
    elif verb == "status":
        return (
            f"Health: {player['health']}\n"
            f"Mana: {player['mana']}\n"
            f"XP: {player['xp']}\n"
            f"Gold: {player['gold']}"
        )

    # Quit command
    elif verb == "quit":
        player["quit"] = True
        return "Game over."

    else:
        return "Unknown command."
