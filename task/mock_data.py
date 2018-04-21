
import random
from faker import Faker

my_faker = Faker()
random_person = []
num_2_gen = 9

def mock_generator(num, data_list):
    for i in range(num):
        data_list.append(my_faker.free_email())
        data_list.append(my_faker.file_name())
        data_list.append(my_faker.last_name())
        data_list.append(my_faker.city())
        data_list.append(my_faker.country())
        data_list.append(my_faker.numerify()+my_faker.numerify()+my_faker.numerify())

mock_generator(num_2_gen, random_person)
print random_person



