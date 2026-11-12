from flask import Flask, request, jsonify, render_template
import os
import chromadb
from google import genai

app = Flask(__name__)

# Initialisation Gemini
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Initialisation ChromaDB (en mémoire pour ce test)
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="mes_documents")

# Fonction pour indexer au démarrage
def indexer_document():
    try:
        with open('document.txt', 'r', encoding='utf-8') as f:
            contenu = f.read()
        
        # Découpage par paragraphes
        morceaux = [p.strip() for p in contenu.split('\n\n') if p.strip()]
        if len(morceaux) < 5:
            morceaux = [p.strip() for p in contenu.split('.') if p.strip()]
            
        ids = [f"id_{i}" for i in range(len(morceaux))]
        collection.add(documents=morceaux, ids=ids)
        print(f"✅ Document indexé ({len(morceaux)} morceaux).")
    except Exception as e:
        print(f"❌ Erreur d'indexation : {e}")

# On indexe le document dès que le serveur démarre
indexer_document()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({"erreur": "Question vide"}), 400

    try:
        # 1. Recherche vectorielle
        resultats = collection.query(query_texts=[question], n_results=3)
        contexte = "\n\n".join(resultats['documents'][0])
        
        # 2. Prompt
        prompt = f"""
        Tu es un assistant intelligent. Réponds à la question en te basant UNIQUEMENT sur les extraits ci-dessous.
        Si la réponse n'est pas dans les extraits, dis poliment que l'information n'est pas dans le document.
        
        Extraits :
        {contexte}
        
        Question : {question}
        """
        
        # 3. Génération
        response = client.models.generate_content(
            model='gemini-3.5-flash',
            contents=prompt,
        )
        return jsonify({"reponse": response.text})
    except Exception as e:
        return jsonify({"erreur": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)