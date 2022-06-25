def dict_to_sort_tuple(_dict):
    return tuple(sorted(_dict.items()))


class DictIterator:
    def __init__(self, _dict):
        self.index = 0
        self.indexes = sorted(_dict.keys())

    def __next__(self):
        if self.index < len(self.indexes):
            self.index += 1
            return self.indexes[self.index - 1]

        raise StopIteration


class Armor:
    def add(self, adding_key):
        self.armor_and_quantity_dict[adding_key] = self.armor_and_quantity_dict.setdefault(adding_key, 0) + 1

    def __init__(self, *armor_and_quantity):
        self.armor_and_quantity_dict = dict(armor_and_quantity)

    def __repr__(self):
        if len(self.armor_and_quantity_dict) == 1:
            return "Armor" + str(dict_to_sort_tuple(self.armor_and_quantity_dict))[:-2] + ')'

        return "Armor" + str(dict_to_sort_tuple(self.armor_and_quantity_dict))


class GhostInArmor(Armor):
    def items(self):
        return list(dict_to_sort_tuple(self.armor_and_quantity_dict))

    def __delitem__(self, key):
        if key in self.armor_and_quantity_dict:
            del self.armor_and_quantity_dict[key]

    def __getitem__(self, item):
        return self.armor_and_quantity_dict.get(item)

    def __init__(self, *armor_and_quantity, name="Canterville"):
        super().__init__(*armor_and_quantity)
        self.name = name

    def __iter__(self):
        return DictIterator(self.armor_and_quantity_dict)

    def __len__(self):
        return len(self.armor_and_quantity_dict)

    def __repr__(self):
        if len(self.armor_and_quantity_dict) == 0:
            return f"GhostInArmor(name='{self.name}')"

        elif len(self.armor_and_quantity_dict) == 1:
            return f"GhostInArmor{str(dict_to_sort_tuple(self.armor_and_quantity_dict))[:-1]} name='{self.name}')"

        else:
            return f"GhostInArmor{str(dict_to_sort_tuple(self.armor_and_quantity_dict))[:-1]}, name='{self.name}')"
