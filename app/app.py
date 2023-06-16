import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("user.avsc", "rb").read())

writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"id": 1, "name": "Galdino", "email": "ricardo@email.com"})
writer.append({"id": 2, "name": "Paulo"})
writer.append({"id": 3, "name": "Elias", "email": "elias@email.com"})
writer.close()

reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print(user)
reader.close()
