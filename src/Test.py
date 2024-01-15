def evaluate_rule(rule, facts):
    conditions = rule['conditions']
    for condition in conditions:
        if not facts.get(condition, False):
            return False
    return True

def main():
    potatoes_diseases = {
        'P001': 'Penyakit Busuk Daun (Late Blight)',
        'P002': 'Penyakit Layu Bakteri (Ralstonia Solanacearum)',
        'P003': 'Penyakit Busuk Umbi',
        'P004': 'Penyakit Daun Menggulung',
        'P005': 'Penyakit Bercak Kering (Early Blight)'
    }

    potatoes_symptoms = {
        'G001': 'Timbul bercak-bercak basah pada bagian tepi daun atau tengah daun?',
        'G002': 'Warna bercak-bercak berubah menjadi coklat sampai hitam, selanjutnya daun akan membusuk dan mati?',
        'G003': 'Daun-daun menjadi layu yang dimulai dari daun muda atau pucuk, dan daun bagian bawah menguning?',
        'G004': 'Pembuluh pada pangkal batang berwarna coklat, dan bila ditekan akan keluar lendir yang berwarna abu-abu keruh?',
        'G005': 'Penyakit sampai ke umbi dengan gejala bercak yang berwarna coklat sampai hitam pada bagian ujung umbi?',
        'G006': 'Daun menguning dan menggulung lalu layu dan kering?',
        'G007': 'Pada bagian umbi terdapat bercak-bercak berwarna coklat?',
        'G008': 'Infeksi akan menyebabkan akar dan umbi mudah busuk?',
        'G009': 'Daun-daun yang sakit menggulung ke atas?',
        'G010': 'Dari tepi ke arah ibu tulang, kadang-kadang menyerupai tabung, jika dipegang daun terasa lebih kaku?',
        'G011': 'Secara keseluruhan warna daun tanaman sakit lebih pucat, kurus, dan tegak dari pada daun sehat, dan umbi-umbi yang dihasilkan berukuran lebih kecil?',
        'G012': 'Daun terinfeksi berbercak kecil yang tersebar tidak teratur?',
        'G013': 'Daun berwarna coklat tua lalu meluas ke daun muda?',
        'G014': 'Permukaan kulit umbi berbercak gelap?'
    }

    potatoes_rules = {
        1: {'conditions': ['G001', 'G002'], 'conclusion': 'P001'},
        2: {'conditions': ['G003', 'G004', 'G005', 'G008'], 'conclusion': 'P002'},
        3: {'conditions': ['G006', 'G007', 'G008'], 'conclusion': 'P003'},
        4: {'conditions': ['G009', 'G010', 'G011'], 'conclusion': 'P004'},
        5: {'conditions': ['G012', 'G013', 'G014'], 'conclusion': 'P005'},
    }

    potatoes_facts = {symptom: False for symptom in potatoes_symptoms}

    # Evaluating rules and updating facts
    for key, value in potatoes_symptoms.items():
        user_input = input(f"Apakah kentang anda mengalami {value}. Enter 'ya' or 'tidak': ")
        if user_input.lower() == 'ya':
            potatoes_facts[key] = True
        elif user_input.lower() == 'tidak':
            potatoes_facts[key] = False

    for key, rule_value in potatoes_rules.items():
        if evaluate_rule(rule_value, potatoes_facts):
            print(f"Anda mungkin mengalami: {potatoes_diseases[rule_value['conclusion']]}")
            break
    else:
        print("Tidak ada diagnosis yang sesuai dengan gejala yang kentang alami.")

main()