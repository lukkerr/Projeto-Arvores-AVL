import json

class Node:
    def __init__(self,dado,top = None):
        self.__dado = dado
        self.__top = top
        self.__right = None
        self.__left = None
    @property
    def dado(self):
        return self.__dado
    @dado.setter
    def dado(self,new):
        self.__dado = new
    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self,new):
        self.__right = new
    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self,new):
        self.__left = new
    @property
    def top(self):
        return self.__top
    @top.setter
    def top(self,new):
        self.__top = new
    def __str__(self):
        return f'{self.__dado}'

class Filme:
    def __init__(self,id,nome,ano):
        self.__id = id
        self.__nome = nome
        self.__ano = ano
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,new):
        self.__id = new
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,new):
        self.__nome = new
    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self,new):
        self.__ano = new
    def __str__(self):
        return '{ '+ f'id: {self.id}, nome: "{self.nome}", ano: {self.ano}' +' }'

#######################################################################

class NodeList:
    def __init__(self,value):
        self.__dado = value
        self.__next = None
    
    @property
    def dado(self):
        return self.__dado
    
    @dado.setter
    def dado(self,newDado):
        self.__dado = newDado
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, newNext):
        self.__next = newNext

    def __str__(self):
        return self.dado

class Lista:
    def __init__(self):
        self.__head = None
        self.__length = 0

    @property
    def head(self):
        return self.__head

    @property
    def length(self):
        return self.__length
    
    @property
    def vazio(self):
        return self.__length == 0

    def add(self,index,newItem = None):
        if newItem == None:
            newItem = index
            index = self.length
        NewNo = NodeList(newItem)
        if self.vazio:
            self.__head = NewNo
        elif index == 0:
            NewNo.next = self.head
            self.__head = NewNo
        else:
            prev = None
            x = self.head
            count = 0
            while count != index:
                prev = x
                x = x.next
                count += 1
            prev.next = NewNo
            NewNo.next = x
        self.__length += 1

    def order(self):
        x = Lista()
        count = 0
        while count != self.length:
            newIndex = 0
            if count == 0:
                x.add(self.index(count))
            else:
                count2 = 0
                while count2 != x.length:
                    if x.index(count2).nome < self.index(count).nome:
                        newIndex += 1
                    else: break
                    count2 += 1
                x.add(newIndex,self.index(count))
            count += 1
        return x

    def index(self,indexItem = 0):
        x = self.head
        count = 0
        while x != None:
            if count == indexItem:
                return x.dado
            else:
                x = x.next
                count += 1

    def __str__(self):
        format = ''
        x = self.head
        while x != None:
            if x.next != None:
                format += f'{x.dado},\n'
            else:
                format += f'{x.dado}'
            x = x.next
        return format

#############################################################

class TreeAVL:
    def __init__(self):
        self.__root = None
    @property
    def root(self):
        return self.__root
    @root.setter
    def root(self,new):
        self.__root = new

    def length(self,root):
        return json.loads('{' + f'''
            "left":{self.length_left(root,0,True)},
            "right":{self.length_right(root,0,True)},
            "balance":{self.length_left(root,0,True)-self.length_right(root,0,True)}
        ''' + '}')

    def length_left(self,branch,length,first = False):
        if branch == None:
            return length-1
        elif first:
            return self.length_left(branch.left,length+1)
        else:
            left = self.length_left(branch.left,length+1)
            right = self.length_left(branch.right,length+1)
            if left > right:
                return left
            else:
                return right

    def length_right(self,branch,length, first = False):
        if branch == None:
            return length-1
        elif first:
            return self.length_right(branch.right,length+1)
        else:
            right = self.length_right(branch.right,length+1)
            left = self.length_right(branch.left,length+1)
            if right > left:
                return right
            else:
                return left

    def insert(self,new,root):
        if self.root == None:
            self.__root = Node(new)
            self.balance(self.root)
        elif new.id < root.dado.id:
            if root.left != None:
                return self.insert(new,root.left)
            root.left = Node(new,root)
            self.balance(self.root)
        elif new.id > root.dado.id:
            if root.right != None:
                return self.insert(new,root.right)
            root.right = Node(new,root)
            self.balance(self.root)

    def em_ordem(self,branch):
        if branch != None:
            self.em_ordem(branch.left)
            print(branch.dado)
            self.em_ordem(branch.right)

    def rotation_right(self,branch):
        print('right')
        aux = branch.left
        branch.left = aux.right
        aux.right = branch
        aux.top = branch.top
        if branch.top == None:
            self.root = aux
        else:
            if branch.top.left == branch:
                branch.top.left = aux
            elif branch.top.right == branch:
                branch.top.right = aux
        branch.top = aux

    def rotation_left(self,branch):
        aux = branch.right
        branch.right = aux.left
        aux.left = branch
        aux.top = branch.top
        if branch.top == None:
            self.root = aux
        else:
            if branch.top.left == branch:
                branch.top.left = aux
            elif branch.top.right == branch:
                branch.top.right = aux
        branch.top = aux

    def balance(self,branch):
        if branch != None:
            self.balance(branch.left)
            if self.length(branch)['balance'] > 1:
                if self.length(branch.left)['balance'] < 0:
                    self.rotation_left(branch.left)
                self.rotation_right(branch)
            elif self.length(branch)['balance'] < -1:
                if self.length(branch.right)['balance'] > 0:
                    self.rotation_right(branch.right)
                self.rotation_left(branch)
            self.balance(branch.right)
    
    def buscar(self,id,branch):
        if branch != None:
            if id > branch.dado.id:
                return self.buscar(id,branch.right)
            elif id < branch.dado.id:
                return self.buscar(id,branch.left)
            elif id == branch.dado.id:
                return '{ '+ f'nome: "{branch.dado.nome}", ano: {branch.dado.ano}' +' }'
        return False
    
    def buscarAno(self,ano,branch):
        if branch != None:
            self.buscarAno(ano,branch.left)
            if ano == branch.dado.ano:
                print(branch.dado)
            self.buscarAno(ano,branch.right)
        
    def orderMovie(self,lista,branch):
        if branch != None:
            self.orderMovie(lista,branch.left)
            lista.add(branch.dado)
            self.orderMovie(lista,branch.right)

x = TreeAVL()
x.insert(Filme(42,'A',2000),x.root)
x.insert(Filme(88,'B',2001),x.root)
x.insert(Filme(15,'C',2000),x.root)
x.insert(Filme(27,'D',2001),x.root)
x.insert(Filme(6,'E',2000),x.root)
x.insert(Filme(4,'F',2001),x.root)

while True:
    print('-------------------------------------------')
    print('--------- DIGITE A OPÇÃO DESEJADA ---------')
    print('-------------------------------------------')
    print('-- (1) INSERIR FILME ----------------------')
    print('-- (2) BUSCAR FILME PELO ID ---------------')
    print('-- (3) BUSCAR FILMES PELO ANO -------------')
    print('-- (4) LISTAR FILMES EM ORDEM ALFABÉTICA --')
    print('-- (5) ALTURA DA ÁRVORE -------------------')
    print('-- (6) EXIBIR A ÁRVORE --------------------')
    print('-- (7) SAIR -------------------------------')
    print('-------------------------------------------')
    option = int(input('Digite a opção desejada: '))
    if option == 1:
        id = int(input('Digite o ID do Filme: '))
        if id == 0:
            continue
        if x.buscar(id,x.root) != False:
            print('\n--- Id já Existente ---\n')
            continue
        nome = input('Digite o Nome do Filme: ')
        ano = int(input('Digite o Ano do Filme: '))
        x.insert(Filme(id,nome,ano),x.root)
        print('\n--- Filme Inserido Sucesso ---\n')
    elif option == 2:
        id = int(input('Digite o ID do Filme: '))
        if id == 0:
            continue
        if x.buscar(id,x.root) == False:
            print('\n--- Id não Existente ---\n')
            continue
        print(f'\n{x.buscar(id,x.root)}\n')
    elif option == 3:
        ano = int(input('Digite o ano a ser Consultado: '))
        if ano == 0:
            continue
        print(f'\n--- Filmes Lançados no Ano de {ano} ---\n')
        x.buscarAno(ano,x.root)
        print('')
    elif option == 4:
        y = Lista()
        x.orderMovie(y,x.root)
        print()
        print(y.order())
        print()
        y = None
    elif option == 5:
        if x.length(x.root)['right'] > x.length(x.root)['left']:
            print(f'\nA Árvore possui altura igual a {x.length(x.root)["right"] + 1}.\n')
        else:
            print(f'\nA Árvore possui altura igual a {x.length(x.root)["left"] + 1}.\n')
    elif option == 6:
        print()
        x.em_ordem(x.root)
        print()
    elif option == 7:
        break
    elif option == 8:
        print(x.root)
        print(x.length(x.root))
        print(x.root.left)
    else:
        print('\n--- Opção Invalída ---\n')
