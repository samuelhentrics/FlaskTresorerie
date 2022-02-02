-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : mar. 01 juin 2021 à 17:01
-- Version du serveur :  10.3.29-MariaDB-0ubuntu0.20.04.1
-- Version de PHP : 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `tresorerie`
--

-- --------------------------------------------------------

--
-- Structure de la table `caf`
--

CREATE TABLE `caf` (
  `annee` int(11) NOT NULL,
  `recettes` float NOT NULL,
  `depenses` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `caf`
--

INSERT INTO `caf` (`annee`, `recettes`, `depenses`) VALUES
(2021, 148620, 77237);

-- --------------------------------------------------------

--
-- Structure de la table `depenses`
--

CREATE TABLE `depenses` (
  `id` int(11) NOT NULL,
  `objet` varchar(255) NOT NULL,
  `montant` float NOT NULL,
  `annee` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `details_emprunts`
--

CREATE TABLE `details_emprunts` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `emprunt_id` int(11) NOT NULL,
  `restant` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `details_emprunts`
--

INSERT INTO `details_emprunts` (`id`, `date`, `emprunt_id`, `restant`) VALUES
(1, '2021-02-01', 4, 2),
(2, '2021-05-01', 4, 1),

-- --------------------------------------------------------

--
-- Structure de la table `emprunts`
--

CREATE TABLE `emprunts` (
  `id` int(11) NOT NULL,
  `libelle` varchar(255) NOT NULL,
  `capital_depart` float NOT NULL,
  `capital` float NOT NULL,
  `interet` float NOT NULL,
  `date` date NOT NULL,
  `periodicite` int(11) NOT NULL,
  `echeance` int(11) NOT NULL,
  `preteur` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `emprunts`
--

INSERT INTO `emprunts` (`id`, `libelle`, `capital_depart`, `capital`, `interet`, `date`, `periodicite`, `echeance`, `preteur`) VALUES
(4, 'Fronton', 160000, 4000, 827, '2011-08-01', 3, 40, 'Delib 2011');

-- --------------------------------------------------------

--
-- Structure de la table `recettes`
--

CREATE TABLE `recettes` (
  `id` int(11) NOT NULL,
  `objet` varchar(255) NOT NULL,
  `montant` float NOT NULL,
  `annee` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `fonction` varchar(255) NOT NULL DEFAULT ' Indéfini ',
  `avatar` varchar(255) NOT NULL DEFAULT ' assets/avatars/ default.png ',
  `telephone` int(11) NOT NULL DEFAULT 123456789,
  `adresse` varchar(255) NOT NULL DEFAULT ' UNDEFINED ',
  `email` varchar(255) NOT NULL DEFAULT ' undefined@undefined.com ',
  `pseudo` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT 0,
  `connected` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `firstname`, `lastname`, `fonction`, `avatar`, `telephone`, `adresse`, `email`, `pseudo`, `password`, `admin`, `connected`) VALUES
(1, 'Super', 'Administrateur', 'Administrateur', 'assets/avatars/admin.jpg', 123456789, 'Inconnu', 'admin@admin.com', 'admin', 'pbkdf2:sha256:150000$Iza2bBg8$14d06fd6cbda0f94fbd3b4c142ad292f42d9f594b0f6ca5f665a120446cbd222', 1, 1),
(2, 'Samuel', 'HENTRICS', 'Admin', 'assets/avatars/samuel.hentrics.jpg', 768705710, 'UNKNOWN', 'samuel.hentrics@gmail.com', 'samuel.hentrics', 'pbkdf2:sha256:150000$jmFP9JvH$eb7321e8cbe504fe16571ec51bf8f0bee082e84b757461612031489ada6f5f6a', 0, 0),
(3, 'Julen', 'Elizalde', 'Admin', 'assets/avatars/julen.elizalde.jpg', 123456789, 'UNKNOWN', 'julen.elizalde@gmail.com', 'julen.elizalde', 'pbkdf2:sha256:150000$jmFP9JvH$eb7321e8cbe504fe16571ec51bf8f0bee082e84b757461612031489ada6f5f6a', 0, 0),
(4, 'Iban', 'Ruspil', 'Testeur', 'assets/avatars/default.png', 123456789, 'INCONNU', 'ruspil@test.com', 'ruspil', 'pbkdf2:sha256:150000$jmFP9JvH$eb7321e8cbe504fe16571ec51bf8f0bee082e84b757461612031489ada6f5f6a', 0, 0),
(5, 'Marc', 'Heureux', 'Banquier', 'assets/avatars/employe1.jpg', 147622754, '14,\n        boulevard de Rodriguez, Herve - Sur - Mer ', 'employe1@gestiontresorerie.fr', 'employe1', 'pbkdf2:sha256:150000$xADmTbBy$242ef86fdaf108e69309b1d63d6202f0d23d01f194640e8c7f990fd40f7de699', 0, 0),
(6, 'Jessica', 'Anderson', 'Secretaire', 'assets/avatars/employe2.jpg', 485120451, '59,\n        chemin Hugues Bazin, Leclerc - La - Forêt ', 'employe2@gestiontresorerie.fr', 'employe2', 'pbkdf2:sha256:150000$JtDgCN1b$646000b51be252b1d6ff4229b056b5ba4418fdebcd0bd775ee0a0969cc8085de', 0, 0),
(7, 'Manu', 'le bricoleur', 'Accueil du public', 'assets/avatars/employe3.jpg', 515120451, '18 Route de la Goulitière, Sucé - sur - Erdre ', 'employe3@gestiontresorerie.fr', 'employe3', 'pbkdf2:sha256:150000$Q5kFskxG$a1ff7c0d438a9af326929a6ea71eff77bb66575095878f11262296be02b24215', 0, 0),
(8, 'Arthuro', 'Cordon', 'Expert Comptable', 'assets/avatars/employe4.jpg', 851205441, '16,\n        chemin Madeleine Ferrand, BoutinBourg ', 'employe4@gestiontresorerie.fr', 'employe4', 'pbkdf2:sha256:150000$tfJiGOdx$a4ff15fe5ad1625d8b53c9210ae4df3057ba4da3029587fab8cf961fe5ce720b', 0, 0),
(9, 'Solange', 'Riviero', 'Secretaire', 'assets/avatars/employe5.jpg', 845214520, '22, place Berger,\n        Guyondan ', 'employe5@gestiontresorerie.fr', 'employe5', 'pbkdf2:sha256:150000$L9kIkUjI$fd58fd59a01535a9889be73a44a66575c9095e3f20a9e5f27e3b4f83fddd80cb', 0, 0),
(10, 'Sylvie', 'Gorgelain', 'Experte Comptable', 'assets/avatars/employe6.jpg', 152045022, '45,\n        place de Brunel, ChauvetVille ', 'employe6@gestiontresorerie.fr', 'employe6', 'pbkdf2:sha256:150000$k0dvZBOj$fd04cde60868263ee4ed5f19ecd9c70ba40f27e5d3484f6a557af59a298a9c1f', 0, 0),
(11, 'Luce', 'Brun', 'Accueil du public', 'assets/avatars/employe7.jpg', 845265485, '64,\n        rue de Marchand, Becker ', 'employe7@gestiontresorerie.fr', 'employe7', 'pbkdf2:sha256:150000$gfEtoZaH$049a4d6290d044ce4ef86dad4b69b78fc9b4c74ae4371c5fc052266b1c12f110', 0, 0),
(12, 'Lydia', 'Fisher', 'Mairesse', 'assets/avatars/maire.jpg', 456758462, '64, avenue Valérie Thibault,\n        LaporteVille ', 'maire@gestiontresorerie.fr', 'maire', 'pbkdf2:sha256:150000$6ASAD6M0$1f8704472da8c5610a7272e5f7310e6d9ba9dcba88507693932504324a05bc7c', 0, 0);

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `caf`
--
ALTER TABLE `caf`
  ADD UNIQUE KEY `annee` (`annee`);

--
-- Index pour la table `depenses`
--
ALTER TABLE `depenses`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `details_emprunts`
--
ALTER TABLE `details_emprunts`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `emprunts`
--
ALTER TABLE `emprunts`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `recettes`
--
ALTER TABLE `recettes`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `depenses`
--
ALTER TABLE `depenses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `details_emprunts`
--
ALTER TABLE `details_emprunts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `emprunts`
--
ALTER TABLE `emprunts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `recettes`
--
ALTER TABLE `recettes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
