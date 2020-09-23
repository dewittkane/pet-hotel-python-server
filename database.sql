
-- Create a database called pet_hotel

CREATE TABLE "owner" (
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR(40) NOT NULL
);

CREATE TABLE "pet" (
	"id" SERIAL PRIMARY KEY,
	"owner_id" INT REFERENCES "owner" ON DELETE CASCADE,
	"pet_name" VARCHAR(40) NOT NULL,
	"breed" VARCHAR(40),
	"color" VARCHAR(20),
	"checked_in" BOOLEAN DEFAULT false
);

INSERT INTO "owner" ("name")
VALUES ('Alex'),
('DeWitt'),
('Karl'),
('Emerson');

INSERT INTO "pet" ("owner_id", "pet_name", "breed", "color")
VALUES ('1', 'Chace', 'Finnish Spitz', 'red-brown'),
('2', 'Big Jon', 'python', 'black-yellow'),
('3', 'Stan', 'main coone', 'brown-white'),
('4', 'Bear', 'tea-cup yorke', 'black-brown');