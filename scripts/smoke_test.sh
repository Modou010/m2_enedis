#!/usr/bin/env bash
echo "=== Smoke test : démarrage app ==="
python3 -c "import streamlit, sys; sys.exit(0)" && echo "✅ Import OK"
streamlit run streamlit/app.py --server.headless true --server.port 8501 &
sleep 10
curl -f http://localhost:8501/ || echo "⚠️ Streamlit non démarré"
pkill -f streamlit
echo "Smoke test terminé."
