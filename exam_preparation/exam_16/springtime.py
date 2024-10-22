def start_spring(**kwargs):
    spring_dict = {}
    for spring_object, obj_type in kwargs.items():
        if obj_type not in spring_dict:
            spring_dict[obj_type] = []
        spring_dict[obj_type].append(spring_object)

    sorted_spring_dict = sorted(spring_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for obj_type, objects in sorted_spring_dict:
        result += f'{obj_type}:\n'
        for obj in sorted(objects):
            result += f'-{obj}\n'

    return result.strip()


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))


example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
