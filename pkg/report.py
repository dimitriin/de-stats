class Report:

    def __init__(self):
        self.skill_dict = {}

    def add_skill(self, skill):
        skill = skill.lower()
        if skill not in self.skill_dict:
            self.skill_dict[skill] = 0
        self.skill_dict[skill] += 1

    def get_top_skills(self, top_count):
        ordered_dict = {k: v for k, v in sorted(self.skill_dict.items(), reverse=True, key=lambda item: item[1])}
        return dict(list(ordered_dict.items())[0: top_count])
