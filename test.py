import time
import pymssql
from sql_faker.data_faker import insert, uuid4, name, job, company, email, ssn, date_of_birth, address, phone
from sql_faker.prizes import one_value_prizes
start = time.time()

def data() -> dict[str, str | int]:
    return {
        'id': uuid4(),
        'name': name(),
        'ssn': ssn(),
        'phone': phone(),
        'job': job(),
        'company': company(),
        'email': email(),
        'date_of_birth': date_of_birth(),
        'address': address()
    }

conn = pymssql.connect(host='127.0.0.1', user='sa', password='zxc208569735', database='test', charset='utf8')
cursor = conn.cursor()

def user(length: int) -> list[str]:
    return ';'.join([insert('[user]', data()) for _ in range(length)])

for i in range(9):
    s = user(10**5)
    cursor.execute(s)
    conn.commit()
    print(f'第{i + 1}次结束')

end = time.time()
print(str(round(end - start, 6)) + 's')