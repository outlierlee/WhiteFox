
Please generate a valid TensorFlow model that fits the profile above. You should only use public TensorFlow APIs. This model does not start or finish a `while loop`. The XLA pipeline should be able to detect it using the needed conditions. 

Model should consist of all the required characteristics which trigger XLA's `WhileLoopInvariantCodeMotion` optimization.