from models import Proceduri

def addRecordsProceduri():
    with open('/home/cristi/DjangoProjects/TurismMedical/proceduri.txt', r) as f:
        for line in f:
            new_entry = Proceduri(name=line)
            new_entry.save

if __name__ == "__main__":
    addRecordsProceduri()
