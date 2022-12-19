TABLE = {} # tabel untuk menyimpan hasil perhitungan CYK

def is_valid(inputString): # fungsi untuk mengecek apakah inputan user diterima atau tidak
    global TABLE # variabel global tabel untuk menyimpan hasil perhitungan CYK
    TABLE.clear() # method untuk menghapus isi dari tabel hasil perhitungan CYK
    prodRules = get_set_of_production() # variabel untuk menyimpan hasil dari fungsi get_set_of_production
    temp = inputString.lower().split(" ") # variabel untuk menyimpan input dengan lower case
    inputString = temp # mengembalikan nilai dari inputString
    for i in range(1,len(inputString)+1): # perulanganuntuk mengisi tabel hasil perhitungan CYK
        for j in range(i, len(inputString)+1):
            TABLE[(i,j)] = [] #  mengisi tabel hasil perhitungan CYK
    for i in reversed(range(1, len(inputString)+1)): # perulangan untuk mengisi tabel hasil perhitungan CYK
        for j in range(1, i+1):
            if (j == j + len(inputString) - i): 
                tempList = [] 
                for key, value in prodRules.items(): 
                    for val in value: 
                        if (val == inputString[j-1] and key not in tempList): 
                            tempList.append(key) 
                TABLE[(j, j + len(inputString) - i)] = tempList # menyimpan hasil perhitungan CYK
            else: 
                tempList = [] 
                resultList = [] 
                for k in range(len(inputString) - i): 
                    first = TABLE[(j,j+k)] 
                    second = TABLE[(j+k+1,j+len(inputString) - i)] 
                    for fi in first: 
                        for se in second: 
                            if (fi + " " + se not in tempList): 
                                tempList.append(fi + " " + se) 
                for key, value in prodRules.items(): 
                    for val in value: 
                        if (val in tempList and key not in resultList): 
                            resultList.append(key) 
                TABLE[(j,j+len(inputString) - i)] = resultList 
    if "K" in TABLE[(1, len(inputString))]: # menentukan apakah input diterima atau tidak dengan melihat apakah K ada di dalam tabel
        return True # string diterima
    else: 
        return False # string ditolak
