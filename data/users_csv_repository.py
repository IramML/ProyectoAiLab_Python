import csv
from domain.user import User

class UsersCSVRepository():
    def __init__(self) -> None:
        self.fileName = 'persons.csv'

   
    def create_user(self, username, password):
        persons_rows = self.__get_persons_rows()
        with open(self.fileName, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
             
            if not persons_rows:
                persons_header = ['Username', 'Contrasena', 'Nivel', 'Personaje']
                filewriter.writerow(persons_header)
            else:
                for row in persons_rows:
                    filewriter.writerow(row)
                    if row[0] == username:
                        return 'taken'
            
            user = [username, password, 1]
            filewriter.writerow(user)
            User.currentUser = User(user[0], user[1], user[2], None)
            csvfile.close()
            return 'success'

    def login_user(self, username, password):
        persons_rows = self.__get_persons_rows()
        for row in persons_rows:
            if row[0] == username and row[1] == password:
                pokepy_id = None
                if row[3]:
                    pokepy_id = row[3]
                User.currentUser = User(row[0], row[1], int(row[2]), int(pokepy_id))
                return 'success'

        return 'no_user'

    def __get_persons_rows(self):
        persons = []
        try:
            with open(self.fileName, 'r') as f:
                try:
                    reader = csv.reader(f)
                    
                    for row in reader:
                        if row:
                            persons.append(row)
                finally:
                    f.close()
        finally:
            return persons

    def choose_history_pymon(self, pymon_number):
        persons_rows = self.__get_persons_rows()
        rows = []
        for row in persons_rows:
            if row[0] == User.currentUser.name:
                row = [row[0], str(row[1]), str(row[2]), str(pymon_number + 1)]
                User.currentUser = User(row[0], row[1], int(row[2]), int(row[3]))
                rows.append(row)
            else:
                rows.append(row)


        with open(self.fileName, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in rows:
                    filewriter.writerow(row)

            csvfile.close()
            return True

    def upgrade_level(self, new_level):
        persons_rows = self.__get_persons_rows()
        rows = []
        for row in persons_rows:
            if row[0] == User.currentUser.name:
                row = [row[0], row[1], new_level, row[3]]
                User.currentUser = User(row[0], row[1], int(row[2]), int(row[3]))
                rows.append(row)
            else:
                rows.append(row)


        with open(self.fileName, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in rows:
                    filewriter.writerow(row)

            csvfile.close()
            return True

    