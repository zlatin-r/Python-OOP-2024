from project.band_members.musician import Musician


class Singer(Musician):
    TYPE_ = "Singer"
    SINGER_AVAILABLE_SKILLS = ("sing high pitch notes", "sing low pitch notes")

    def __init__(self, name, age):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.SINGER_AVAILABLE_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."
