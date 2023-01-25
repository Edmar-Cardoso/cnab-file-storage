from rest_framework import serializers
from .models import File
from datetime import datetime

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            'file',
            'id', 
            'transaction_type', 
            'transaction_at', 
            'value', 
            'cpf', 
            'card', 
            'transaction_hour',
            'owner',
            'name',
        ]
        read_only_fields = [
            'id', 
            'transaction_type', 
            'transaction_at', 
            'value', 
            'cpf', 
            'card', 
            'transaction_hour',
            'owner',
            'name',
        ]
        extra_kwargs = {
            "file": {"write_only":True}
        }

    def create(self, validadeted_data: dict) -> File:
        # placing a marker to separate the string

        """ new_string = ""
        for x in range(len(validadeted_data["file"])):
            if x % 81 == 0 and x > 0:
                new_string += "##" + validadeted_data["file"][x]
            else:
                new_string += validadeted_data["file"][x] """
        
        # to-do

        file = validadeted_data["file"]

        #for file in array_files:
        data_file = {
            'transaction_type': int(file[0:1]), 
            'transaction_at': datetime.strptime(f'{file[1:5]}-{file[5:7]}-{file[7:9]}', '%Y-%m-%d').date(),
            'value': float(int(file[9:19])/100),
            'cpf': file[19:30],
            'card': file[30:42],
            'transaction_hour': f'{file[42:44]}:{file[44:46]}:{file[46:48]}',
            'owner': file[48:62],
            'name': file[62: 81],
            'file': ""
        }

        return File.objects.create(**data_file)

