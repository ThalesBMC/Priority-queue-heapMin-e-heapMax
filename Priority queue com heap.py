class PriorityQueue(object):
    def __init__(self): 
        self.queue = []
        self.semAssento=[]
        self.numCadastro=0
        self.removido=False
    def heapMin(self,data):
        iMenor=0
        contI=-1
        for i in self.queue:
            contI+=1
            contK=-1
            for k in i:
                contK+=1
                if int(iMenor)==0:
                    iMenor=k[0]
                    IMenorPosition=contI
                    IMenorPositionK=contK
                elif int(iMenor) < int(k[0]):
                    pass
                elif  int(k[0]) < int(iMenor):
                    iMenor=  int(k[0])
                    IMenorPosition=contI
                    IMenorPositionK=contK
        if int(iMenor) < int(data[0]):
            menor=self.queue[IMenorPosition][IMenorPositionK]
            self.semAssento.append(menor)
            self.queue[IMenorPosition][IMenorPositionK] = data
            separarMaior= data[1].split(" ")
            IPosition= IMenorPosition+1
            fraseInseridoMaior="{} ({}) foi alocado(a) na fileira {}".format(separarMaior[0],separarMaior[1],IPosition)
            print(fraseInseridoMaior)
        else:
            self.semAssento.append(data)
            separarMaior= data[1].split(" ")
            fraseSem="{} ({}) nao foi alocado(a) em nenhuma fileira".format(separarMaior[0],separarMaior[1])
            if self.removido ==False:
                print(fraseSem)
            self.removido=False
             
    def ver(self,data):
        contIver=0
        achou=False
        for i in self.queue:
            contIver+=1
            for k in i:
                try:
                    if k[1] == data:
                        achou=True
                        fraseAchou="Sentado(a) na fileira {}".format(contIver)
                        return fraseAchou  
                except:
                    pass
        if achou==False:
            for j in self.semAssento:
                if j[1] == data:
                    achou=True
                    return "Sem assento"          
        if achou==False:
            return "Inexistente"
    def inserir(self,data):
        continuar=True
        for k in range(len(self.queue)):
            if continuar ==True:
                for l in range(len(self.queue[0])):
                    if self.queue[k][l] == 0:
                        continuar=False
                        self.queue[k][l] = data
                        separar= data[1].split(" ")
                        fraseInserido="{} ({}) foi alocado(a) na fileira {}".format(separar[0],separar[1],k+1)
                        return fraseInserido            
        if continuar==True:
            self.heapMin(data)
    def criarlistaDeLista(self,filas,vagas):
        vagasFila=[[0] * int(vagas) for i in range(int(filas))]
        self.queue= vagasFila
    def numeroCadastrar(self):
        self.numCadastro+=1
        return(self.numCadastro)
    def remover(self,data):
        contIrem=-1
        achou=False
        achou2=False
        for i in self.queue:
            contKrem=-1
            contIrem+=1
            for k in i:
                contKrem+=1
                try:
                    if str(k[1]) == str(data):
                        self.queue[contIrem][contKrem] =0
                        print("Removido(a)")
                        achou=True
                        achou2=True
                except:
                    pass     
        if achou==False:
            cont=-1
            for j in self.semAssento:
                cont+=1
                if j[1] == data:
                    achou=True
                    self.semAssento.pop(cont)
                    print("Removido(a)")
                    break
        if achou==False:
            print("Inexistente")
        if achou2 ==True and len(self.semAssento) > 0:
            maiorValor= self.heapMax()
            self.removido=True
            self.inserir(maiorValor)
            cont2=0
            for f in self.semAssento:
                cont2+=1
                if f[1] == maiorValor:
                    achou=True
                    self.semAssento.pop(cont2)
            self.removido=False
    def heapMax(self):
        maiorHeap=0
        for j in self.semAssento:
                if int(j[0]) > int(maiorHeap):
                    maiorHeap=j[0]
                    heapReturn= j
        return heapReturn
    def printar(self):
        print(self.queue)
        print(self.semAssento)
myQueue = PriorityQueue()
verdade=True
contTamanho=0
while verdade==True:
    try:
       folha=input("")
       numero=""
       if contTamanho == 0:
        myQueue.criarlistaDeLista(folha[0],folha[2])
        contTamanho+=1 
       if "CAD" in folha:
            separadoCAD =folha.split(" ")
            numeroCad=myQueue.numeroCadastrar()
            adicionar=str(separadoCAD[1])+" "+ str(numeroCad)
            cadPrint = myQueue.inserir([separadoCAD[2],adicionar])
            if cadPrint != None:
                print(cadPrint)
       elif "VER" in folha:
            separadoVER =folha.split(" ")
            pesquisa =myQueue.ver(str(separadoVER[1]+" "+separadoVER[2]))
            print(pesquisa)
       elif "REM" in folha:
           separadoREM =folha.split(" ")
           myQueue.remover(str(separadoREM[1]+" "+separadoREM[2]))
       elif "print" in folha:
           myQueue.printar()
    except EOFError:
        verdade = False
