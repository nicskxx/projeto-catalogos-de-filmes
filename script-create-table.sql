CREATE TABLE IF NOT EXISTS "usuarios" (
	"id" SERIAL NOT NULL,
	"nome" VARCHAR(255) NOT NULL,
	"email" VARCHAR(255) NOT NULL UNIQUE,
	"senha" VARCHAR(255) NOT NULL,
	"criado_em" TIMESTAMP NOT NULL DEFAULT 'now ()',
	"atualizado_em" TIMESTAMP NOT NULL,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "filmes" (
	"id" SERIAL NOT NULL,
	"usuario_id" INTEGER NOT NULL,
	"titulo" VARCHAR(255) NOT NULL,
	"ano_lançamento" TIMESTAMP NOT NULL,
	"genero" VARCHAR(255) NOT NULL,
	"nota" DECIMAL(3,1) CHECK(nota >= 0 AND nota <= 10),
	"capa_url" TEXT,
	"atualizado_em" TIMESTAMP,
	"criado_em" TIMESTAMP NOT NULL DEFAULT 'now ()',
	PRIMARY KEY("id")
);

ALTER TABLE "filmes"
ADD FOREIGN KEY("usuario_id") REFERENCES "usuarios"("id")
ON UPDATE NO ACTION ON DELETE NO ACTION;