# Manejo de resultados de diferentes modelos
import json
import os
from datetime import datetime

class ModelResults:
    """
    Clase para manejar los resultados de diferentes modelos
    """
    RESULTS_FILE = "results/model_comparisons.json"
    
    @classmethod
    def save_results(cls, model_name: str, metrics: dict, description: str = ""):
        """
        Guarda los resultados de un modelo
        """
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(cls.RESULTS_FILE), exist_ok=True)
        
        # Cargar resultados existentes
        results = cls.load_results()
        
        # Agregar nuevo resultado
        results[model_name] = {
            "metrics": metrics,
            "description": description,
            "timestamp": datetime.now().isoformat()
        }
        
        # Guardar resultados actualizados
        with open(cls.RESULTS_FILE, 'w') as f:
            json.dump(results, f, indent=2)
    
    @classmethod
    def load_results(cls) -> dict:
        """
        Carga los resultados existentes
        """
        if os.path.exists(cls.RESULTS_FILE):
            with open(cls.RESULTS_FILE, 'r') as f:
                return json.load(f)
        return {}
    
    @classmethod
    def generate_comparison_markdown(cls) -> str:
        """
        Genera una comparación en formato markdown
        """
        results = cls.load_results()
        if not results:
            return "No hay resultados disponibles."
        
        markdown = "# Comparación de Modelos\n\n"
        markdown += "### Resultados de los Modelos:\n\n"
        
        for model_name, data in results.items():
            metrics = data['metrics']
            markdown += f"1. **{model_name}**:\n"
            for metric, value in metrics.items():
                if metric != 'threshold':
                    markdown += f"   - {metric}: {value:.4f}\n"
            markdown += "\n"
        
        return markdown 