import csv, json
# import readline

class Friend():
    def __init__(self, name, surname, birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.name} {self.surname} {self.birthdate}"

def read_csv(filename):
    with open(filename, 'r') as base:
        reader = csv.reader(base)
        next(reader)
        friends = []
        for row in reader:
            friends.append(Friend(*row))
    return friends


def write_csv(filename, friends):
    with open(filename, 'w') as base:
        writer = csv.writer(base)
        writer.writerow(["Name", "Surname", "Birthdate"])
        for friend in friends:
            writer.writerow([friend.name, friend.surname, friend.birthdate])


def read_json(filename):
    with open(filename) as infile:
        data = json.load(infile)
        friends = [Friend(entry["name"], entry["surname"], entry["birthdate"]) for entry in data]
    return friends


def write_json(filename, friends):
    friends = [{"name":friend.name,
                "surname": friend.surname,
                "birthdate": friend.birthdate}
                for friend in friends]
    with open(filename, 'w') as outfile:
        json.dump(friends, outfile)



if __name__ == "__main__":
    while True:
        base = input("Which database would you like to access?\n1. json\n2. csv\n3. quit\n")
        if base not in {'1', '2', '3'}:
            print('Try again. Type "1", "2" or "3"')

        else: break

    if base == '3': exit(0)

    csv_filename, json_filename = "data/friendlist.csv", 'data/friendlist.json'
    friends = read_csv(csv_filename) if base == '2' else read_json(json_filename)

    while True:
        print('\n',50*'*', "\nCurrently saved friends:\n", sep='')
        for i, friend in enumerate(friends):
            print(i, friend)
        print(50*'*' + '\n')


        print("What would you like to do?\n"
            "1. remove a friend\n"
            "2. add a friend\n"
            "3. quit")
        while True:
            choice = input()
            if choice not in {'1', '2', '3'}: print('Try again. Type "1", "2" or "3"')
            else: break

        if choice == '1':
            while True:
                try:
                    friend_id = int(input("Which friend? (enter a corresponding number)\n"))
                    del friends[friend_id]
                    break
                except ValueError:
                    print("An error has occured. Try again.")
                    continue
        elif choice =='2':
            data = input("Enter friend's data in the following format:\nName Surname Birthdate\n")
            friends.append(Friend(*data.split()))
        elif choice == '3': exit(0)

        if base == '1': write_json(json_filename, friends)
        else: write_csv(csv_filename, friends)












