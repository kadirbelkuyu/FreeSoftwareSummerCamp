# def filtrele(data):
#     if data.find("#") > -1:
#         return True
#     return False
#
# with open("dosya.fastq") as file:
#     data = file.read().split("\n")
#     hepsi = list(filter(filtrele,data))
#     for i in hepsi:
#         print(i)


class ParseFASTQ():
    file_data = []
    filetered_data = []
    filter_keyword = None

    def __init__(self,file_name):
        with open(file_name) as file_data:
            self.file_data = file_data.read().split("\n")

    def filter(self,data):
        if data.find("#") > -1:
            return True
        else:
            return False
    def finder(self,keyword):
        self.filter_keyword = keyword
        self.filetered_data = list(filter(self.filter_keyword,self.data))

        def count(self):
            return len(self.filetered_data)
        def result(self):
            return self.filetered_data
parsed_file = ParseFASTQ("dosya.fastq")
parsed_file.find("#")
print(parsed_file.count())









