from typing import List

class UnderstandModelPerformance:
    def __init__(self, objective: str, assetPair: str, timeResolution: str, predictionHorizon: str, selectedFeatures: List[str]):
        self.objective = objective
        self.assetPair = assetPair
        self.timeResolution = timeResolution
        self.predictionHorizon = predictionHorizon
        self.selectedFeatures = selectedFeatures

    def defineExperiment(self):
        # Implement the logic to define an experiment
        pass

    def setComparisonObjective(self, objective: str):
        self.objective = objective

    def requestModelComparison(self, cm_instance):
        cm_instance.runComparison()