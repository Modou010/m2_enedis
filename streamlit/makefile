.PHONY: help build up down restart logs clean streamlit api stop-streamlit stop-api

# Couleurs pour l'affichage
GREEN=\033[0;32m
YELLOW=\033[1;33m
NC=\033[0m # No Color

help: ## Afficher l'aide
	@echo "$(GREEN)═══════════════════════════════════════════════════$(NC)"
	@echo "$(GREEN)   GreenTech Solutions - Commandes Docker$(NC)"
	@echo "$(GREEN)═══════════════════════════════════════════════════$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(YELLOW)%-20s$(NC) %s\n", $$1, $$2}'

build: ## Construire les images Docker
	@echo "$(GREEN)🔨 Construction des images Docker...$(NC)"
	docker-compose build

up: ## Démarrer tous les services
	@echo "$(GREEN)🚀 Démarrage de tous les services...$(NC)"
	docker-compose up -d
	@echo "$(GREEN)✅ Services démarrés !$(NC)"
	@echo "$(YELLOW)📊 Streamlit: http://localhost:8501$(NC)"
	@echo "$(YELLOW)🔌 API: http://localhost:8000$(NC)"

down: ## Arrêter tous les services
	@echo "$(GREEN)🛑 Arrêt de tous les services...$(NC)"
	docker-compose down

restart: down up ## Redémarrer tous les services

streamlit: ## Démarrer uniquement Streamlit
	@echo "$(GREEN)📊 Démarrage de Streamlit...$(NC)"
	docker-compose up -d streamlit
	@echo "$(GREEN)✅ Streamlit démarré sur http://localhost:8501$(NC)"

api: ## Démarrer uniquement l'API
	@echo "$(GREEN)🔌 Démarrage de l'API...$(NC)"
	docker-compose up -d api
	@echo "$(GREEN)✅ API démarrée sur http://localhost:8000$(NC)"

stop-streamlit: ## Arrêter Streamlit
	@echo "$(GREEN)🛑 Arrêt de Streamlit...$(NC)"
	docker-compose stop streamlit

stop-api: ## Arrêter l'API
	@echo "$(GREEN)🛑 Arrêt de l'API...$(NC)"
	docker-compose stop api

logs: ## Voir les logs de tous les services
	docker-compose logs -f

logs-streamlit: ## Voir les logs de Streamlit
	docker-compose logs -f streamlit

logs-api: ## Voir les logs de l'API
	docker-compose logs -f api

ps: ## Voir l'état des services
	@echo "$(GREEN)📊 État des services:$(NC)"
	@docker-compose ps

shell-streamlit: ## Ouvrir un shell dans le conteneur Streamlit
	docker-compose exec streamlit /bin/bash

shell-api: ## Ouvrir un shell dans le conteneur API
	docker-compose exec api /bin/bash

clean: ## Nettoyer les conteneurs, images et volumes
	@echo "$(YELLOW)⚠️  Nettoyage complet (conteneurs, images, volumes)...$(NC)"
	docker-compose down -v
	docker system prune -f
	@echo "$(GREEN)✅ Nettoyage terminé$(NC)"

rebuild: clean build up ## Reconstruire et redémarrer tout

health: ## Vérifier la santé des services
	@echo "$(GREEN)🏥 Vérification de la santé des services:$(NC)"
	@docker inspect --format='{{.State.Health.Status}}' greentech-streamlit 2>/dev/null || echo "Streamlit: non démarré"
	@docker inspect --format='{{.State.Health.Status}}' greentech-api 2>/dev/null || echo "API: non démarré"