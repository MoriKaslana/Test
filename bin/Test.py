class AutismDiagnosisSystem:
    def __init__(self):
        self.facts = {}
        self.rules = {
            'rule1': {'social_interaction': False, 'communication_skills': False, 'repetitive_behavior': True},
            'rule2': {'social_interaction': True, 'communication_skills': False, 'repetitive_behavior': True},
            'rule3': {'social_interaction': False, 'communication_skills': True, 'repetitive_behavior': True},
            'rule4': {'social_interaction': True, 'communication_skills': True, 'repetitive_behavior': False}
        }

    def add_fact(self, fact, value):
        self.facts[fact] = value

    def forward_chaining(self):
        while True:
            new_facts = False
            for rule, conditions in self.rules.items():
                if rule not in self.facts:
                    if all(self.facts[condition] == conditions[condition] for condition in conditions):
                        self.facts[rule] = True
                        new_facts = True

            if not new_facts:
                break

    def diagnose_autism(self):
        self.forward_chaining()

        print("Hasil Diagnosis Autisme:")
        if self.facts.get('rule4', False):
            print("Pasien tidak mengalami autisme.")
        else:
            print("Pasien mungkin mengalami autisme. Konsultasikan dengan spesialis untuk evaluasi lebih lanjut.")


# Membuat instance sistem pakar autisme
autism_system = AutismDiagnosisSystem()

# Menambahkan fakta awal
autism_system.add_fact('social_interaction', True)
autism_system.add_fact('communication_skills', False)
autism_system.add_fact('repetitive_behavior', True)

# Menjalankan diagnosa autisme
autism_system.diagnose_autism()
