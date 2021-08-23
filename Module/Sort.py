Names = ['IMG_3659', 'IMG_3660', 'IMG_3736', 'IMG_3737', 'IMG_3742', 'IMG_5165', 'IMG_5166', 'IMG_5167']
Base_excel = ['IMG_228','IMG_3660', 'IMG_3736','IMG_1']
Base_time = ['2020','2021', '2022','2023']

class sort_massive:
    def sort_massive(Names,Base_excel,Base_time):
        handpicked = []
        rubbish = []
        ID = 0
        while ID < len(Names):
            output = [x for x,y in enumerate(Base_excel) if y.split()[0] == Names[ID]]
            if output == []:
                rubbish.append(Names[ID])
            else:
                handpicked.append(str(ID+1)+" "+ str(Names[ID])+" "+ str(Base_time[output[0]]))         
            ID +=1   
        print("SORTED: ", handpicked)
        print("MUSOR: ",rubbish)
                
                    
    

sort_massive.sort_massive(Names,Base_excel,Base_time)