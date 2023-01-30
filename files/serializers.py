from rest_framework import serializers
from .models import File
from stores.models import Store
from datetime import datetime

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        read_only_fields = [
            'id', 
            'transaction_type', 
            'transaction_at', 
            'value',      
            'card', 
            'transaction_hour',
            'store'
        ]
        extra_kwargs = {
            "file": {"write_only":True}
        }   
        depth = 1

    def create(self, validadeted_data: dict) -> dict:
        # placing a marker to separate the string:

        new_string = ""
        for x in range(len(validadeted_data["file"])):
            if x % 81 == 0 and x > 0:
                new_string += "##" + validadeted_data["file"][x]
            else:
                new_string += validadeted_data["file"][x]

        # finding transaction type:

        def transaction_type(int):
            if int == 1:
                return "débito"
            elif int == 2:
                return "boleto"
            elif int == 3:
                return "financiamento"
            elif int == 4:
                return "crédito"
            elif int == 5:
                return "recebimento empréstimo"
            elif int == 6:
                return "vendas"
            elif int == 7:
                return "recebimento TED"
            elif int == 8:
                return "recebimento DOC"
            elif int == 9:
                return "alugel"

        # persisting data in the database:
        
        array_files = new_string.split("##")

        for file in array_files:
            data_transaction_store = { 
                'owner': file[48:62],
                'name': file[62: 81],
                'cpf': file[19:30],
            }

            data_file = {
                'transaction_type': transaction_type(int(file[0:1])), 
                'transaction_at': datetime.strptime(f'{file[1:5]}-{file[5:7]}-{file[7:9]}', '%Y-%m-%d').date(),
                'value': float(int(file[9:19])/100),
                'card': file[30:42],
                'transaction_hour': f'{file[42:44]}:{file[44:46]}:{file[46:48]}',
                'file': ""
            }

            transaction_store = Store.objects.get_or_create(**data_transaction_store)[0]

            # updating the store total

            if int(file[0:1]) == 2 or int(file[0:1]) == 3 or int(file[0:1]) == 9:
                transaction_store.total = transaction_store.total - data_file['value']
                transaction_store.save()
            else:
                transaction_store.total = transaction_store.total + data_file['value']
                transaction_store.save()

            data_file['store'] = transaction_store

            File.objects.create(**data_file)

        return {}

