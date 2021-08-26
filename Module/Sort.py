class sort_massive:
    def sort_massive(Names,Base_excel,Base_time):
        handpicked_ID = []
        handpicked_NAME = []
        handpicked_TIME = []
        rubbish = []
        ID = 0
        while ID < len(Names):
            output = [x for x,y in enumerate(Base_excel) if y.split()[0] == Names[ID]]
            if output == []:
                rubbish.append(Names[ID])
            else:     
                handpicked_ID.append(ID)
                handpicked_NAME.append(Names[ID])
                handpicked_TIME.append(Base_time[output[0]]) 
            ID +=1   
        return handpicked_ID,handpicked_NAME,handpicked_TIME,rubbish
