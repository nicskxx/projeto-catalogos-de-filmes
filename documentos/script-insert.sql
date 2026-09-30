
INSERT INTO usuarios (nome, email, senha, atualizado_em)
VALUES
('Nicolas', 'nicolas@gmail.com', '123456', NOW()),
('João', 'joao@gmail.com', '123456', NOW()),
('Pedro', 'pedro@gmail.com', '123456', NOW()),
('Lucas', 'lucas@gmail.com', '123456', NOW()),
('Gabriel', 'gabriel@gmail.com', '123456', NOW());




SELECT * FROM usuarios;


INSERT INTO filmes
(usuario_id, titulo, ano_lançamento, genero, nota, capa_url, atualizado_em)
VALUES
(1, 'Interestelar', '2014-11-06', 'Ficção Científica', 9.0, 'https://exemplo.com/interestelar.jpg', NOW()),
(2, 'O Poderoso Chefão', '1972-03-24', 'Drama', 9.2, 'https://exemplo.com/poderoso-chefao.jpg', NOW()),
(3, 'Batman: O Cavaleiro das Trevas', '2008-07-18', 'Ação', 9.0, 'https://exemplo.com/batman.jpg', NOW()),
(4, 'Homem-Aranha: Sem Volta Para Casa', '2021-12-17', 'Ação', 8.2, 'https://exemplo.com/homem-aranha.jpg', NOW()),
(5, 'Vingadores: Ultimato', '2019-04-26', 'Ação', 8.4, 'https://exemplo.com/vingadores.jpg', NOW()),
(1, 'Toy Story', '1995-11-22', 'Animação', 8.3, 'https://exemplo.com/toy-story.jpg', NOW()),
(2, 'O Rei Leão', '1994-06-24', 'Animação', 8.5, 'https://exemplo.com/rei-leao.jpg', NOW()),
(3, 'Jurassic Park', '1993-06-11', 'Aventura', 8.2, 'https://exemplo.com/jurassic-park.jpg', NOW()),
(4, 'Matrix', '1999-03-31', 'Ficção Científica', 8.7, 'https://exemplo.com/matrix.jpg', NOW()),
(5, 'Titanic', '1997-12-19', 'Romance', 7.9, 'https://exemplo.com/titanic.jpg', NOW());



SELECT * FROM filmes;