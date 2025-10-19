# 🌊 FloatChat — Multi-Agent Generative AI for Ocean Data Intelligence

> “Where ocean science meets artificial intelligence.”  
> FloatChat transforms ARGO’s complex NetCDF datasets into interactive, conversational, and visual insights — powered by multi-agent AI.

---

## 🎯 Goal

To **develop a multi-agent AI system** that can query and visualize **ARGO oceanographic data** (temperature, salinity, and biogeochemical parameters) using natural language — providing **interactive insights without coding**.

---

## ⚠️ Problem

- ARGO data (NetCDF) is **complex and heterogeneous**, making it difficult to access and interpret.  
- Existing dashboards or single-agent tools are **limited and non-intuitive** for non-technical users.  
- This lack of accessibility hinders **climate monitoring**, **fisheries management**, and **disaster preparedness**.

---

## 💡 Solution — Multi-Agent Generative AI System

FloatChat introduces an **AI-driven multi-agent framework** for intelligent ocean data exploration.

### 🧠 Agents
| Agent | Role |
|--------|------|
| **Query Agent** | Understands user natural language queries. |
| **Data Agent** | Retrieves & processes ARGO data via FAISS Vector DB. |
| **Visualization Agent** | Generates scientific plots & visual summaries. |

### ⚙️ Backend
- **FastAPI + Streamlit** for interaction and deployment  
- **Phi-3 Mini (Hugging Face)** as the core LLM  
- **FAISS + Sentence Transformers** for RAG retrieval  
- **Matplotlib / Plotly** for depth-time and salinity-temperature plots  

### 🖥️ Dashboard Features
- 🌍 Float trajectories  
- 📊 Depth-time & parameter plots  
- 🔍 Profile comparisons  
- 💬 Conversational querying like:  
  > “Show salinity near the equator for March 2023.”

### 🔮 Scalable Architecture
Extendable to include:
- 🌊 Gliders, buoys, satellite data  
- 🔁 Forecasting & anomaly detection agents  
- 📡 Real-time monitoring pipelines  

---

## 🔧 Feasibility

### 🧩 Technical Foundation
| Component | Technology |
|------------|-------------|
| **Backend** | FastAPI |
| **AI Layer** | Multi-agent Phi-3 + FAISS RAG |
| **Frontend** | Streamlit (Ancient Blue UI) |
| **Visualization** | Matplotlib, Plotly |
| **Data Source** | ARGO NetCDF (mock subset for prototype) |

### 🧱 Development Plan
- **Prototype:** Indian Ocean ARGO subset (mock data)
- **Demo:** Chatbot → Multi-agent workflow → JSON + Visualization
- **Deployment:** Lightweight (local) or GPU-backed (cloud credits)

### ✅ Viability
- **User-Friendly:** Conversational + dashboard = no coding needed  
- **Extendable:** Plug in new ocean data sources easily  
- **Low-Cost:** 100% open-source (FastAPI, FAISS, Phi-3, Plotly)  
- **Deployable:** Scalable for INCOIS, ISRO, or university research centers  

---

## 🌍 Impacts & Benefits

| Impact Area | Benefits |
|--------------|-----------|
| **Accessibility** | Converts ARGO’s complex NetCDF data into simple Q&A insights |
| **Decision-Making** | Aids in climate, fisheries, and coastal disaster management |
| **Education & Research** | Interactive tool for oceanography students & researchers |
| **Agencies (INCOIS / ISRO)** | Enables float monitoring, climate resilience, & preparedness |
| **Public Awareness** | Democratizes access to critical environmental data |

---

## 🚀 Future Opportunities

- **Real-Time Data Integration:** Buoys, gliders, satellites  
- **Advanced Analytics:** Monsoon forecasting, anomaly detection  
- **Agentic Expansion:**  
  - Forecasting future ocean states  
  - Personalized insights for stakeholders  
  - Automated alerts for cyclones or coastal anomalies  

---

## 🧰 Tech Stack

| Layer | Tools |
|--------|-------|
| **Frontend** | Streamlit |
| **Backend API** | FastAPI |
| **LLM** | Microsoft Phi-3 Mini (Hugging Face) |
| **Retrieval Engine** | FAISS Vector Store |
| **Embeddings** | Sentence Transformers (`all-MiniLM-L6-v2`) |
| **Visualization** | Matplotlib / Plotly |
| **Data Source** | ARGO NetCDF Datasets |

---

## ⚙️ Installation

```bash
# Clone repo
git clone https://github.com/<your-username>/floatchat.git
cd floatchat

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
