from src.llm_interface import LocalLLM
from src.rag_pipeline import RAGPipeline
from src.visualization import generate_plot

llm = LocalLLM()
rag = RAGPipeline()

class QueryAgent:
    def process(self, query: str):
        return f"Parsed user intent from: {query}"

class DataAgent:
    def process(self, query: str):
        results = rag.retrieve(query)
        return [r.page_content for r in results]

class VisualizationAgent:
    def process(self, data):
        path = generate_plot()
        return path

class Coordinator:
    def handle(self, query: str):
        q_agent = QueryAgent()
        d_agent = DataAgent()
        v_agent = VisualizationAgent()

        intent = q_agent.process(query)
        data = d_agent.process(intent)
        visualization_path = v_agent.process(data)

        return {
            "query": query,
            "intent": intent,
            "data": data,
            "visualization": visualization_path
        }
