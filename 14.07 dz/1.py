import json
import time


def load_quest(quest_name):
    with open(f"quests/{quest_name}.json", "r", encoding="utf-8") as f:
        quest_data = json.load(f)
    return quest_data


def process_scene(scene, inventory):
    print(scene["DESCRIPTION"])
    time.sleep(2)

    if "ACTIONS" in scene:
        for i, action in enumerate(scene["ACTIONS"], start=1):
            conditions_met = True
            if "when" in action:
                conditions_met = check_conditions(action["when"], inventory)
            
            if conditions_met:
                print(f"{i}. {action['text']}")
        
        choice = input("Выберите действие: ")
        choice_index = int(choice) - 1
        chosen_action = scene["ACTIONS"][choice_index]
        perform_action(chosen_action, inventory)


def check_conditions(conditions, inventory):
    for condition, value in conditions.items():
        if condition == "HAVE":
            if value not in inventory:
                return False
        elif condition == "LACK":
            if value in inventory:
                return False
        elif condition == "MISSED":
            if value in visited_scenes:
                return False
        elif condition == "PASSED":
            if value not in visited_scenes:
                return False
    return True


def perform_action(action, inventory):
    action_type = action["action"]
    if action_type == "GO":
        print(action["response"])
        next_scene = action["target"]
        visited_scenes.add(next_scene)
        process_scene(quest_data["game"][next_scene], inventory)
    elif action_type == "ALERT":
        print(action["response"])
        process_scene(current_scene, inventory)


quest_data = load_quest("quest")

print(f"Добро пожаловать в {quest_data['game_info']['title']}!")
inventory = set()
visited_scenes = {"SCENE_0"}
current_scene = quest_data["game"]["SCENE_0"]
process_scene(current_scene, inventory)
