# Predicción de Accidentes Cerebrovasculares

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MOPineyro/prediccion_accidentes_cerebrovasculares/blob/main/prediccion_accidentes_cerebrovasculares.ipynb)

Análisis y modelado predictivo para la detección temprana de riesgo de accidentes cerebrovasculares.

## Descripción del Proyecto

Este proyecto implementa diferentes modelos de machine learning para predecir el riesgo de accidentes cerebrovasculares basado en características médicas y demográficas. El objetivo es desarrollar una herramienta de screening inicial que pueda ayudar en la identificación temprana de pacientes en riesgo.

## Dataset

- **Fuente**: Kaggle Stroke Prediction Dataset
- **URL**: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
- **Características**: Incluye datos demográficos, condiciones médicas y factores de estilo de vida
- **Target**: Variable indicando ocurrencia de accidente cerebrovascular

## Resultados Principales

### Conclusiones Clave

1. **Detección de Casos Positivos**:

   - La red neuronal optimizada muestra mejor capacidad para detectar casos positivos
   - Importante en el contexto médico donde los falsos negativos son críticos

2. **Balance de Métricas**:

   - Trade-off entre precisión y recall
   - Los modelos optimizados priorizan la detección de casos positivos

3. **Aplicabilidad**:
   - Recomendado como herramienta de screening inicial
   - Complemento para la evaluación médica profesional

## Contribuciones y Mejoras Futuras

- Implementación de técnicas adicionales de balanceo de datos
- Exploración de arquitecturas de red más complejas
- Incorporación de validación cruzada
- Optimización de hiperparámetros más exhaustiva
