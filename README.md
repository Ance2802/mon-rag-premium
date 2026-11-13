🚀 **Démo en ligne :** [https://mon-rag-premium.onrender.com](https://mon-rag-premium.onrender.com)

# ✨ RAG Premium Assistant (Docker + Gemini + ChromaDB)

## 📝 Description
Ce projet est une application web intelligente capable de lire un document texte (`document.txt`) et de répondre à des questions en se basant **uniquement** sur son contenu. 

L'application utilise la technologie **RAG (Retrieval-Augmented Generation)** pour éviter les hallucinations de l'IA, et propose une interface utilisateur moderne avec un effet "Glassmorphism" (verre dépoli).

## 🏗️ Architecture Technique
Le projet repose sur 3 piliers :
1. **Le Frontend** : Une interface HTML/CSS/JS épurée avec un design sombre et des animations fluides.
2. **Le Backend (Flask)** : Un serveur Python qui gère les requêtes de l'utilisateur.
3. **Le Moteur RAG** :
   - **Découpage** : Le texte est découpé en paragraphes intelligents.
   - **Base Vectorielle (ChromaDB)** : Les morceaux de texte sont stockés sous forme de vecteurs pour une recherche sémantique rapide.
   - **IA (Gemini)** : Les extraits les plus pertinents sont envoyés à Gemini pour générer une réponse contextuelle.

## 🚀 Stack Technique
- **Langage** : Python 3.12
- **Framework Web** : Flask
- **Base de données vectorielle** : ChromaDB
- **Intelligence Artificielle** : Google Gemini API (`gemini-3.5-flash`)
- **Déploiement** : Docker

## 🛠️ Comment lancer le projet

### 1. Cloner le dépôt
```bash
git clone https://github.com/Ance2802/mon-rag-premium.git
cd mon-rag-premium
