use('LojaAnalytics_DB');

// Limpa a coleção antes de povoar
db.Vendas.drop();

db.Vendas.insertMany([
  { "produto": "Teclado Mecânico RGB", "categoria": "Periféricos", "preco": 250.00, "quantidade": 4, "status": "Concluido", "cidade": "Campinas" },
  { "produto": "Mouse Gamer 12000 DPI", "categoria": "Periféricos", "preco": 120.00, "quantidade": 10, "status": "Concluido", "cidade": "Limeira" },
  { "produto": "Monitor UltraWide 29'", "categoria": "Monitores", "preco": 1200.00, "quantidade": 1, "status": "Cancelado", "cidade": "Campinas" },
  { "produto": "Headset 7.1 Surround", "categoria": "Áudio", "preco": 300.00, "quantidade": 5, "status": "Concluido", "cidade": "Piracicaba" },
  { "produto": "Cadeira Ergonômica", "categoria": "Mobiliário", "preco": 950.00, "quantidade": 2, "status": "Concluido", "cidade": "Limeira" },
  { "produto": "Mousepad Speed Extra Grande", "categoria": "Periféricos", "preco": 80.00, "quantidade": 15, "status": "Concluido", "cidade": "Campinas" },
  { "produto": "Caixa de Som Bluetooth", "categoria": "Áudio", "preco": 180.00, "quantidade": 3, "status": "Cancelado", "cidade": "Piracicaba" }
]);

db.Vendas.aggregate([
  // Estágio 1: $match -> Filtrar apenas vendas com status "Concluido"
  {
    $match: { status: "Concluido" }
  },

  // Estágio 2: $group -> Agrupar por categoria e calcular a soma total das vendas
  {
    $group: {
      _id: "$categoria",
      total_faturamento: {
        $sum: { $multiply: ["$preco", "$quantidade"] }
      },
      quantidade_itens_vendidos: { $sum: "$quantidade" }
    }
  },

  // Estágio 3: $project -> Formatar a saída (renomear campos e ocultar o _id padrão)
  {
    $project: {
      _id: 0,
      categoria: "$_id",
      total_faturamento: 1,
      quantidade_itens_vendidos: 1
    }
  },

  // Estágio 4: $sort -> Ordenar do maior faturamento para o menor (-1)
  {
    $sort: { total_faturamento: -1 }
  }
]);