class Usuario():

    def __init__(self, id, login, senha, datadeexpiracao):
        self._id = id
        self._login = login
        self._senha = senha
        self._datadeexpiracao = datadeexpiracao

    

class Coordenador():

    def __init__(self, id, idusuario, nome, email, celular):
        self.id = id
        self.idusuario = idusuario
        self.nome = nome
        self.email = email
        self.celular = celular

    def __str__(self):
        return 'Coordenador: {} Usuario: {}  E-mail: {} Celular: {}'.format(self.nome, self.idusuario, self.email,
                                                                            self.celular)


class Aluno():

    def __init__(self, id, idusuario, nome, email, celular, ra, foto):
        self.id = id
        self.idusuario = idusuario
        self.nome = nome
        self.email = email
        self.celular = celular
        self.ra = ra
        self.foto = foto

    def __str__(self):
        return 'Aluno: {} Usuario: {} E-mail: {} Celular: {} Ra: {}'.format(self.nome, self.idusuario, self.email,
                                                                            self.celular, self.ra, self.foto)


class Professor():

    def __init__(self, id, idusuario, email, celular, apelido):
        self.id = id
        self.idusuario = idusuario
        self.email = email
        self.celular = celular
        self.apelido = apelido

    def __str__(self):
        return 'Usuario: {} E-mail: {} Celular: {} Apelido: {}'.format(self.idusuario, self.email, self.celular,
                                                                       self.apelido)


class Disciplina():

    def __init__(self, id, nome, data, status, planodensino, cargahoraria, competencias, habilidades, ementa,
                 conteudoprogramatico, bibliografiabasica, bibliografiacomplementar, percentualpratico,
                 percentualteorico, idcoordenador):
        self.id = id
        self.nome = nome
        self.data = data
        self.status = status
        self.planodensino = planodensino
        self.cargahoraria = cargahoraria
        self.competencias = competencias
        self.habilidades = habilidades
        self.ementa = ementa
        self.conteudoprogramatico = conteudoprogramatico
        self.bibliografiabasica = bibliografiabasica
        self.bibliografiacomplementar = bibliografiacomplementar
        self.percentualpratico = percentualpratico
        self.percentualteorico = percentualteorico
        self.idcoordenador = idcoordenador

    def __str__(self):
        return 'Disciplina: {} Data: {} Status: {} Plano de ensino: {} Carga horaria: {} Competencias: {} Habilidades: {} Ementa: {} Conteudo Programático:{} Bibliografia Basica: {} Bibliografia Complementar:{} PercentualPratico: {} Percentual Teorico: {} Coordenador: {} '.format(
            self.nome, self.data, self.status,
            self.planodensino, self.cargahoraria, self.competencias, self.habilidades, self.ementa,
            self.conteudoprogramatico, self.bibliografiabasica, self.bibliografiacomplementar, self.percentualpratico,
            self.percentualteorico, self.idcoordenador)


class Disciplina_Ofertada():

    def __init__(self, id, idcoordenador, dtiniciomatricula, dtfimmatricula, iddisciplina,
                 idcurso, ano, semestre, turma, idprofessor, metodologia, recursos, criterioAvaliacao, planodeaulas):
        self.id = id
        self.idcoordenador = idcoordenador
        self.dtiniciomatricula = dtfimmatricula
        self.dtfimmatricula = dtfimmatricula
        self.idisciplina = iddisciplina
        self.idcurso = idcurso
        self.ano = ano
        self.semestre = semestre
        self.turma = turma
        self.idprofessor = idprofessor
        self.metodologia = metodologia
        self.recursos = recursos
        self.criterioAvaliacao = criterioAvaliacao
        self.planodeaulas = planodeaulas
    
    def __str__(self):
        return 'Coordenador: {} Data inicio de matricula: {} Data do fim da matricula: {} Disciplina: {} Curso: {} Ano: {} Semestre: {} Turma: {} Professor: {} Metodologia:{} Recursos: {} Criterio de Avaliacao:{} Plano de aulas: {}'.format(
            self.idcoordenador, self.dtiniciomatricula, self.dtfimmatricula, self.iddisciplina,
            self.idcurso, self.ano, self.semestre, self.turma, self.idprofessor,
            self.metodologia, self.recursos, self.criterioAvaliacao, self.planodeaulas)


class Curso():

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return 'Nome: {}'.format(self.nome)

class SolicitacaoMatricula():

    def __init__(self, id, idaluno, iddisciplinaofertada, dtsolicitacao, idcoordenador, status):
        self.id = id
        self.idaluno = idaluno
        self.iddisciplinaofertada = iddisciplinaofertada
        self.dtsolicitacao = dtsolicitacao
        self.idcoordenador = idcoordenador
        self.status = status


    def __str__(self):
        return 'Aluno: {} Disciplina Ofertada: {} Data de Solicitação: {} Coordenador: {} Status: {}'.format(
            self.idaluno, self.iddisciplinaofertada, self.dtsolicitacao, self.idcoordenador, self.status)


class Atividade():

    def __init__(self, id, titulo, descricao, conteudo, tipo, extras, idprofessor):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.conteudo = conteudo
        self.tipo = tipo
        self.extras = extras
        self.idprofessor = idprofessor

    def __str__(self):
        return 'Atividade: {} Descricao: {} Conteudo: {} Tipo: {} Extras: {} Professor {}'.format(
            self.titulo, self.descricao, self.conteudo, self.tipo, self.extras, self.idprofessor)


class AtividadeVinculada():

    def __init__(self, id, idatividade, idprofessor, iddisciplinaofertada, rotulo, status, dtiniciorespostas,
                 dtfimrespostas):
        self.id = id
        self.idatividade = idatividade
        self.idprofessor = idprofessor
        self.iddisciplinaofertada = iddisciplinaofertada
        self.rotulo = rotulo
        self.status = status
        self.dtiniciorespostas = dtiniciorespostas
        self.dtfimrespostas = dtfimrespostas
    
    def __str__(self):
        return 'Atividade: {} Professor: {} Disciplina Ofertada: {} Rotulo: {} Status: {} Data inicio de respostas: {} Data fim respostas: {}'.format(
            self.idatividade, self.idprofessor, self.iddisciplinaofertada, self.rotulo, self.status,  self.dtiniciorespostas, self.dtfimrespostas)


class Entrega():

    def __init__(self, id, idaluno, idatividadevinculada, titulo, resposta, dtentrega, status, idprofessor, nota,
                 dtavaliacao, obs):
        self.id = id
        self.idaluno = idaluno
        self.idatividadevinculada = idatividadevinculada
        self.titulo = titulo
        self.resposta = resposta
        self.dtentrega = dtentrega
        self.status = status
        self.idprofessor = idprofessor
        self.nota = nota
        self.dtavaliacao = dtavaliacao
        self.obs = obs

    def __str__(self):
        return 'Aluno: {} Atividade Vinculada: {}Titulo: {} Resposta: {} Data de entrega: {} Status: {} Professor: {} Nota: {} Data de avaliacao: {} Obs: {}'.format(
            self.idaluno, self.idatividadevinculada, self.titulo, self.resposta, self.dtentrega,  self.status, self.idprofessor, self.nota, self.dtavaliacao, self.obs)

class Mensagem():

    def __init__(self, id, idaluno, idprofessor, assunto, referencia, conteudo, status, dtenvio, dtresposta, resposta):
        self.id = id
        self.idaluno = idaluno
        self.idprofessor = idprofessor
        self.assunto = assunto
        self.referencia = referencia
        self.conteudo = conteudo
        self.status = status
        self.dtenvio = dtenvio
        self.dtresposta = dtresposta
        self.resposta = resposta
    
    def __str__(self):
        return 'Aluno: {} Professor: {} Assunto: {} Referencia: {} Conteudo: {} Status: {} Data de envio: {} Data de resposta: {} Resposta: {}'.format(
            self.idaluno, self.idprofessor, self.assunto, self.referencia, self.conteudo,  self.status, self.dtenvio, self.dtresposta, self.resposta)


#testando
u1 = Usuario(1, 'dressalima', '1234', '09/07/2021')

u2 = Usuario(2, 'angel12', '3377', '08/12/2021')
u3 = Usuario(3, 'menina22', '2221', '03/03/2022')
u4 = Usuario(4, 'dothy44', '5521', '08/11/2023')

p1= Professor(1,u2,"alex@gmail.com", "99870-0978","Alex")

aluno1 = Aluno(1, u1, 'Andressa', 'andressinha@gmail.com', '99190-7788', '1801004', "heuheu")

coord1 = Coordenador(1, u2, 'Angelica Sousa', 'angelica@gmail.com', '97199-0078')

c1= Curso(1,"Matematica")
a1= Atividade(1,"Conjuntos","heueh", "heue", "heueh", "heueh", p1   )

print(aluno1)
