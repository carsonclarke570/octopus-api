USE octopus_db;

INSERT INTO `Host`
VALUES
    (1, 'Big Daddy Nerd', NOW(), NOW());

INSERT INTO `Queue`
VALUES
    (1, NOW(), NOW());

INSERT INTO `Party`
VALUES
    (1, 1, 1, 'COVID-19 Bananza', 'This is a code', 'acc', 'ref', NOW(), NOW());

INSERT INTO `Member`
VALUES
    (1, 1, 'Bobby Hill', NOW(), NOW()),
    (2, 1, 'Joseph Cena', NOW(), NOW()),
    (3, 1, 'Im at soup', NOW(), NOW()),
    (4, 1, 'Cawona Viwus', NOW(), NOW()),
    (5, 1, 'Dad', NOW(), NOW());

INSERT INTO `Song`
VALUES
    (1, 1, 1, 'I Write Blessings', 11, NOW(), NOW()),
    (2, 3, 1, 'Shrek TM', -5, NOW(), NOW()),
    (3, 5, 1, 'Out of me swamp', 3, NOW(), NOW()),
    (4, 2, 1, 'Coming', 25, NOW(), NOW()),
    (5, 2, 1, 'My Cage', 23, NOW(), NOW()),
    (6, 1, 1, 'Out of', 24, NOW(), NOW()),
    (7, 1, 1, 'And Ive Been Doing Just Fine', 21, NOW(), NOW());