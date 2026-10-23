use('LojaEletronicos_DB');

db.pedidos.insertOne({
  _id: "PED-10045",
  data_pedido: "2026-10-18",
  status: "Em Processamento",
  valor_total: 496.20,
  cliente: {
    nome: "Murilo Gonzaga",
    email: "murilo.gonzaga@email.com",
    endereco_entrega: {
      rua: "Rua das Flores",
      numero: 120,
      bairro: "Centro",
      cidade: "Araras"
    }
  },
  itens: [
    { produto: "Teclado Mecânico", quantidade: 1, preco_unitario: 280.50 },
    { produto: "Mouse Sem Fio", quantidade: 2, preco_unitario: 89.90 },
    { produto: "Cabo HDMI 2m", quantidade: 1, preco_unitario: 35.90 }
  ]
});

db.pedidos.find({ _id: "PED-10045" });

/*
EXERCÍCIO REFLEXIVO

Pergunta: Qual é a grande vantagem do MongoDB ao guardar tudo isso dentro de
um único documento incorporado?

Resposta: A grande vantagem é que o pedido já fica completo em um só lugar.
Os dados do cliente, o endereço de entrega e os itens comprados são lidos
juntos, em uma única consulta, sem precisar de JOIN entre as tabelas
Clientes, Enderecos, Pedidos e Itens. Isso deixa a consulta mais simples e
mais rápida, porque o banco não precisa cruzar várias tabelas, e o documento
fica autocontido, representando o pedido exatamente como ele era na hora da
compra. Também facilita a modelagem, já que os dados que são usados juntos
ficam guardados juntos.
*/