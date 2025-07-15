#!/bin/bash
echo "🔍 Verificando app..."

curl -f http://localhost:8080/health && echo "✅ Health OK" || echo "❌ Health Falló"
curl -f http://localhost:8080/ && echo "✅ Home OK" || echo "❌ Home Falló"
curl -f http://localhost:8080/ping && echo "✅ Ping OK" || echo "❌ Ping Falló"
