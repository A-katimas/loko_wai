# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jtardieu <jtardieu@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/22 17:36:49 by jtardieu          #+#    #+#              #
#    Updated: 2026/02/04 18:39:40 by jtardieu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    __instance = [];

    def __init__(self, name ,starting_height ,starting_age):
        self.set_name(name)
        self.set_height(int (starting_height));
        self.set_age(int(starting_age));
        Plant.__instance.append(self);
        print(f"{self}")

    def older(self):
        self.grow();
        self.set_age(int (self.age) + int(1));

    def grow(self):
        self.set_height(int(self.height) +int(1));

    def set_height(self, new_height):
        self.height = new_height;

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self,name):
        self.name = name

    @classmethod
    def print_instance(cls) :
        for plant in (Plant.__instance):
            print(f"Current {"".join(list(reversed(plant.__class__.__name__)))}:", plant.name,f"({plant.height}cm, {plant.age} days)")
        print("\n");

    def __repr__(self):
        table = {"flower": f"{1} is blowmingh",
            "tree": f"{1} provide shadow ",
            "vegetabels": f"covers {1} is rich on viutamin d"}
        return ("")

class Flower (Plant) :
    __instance_flower = [];

    def __init__ (self ,name ,starting_height ,starting_age , color ):
        self.color = color;
        super().__init__(name ,starting_height, starting_age)
        Flower.__instance_flower.append(self);

    def bloom(self):
        return(f"{self.name} is blooming beautifully!")

    @classmethod
    def print_instance(cls) :
        for flower in (cls.__instance_flower):
            print(f"Current {flower.__class__.__name__}:", flower.name,f"({flower.height}cm, {flower.age} days)")
        print("\n");

    def __repr__(self):
        return(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

class Tree (Plant) :
    __instance_tree = [];

    def __init__(self, name, starting_height, starting_age,  trunk_diameter):
        diameter =  trunk_diameter
        super().__init__(name, starting_height, starting_age)
        Tree.__instance_tree.append(self);

    def produce_shade(slef):
        return(f"Oak provides 78 square meters of shade")

    @classmethod
    def print_instance(cls) :
        for tree in (cls.__instance_tree):
            print(f"Current {Tree.__class__.__name__}:", tree.name,f"({tree.height}cm, {tree.age} days)")
        print("\n");

    def __repr__(self):
        return(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

def main():
    print("=== Garden Plant Types ===")
    jardin = [Flower("Rose", 44, 5, "red"),
              Plant("oack",150,3),
              Plant("pamplemouse",13,3)]
    print(jardin[0].bloom());

    Plant.print_instance();
    Flower.print_instance();

if __name__ == "__main__":
    main();
