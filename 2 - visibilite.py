class Visibilite:
    """
        en python il n'y a pas de visibilité officielle mais il existe des conventions
        pas de _ signifie attribut public
        _ signifie protected
        __ signifie privé
    """

    def __init__(self) -> None:
        public = "variable publique"
        _protected = "variable protégée"
        __private = "variable privée"