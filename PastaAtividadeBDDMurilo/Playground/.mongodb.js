// ==========================================
// ATIVIDADE PRÁTICA - MONGODB E JSON
// Banco de dados: EngenheiroCoelho_DB
// Coleção: Estudantes
// ==========================================

// 1. Selecionar o banco de dados
use('EngenheiroCoelho_DB');

// 2. Inserir dois alunos na coleção Estudantes
db.Estudantes.insertMany([
    {
        nome: "Jusicrelda Pinha",
        idade: 3,
        disciplinas: [
            "Banco de Dados",
            "Robótica",
            "Programação"
        ]
    },
    {
        nome: "Rosenildo Silva",
        idade: 7,
        contato: {
            email: "rosenildo@email.com",
            telefone: "(19) 99999-8888"
        }
    }
]);

// 3. Consultar e exibir todos os alunos
db.Estudantes.find();